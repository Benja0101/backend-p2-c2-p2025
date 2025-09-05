# 📝 FORMULARIOS DE LA APLICACIÓN INVENTARIO
# Este archivo define los formularios para capturar y validar datos de usuario

from django import forms
from .models import Productos

# 📋 Formulario para productos basado en el modelo Productos
class ProductoForm(forms.ModelForm):
    """
    Formulario automático generado desde el modelo Productos
    - Incluye validación automática de tipos de datos
    - Genera campos HTML apropiados para cada tipo de campo
    - Maneja la creación y edición de productos
    """
    
    class Meta:
        # 🎯 Modelo base para el formulario
        model = Productos
        
        # 📝 Campos que se incluirán en el formulario
        # Se corresponden con los campos del modelo Productos
        fields = ['nombre', 'descripcion', 'precio', 'stock']
        
        # 🎨 OPCIONAL: Se pueden agregar widgets personalizados
        # widgets = {
        #     'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        #     'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        #     'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        #     'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        # }
        
        # 🏷️ OPCIONAL: Etiquetas personalizadas para los campos
        # labels = {
        #     'nombre': 'Nombre del Producto',
        #     'descripcion': 'Descripción Detallada',
        #     'precio': 'Precio (€)',
        #     'stock': 'Cantidad en Stock',
        # }

# 📝 NOTA: Django automáticamente:
# - Valida que los campos requeridos no estén vacíos
# - Verifica que el precio sea un número decimal válido
# - Confirma que el stock sea un número entero
# - Genera HTML apropiado para cada tipo de campo