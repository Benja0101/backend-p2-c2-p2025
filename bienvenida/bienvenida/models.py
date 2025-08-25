from django.db import models
#desde django importo modelos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    #defino el campo nombre como un campo de texto con una longitud máxima de 100 caracteres
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    #defino el campo precio como un campo decimal con un máximo de 6 dígitos y 2 decimales
    
    
    
    def __str__(self):
        return self.nombre
    #defino el método __str__ para que devuelva el nombre del producto cuando se imprima el objeto
    
    
