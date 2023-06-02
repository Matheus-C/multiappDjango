from django.urls import path, register_converter

from . import views

app_name = 'jogoVida'

class ListConverter:
    regex = '.*\/*'

    def to_python(self, list):
        return list

    def to_url(self, list):
        return list

register_converter(ListConverter, 'list')

urlpatterns = [path('', views.index, name='index'), 
               path('novo', views.novo, name='novo'),
               path('<list:matriz>proximo', views.proximo, name='proximo'),
               ]