
from rest_framework import serializers
from app.models import Carpeta


class CarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpeta
        fields = ['id', 'nombre', 'created_at', 'updated_at', 'subcarpeta']
        
class Folders(serializers.ModelSerializer):
    class Meta:
        model=Carpeta
        fields='__all__'
        
class newFolder(serializers.ModelSerializer):
    class Meta:
        model=Carpeta
        fields=['nombre']