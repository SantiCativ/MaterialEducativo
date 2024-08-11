from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import AbstractUser


# fsCertificates = FileSystemStorage(location='media/certificates')
# fsPhotos=FileSystemStorage(location='media/photos')
fsDocuments=FileSystemStorage(location='media/documents')


   
    
class Usuarios(AbstractUser):#AbstractUser contiene el modelo predeterminado que usa django
    foto=models.ImageField(upload_to='photos',null=True,blank=True)
    certificado= models.FileField(upload_to='certificates',null=False,blank=False)
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
    file=models.FileField(upload_to='documents',null=False,blank=False)
    owner=models.ForeignKey(Usuarios,on_delete=models.CASCADE,related_name='documents') #politica de integridad referencial(VER)
    score_sum=models.DecimalField(default=0,max_digits=10,decimal_places=2)#contiene la suma de todas las calificaciones
    score_cant=models.IntegerField(default=0)#contiene la cantidad de calificaciones realizadas a un documento
    state= models.CharField(max_length=20, choices=(
        (1, 'visible'),
        (2, 'oculto'),
        
    ), default='1')
    @property#esto sirve para que la funcion average_score la pueda llamar como si fuera un campo de mi modelo, solo aplica ala funcion que tiene acontinuacion
    def average_score(self):#me devuelve el promedio de calificaciones
        if self.score_cant==0 :#si no tiene calificaciones devuelve 0
            return 0
        return self.score_sum/self.score_cant#en caso de tener calificaciones me devuelve el promedio
    
    def add_score(self,number):#este metodo me sirve para guardar una calficacion a un documento
       self.score_sum+=number
       self.score_cant+=1
       self.save()

    def __str__(self):
        return self.title
