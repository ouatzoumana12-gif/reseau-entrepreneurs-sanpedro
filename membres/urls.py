from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('annuaire/', views.annuaire, name='annuaire'),
    path('inscription/', views.inscription, name='inscription'),
]
