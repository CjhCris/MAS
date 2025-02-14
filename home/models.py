from django.db import models
from django.contrib.auth.models import User  

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=255, unique=True)
    rut = models.CharField(max_length=12, unique=True)  
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)  

    def __str__(self):
        return self.nombre


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.rut}"

    

class Tienda(models.Model):
    codigo_eds = models.CharField(max_length=6, primary_key=True, unique=True)  
    razon_social = models.CharField(max_length=50)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    nombre_admin = models.CharField(max_length=100)
    apellidos_admin = models.CharField(max_length=100)
    rut_admin = models.CharField(max_length=12, unique=True)
    codigo_empresa = models.CharField(max_length=10)  
    verificacion_sii = models.BooleanField(default=False)  
    numero_cajeros = models.CharField(max_length=2)
    rut_razonsocial = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    comuna = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)  
    region = models.CharField(max_length=100)
    cta_tbk = models.CharField(max_length=100, default="0")
    tipo_eds = models.CharField(max_length=15)

    TIPO_EDS_CHOICES = [
        ('ASISTIDO', 'Asistido'),
        ('MIXTA', 'Mixta'),
        ('AUTOSERVICIO', 'Autoservicio')
    ]
    tipo_eds = models.CharField(max_length=15, choices=TIPO_EDS_CHOICES)

    cantidad_bano = models.CharField(max_length=1)
    altura_mueble = models.CharField(max_length=4)  
    generador = models.BooleanField(default=False)  
    tipo_tienda = models.CharField(max_length=15, default="0")
    vuelto_tienda =models.BooleanField(default=False)
    vuelto_mrc = models.BooleanField(default=False)
    pos_a80 = models.BooleanField(default=False)
    ubereats = models.BooleanField(default=False)
    rappi = models.BooleanField(default=False)  
    pedidosya = models.BooleanField(default=False)
    justo = models.BooleanField(default=False)
    preciodiferenciado = models.BooleanField(default=False)
    baño_cliente = models.BooleanField(default=False)
    cantidad_pos = models.CharField(max_length=15, default="0")
    ups_respaldo = models.BooleanField(default=False)
    comentarios = models.TextField(max_length=2000)  

    def __str__(self):
        return f"{self.codigo_eds} - {self.razon_social}"
    
    

class Documento(models.Model):
    SERVICIOS = [
        ('Relevamiento', 'Relevamiento'),
        ('Comisionado', 'Comisionado'),
        ('Implementación', 'Implementación'),
        ('Otro', 'Otro')
    ]
    
    id = models.AutoField(primary_key=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True, blank=True)
    tipo_servicio = models.CharField(max_length=50, choices=SERVICIOS, default='Otro')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    archivo = models.FileField(upload_to='documentos/', null=True, blank=True)

    def __str__(self):
        return f"Documento {self.id} - {self.tipo_servicio} - {self.tienda.codigo_eds}"
    


