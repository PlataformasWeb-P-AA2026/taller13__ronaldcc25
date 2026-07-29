from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from administracion.serializers import UserSerializer, GroupSerializer, \
EdificioSerializer, DepartamentoSerializer

from administracion.models import *
from administracion.forms import *
def index(request):
    """
        Página principal con botones a las listas y las tablas integradas.
    """
    edificios = Edificio.objects.all()
    departamentos = Departamento.objects.all()
    contexto = {
        'edificios': edificios, 
        'numero_edificios': len(edificios),
        'departamentos': departamentos,
        'numero_departamentos': len(departamentos)
    }
    return render(request, 'index.html', contexto)

def lista_edificios(request):
    """
        Listar los registros del modelo Edificio.
    """
    edificios = Edificio.objects.all()
    contexto = {'edificios': edificios, 'numero_edificios': len(edificios)}
    return render(request, 'edificios_lista.html', contexto)

def lista_departamentos(request):
    """
        Listar los registros del modelo Departamento.
    """
    departamentos = Departamento.objects.all()
    contexto = {'departamentos': departamentos, 'numero_departamentos': len(departamentos)}
    return render(request, 'departamentos_lista.html', contexto)



# crear vistas a través de viewsets
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EdificioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Edificios to be viewed or edited.
    """
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Departamentos to be viewed or edited.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]