
from rest_framework import serializers
from app.models import Carpeta


class CarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpeta
        fields = ['id', 'nombre', 'created_at', 'updated_at', 'subcarpeta']
        
        
class newFolder(serializers.ModelSerializer):
    class Meta:
        model=Carpeta
        fields=['nombre']