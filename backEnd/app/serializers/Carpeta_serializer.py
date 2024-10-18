
from rest_framework import serializers
from app.models import Carpeta


class CarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpeta
        fields = ['id', 'nombre', 'created_at', 'updated_at', 'subcarpeta']
        
class Folders(serializers.ModelSerializer):#este serializer esta destinado para ser usado en metodos get
    class Meta:
        model=Carpeta
        fields='__all__'
        
class newFolder(serializers.ModelSerializer):#este serializer esta destinado para ser usado en el metodo de creacion
    class Meta:
        model=Carpeta
        fields=['nombre']