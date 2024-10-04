from django.shortcuts import get_object_or_404
from rest_framework import generics
from app.serializers.Carpeta_serializer import *
from app.models import Carpeta,Usuarios
from rest_framework.permissions import IsAuthenticated

class CarpetasModificadas(generics.ListAPIView):
    serializer_class = CarpetaSerializer
   # permission_classes = [IsAuthenticated]  # Para asegurarse de que el usuario esté autenticado

    def get_queryset(self):
        idUser = self.kwargs['idUser']  # Tomamos el id del usuario desde la URL
        return Carpeta.objects.filter(usuario=idUser).order_by('-updated_at')[:3]
