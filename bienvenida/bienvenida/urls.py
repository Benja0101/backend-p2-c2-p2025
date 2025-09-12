"""
URL configuration for bienvenida project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.inicio),
    path('admin/', admin.site.urls),
    path('inicio/',views.mostrarBienvenida),
    path('productos/',views.lista_productos),
    path('inventario/', include('inventario.urls')),
    path('productos/crear/', views.CrearProducto, name='crear_producto'),




]

#el url.py sirve para definir las rutas de la aplicación web de Django
# asociando URLs específicas con las vistas correspondientes que manejarán las solicitudes y devolverán respuestas. 