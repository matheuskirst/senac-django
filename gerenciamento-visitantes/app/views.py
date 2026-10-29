from uuid import uuid4
from datetime import datetime

from django.db.models import Q, Count, Avg
from django.db.models.functions import ExtractYear
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import Visitor
from .enums import TicketType
from .forms import VisitorForm
from .dtos import Statistics

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/home.html')

def list_visitors(request: HttpRequest) -> HttpResponse:
    search_name_or_cpf = request.GET.get(key='search_name_or_cpf', default='').strip()
    search_ticket_type = request.GET.get(key='ticket-type', default='')
    search_ticket_date = request.GET.get(key='ticket_date', default='')

    visitors = Visitor.objects.all()

    visitors = visitors.filter(
        Q(first_name__icontains=search_name_or_cpf)
        | Q(last_name__icontains=search_name_or_cpf)
        | Q(cpf__contains=search_name_or_cpf)
    )

    valid_type = getattr(TicketType, search_ticket_type.upper(), None)

    if valid_type:
        visitors = visitors.filter(ticket_type=valid_type)

    if search_ticket_date:
        try:
            ticket_date = datetime.strptime(search_ticket_date, '%Y-%m-%d')
        except:
            ticket_date = ''
        visitors = visitors.filter(ticket_date=ticket_date)

    context = {
        'visitors': visitors,
        'search_name_or_cpf': search_name_or_cpf,
        'ticket_type': search_ticket_type,
        'TicketType': TicketType,
        'ticket_date': search_ticket_date,
    }

    return render(request, 'pages/list-visitors.html', context)

def create_visitor(request: HttpRequest) -> HttpResponse:
    template_name = 'pages/create-visitor.html'

    if request.method == 'GET':
        context = {
            'TicketType': TicketType
        }
        return render(request, template_name, context)

    if request.method == 'POST':
        form = VisitorForm(request.POST)

        if form.is_valid():
            new_visitor: Visitor = form.save(commit=False)
            new_visitor.ticket_code = str(uuid4())
            new_visitor.save()

            return redirect(to='list-visitors')

        context = {
            'TicketType': TicketType,
            'form_errors': form.errors.as_data(),
            'request': request.POST
        }

        return render(request, template_name, context)

def update_visitor(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == 'GET':
        visitor = Visitor.objects.get(pk=id)
        context = {
            'visitor': visitor,
            'TicketType': TicketType
        }
        return render(request, 'pages/update-visitor.html', context)
    
    if request.method == 'POST':
        visitor = Visitor.objects.get(pk=id)
        form = VisitorForm(request.POST, instance=visitor)

        if form.is_valid():
            form.save()
            return redirect('visitors')

def delete_visitor(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == 'POST':
        visitor = Visitor.objects.get(pk=id)
        visitor.delete()
        return redirect(to='visitors')

def statistics(request: HttpRequest) -> HttpResponse:
    statistics = Visitor.objects.aggregate(
        visitors_count=Count('id'),
        ticket_normal_count=Count('id', filter=Q(ticket_type=TicketType.NORMAL)),
        ticket_vip_count=Count('id', filter=Q(ticket_type=TicketType.VIP)),
        ticket_premium_count=Count('id', filter=Q(ticket_type=TicketType.PREMIUM)),
        average_age=Avg(datetime.today().year - ExtractYear('birthdate'))
    )

    # average age solution: https://forum.djangoproject.com/t/average-age-from-birth-date/2454/4

    context = {
        'stats': Statistics(**statistics)
    }

    return render(request, 'pages/statistics.html', context)
1