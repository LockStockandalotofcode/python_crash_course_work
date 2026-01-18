"""Defines URL patterns for pizzas app."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
]