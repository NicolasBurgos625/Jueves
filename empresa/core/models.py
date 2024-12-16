from django.db import models
from django.contrib.auth.models import User

class Trabajador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='trabajador')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    rol = models.CharField(max_length=50, choices=[('jefe', 'Jefe'), ('repartidor', 'Repartidor'), ('recursos_humanos', 'Recursos Humanos'), ('recepcionista', 'Recepcionista')])

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Paquete(models.Model):
    codigo = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    estado = models.CharField(max_length=50)
    repartidor = models.ForeignKey(Trabajador, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.codigo
    
class Notificacion(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='notificaciones')
    mensaje = models.CharField(max_length=255)
    visto = models.BooleanField(default=False)  # Para marcar si ya se vio
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)  # Para saber si la notificación está activa

    def __str__(self):
        return self.mensaje



