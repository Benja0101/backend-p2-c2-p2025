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
        # 📥 Procesar datos enviados desde el formulario
        form = ProductoForm(request.POST)
        if form.is_valid():
            # ✅ Si los datos son válidos, guardar en la base de datos
            form.save()
            # 🔄 Redirigir a la lista de productos después de crear
            return redirect('productos')
    else:
        # 📄 Mostrar formulario vacío para GET request
        form = ProductoForm()
    
    # 🖥️ Renderizar la plantilla con el formulario
    return render(request, 'inventario/crear-producto.html', {'form': form})


# ✏️ VISTA: Actualizar producto existente
def producto_update(request, pk):
    """
    Maneja la edición de productos existentes
    - pk: clave primaria del producto a editar
    """
    # 🔍 Obtener el producto específico de la base de datos
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
        # 📄 Mostrar formulario pre-llenado con datos del producto
        form = ProductoForm(instance=producto)
    
    # 🖥️ Renderizar plantilla de edición
    return render(request, 'inventario/editar-producto.html', {'form': form})


# 📋 VISTA: Listar todos los productos
def producto_list(request):
    """
    Muestra una lista de todos los productos en el inventario
    """
    # 📊 Obtener todos los productos de la base de datos
    productos = Productos.objects.all()
    
    # 🖥️ Renderizar plantilla con la lista de productos
    return render(request, 'inventario/lista-productos.html', {'productos': productos})


# 🗑️ VISTA: Eliminar producto
def producto_eliminar(request, pk):
    """
    Maneja la eliminación de productos
    - pk: clave primaria del producto a eliminar
    """
    # 🔍 Obtener el producto específico
    producto = Productos.objects.get(pk=pk)
    
    if request.method == 'POST':
        # ❌ Confirmar eliminación y borrar de la base de datos
        producto.delete()
        # 🔄 Redirigir a la lista después de eliminar
        return redirect('productos')
    
    # ⚠️ Mostrar página de confirmación antes de eliminar
    return render(request, 'inventario/eliminar-producto.html', {'producto': producto})


