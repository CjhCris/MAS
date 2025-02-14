from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import PerfilUsuario

# Función para validar el formato del RUT chileno
def calcular_dv(rut):
    """Calcula el dígito verificador del RUT chileno."""
    rut = rut.replace("-", "").replace(".", "")  # Eliminar posibles puntos y guion
    rut_numero = int(rut[:-1])  # El RUT sin el dígito verificador
    dv = rut[-1].lower()  # El dígito verificador (puede ser un número o 'k')

    # Algoritmo para calcular el dígito verificador
    suma = 0
    multiplicador = 2
    while rut_numero > 0:
        suma += (rut_numero % 10) * multiplicador
        rut_numero //= 10
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    resto = suma % 11
    dv_calculado = 11 - resto
    if dv_calculado == 11:
        dv_calculado = "0"
    elif dv_calculado == 10:
        dv_calculado = "k"
    
    return str(dv_calculado)

def validar_rut(value):
    """Valida el RUT chileno."""
    value = value.replace(" ", "").replace("-", "").replace(".", "")  
    if len(value) < 8 or len(value) > 9:  
        raise ValidationError("El RUT ingresado no es válido.")
    
    rut_numero = value[:-1]  # RUT sin el dígito verificador
    dv = value[-1].lower()  # Dígito verificador
    
    if not rut_numero.isdigit():
        raise ValidationError("El RUT debe contener solo números y un dígito verificador válido.")
    # Calcular el dígito verificador
    dv_calculado = calcular_dv(value)  
    if dv != dv_calculado:
        raise ValidationError(f"El dígito verificador {dv} no es válido para el RUT {rut_numero}.")
    
    return value

# Validador de correo electrónico (para verificar si ya está registrado)
def validar_email(value):
    """Valida si el correo electrónico ya está registrado en la base de datos."""
    if User.objects.filter(email=value).exists():
        raise ValidationError("Este correo electrónico ya ha sido registrado.")
    return value

# Validador de nombre de usuario (para verificar si ya está registrado)
def validar_username(value):
    """Valida si el nombre de usuario ya está registrado en la base de datos."""
    if User.objects.filter(username=value).exists():
        raise ValidationError("Este nombre de usuario ya ha sido registrado.")
    return value

# Formulario de Registro de Usuario
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, validators=[validar_email])
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    rut = forms.CharField(label="RUT", max_length=12, required=True, validators=[validar_rut])
    username = forms.CharField(max_length=150, required=True, validators=[validar_username])  

    # Contraseñas
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    # Validación para comprobar que las contraseñas coinciden
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            PerfilUsuario.objects.create(user=user, rut=self.cleaned_data['rut'])
        return user


class CambioContrasenaForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña actual", required=True)
    new_password1 = forms.CharField(widget=forms.PasswordInput(), label="Nueva contraseña", required=True)
    new_password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmar nueva contraseña", required=True)

    # Validación personalizada para asegurarnos de que las contraseñas coinciden
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data