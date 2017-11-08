from django.conf.urls import url, include
from django.contrib.auth import views as auth_views


from . import views


urlpatterns= [
    url(r'^change-password/$', auth_views.PasswordChangeView.as_view(template_name='profil/change-password.html')),
    url(r'^connexion$', views.connexion, name='connexion'),    
    #url(r'^login/$', auth_views.login, {'template_name': 'profil/login.html'}, name='login'),  
    url(r'^logout/$', auth_views.logout, {'next_page': '/profil/login'}, name='logout'), 
    url('^', include('django.contrib.auth.urls')), 
    
]