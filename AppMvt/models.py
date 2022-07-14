from django.db import models

# Create your models here.
class Familiar(models.Model):
    
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    email= models.EmailField()
    profesion= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField()

class Mascota(models.Model):

    nombre=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)

class Hogar(models.Model):

    direccion=models.CharField(max_length=100)
