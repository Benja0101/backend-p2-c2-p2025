# 🌐 CONFIGURACIÓN DE URLs DE LA APLICACIÓN INVENTARIO
# Este archivo define todas las rutas específicas para la gestión de productos

from django.urls import path
from . import views 

# 📋 Lista de patrones de URL para la aplicación de inventario
urlpatterns = [
    # 📖 Ruta para mostrar la lista completa de productos
    # URL: /inventario/productos/
    path('productos/', views.producto_list, name='productos'),
    
    # ➕ Ruta para crear un nuevo producto
    # URL: /inventario/productos/crear/
    path('productos/crear/', views.productoCreate, name='crear_producto'),
    
    # ✏️ Ruta para editar un producto específico (usando su ID)
    # URL: /inventario/productos/editar/1/ (donde 1 es el ID del producto)
    path('productos/editar/<int:pk>/', views.producto_update, name='editar_producto'),
    
    # 🗑️ Ruta para eliminar un producto específico (usando su ID)
    # URL: /inventario/productos/eliminar/1/ (donde 1 es el ID del producto)
    path('productos/eliminar/<int:pk>/', views.producto_eliminar, name='eliminar_producto'),
]

# 📝 NOTA: Estas URLs se incluyen en el urls.py principal mediante include('inventario.urls')
# El prefijo 'inventario/' se añade automáticamente desde el urls.py principal
