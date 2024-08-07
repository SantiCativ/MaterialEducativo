# Generated by Django 4.2 on 2024-07-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_usuarios_certificado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='file',
            field=models.FileField(upload_to='media/documents'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='certificado',
            field=models.FileField(upload_to='media/certificates'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='media/photos'),
        ),
    ]
