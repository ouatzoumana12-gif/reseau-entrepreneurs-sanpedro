from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Entrepreneur
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Create your views here.

def accueil(request):
    return render(request, 'accueil.html')


def annuaire(request):
    entrepreneurs = Entrepreneur.objects.all().order_by('-date_creation')
    return render(request, 'annuaire.html', {'entrepreneurs': entrepreneurs})


def inscription(request):
    message = None
    if request.method == 'POST':
        nom = request.POST.get('nom', '').strip()
        entreprise = request.POST.get('entreprise', '').strip()
        secteur = request.POST.get('secteur', '').strip()
        email = request.POST.get('email', '').strip()
        # validation simple
        if not (nom and entreprise and secteur and email):
            message = "Veuillez remplir tous les champs."
        else:
            try:
                validate_email(email)
                # vérifier unicité email côté base
                if Entrepreneur.objects.filter(email=email).exists():
                    message = "Cet email est déjà inscrit !"
                else:
                    Entrepreneur.objects.create(nom=nom, entreprise=entreprise, secteur=secteur, email=email)
                    return redirect('annuaire')
            except ValidationError:
                message = "Email invalide."
    return render(request, 'inscription.html', {'message': message})
