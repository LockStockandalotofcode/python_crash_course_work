"""Defines URL patterns for pizzas app."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Page to shocase all pizzas.
    path('pizzas/', views.pizzas, name='pizzas'),
    # Page for individual pizza.
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza',)
]