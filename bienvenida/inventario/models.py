
# Este archivo define la estructura de los datos que se almacenarán en la base de datos

from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.nombre






# 📝 NOTA: Django creará automáticamente:
# - Un campo 'id' como clave primaria
# - Campos de fecha 'created_at' y 'updated_at' si se agregan después
# - Métodos para consultas como Productos.objects.all(), filter(), get(), etc.


