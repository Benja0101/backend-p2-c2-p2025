from django.shortcuts import render
from .models import Productos
from .forms import ProductoForm
from django.shortcuts import redirect

def productoCreate(request):
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
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'inventario/editar-producto.html', {'form': form})


def producto_list(request):
    productos = Productos.objects.all()
    return render(request, 'inventario/lista-productos.html', {'productos': productos})


def producto_eliminar(request, pk):
    producto = Productos.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    return render(request, 'inventario/eliminar-producto.html', {'producto': producto})


