from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=90)
    camada = models.IntegerField()
class Estudiante(models.Model):
    nombre = models.CharField(max_length=90)
    apellido = models.CharField(max_length=90)
    correo = models.EmailField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=90)
    apellido = models.CharField(max_length=90)
    correo = models.EmailField()   
    profesion = models.CharField(max_length=90)
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=90)
    fechaEntrega = models.DateField()