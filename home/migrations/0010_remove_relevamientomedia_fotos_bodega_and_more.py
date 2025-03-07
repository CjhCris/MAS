# Generated by Django 5.0.6 on 2025-02-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_relevamientomedia_foto_boleta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relevamientomedia',
            name='fotos_bodega',
        ),
        migrations.RemoveField(
            model_name='relevamientomedia',
            name='fotos_bolleria',
        ),
        migrations.RemoveField(
            model_name='relevamientomedia',
            name='fotos_enchufes',
        ),
        migrations.RemoveField(
            model_name='relevamientomedia',
            name='fotos_pantallas',
        ),
        migrations.RemoveField(
            model_name='relevamientomedia',
            name='fotos_productos_errores',
        ),
        migrations.RemoveField(
            model_name='relevamientomedia',
            name='fotos_puntos_red',
        ),
        migrations.RemoveField(
            model_name='relevamientomedia',
            name='fotos_refrigeradores',
        ),
        migrations.RenameField(
            model_name='relevamientomedia',
            old_name='foto_distancia_meson_puerta',
            new_name='foto_distancia_meson_puerta_1',
        ),
        migrations.RenameField(
            model_name='relevamientomedia',
            old_name='foto_rack',
            new_name='foto_rack_1',
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bodega_1',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bodega/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bodega_2',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bodega/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bodega_3',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bodega/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bodega_4',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bodega/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bodega_5',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bodega/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bodega_6',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bodega/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bodega_7',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bodega/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bodega_8',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bodega/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bodega_9',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bodega/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bolleria_1',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bolleria/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bolleria_2',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bolleria/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bolleria_3',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bolleria/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bolleria_4',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bolleria/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bolleria_5',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bolleria/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_bolleria_6',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/bolleria/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_enchufes_1',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/enchufes/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_enchufes_2',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/enchufes/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_enchufes_3',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/enchufes/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_pantallas_1',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/pantallas/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_pantallas_2',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/pantallas/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_pantallas_3',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/pantallas/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_pantallas_4',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/pantallas/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_pantallas_5',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/pantallas/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_pantallas_6',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/pantallas/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_puntos_red_1',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/puntos_red/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_puntos_red_2',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/puntos_red/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_puntos_red_3',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/puntos_red/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_refrigeradores_1',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/refrigeradores/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_refrigeradores_2',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/refrigeradores/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_refrigeradores_3',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/refrigeradores/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_refrigeradores_4',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/refrigeradores/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_refrigeradores_5',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/refrigeradores/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='fotos_refrigeradores_6',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/refrigeradores/'),
        ),
        migrations.DeleteModel(
            name='FotoBodega',
        ),
        migrations.DeleteModel(
            name='FotoBolleria',
        ),
        migrations.DeleteModel(
            name='FotoEnchufe',
        ),
        migrations.DeleteModel(
            name='FotoPantalla',
        ),
        migrations.DeleteModel(
            name='FotoProductoError',
        ),
        migrations.DeleteModel(
            name='FotoPuntoRed',
        ),
        migrations.DeleteModel(
            name='FotoRefrigerador',
        ),
    ]
