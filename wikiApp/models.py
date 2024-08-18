from django.db import models

# Create your models here.
class Tema( models.Model ):
    nombreTema = models.CharField(max_length=48, null=True, blank=True)
    descripcionTema = models.CharField(max_length=256, null=True, blank=True)

class Articulo( models.Model ):
    nombreArticulo = models.CharField(max_length=48, null=True, blank=True)
    contenidoArticulo = models.CharField(max_length=256, null=True, blank=True)
    temaRelacionado = models.ForeignKey(Tema, null=True, blank=True, on_delete=models.SET_NULL)
