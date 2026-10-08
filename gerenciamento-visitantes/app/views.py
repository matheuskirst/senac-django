from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def visitors(request):
    return render(request, 'visitors.html')
