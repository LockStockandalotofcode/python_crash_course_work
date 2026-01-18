from django.shortcuts import render

def index(request):
    """The home page for pizzas app."""
    return render(request, 'pizzas/index.html')