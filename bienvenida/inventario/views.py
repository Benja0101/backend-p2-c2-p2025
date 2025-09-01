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
    return render(request, 'productos/crear-producto.html', {'form': form})


def producto_update(request, pk):
    producto = Productos.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar-producto.html', {'form': form})


def producto_list(request):
    productos = Productos.objects.all()
    return render(request, 'productos/lista-productos.html', {'productos': productos})


def producto_eliminar(request, pk):
    producto = Productos.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    return render(request, 'productos/eliminar-producto.html', {'producto': producto})


