# Generated by Django 5.0.1 on 2024-02-05 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_educativa', '0002_alumnos'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='documentos',
            name='fecha',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='documentos',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]