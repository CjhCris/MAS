from django.urls import path
from .views import home , registro_usuario, login_usuario, cambiar_contrasena

urlpatterns = [
    path('', home, name='home'),
    path('registro/', registro_usuario, name='registro'),
    path('login/', login_usuario, name='login'),
    path('cambiar-contrasena/', cambiar_contrasena, name='cambiar_contrasena')
]
