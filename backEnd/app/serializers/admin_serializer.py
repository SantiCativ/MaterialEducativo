from rest_framework import serializers
from app.models import Departamento,Carrera,Materia

#ESTE SERIALIZADOR PARA LOS CRUDS DE DEPARTAMENTO,CARRERA Y MATERIA


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields=['nombre']
        

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields=['nombre']
        
class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields=['nombre']
