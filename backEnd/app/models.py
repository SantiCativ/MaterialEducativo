from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


#este metodo me crea y devuelve una ruta para una carpeta con el id del usuario, es dinamico
def GetRutaField(instancia_user,namefield):
   return 'user_{0}/{1}'.format(instancia_user.id,namefield)
   


class Documentos(models.Model):
    nombre=models.CharField(max_length=50, null=True)
    fecha=models.DateField(null=True)

    def __str__(self) -> str:
        return self.nombre
    
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username=username)
    
class Usuarios(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=50, unique=True)
    email=models.EmailField(max_length=100,unique=True)
    foto=models.ImageField(null=True,blank=True,upload_to=GetRutaField)
    password= models.CharField(max_length=100)
    certificado= models.FileField(null=False,blank=False,upload_to=GetRutaField)
    is_staff=models.BooleanField(default=False, blank=False)#este campo sirve para saber si es un admin o no
    is_active=models.BooleanField(default=True)
    objects=UserManager()
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