from django.shortcuts import render
from .models import Visitor

def home(request):
    return render(request, 'home.html')

def visitors(request):
    visitors = Visitor.objects.all()

    response = {
        'visitors': visitors
    }

    return render(request, 'visitors.html', response)
