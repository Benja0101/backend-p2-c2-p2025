# 📁 Carpeta de Migraciones

Esta carpeta contiene archivos que gestionan los cambios en la estructura de la base de datos.

## Archivos de migración:

### 🗄️ **Proyecto Principal (bienvenida/migrations/)**
- **0001_initial.py**: Primera migración que crea las tablas iniciales
- **0002_productos_delete_producto.py**: Migración que actualiza el modelo de productos

### 🗄️ **Aplicación Inventario (inventario/migrations/)**
- Actualmente sin migraciones propias

## ¿Qué son las migraciones?

Las migraciones son como un "control de versiones" para tu base de datos:

🔄 **Crean tablas** cuando defines nuevos modelos
🔄 **Modifican columnas** cuando cambias campos en los modelos  
🔄 **Eliminan tablas** cuando borras modelos
🔄 **Mantienen historial** de todos los cambios realizados

## Comandos útiles:
```bash
python manage.py makemigrations  # Crea nuevas migraciones
python manage.py migrate         # Aplica migraciones a la BD
python manage.py showmigrations  # Muestra estado de migraciones
```

## Propósito:
Permite mantener la estructura de la base de datos sincronizada entre diferentes entornos (desarrollo, producción) y colaboradores del proyecto.





admin123