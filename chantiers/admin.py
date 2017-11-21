from django.contrib import admin
from django.utils.text import Truncator

# Register your models here.

from .models import *


class MessageInline(admin.StackedInline):
    model = Message
    extra = 0

class FichierInLine(admin.StackedInline):
    model = Fichier
    extra = 0

class ChantierAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    inlines = [FichierInLine, MessageInline]
    

class MarcheAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'chantier')
    list_filter = ('category', 'chantier',)
    search_fields = ('name',)



    

admin.site.register(Chantier, ChantierAdmin)

admin.site.register(CategorieFichier)



