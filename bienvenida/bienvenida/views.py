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
    
    
    
def CrearProducto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        nuevo_producto = models.Productos(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
        nuevo_producto.save()
        return HttpResponse("¡Producto creado exitosamente!")
    return render(request, 'productos/crear-productos.html')


