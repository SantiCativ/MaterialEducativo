from django.shortcuts import get_object_or_404
from rest_framework import generics
from app.serializers.admin_serializer import *
from app.models import Departamento,Carrera,Materia
from rest_framework.permissions import IsAuthenticated

class GetDepartamentos(generics.ListAPIView):
     queryset=Departamento.objects.all()
     serializer_class=DepartamentoSerializer
     
class GetCarreras(generics.ListAPIView):
     queryset=Carrera.objects.all()
     serializer_class=CarreraSerializer
     
class GetMaterias(generics.ListAPIView):
     queryset=Materia.objects.all()
     serializer_class=MateriaSerializer
     
# class GetCarreras(generics.ListAPIView):
#      queryset=Carrera.objects.all()
#      serializer_class=CarreraSerializer
     