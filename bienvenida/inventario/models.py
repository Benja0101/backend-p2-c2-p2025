# 🗃️ MODELOS DE DATOS DE LA APLICACIÓN INVENTARIO
# Este archivo define la estructura de los datos que se almacenarán en la base de datos

from django.db import models

# 📦 Modelo para representar productos en el inventario
class Productos(models.Model):
    # 📝 Nombre del producto (máximo 100 caracteres)
    nombre = models.CharField(max_length=100)
    
    # 📋 Descripción detallada del producto (máximo 255 caracteres)
    descripcion = models.CharField(max_length=255)
    
    # 💰 Precio del producto (máximo 10 dígitos, 2 decimales)
    # Ejemplo: 99999999.99
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    # 📊 Cantidad disponible en stock (número entero)
    stock = models.IntegerField()
    
    # 🏷️ Método para mostrar el nombre del producto cuando se imprime el objeto
    # Se usa en el admin de Django y en formularios
    def __str__(self):
        return self.nombre

# 📝 NOTA: Django creará automáticamente:
# - Un campo 'id' como clave primaria
# - Campos de fecha 'created_at' y 'updated_at' si se agregan después
# - Métodos para consultas como Productos.objects.all(), filter(), get(), etc.


