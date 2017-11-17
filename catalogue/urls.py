from django.conf.urls import  url, include
from django.views.generic import ListView
from . import views
from .models import *

urlpatterns =[
    url(r'^$', views.ListeHouse.as_view(), name ="liste_house"),
    url(r'^(?P<pk>\d+)$', views.DetailHouse.as_view(), name ='detail_house'),   
    
]