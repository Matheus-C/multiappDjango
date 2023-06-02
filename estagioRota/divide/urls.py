from django.urls import path

from . import views

app_name = 'divide'


urlpatterns = [path('', views.index, name='index'), 
               path('cadastro', views.cadastro, name='cadastro'),
               path('resultado', views.resultado, name='resultado'),
               ]