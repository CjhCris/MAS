from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import CambioContrasenaForm

# Vista para el registro de usuario
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Has iniciado sesión automáticamente.')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")  
    else:
        form = RegistroUsuarioForm()
    return render(request, 'home/registro.html', {'form': form})

# Vista para el inicio de sesión
def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {user.first_name}!')
                return redirect('home')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor, revisa los datos ingresados.')
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})


from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

@login_required
def cambiar_contrasena(request):
    if request.method == "POST":
        form = CambioContrasenaForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()  
            update_session_auth_hash(request, form.user)  
            messages.success(request, "¡Contraseña cambiada con éxito!")
            return redirect('perfil')  
        else:
            messages.error(request, "Hubo un error al intentar cambiar la contraseña.")
    else:
        form = CambioContrasenaForm(user=request.user)

    return render(request, 'home/cambiar_contrasena.html', {'form': form})
