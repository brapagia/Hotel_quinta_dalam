from django.shortcuts import render

# Cada función representa una página web de tu sitio
def inicio(request):
    return render(request, 'hotel_app/Index.html')

def catalogo(request):
    return render(request, 'hotel_app/Catalogo.html')

def reservaciones(request):
    return render(request, 'hotel_app/Reservaciones.html')

def registro(request):
    return render(request, 'hotel_app/Registro.html')

def iniciosesion(request):
    return render(request, 'hotel_app/Iniciosesion.html')

def contacto(request):
    return render(request, 'hotel_app/Contacto.html')

def conocenos(request):
    return render(request, 'hotel_app/Conocenos.html')

def panel_admin(request):
    return render(request, 'hotel_app/admin.html')

def altas_bajas(request):
    return render(request, 'hotel_app/AltasBajasForm.html')