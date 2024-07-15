from django.db import models

def GetRutaField(instancia_user,namefield):
   return 'user_{0}/{1}'.format(instancia_user.id,namefield)

class Documentos(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    fecha = models.DateField(null=True)

    def __str__(self) -> str:
        return self.nombre


class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    foto = models.ImageField(null=True, blank=True,upload_to=GetRutaField)
    contrasenia = models.CharField(max_length=100)
    certificado = models.FileField(null=False, blank=False,upload_to='certificados/')
    estado = models.CharField(
        max_length=20,
        choices=(
            (1, "Pendiente"),
            (2, "Aprobado"),
            (3, "Rechazado"),
        ),
        default="1",
    )

    rol = models.CharField(
        max_length=20,
        choices=(
            (1, "Estudiante"),
            (2, "Administrador"),
        ),
        default="1",
    )

    def __str__(self):
        return self.nombre
