from django.contrib import admin
from .models import Entrepreneur

@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'entreprise', 'secteur', 'email', 'date_creation')
    search_fields = ('nom', 'entreprise', 'secteur', 'email')
