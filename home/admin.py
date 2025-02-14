from django.contrib import admin
from .models import Empresa, PerfilUsuario, Documento, Tienda, RelevamientoMedia, ImagenError

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'rut')
    search_fields = ('nombre', 'rut')

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tienda', 'tipo_servicio', 'fecha', 'hora_inicio', 'hora_termino', 'archivo')
    list_filter = ('tipo_servicio', 'fecha', 'tienda')
    search_fields = ('tienda__codigo_eds', 'tipo_servicio', 'fecha')
    list_per_page = 10  


@admin.register(Tienda)
class TiendaAdmin(admin.ModelAdmin):
    list_display = ('codigo_eds', 'razon_social', 'correo_electronico', 'telefono', 'nombre_admin', 'numero_cajeros', 'comuna', 'ciudad', 'region', 'cta_tbk', 'tipo_eds', 'tipo_tienda', 'vuelto_tienda', 'vuelto_mrc', 'pos_a80', 'ubereats', 'rappi', 'pedidosya', 'justo', 'preciodiferenciado', 'baño_cliente', 'cantidad_pos', 'ups_respaldo')
    search_fields = ('codigo_eds', 'razon_social', 'correo_electronico', 'nombre_admin')
    list_filter = ('tipo_eds', 'region', 'verificacion_sii')
    ordering = ('razon_social',)


class RelevamientoMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'relevamiento', 'foto_estacion_servicio', 'foto_boleta', 'video_tienda', 'foto_distancia_meson_puerta', 'foto_rack', 'video_rack', 'foto_ups', 'foto_red_wifi', 'foto_sii', 'foto_ip', 'foto_sistema_operativo', 'foto_version_office')
    
    # Filtros y búsqueda
    search_fields = ['relevamiento__tienda__codigo_eds']
    list_filter = ['relevamiento']
    
    # Fila para previsualizar las imágenes
    def get_image_preview(self, obj):
        return f"<img src='{obj.foto_estacion_servicio.url}' width='100' />" if obj.foto_estacion_servicio else "No image"
    get_image_preview.allow_tags = True

    # Lista de campos en la vista de detalles
    fieldsets = (
        (None, {
            'fields': ('relevamiento',)
        }),
        ('Fotos y Videos', {
            'fields': (
                'foto_estacion_servicio','foto_boleta', 'video_tienda', 'foto_distancia_meson_puerta', 'foto_rack', 'video_rack',
                'foto_ups', 'foto_red_wifi', 'foto_sii', 'foto_ip', 'foto_sistema_operativo', 'foto_version_office'
            )
        }),
        ('Fotos de Bodega', {
            'fields': (
                'fotos_bodega_1', 'fotos_bodega_2', 'fotos_bodega_3', 'fotos_bodega_4', 'fotos_bodega_5', 'fotos_bodega_6', 
                'fotos_bodega_7', 'fotos_bodega_8', 'fotos_bodega_9'
            )
        }),
        ('Fotos de Puntos de Red', {
            'fields': ('fotos_puntos_red_1', 'fotos_puntos_red_2', 'fotos_puntos_red_3')
        }),
        ('Fotos de Enchufes', {
            'fields': ('fotos_enchufes_1', 'fotos_enchufes_2', 'fotos_enchufes_3')
        }),
        ('Fotos de Pantallas', {
            'fields': (
                'fotos_pantallas_1', 'fotos_pantallas_2', 'fotos_pantallas_3', 'fotos_pantallas_4', 
                'fotos_pantallas_5', 'fotos_pantallas_6'
            )
        }),
        ('Fotos de Bollería', {
            'fields': (
                'fotos_bolleria_1', 'fotos_bolleria_2', 'fotos_bolleria_3', 'fotos_bolleria_4', 
                'fotos_bolleria_5', 'fotos_bolleria_6'
            )
        }),
        ('Fotos de Refrigeradores', {
            'fields': (
                'fotos_refrigeradores_1', 'fotos_refrigeradores_2', 'fotos_refrigeradores_3', 'fotos_refrigeradores_4', 
                'fotos_refrigeradores_5', 'fotos_refrigeradores_6'
            )
        }),
        ('Fotos de Medidas', {
            'fields': ('foto_altura', 'foto_profundidad', 'foto_ancho', 'foto_voltaje')
        }),
        ('Fotos de Vista', {
            'fields': ('foto_vista_atendedor', 'foto_vista_cliente')
        })
    )

    list_display_links = ('id', 'relevamiento')
    ordering = ('id',)

admin.site.register(RelevamientoMedia, RelevamientoMediaAdmin)




# Define un admin personalizado para Documento
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']  # Agrega los campos que desees mostrar
    search_fields = ['nombre']  # Si deseas permitir la búsqueda por nombre

# Define el admin para ImagenError
class ImagenErrorAdmin(admin.ModelAdmin):
    list_display = ['id', 'documento', 'imagen_error']
    search_fields = ['documento__nombre']

# Registra los modelos con su respectivo admin
admin.site.register(ImagenError, ImagenErrorAdmin)
