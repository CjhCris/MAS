from django.urls import path
from .views import home , registro_usuario, login_usuario, cambiar_contrasena, navegar_drive, formulario_tienda
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('registro/', registro_usuario, name='registro'),
    path('login/', login_usuario, name='login'),
    path('cambiar-contrasena/', cambiar_contrasena, name='cambiar_contrasena'),
    path('drive/navegar/', navegar_drive, name='navegar_drive'), 
    path('drive/navegar/', views.navegar_drive, name='navegar_drive'),
    path('drive/navegar/<str:folder_id>/', views.navegar_drive, name='navegar_drive'),
    path('formulario_tienda/<str:drive_id>/', views.formulario_tienda, name='formulario_tienda'),
    path('guardar_formulario_admin/', views.guardar_formulario_admin, name='guardar_formulario_admin'),
    path('guardar_formulario_infraestructura/', views.guardar_formulario_infraestructura, name='guardar_formulario_infraestructura'),
   

    
]
