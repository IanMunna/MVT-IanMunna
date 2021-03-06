from os import lseek
from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from AppMvt.models import Familiar, Mascota, Hogar
from django.template import Context, Template
from AppMvt.forms import familiarForm
from AppMvt.forms import FormBusuquedaFamiliar

#vistas de la web 
def inicio(request):
    return render (request, "AppMvt/familiares.html")

def inicio(request):
    return render (request, "AppMvt/hogar.html")

def inicio(request):
    return render (request, "AppMvt/mascota.html")

def inicio(request):
    return render (request, "AppMvt/inicio.html")

def busquedaFamiliar(request):
    return render(request, "AppMvt/busquedaFamiliar.html")

def buscar(request):
    edadFamiliar= request.GET.get('edad')

    if edadFamiliar:
        buscar= Familiar.objects.filter(edad__icontains=edadFamiliar)
    else:
        buscar= Familiar.objects.all()
    form= FormBusuquedaFamiliar()
    return render(request, "AppMvt/busquedaFamiliar.html", {"buscar":buscar, "form":form})

#este es un formulario creado con html(el cual fue reemplazado con el uso de 'Forms')
"""def usuariosFormulario(request):
    
    if (request.method == "POST"):
        nombre= request.POST.get("nombre")
        apellido= request.POST.get("apellido")
        edad= request.POST.get("edad")
        email= request.POST.get("mail")
        profesion= request.POST.get("profesion")
        fecha_nacimiento= request.POST.get("fecha_nacimiento")
        familiar=  Familiar(nombre=nombre, apellido=apellido, edad=edad, email=email, profesion=profesion, fecha_nacimiento=fecha_nacimiento)
        familiar.save()
        return render (request, "AppMvt/inicio.html")


    return render (request, "AppMvt/templates/AppMvt/familiarFormulario.html")"""

def familiarFormulario(request):
    
    if request.method == "POST":
        miFormulario= familiarForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info= miFormulario.cleaned_data
            familiar=  Familiar(nombre=info["nombre"], apellido=info["apellido"], edad=info["edad"], email=info["email"], profesion=info["profesion"], fecha_nacimiento=info["fecha_nacimiento"])
            familiar.save()
            return render (request, "AppMvt/inicio.html")
    else:
        miFormulario= familiarForm()
    return render(request, "AppMvt/familiarFormulario.html", {"miFormulario":miFormulario})


########. models especificos. ########
def familiar(self):

    familiar= Familiar(nombre="Eric", apellido="Munna", edad="16", email="ericmunna@example.com", profesion="estudiante", fecha_nacimiento="2007-01-13")
    familiar.save()
    texto= f"Familiar creado: {familiar.nombre} {familiar.apellido} {familiar.edad} {familiar.email} {familiar.profesion} {familiar.fecha_nacimiento}"
    familiar1= Familiar(nombre="Zara", apellido="Munna", edad="48", email="zaramunna@example.com", profesion="astronauta", fecha_nacimiento="1974-04-23")
    familiar1.save()
    texto= f"Familiar creado: {familiar1.nombre} {familiar1.apellido} {familiar1.edad} {familiar1.email} {familiar1.profesion} {familiar1.fecha_nacimiento}"
    familiar2= Familiar(nombre="Juan", apellido="Munna", edad="34", email="ujuancito@example.com", profesion="director de primaria", fecha_nacimiento="1988-06-21")
    familiar2.save()
    texto= f"Familiar creado: {familiar2.nombre} {familiar2.apellido} {familiar2.edad} {familiar2.email} {familiar2.profesion} {familiar2.fecha_nacimiento}"


    diccionario= {
        "familiarNom": familiar.nombre , "familiarApe": familiar.apellido, "familiarEdad": familiar.edad, "familiarEmail": familiar.email, "familiarProf": familiar.profesion, "familiarFech": familiar.fecha_nacimiento,
        "familiar1Nom": familiar1.nombre , "familiar1Ape": familiar1.apellido, "familiar1Edad": familiar1.edad, "familiar1Email": familiar1.email, "familiar1Prof": familiar1.profesion, "familiar1Fech": familiar1.fecha_nacimiento,
        "familiar2Nom": familiar2.nombre , "familiar2Ape": familiar2.apellido, "familiar2Edad": familiar2.edad, "familiar2Email": familiar2.email, "familiar2Prof": familiar2.profesion, "familiar2Fech": familiar2.fecha_nacimiento,
    }

    miHtml= open("/Users/ianmunna/Documents/DesafioClase18/MVT/AppMvt/templates/AppMvt/familiares.html")

    plantilla= Template(miHtml.read())

    miHtml.close()

    contexto= Context(diccionario)

    document= plantilla.render(contexto)

    return HttpResponse(document)

def mascota(self):

    mascota= Mascota(nombre="perro", raza="ovejero")
    mascota.save()
    texto= f"Mascota creada: {mascota.nombre} {mascota.raza}"
    mascota1= Mascota(nombre="gato", raza="siames")
    mascota1.save()
    texto= f"Mascota creada: {mascota1.nombre} {mascota1.raza}"
    mascota2= Mascota(nombre="pajaro", raza="cotorra")
    mascota2.save()
    texto= f"Mascota creada: {mascota2.nombre} {mascota2.raza}"

    diccionario= {
        "mascotaNom": mascota.nombre , "mascotaRaz": mascota.raza,
        "mascota1Nom": mascota1.nombre, "mascota1Raz": mascota1.raza,
        "mascota2Nom": mascota2.nombre, "mascota2Raz": mascota2.raza,
    }
    
    miHtml= open("/Users/ianmunna/Documents/DesafioClase18/MVT/AppMvt/templates/AppMvt/mascota.html")

    plantilla= Template(miHtml.read())

    miHtml.close()

    contexto= Context(diccionario)

    document= plantilla.render(contexto)

    return HttpResponse(document)

def hogar(self):

    hogar= Hogar(direccion="Independencia 3600")
    hogar.save()
    texto= f"Hogar creado: {hogar.direccion}"
    hogar1= Hogar(direccion="Avenida Libertad 1844")
    hogar1.save()
    texto= f"Hogar creado: {hogar1.direccion}"
    hogar2= Hogar(direccion="Comechingones Sur 9021")
    hogar2.save()
    texto= f"Hogar creado: {hogar2.direccion}"

    diccionario= {
        "hogarDir": hogar.direccion ,
        "hogar1Dir": hogar1.direccion , 
        "hogar2Dir": hogar2.direccion ,
    }

    miHtml= open("/Users/ianmunna/Documents/DesafioClase18/MVT/AppMvt/templates/AppMvt/hogar.html")

    plantilla= Template(miHtml.read())

    miHtml.close()

    contexto= Context(diccionario)

    document= plantilla.render(contexto)

    return HttpResponse(document)



