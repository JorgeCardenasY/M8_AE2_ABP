from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('analytics/', views.analytics, name='analytics'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('proyectos/', views.proyectos, name='proyectos'),
]
