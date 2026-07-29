from django.db import models

# Create your models here.

class Edificio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    OPCIONES_TIPO = [
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    ]
    tipo = models.CharField(max_length=20, choices=OPCIONES_TIPO)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)


class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=200)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    num_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %s" % (self.nombre_propietario, self.costo)
