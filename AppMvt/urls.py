from django import views
from django.urls import path 
from AppMvt import views  


urlpatterns = [
    path('Familiares/', views.familiar, name='familiares'),
    path('Mascota/', views.mascota, name='mascota'),
    path('Hogar/', views.hogar, name='hogar'),
    path('', views.inicio, name='inicio'),
    path('familiarFormulario/', views.familiarFormulario, name='familiarFormulario'),
    path('busquedaFamiliar/', views.busquedaFamiliar, name='busquedaFamiliar'),
    path('buscar/', views.buscar),
]