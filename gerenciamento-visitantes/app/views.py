from uuid import uuid4
from datetime import datetime
from django.db.models import Q, Count, Avg
from django.db.models.functions import ExtractYear
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Visitor
from .dtos import Statistics

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/home.html')

def visitors(request: HttpRequest) -> HttpResponse:
    search = request.GET.get(key='search', default='').strip()
    ticket_type = request.GET.get(key='ticket-type', default='')

    visitors = Visitor.objects.all()

    visitors = visitors.filter(
        Q(first_name__icontains=search)
        | Q(last_name__icontains=search)
        | Q(cpf__contains=search)
    )

    valid_type = getattr(Visitor.TicketType, ticket_type.upper(), None)

    if valid_type:
        visitors = visitors.filter(ticket_type=valid_type)

    response = {
        'visitors': visitors,
        'search': search,
        'ticket_type': ticket_type,
        'TicketType': Visitor.TicketType
    }

    return render(request, 'pages/visitors.html', response)

def create_visitor(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        visitor = Visitor()
        visitor.first_name = request.POST['first_name']
        visitor.last_name = request.POST['last_name']
        visitor.cpf = request.POST['cpf']
        visitor.birthdate = datetime.strptime(request.POST['birthdate'], '%Y-%m-%d')
        visitor.ticket_date = datetime.strptime(request.POST['ticket_date'], '%Y-%m-%d')
        visitor.ticket_type = request.POST['ticket_type']
        visitor.ticket_code = str(uuid4())

        visitor.save()

        return redirect(to='visitors')

    response = {
        'TicketType': Visitor.TicketType
    }

    return render(request, 'pages/create-visitor.html', response)

def update_visitor(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == 'POST':
        visitor = Visitor.objects.get(pk=id)
        visitor.first_name = request.POST['first_name']
        visitor.last_name = request.POST['last_name']
        visitor.cpf = request.POST['cpf']
        visitor.birthdate = datetime.strptime(request.POST['birthdate'], '%Y-%m-%d')
        visitor.ticket_date = datetime.strptime(request.POST['ticket_date'], '%Y-%m-%d')
        visitor.ticket_type = request.POST['ticket_type']

        visitor.save()
        return redirect('visitors')

    visitor = Visitor.objects.get(pk=id)

    response = {
        'visitor': visitor,
        'TicketType': Visitor.TicketType
    }

    return render(request, 'pages/update-visitor.html', response)

def delete_visitor(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == 'POST':
        visitor = Visitor.objects.get(pk=id)
        visitor.delete()
        return redirect(to='visitors')

def statistics(request: HttpRequest) -> HttpResponse:
    statistics = Visitor.objects.aggregate(
        visitors_count=Count('id'),
        ticket_normal_count=Count('id', filter=Q(ticket_type=Visitor.TicketType.NORMAL)),
        ticket_vip_count=Count('id', filter=Q(ticket_type=Visitor.TicketType.VIP)),
        ticket_premium_count=Count('id', filter=Q(ticket_type=Visitor.TicketType.PREMIUM)),
        average_age=Avg(datetime.today().year - ExtractYear('birthdate'))
    )

    # average age solution: https://forum.djangoproject.com/t/average-age-from-birth-date/2454/4

    response = {
        'stats': Statistics(**statistics)
    }

    return render(request, 'pages/statistics.html', response)
