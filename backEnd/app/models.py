from django.db import models
from django.contrib.auth.models import AbstractUser


def GetRutaField(instancia_user,namefield):
   return 'user_{0}/{1}'.format(instancia_user.id,namefield)
   
    
class Usuarios(AbstractUser):#AbstractUser contiene el modelo predeterminado que usa django
    foto=models.ImageField(null=True,blank=True,upload_to=GetRutaField)
    certificado= models.FileField(null=False,blank=False,upload_to=GetRutaField)
    USERNAME_FIELD = 'username'#este campo es por el cual se buscara al user en el metodo get_by_natural_key para autenticarlo
    EMAIL_FIELD = 'email'#este campo no es usado en la autenticacion
    REQUIRED_FIELDS =['email', 'password', 'certificado']
    estado = models.CharField(max_length=20, choices=(
        (1, 'Pendiente'),
        (2, 'Aprobado'),
        (3, 'Rechazado'),
    ), default='1')
    rol = models.CharField(max_length=20, choices=(#el campo rol podemos borrarlo porque ya esta is_staff que usa django
        (1, 'Estudiante'),
        (2, 'Administrador'),
        
    ), default='1')
    
    def __str__(self):
        return self.username
    
class Documentos(models.Model):
    title=models.CharField(max_length=50, null=False,blank=False)
    created_date=models.DateField(auto_now=True)
    file=models.FileField(null=False,blank=False,upload_to='files/', default='default/file/path.txt')
    owner=models.ForeignKey(Usuarios,on_delete=models.CASCADE,related_name='documents') #politica de integridad referencial(VER)
    state= models.CharField(max_length=20, choices=(#el campo rol podemos borrarlo porque ya esta is_staff que usa django
        (1, 'visible'),
        (2, 'oculto'),
        
    ), default='1')

    def __str__(self) -> str:
        return self.title
