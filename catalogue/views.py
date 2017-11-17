from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


# Create your views here.


class ListeHouse(ListView):
    
    model = House
    context_object_name = 'liste_houses'
    template_name = 'catalogue/liste_houses.html'
    



class DetailHouse(DetailView):
    context_object_name = "detail_house"
    template_name = "catalogue/detail_house.html"
    model = House
