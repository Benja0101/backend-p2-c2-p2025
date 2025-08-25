from django.http import HttpResponse
def inicio(request):
    return HttpResponse("¡Bienvenido a mi sitio web!")


def mostrarBienvenida(request):
    tu_nombre = "Benjamin Salazar"
    return HttpResponse(f"¡Bienvenido a mi sitio web, {tu_nombre}!")