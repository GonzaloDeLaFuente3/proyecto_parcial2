from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tipo_plato(models.Model):

    descripcion= models.CharField(max_length=300)
    vigencia = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion



class Vianda(models.Model):
    FRECUENCIA = [
        ('semanal', 'Semanal'),
        ('quincenal', 'Quincenal'),

    ]
    TIPO_COMIDA = [
        ('normal', 'Normal'),
        ('vegetariano', 'Vegetariano'),
        ('diabetico', 'Diabetico')
    ]
    ESTADO_OPCIONES = [
        ('pendiente', 'Pendiente'),
        ('en preparacion', 'En preparación'),
        ('en camino', 'En camino'),
        ('entregado', 'Entregado'),
        ('devuelto', 'Devuelto'),
        ('cancelado', 'Cancelado')
    ]
    frecuencia = models.CharField(max_length=300, choices=FRECUENCIA)
    tipoComida = models.CharField(max_length=300, choices=TIPO_COMIDA)
    fecha_inicio = models.DateField()
    cantidad_vianda = models.IntegerField()
    estado = models.CharField(max_length=350, choices=ESTADO_OPCIONES, default='pendiente')
    tipo_platos = models.ManyToManyField(Tipo_plato)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
