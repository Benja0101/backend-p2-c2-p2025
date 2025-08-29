from django.http import HttpResponse
from django.shortcuts import render
from . import models

def inicio(request):
    return HttpResponse("¡Bienvenido a mi sitio web!")

#funcion para el mensaje de bienvenida
def mostrarBienvenida(request):
    tu_nombre = "Benjamin Salazar"
    return HttpResponse(f"¡Bienvenido a mi sitio web, {tu_nombre}!")

def lista_productos(request):
    productos = models.Productos.objects.all()#rescato todos los productos de la base de datos como en un lista de diccionarios
    return render(request, 'productos/lista.html', {'productos': productos})
    #renderizo la plantilla productos.html y le paso el contexto con los productos  
    
    
#el view sirve para manejar las solicitudes y devolver respuestas en una aplicación web de Django.  
