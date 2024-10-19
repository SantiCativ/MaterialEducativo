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
        fields=["title", "created_at","file"]
        
class userDocumentsFavorito(serializers.ModelSerializer):#este es un serialzidor generico, solo para recuper un doc para el usuario
        owner_name = serializers.CharField(source='owner.username', read_only=True)    
        class Meta:
         model=Documentos
         fields=["title", "created_at","file","owner_name"]
         
         
class DocumentsSuggested(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.username', read_only=True)
    owner_foto = serializers.CharField(source='owner.foto', read_only=True)
    
    class Meta:
        model=Documentos
        fields=["title", "created_at","file","owner_name","owner_foto"]
    
        

