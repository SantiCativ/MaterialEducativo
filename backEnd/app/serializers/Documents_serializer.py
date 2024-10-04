from rest_framework import serializers
from app.models import Documentos
from app.serializers.User_serializer import *

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Documentos
        fields=["title", "created_at","file", "owner_id", "state"]
        
    def create(self, validated_data):
        return Documentos.objects.create(**validated_data)
    
class Documents(serializers.ModelSerializer):
    owner=getUser()
    class Meta:
        model=Documentos
        fields='__all__'
        
class updateState(serializers.ModelSerializer):
    class Meta:
        model=Documentos
        fields=['state']
        
        


        
        
        