from django.db import models

# Create your models here.
class Familiar(models.Model):
    
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    email= models.EmailField()
    profesion= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField()

    def __str__(self):
        return self.nombre+" "+str(self.fecha_nacimiento)

class Mascota(models.Model):

    nombre=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Hogar(models.Model):

    direccion=models.CharField(max_length=100)

    def __str__(self):
        return self.direccion

