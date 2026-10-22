from uuid import uuid4
from datetime import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Visitor

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home/home.html')

def visitors(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        ...
        return redirect(to='visitors')

    visitors = Visitor.objects.all()

    response = {
        'visitors': visitors
    }

    return render(request, 'visitors/visitors.html', response)

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

    return render(request, 'visitors/create-visitor.html')

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
        'visitor': visitor
    }

    return render(request, 'visitors/update-visitor.html', response)

def delete_visitor(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == 'POST':
        visitor = Visitor.objects.get(pk=id)
        visitor.delete()

    return redirect(to='visitors')