class RelevamientoMedia(models.Model):
    id = models.AutoField(primary_key=True)

    # Relación con Documento (debe ser un Documento de tipo 'Relevamiento')
    relevamiento = models.ForeignKey(Documento, on_delete=models.CASCADE, limit_choices_to={'tipo_servicio': 'Relevamiento'})

    # Fotos y Videos
    foto_estacion_servicio = models.ImageField(upload_to='relevamiento_media/estacion_servicio/', null=True, blank=True)
    foto_boleta = models.ImageField(upload_to='relevamiento_media/estacion_servicio/', null=True, blank=True)
    video_tienda = models.FileField(upload_to='relevamiento_media/video_tienda/', null=True, blank=True)

    
    foto_distancia_meson_puerta = models.ImageField(upload_to='relevamiento_media/distancia_meson_puerta/', null=True, blank=True)

    foto_rack = models.ImageField(upload_to='relevamiento_media/rack/', null=True, blank=True)
    video_rack = models.FileField(upload_to='relevamiento_media/video_rack/', null=True, blank=True)  # Video del Rack

    fotos_bodega_1 = models.ImageField(upload_to='relevamiento_media/bodega/', null=True, blank=True)
    fotos_bodega_2 = models.ImageField(upload_to='relevamiento_media/bodega/', null=True, blank=True)
    fotos_bodega_3 = models.ImageField(upload_to='relevamiento_media/bodega/', null=True, blank=True)
    fotos_bodega_4 = models.ImageField(upload_to='relevamiento_media/bodega/', null=True, blank=True)
    fotos_bodega_5 = models.ImageField(upload_to='relevamiento_media/bodega/', null=True, blank=True)
    fotos_bodega_6 = models.ImageField(upload_to='relevamiento_media/bodega/', null=True, blank=True)
    fotos_bodega_7 = models.ImageField(upload_to='relevamiento_media/bodega/', null=True, blank=True)
    fotos_bodega_8 = models.ImageField(upload_to='relevamiento_media/bodega/', null=True, blank=True)
    fotos_bodega_9 = models.ImageField(upload_to='relevamiento_media/bodega/', null=True, blank=True)

    fotos_puntos_red_1 = models.ImageField(upload_to='relevamiento_media/puntos_red/', null=True, blank=True)
    fotos_puntos_red_2 = models.ImageField(upload_to='relevamiento_media/puntos_red/', null=True, blank=True)
    fotos_puntos_red_3 = models.ImageField(upload_to='relevamiento_media/puntos_red/', null=True, blank=True)

    fotos_enchufes_1 = models.ImageField(upload_to='relevamiento_media/enchufes/', null=True, blank=True)
    fotos_enchufes_2 = models.ImageField(upload_to='relevamiento_media/enchufes/', null=True, blank=True)
    fotos_enchufes_3 = models.ImageField(upload_to='relevamiento_media/enchufes/', null=True, blank=True)

    fotos_pantallas_1 = models.ImageField(upload_to='relevamiento_media/pantallas/', null=True, blank=True)
    fotos_pantallas_2 = models.ImageField(upload_to='relevamiento_media/pantallas/', null=True, blank=True)
    fotos_pantallas_3 = models.ImageField(upload_to='relevamiento_media/pantallas/', null=True, blank=True)
    fotos_pantallas_4 = models.ImageField(upload_to='relevamiento_media/pantallas/', null=True, blank=True)
    fotos_pantallas_5 = models.ImageField(upload_to='relevamiento_media/pantallas/', null=True, blank=True)
    fotos_pantallas_6 = models.ImageField(upload_to='relevamiento_media/pantallas/', null=True, blank=True)

    fotos_bolleria_1 = models.ImageField(upload_to='relevamiento_media/bolleria/', null=True, blank=True)
    fotos_bolleria_2 = models.ImageField(upload_to='relevamiento_media/bolleria/', null=True, blank=True)
    fotos_bolleria_3 = models.ImageField(upload_to='relevamiento_media/bolleria/', null=True, blank=True)
    fotos_bolleria_4 = models.ImageField(upload_to='relevamiento_media/bolleria/', null=True, blank=True)
    fotos_bolleria_5 = models.ImageField(upload_to='relevamiento_media/bolleria/', null=True, blank=True)
    fotos_bolleria_6 = models.ImageField(upload_to='relevamiento_media/bolleria/', null=True, blank=True)

    fotos_refrigeradores_1 = models.ImageField(upload_to='relevamiento_media/refrigeradores/', null=True, blank=True)
    fotos_refrigeradores_2 = models.ImageField(upload_to='relevamiento_media/refrigeradores/', null=True, blank=True)
    fotos_refrigeradores_3 = models.ImageField(upload_to='relevamiento_media/refrigeradores/', null=True, blank=True)
    fotos_refrigeradores_4 = models.ImageField(upload_to='relevamiento_media/refrigeradores/', null=True, blank=True)
    fotos_refrigeradores_5 = models.ImageField(upload_to='relevamiento_media/refrigeradores/', null=True, blank=True)
    fotos_refrigeradores_6 = models.ImageField(upload_to='relevamiento_media/refrigeradores/', null=True, blank=True)

   
    foto_altura = models.ImageField(upload_to='relevamiento_media/altura/', null=True, blank=True)
    foto_profundidad = models.ImageField(upload_to='relevamiento_media/profundidad/', null=True, blank=True)
    foto_ancho = models.ImageField(upload_to='relevamiento_media/ancho/', null=True, blank=True)
    foto_voltaje = models.ImageField(upload_to='relevamiento_media/voltaje/', null=True, blank=True)

   
    foto_vista_atendedor = models.ImageField(upload_to='relevamiento_media/vista_atendedor/', null=True, blank=True)
    foto_vista_cliente = models.ImageField(upload_to='relevamiento_media/vista_cliente/', null=True, blank=True)

    foto_ups = models.ImageField(upload_to='relevamiento_media/ups/', null=True, blank=True)  # Foto del UPS
    foto_red_wifi = models.ImageField(upload_to='relevamiento_media/red_wifi/', null=True, blank=True)  # Foto de las redes wifi
    foto_sii = models.ImageField(upload_to='relevamiento_media/sii/', null=True, blank=True)  # Foto del SII
    foto_ip = models.ImageField(upload_to='relevamiento_media/ip/', null=True, blank=True)  # Foto de la IP
    foto_sistema_operativo = models.ImageField(upload_to='relevamiento_media/sistema_operativo/', null=True, blank=True)  # Foto del sistema operativo
    foto_version_office = models.ImageField(upload_to='relevamiento_media/version_office/', null=True, blank=True)  # Foto de versión de Office

    def __str__(self):
        return f"Relevamiento {self.relevamiento.id} - {self.relevamiento.tienda.codigo_eds}"


class ImagenError(models.Model):
    id = models.AutoField(primary_key=True)
    
    
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE, related_name='imagenes_error')
    
    
    imagen_error = models.ImageField(upload_to='documentos/errores/', null=True, blank=True)
    
    def __str__(self):
        return f"Error {self.id} - Documento {self.documento.nombre}"
