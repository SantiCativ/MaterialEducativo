from django.shortcuts import get_object_or_404
from rest_framework import generics
from app.serializers.Carpeta_serializer import *
from app.models import Carpeta,Usuarios
from rest_framework.permissions import IsAuthenticated

#ACLARACION GENERAL DE ISAUTHENTICATED, TODOS LOS CONTROLADORES QUE TIENEN ESO SIGNIFICA QUE EN LA REQUEST VENDRA LA DATA
#DEL USER QUE REALIZO LA PETICION, EN CASO DE QUE EL CONTROLADOR NO TENGA ISAUTHENTICATED ESO HARA QUE LA REQUEST TENGA 
#UN CAMPO USER, PERO ESTE NO TENDRA LA DATA DE NINGUN USUARIO SINO QUE TENDRA UN ESTADO ANONIMO, POR ELLO LA REQUEST SIEMPRE
#TENDRA EL CAMPO USER, PERO SU VALOR DEPENDE DE SI EL CONTROLADOR PIDE AUTENTICACION O NO.

#este controlador solo necesita el idUser que ya viene en la url
class CarpetasModificadas(generics.ListAPIView):#este controlador piede autenticacion porque las carpetas pertenecen a un user que debe estar en la BD
    serializer_class=CarpetaSerializer
    permission_classes = [IsAuthenticated]  # Para asegurarse de que el usuario esté autenticado

    def get_queryset(self):
        idUser=self.kwargs['idUser']  # Tomamos el id del usuario desde la URL
        return Carpeta.objects.filter(usuario=idUser).order_by('-updated_at')[:3]

#este controlador solo necesita el id del user que hizo la peticion, el id ya viene en la url
class UserFolders(generics.ListAPIView):#este controlador es para el uso del user para mostar sus carpetas
    serializer_class=Folders
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user_id=self.kwargs['pk']  # Asumiendo que el user_id se pasa como parte de la URL
        user=get_object_or_404(Usuarios,id=user_id)  # Obtiene el usuario o lanza un 404
        return Carpeta.objects.filter(usuario=user)
    
#este controlador usa el id de una carpeta que pide el user, el id de la carpeta ya viene en la url
class UserFolder(generics.RetrieveAPIView):#devuelve una carpeta en especifico de un user
    queryset=Carpeta.objects.all()
    serializer_class=Folders
    permission_classes=[IsAuthenticated]
    def get_object(self):
        user=self.request.user
        carpeta_id=self.kwargs.get('pk')
        return Carpeta.objects.get(id=carpeta_id,usuario=user)
    
class CreateFolderUser(generics.CreateAPIView):
    serializer_class=newFolder
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)#le asigno el usuario autenticado al campo usuario de la carpeta para establecer la relacion
        
