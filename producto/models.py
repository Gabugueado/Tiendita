from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    description = models.CharField(max_length=50) #252 por las estupidas imagenes que te da paja hacerlas responsive
    precio = models.IntegerField()

    def __str__(self):
         return self.nombre 