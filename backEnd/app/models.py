from django.db import models

# Create your models here.
class Documentos(models.Model):
    nombre=models.CharField(max_length=50, null=True)
    fecha=models.DateField(null=True)

    def __str__(self) -> str:
        return self.nombre
    
class Alumnos(models.Model):
    nombre=models.CharField( max_length=50, null=True)
    email=models.EmailField(max_length=254, null=True)