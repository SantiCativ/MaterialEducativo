from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model=Usuarios
        fields= "__all__"
  
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:#sirve para persozaliar el json o diccionario que genera el serializador
        model=Usuarios
        fields=['username', 'email','password','certificado']
        
    def create(self, validated_data):#este metodo es llamado por el metodo save
        validated_data['password']=self.convert_hash_password(validated_data['password'])#obtengo un hash de la contraseña
        usuario=Usuarios.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            certificado=validated_data['certificado'],
            email=validated_data['email'],
            estado='Pendiente', 
            rol='Estudiante'  
            )
        return usuario #devuelvo el usuario creado al controlador que retornara una respuesta dependiendo si la creacion se logro
    
    def convert_hash_password(self, password):#este metodo recibe la contraseña del diccionario valided_data y devuelve un hash
        return make_password(password)
#Usuarios.objects.create=crea una instancia de usuario y la guarda en la base de datos

class UpdatedUserSerializer(serializers.ModelSerializer):
  class Meta:
      model=Usuarios
      fields=['username', 'password','certificado','email','foto']

