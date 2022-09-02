from django.urls import path  # Incluido

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),  # Criado a rota
]
