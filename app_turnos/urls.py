from django.contrib import admin
from django.urls import path
from app_turnos import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('home', views.home, name='home'),

]
