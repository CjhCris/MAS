from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import CambioContrasenaForm
from .google_services import list_drive_folders, list_sheets_in_folder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from googleapiclient.discovery import build
from google.oauth2 import service_account
from .models import Tienda, Administrativo, Infraestructura
from django.conf import settings
import gspread
from oauth2client.service_account import ServiceAccountCredentials




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

def formulario_tienda(request, drive_id):
    # Lógica para manejar el parámetro 'drive_id'
    return render(request, 'home/formulario_tienda.html', {'drive_id': drive_id})

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




def navegar_drive(request, folder_id=None):
    
    if folder_id is None:
        folder_id = '19UXjCAiZu31lSnyH11272jt3WD8u4wLC'  
    
    
    folders = list_drive_folders(folder_id)
    
    sheets = list_sheets_in_folder(folder_id)
    
    return render(request, 'home/drive_browse.html', {
        'folders': folders,
        'sheets': sheets,
        'folder_id': folder_id
    })





SERVICE_ACCOUNT_FILE = 'home/credentials/credenciales_sheets.json'  # Ruta al archivo JSON de la cuenta de servicio
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def formulario_tienda(request, drive_id):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Autenticación con Google Sheets API
        SERVICE_ACCOUNT_FILE = 'home/credentials/credenciales_sheets.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=creds)

        # Diccionario que asocia los campos del formulario con las celdas de Google Sheets
        campos_a_celdas = {
            'codigo_eds': 'B22',
            'codigo_empresa': 'B14',
            'razon_social': ['B8', 'B19'],
            'cuenta_tbk': 'B16',
            'region': 'B28',
            'localidad': 'B27',
            'tienda_24hrs': 'B47',
            'pagos_noche': 'B50',
            'verificacion_sii': 'B15',
            'numero_cajeros': 'B17',
            'ciudad': 'B26',
            'horarios_turno': 'B32',
            'puerta_seguridad_cerrada': 'B48',
            'tipo_eds': 'B30',
            'rut_razonsocial': 'B20',
            'direccion': 'B24',
            'comuna': 'B25',
            'personal_turno': 'B33',
            'distancia_caja_puerta': 'B49',
        }

        def limpiar_valor(valor):
            return valor.strip() if isinstance(valor, str) and valor.strip() else '-'

        try:
            # Procesar los datos del formulario
            tipo_eds = limpiar_valor(data.get('tipo_eds', ''))
            if tipo_eds == '-':  # Verificar si no hay valor y asignar un valor por defecto
                tipo_eds = 'Desconocido'  # O el valor que se debería asignar por defecto

            tienda = Tienda(
                codigo_eds=limpiar_valor(data.get('codigo_eds', '')),
                razon_social=limpiar_valor(data.get('razon_social', '')),
                codigo_empresa=limpiar_valor(data.get('codigo_empresa', '')),
                verificacion_sii=limpiar_valor(data.get('verificacion_sii', '')) == 'SI',
                numero_cajeros=int(limpiar_valor(data.get('numero_cajeros', '0'))),
                rut_razonsocial=limpiar_valor(data.get('rut_razonsocial', '')),
                direccion=limpiar_valor(data.get('direccion', '')),
                comuna=limpiar_valor(data.get('comuna', '')),
                ciudad=limpiar_valor(data.get('ciudad', '')),
                localidad=limpiar_valor(data.get('localidad', '')),
                region=limpiar_valor(data.get('region', '')),
                cta_tbk=limpiar_valor(data.get('cuenta_tbk', '')),
                tipo_eds=limpiar_valor(data.get('tipo_eds', '')), # Guardar correctamente el valor de tipo_eds
            )
            tienda.save()

            # Enviar los datos a Google Sheets
            for campo, celda in campos_a_celdas.items():
                valor = limpiar_valor(data.get(campo, ''))

                if isinstance(celda, list):
                    for c in celda:
                        service.spreadsheets().values().update(
                            spreadsheetId=drive_id,
                            range=f"'Datos Comerciales'!{c}",
                            valueInputOption='RAW',
                            body={'values': [[valor]]}
                        ).execute()
                else:
                    service.spreadsheets().values().update(
                        spreadsheetId=drive_id,
                        range=f"'Datos Comerciales'!{celda}",
                        valueInputOption='RAW',
                        body={'values': [[valor]]}
                    ).execute()

            # Concatenar código_eds + localidad en B23
            cod_eds = limpiar_valor(data.get('codigo_eds', ''))
            localidad = limpiar_valor(data.get('localidad', ''))
            concatenado = f"{cod_eds} {localidad}".strip()

            service.spreadsheets().values().update(
                spreadsheetId=drive_id,
                range="'Datos Comerciales'!B23",
                valueInputOption='RAW',
                body={'values': [[concatenado or '-']]}  # Si concatenado está vacío, se pone "-"
            ).execute()

            return JsonResponse({'status': 'success'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return render(request, 'home/formulario_tienda.html', {'sheet_id': drive_id}) 
   
# FORMULARIO ADMINISTRATIVO

 # Actualiza esta ruta
SERVICE_ACCOUNT_FILE = 'home/credentials/credenciales_sheets.json'  # Ruta al archivo JSON de la cuenta de servicio
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
def guardar_formulario_admin(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        try:
            # Leer código EDS desde hoja de cálculo (celda B22)
            creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)
            service = build('sheets', 'v4', credentials=creds)

            hoja = 'Datos comerciales'
            spreadsheet_id = data.get('sheet_id')  # Obtiene el ID de la hoja

            # Obtener el código EDS desde la celda B22
            result = service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id,
                range=f"{hoja}!B22"
            ).execute()
            codigo_eds = result.get('values', [['']])[0][0]

            # Obtener la tienda basada en el código EDS
            tienda = Tienda.objects.get(codigo_eds=codigo_eds)

            # Crear el registro del administrador
            admin = Administrativo.objects.create(
                rut_admin=data.get('rut_admin'),
                nombre_admin=data.get('nombre_admin'),
                apellidos_admin=data.get('apellido_admin'),
                telefono=data.get('telefono'),
                correo_electronico=data.get('correo'),
                tienda=tienda
            )

            # Escribir datos en celdas específicas
            valores_a_insertar = {
                'B10': data.get('telefono'),
                'B11': data.get('nombre_admin'),
                'B12': data.get('apellido_admin'),
                'B13': data.get('rut_admin'),
                'B09': data.get('correo'),  # Se usa B14 para evitar conflicto con B10
            }

            for celda, valor in valores_a_insertar.items():
                service.spreadsheets().values().update(
                    spreadsheetId=spreadsheet_id,
                    range=f"{hoja}!{celda}",
                    valueInputOption='RAW',
                    body={'values': [[valor]]}
                ).execute()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Método no permitido'})
    # Autenticación con Google Sheets API

# Infraestructura

SERVICE_ACCOUNT_FILE = 'home/credentials/credenciales_sheets.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def guardar_formulario_infraestructura(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        try:
            creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)
            service = build('sheets', 'v4', credentials=creds)

            spreadsheet_id = data.get('sheet_id')
            hoja_comercial = 'Datos comerciales'
            hoja_tecnica = 'Datos Técnicos'

            # Obtener el código EDS desde la celda B22
            result = service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id,
                range=f"{hoja_comercial}!B22"
            ).execute()
            codigo_eds = result.get('values', [['']])[0][0]

            tienda = Tienda.objects.get(codigo_eds=codigo_eds)

            # Crear el registro en la base de datos
            infraestructura = Infraestructura.objects.create(
                tienda=tienda,
                altura_mueble=data.get('altura_mueble', 0),
                generador=(data.get('generador') == 'si'),
                tipo_tienda=data.get('tipo_tienda'),
                vuelto_tienda=(data.get('vuelto_tienda') == 'si'),
                vuelto_mrc=(data.get('vuelto_mrc') == 'si'),
                pos_a80=(data.get('pos_a80') == 'si'),
                vuelto_a80=(data.get('vuelto_a80') == 'si'),
                baño_cliente=(data.get('bano_cliente') == 'si'),
                cantidad_pos=data.get('cantidad_pos', 0),
                ups_respaldo=(data.get('ups_respaldo') == 'si')
            )

            # Preparar valores para la hoja "Datos comerciales"
            valores_comerciales = {
                'B31': data.get('tipo_tienda'),
                'B57': 'SI' if data.get('vuelto_tienda') == 'SI' else 'NO',
                'B58': 'SI' if data.get('vuelto_mrc') == 'SI' else 'NO',
                'B59': 'SI' if data.get('vuelto_a80') == 'SI' else 'NO',
                'B67': 'SI' if data.get('bano_cliente') == 'SI' else 'NO',
                'B88': data.get('cantidad_pos')
            }

            if data.get('bano_cliente') == 'NO':
                valores_comerciales.update({
                    'B68': '-',
                    'B69': '-',
                    'B70': '-',
                    'B71': '-'
                })
            else:
                if data.get('cobro_bano') == 'NO':
                    valores_comerciales.update({
                        'B70': '-',
                        'B71': '-'
                    })
                else:
                    valores_comerciales.update({
                        'B68': data.get('cobro_bano'),
                        'B69': data.get('monto_bano'),
                        'B70': data.get('metodo_pago'),
                        'B71': data.get('metodo_apertura_detalle') if data.get('metodo_apertura') == 'otro' else data.get('metodo_apertura')
                    })

            for celda, valor in valores_comerciales.items():
                service.spreadsheets().values().update(
                    spreadsheetId=spreadsheet_id,
                    range=f"{hoja_comercial}!{celda}",
                    valueInputOption='RAW',
                    body={'values': [[valor]]}
                ).execute()

            # Preparar valores para la hoja "Datos Técnicos"
            valores_tecnicos = {
                'B15': data.get('altura_mueble'),
                'V47': 'SI' if data.get('generador') == 'SI' else 'NO',
                'V52': 'SI' if data.get('ups_respaldo') == 'SI' else 'NO'
            }

            for celda, valor in valores_tecnicos.items():
                service.spreadsheets().values().update(
                    spreadsheetId=spreadsheet_id,
                    range=f"{hoja_tecnica}!{celda}",
                    valueInputOption='RAW',
                    body={'values': [[valor]]}
                ).execute()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Método no permitido'})

def test_google_auth():
    try:
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        print("Autenticación exitosa")
        return creds
    except Exception as e:
        print(f"Error de autenticación: {str(e)}")
        return None

test_google_auth()


