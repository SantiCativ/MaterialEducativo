from rest_framework import serializers
from app.models import Documentos,Carpeta
from app.serializers.User_serializer import *

class DocumentSerializer(serializers.ModelSerializer):#sirve para la creacion de un documento
    class Meta:
        model=Documentos
        fields=["title", "created_at","file", "owner_id", "state"]
        
    def create(self, validated_data):
        return Documentos.objects.create(**validated_data)
    
class Documents(serializers.ModelSerializer):#esta orientado para ser usado en la zona del admin
    owner=getUser()
    class Meta:
        model=Documentos
        fields='__all__'
        
class updateState(serializers.ModelSerializer):
    class Meta:
        model=Documentos
        fields=['state']
        
class userDocuments(serializers.ModelSerializer):#este es un serialzidor generico, solo para recuper un doc para el usuario
    class Meta:
        model=Documentos
        fields=["title", "created_date","file"]
        
class userDocumentsFavorito(serializers.ModelSerializer):#este es un serialzidor generico, solo para recuper un doc para el usuario
        owner_name = serializers.CharField(source='owner.username', read_only=True)    
        class Meta:
         model=Documentos
         fields=["title", "created_date","file","owner_name"]
        
class Folders(serializers.ModelSerializer):#este serializer esta destinado para ser usado en metodos get
    class Meta:
        model=Carpeta
        fields='__all__'
        
class newFolder(serializers.ModelSerializer):#este serializer esta destinado para ser usado en el metodo de creacion
    class Meta:
        model=Carpeta
        fields=['nombre']
