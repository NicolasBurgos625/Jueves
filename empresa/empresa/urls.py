"""
URL configuration for empresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import redirect
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', lambda request: redirect('index')),  
    path('index/', views.login_view, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('jefe/', views.jefe_dashboard, name='jefe_dashboard'),  # Para todos los empleados
    path('dashboard/<str:rol>/', views.jefe_dashboard, name='jefe_dashboard_rol'),  # Para filtrar por rol
    path('recursos_humanos/', views.recursos_humanos_dashboard, name='recursos_humanos_dashboard'),
    path('repartidor/', views.repartidor_dashboard, name='repartidor_dashboard'),
    path('recepcionista/', views.recepcionista_dashboard, name='recepcionista_dashboard'),
    path('editar_trabajador/', views.editar_trabajador, name='editar_trabajador'),
    path('descargar_tabla/', views.descargar_tabla, name='descargar_tabla'),
    path('paquete/<int:paquete_id>/', views.paquete_detail, name='paquete_detail'),
    path('asignar_paquete/<int:paquete_id>/', views.asignar_paquete, name='asignar_paquete'),
    path('registrar_trabajador/', views.registrar_trabajador, name='registrar_trabajador'),
    path('paquete/<int:paquete_id>/actualizar_estado/', views.actualizar_estado_paquete, name='actualizar_estado_paquete'),
    path('eliminar_trabajador/<int:trabajador_id>/', views.eliminar_trabajador, name='eliminar_trabajador'),
    path('modificar_trabajador/<int:trabajador_id>/', views.modificar_trabajador, name='modificar_trabajador'),
    path('desactivar_notificacion/<int:notificacion_id>/', views.desactivar_notificacion, name='desactivar_notificacion'),
    path('paquete/<int:paquete_id>/', views.paquete_detail, name='paquete_detail'),
    path('paquete/editar/<int:paquete_id>/', views.editar_paquete, name='editar_paquete'),
]








