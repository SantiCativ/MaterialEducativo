# Generated by Django 5.0.1 on 2024-02-05 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_educativa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]