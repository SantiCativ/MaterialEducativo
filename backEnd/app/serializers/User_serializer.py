from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from app.models import Usuarios
from django.contrib.auth.tokens import default_token_generator

class resetPasswordConfirm(serializers.ModelSerializer):#falta que envie un email para cambiar contraseña
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=5, write_only=True)
    email = serializers.EmailField()
    class Meta:
        model = Usuarios
        fields = ['email','token', 'new_password']

    def validate(self, data):
        email = data.get('email')
        token=data.get('token')
        new_password=data.get('new_password')
        if not email:
            raise serializers.ValidationError({'email': 'Email es requerido'})
        if not token:
            raise serializers.ValidationError({'token': 'Token es requerido'})
        if not new_password:
            raise serializers.ValidationError({'new_password': 'Nueva contraseña es requerida'})
        try:
            user = Usuarios.objects.get(email=email)
        except Usuarios.DoesNotExist:
            raise serializers.ValidationError({'email': 'Usuario no encontrado.'})
        if not default_token_generator.check_token(user,token):
            raise serializers.ValidationError({'token':'Token inválido o expirado.'})
        data['user'] = user
        return data

    def save(self, **kwargs):
        email = self.validated_data['email']
        new_password=self.validated_data['new_password']
        user = Usuarios.objects.get(email=email)
        user.set_password(new_password)
        user.save()  
        return user


class getUsers(serializers.ModelSerializer):
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)
    class Meta:
        model = Usuarios
        fields = ["id", "username", "email", "certificado", "estado", "estado_display"]

class getUser(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ["id", "username", "email", "certificado", "estado"]
        
class createUser(serializers.ModelSerializer):
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

class updatedUser(serializers.ModelSerializer):
  class Meta:
      model=Usuarios
      fields=['username', 'password','certificado','email','foto']

# Usuarios.objects.create=crea una instancia de usuario y la guarda en la base de datos

class updatedEstado(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['estado']
        
class resetPassword(serializers.ModelSerializer):
    class Meta:
        model=Usuarios  
        fields=['email']  
    def validate_email(self, value):
        if not Usuarios.objects.filter(email=value).exists():
            raise serializers.ValidationError("no existe ningún usuario registrado con este email.")
        return value 


