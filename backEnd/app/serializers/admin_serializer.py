from rest_framework import serializers
from app.models import Departamento,Carrera,Materia

#ESTE SERIALIZADOR PARA LOS CRUDS DE DEPARTAMENTO,CARRERA Y MATERIA


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields='__all__'
