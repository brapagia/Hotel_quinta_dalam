"""
URL configuration for hotel_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from hotel_app import views  # Importamos las vistas que acabamos de crear

urlpatterns = [
    path('admin_django/', admin.site.urls), # URL del administrador interno de Django
    
    # Rutas de tu página web
    path('', views.inicio, name='inicio'), # Al entrar a la web principal (sin ruta) carga Index.html
    path('catalogo/', views.catalogo, name='catalogo'),
    path('reservaciones/', views.reservaciones, name='reservaciones'),
    path('registro/', views.registro, name='registro'),
    path('iniciar-sesion/', views.iniciosesion, name='iniciosesion'),
    path('contacto/', views.contacto, name='contacto'),
    path('conocenos/', views.conocenos, name='conocenos'),
    path('panel-admin/', views.panel_admin, name='panel_admin'),
    path('altas-bajas/', views.altas_bajas, name='altas_bajas'),
]
