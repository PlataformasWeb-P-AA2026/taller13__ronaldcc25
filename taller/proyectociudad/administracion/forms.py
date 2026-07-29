from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administracion.models import Edificio, Departamento


class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Nombre del edificio'),
            'direccion': _('Dirección'),
            'ciudad': _('Ciudad'),
            'tipo': _('Tipo de edificio'),
        }


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'num_cuartos', 'edificio']
        labels = {
            'nombre_propietario': _('Nombre completo del propietario'),
            'costo': _('Costo del departamento'),
            'num_cuartos': _('Número de cuartos'),
            'edificio': _('Edificio'),
        }
