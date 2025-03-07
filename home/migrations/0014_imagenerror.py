# Generated by Django 5.0.6 on 2025-02-10 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_delete_imagenerror'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenError',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen_error', models.ImageField(blank=True, null=True, upload_to='documentos/errores/')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_error', to='home.documento')),
            ],
        ),
    ]
