from django import views
from django.urls import path 
from AppMvt import views  


urlpatterns = [
    path('Familiares/', views.familiar),
    path('Mascota/', views.mascota),
    path('Hogar/', views.hogar),
    path('', views.inicio),
]