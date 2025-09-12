# 🎯 VISTAS DE LA APLICACIÓN INVENTARIO
# Este archivo contiene toda la lógica para manejar las peticiones HTTP y respuestas

from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductoForm

# ➕ VISTA: Crear nuevo producto
def productoCreate(request):
    """
    Maneja la creación de nuevos productos
    - GET: Muestra el formulario vacío
    - POST: Procesa los datos del formulario y guarda el producto
    """
    if request.method == 'POST':
        
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    
    return render(request, 'inventario/crear-producto.html', {'form': form})

def producto_update(request, pk):
    producto = Productos.objects.get(pk=pk)
    if request.method == 'POST':
        # 📥 Procesar datos actualizados del formulario
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            # ✅ Guardar cambios en la base de datos
            form.save()
            # 🔄 Redirigir a la lista después de actualizar
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/editar-producto.html', {'form': form})

def producto_list(request):
    productos = Productos.objects.all()
    return render(request, 'inventario/lista-productos.html', {
        'object_list': productos  # Así el template puede usar cualquiera de los dos nombres
    })
    
def producto_eliminar(request, pk):
    producto = Productos.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    
    return render(request, 'inventario/eliminar-producto.html', {'producto': producto})


