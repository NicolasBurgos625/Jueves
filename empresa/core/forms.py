from django import forms
from .models import Trabajador, Paquete
from django.contrib.auth.models import User

class TrabajadorForm(forms.ModelForm):
    username = forms.CharField(max_length=150, help_text="Nombre de usuario para iniciar sesión")
    password = forms.CharField(widget=forms.PasswordInput, help_text="Contraseña para iniciar sesión")
    email = forms.EmailField(required=False)

    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellido', 'rut', 'direccion', 'telefono', 'rol']

    def save(self, commit=True):
        # Primero crear el usuario
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data.get('email', '')
        )
        user.is_staff = True  # Para acceder al admin
        user.save()

        # Luego crear el trabajador con el usuario
        trabajador = super().save(commit=False)
        trabajador.user = user
        
        if commit:
            trabajador.save()
        
        return trabajador

class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ['codigo', 'destinatario', 'direccion', 'estado', 'repartidor']
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password'] 

class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ['codigo', 'destinatario', 'direccion', 'estado', 'repartidor']  # Incluye los campos que deseas permitir que se editen


class EditarTrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellido', 'direccion', 'telefono']  # Excluir 'rut' y 'rol'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Si la instancia existe, asignamos los valores de 'rut' y 'rol' a initial
        if self.instance:
            self.fields['nombre'].initial = self.instance.nombre
            self.fields['apellido'].initial = self.instance.apellido
            self.fields['direccion'].initial = self.instance.direccion
            self.fields['telefono'].initial = self.instance.telefono

            # No permitimos modificar 'rut' y 'rol' en el formulario
            self.fields['rut'] = forms.CharField(initial=self.instance.rut, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
            self.fields['rol'] = forms.CharField(initial=self.instance.rol, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def save(self, commit=True):
        trabajador = super().save(commit=False)
        
        # Aseguramos que el 'rut' y 'rol' no cambien
        trabajador.rut = self.instance.rut
        trabajador.rol = self.instance.rol
        
        if commit:
            trabajador.save()
        return trabajador