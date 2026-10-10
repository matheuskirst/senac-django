from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visitors/', views.visitors, name='visitors'),
    path('visitors/create/', views.create_visitor, name='create-visitor')
]
