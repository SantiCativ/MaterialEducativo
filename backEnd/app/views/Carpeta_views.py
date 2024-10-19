from django.shortcuts import get_object_or_404
from rest_framework import generics
from app.serializers.Carpeta_serializer import *
from app.models import Carpeta,Usuarios
from rest_framework.permissions import IsAuthenticated

#?ACLARACION GENERAL DE ISAUTHENTICATED, TODOS LOS CONTROLADORES QUE TIENEN ESO SIGNIFICA QUE EN LA REQUEST VENDRA LA DATA
#?DEL USER QUE REALIZO LA PETICION, EN CASO DE QUE EL CONTROLADOR NO TENGA ISAUTHENTICATED ESO HARA QUE LA REQUEST TENGA 
#?UN CAMPO USER, PERO ESTE NO TENDRA LA DATA DE NINGUN USUARIO SINO QUE TENDRA UN ESTADO ANONIMO, POR ELLO LA REQUEST SIEMPRE
#?TENDRA EL CAMPO USER, PERO SU VALOR DEPENDE DE SI EL CONTROLADOR PIDE AUTENTICACION O NO.


class CarpetasModificadas(generics.ListAPIView):
    serializer_class=CarpetaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUser=self.kwargs['idUser']
        return Carpeta.objects.filter(usuario=idUser).order_by('-updated_at')[:3]

class UserFolders(generics.ListAPIView):
    serializer_class=Folders
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user_id=self.kwargs['pk']  
        user=get_object_or_404(Usuarios,id=user_id)
        return Carpeta.objects.filter(usuario=user)
    

class UserFolder(generics.RetrieveAPIView):
    queryset=Carpeta.objects.all()
    serializer_class=Folders
    permission_classes=[IsAuthenticated]
    def get_object(self):
        user=self.request.user
        carpeta_id=self.kwargs.get('pk')
        return Carpeta.objects.get(id=carpeta_id,usuario=user)
    
class CreateFolder(generics.CreateAPIView):
    serializer_class=newFolder
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
        
