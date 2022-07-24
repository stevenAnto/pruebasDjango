from django.db import models

class Persona(models.Model):
    nombres = models.CharField(max_length =100)
    apellidos = models.CharField(max_length = 100)
    edad = models.IntegerField(null=True)
    donador = models.BooleanField(blank=True)

# Create your models here.
