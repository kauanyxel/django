from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contatos'),
    path('sobre/', views.sobre, name='sobre'),
    path('servicos/', views.Servicos, name='servicos'),
]