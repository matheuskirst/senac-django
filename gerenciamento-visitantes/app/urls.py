from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visitors/', views.visitors, name='visitors'),
    path('visitors/create/', views.create_visitor, name='create-visitor'),
    path('visitors/update/<int:id>/', views.update_visitor, name='update-visitor'),
    path('visitors/delete/<int:id>/', views.delete_visitor, name='delete-visitor'),
    path('statistics/', views.statistics, name='statistics')
]
