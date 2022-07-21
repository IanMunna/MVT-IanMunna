from django import forms


class familiarForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    edad= forms.IntegerField()
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50)
    fecha_nacimiento= forms.DateField()

class FormBusuquedaFamiliar(forms.Form):
    edad= forms.IntegerField()