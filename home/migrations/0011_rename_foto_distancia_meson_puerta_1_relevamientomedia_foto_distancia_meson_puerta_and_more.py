# Generated by Django 5.0.6 on 2025-02-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_relevamientomedia_fotos_bodega_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relevamientomedia',
            old_name='foto_distancia_meson_puerta_1',
            new_name='foto_distancia_meson_puerta',
        ),
        migrations.RenameField(
            model_name='relevamientomedia',
            old_name='foto_rack_1',
            new_name='foto_rack',
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='foto_ip',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/ip/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='foto_red_wifi',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/red_wifi/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='foto_sii',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/sii/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='foto_sistema_operativo',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/sistema_operativo/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='foto_ups',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/ups/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='foto_version_office',
            field=models.ImageField(blank=True, null=True, upload_to='relevamiento_media/version_office/'),
        ),
        migrations.AddField(
            model_name='relevamientomedia',
            name='video_rack',
            field=models.FileField(blank=True, null=True, upload_to='relevamiento_media/video_rack/'),
        ),
    ]
