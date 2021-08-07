from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50) #252 por las estupidas imagenes que te da paja hacerlas responsive
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self):
         return self.nombre