"""
    Manejo de urls para la aplicación
    administracion
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('edificios/', views.lista_edificios, name='lista_edificios'),
        path('departamentos/', views.lista_departamentos, name='lista_departamentos'),
 ]
