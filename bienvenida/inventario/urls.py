from django.urls import path

from . import views 

urlpatterns = [
    path('productos/', views.producto_list, name='productos'),
    path('productos/crear/', views.productoCreate, name='crear_producto'),
    path('productos/editar/<int:pk>/', views.producto_update, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.producto_eliminar, name='eliminar_producto'),
]
