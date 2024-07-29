from django.shortcuts import get_object_or_404
from rest_framework import generics
from app.serializers.Documents_serializer import *
from app.models import Documentos
from rest_framework.permissions import IsAuthenticated

class CreateDocument(generics.CreateAPIView):
    serializer_class=DocumentSerializer
    permission_classes = [IsAuthenticated]
    #sobreescribo el metodo perform para que le asigne la instancia del user que hizo la peticion al campo owner
    def perform_create(self, serializer):
        user=self.request.user#asigno a user la instancia del usuario que esta en request.user
        serializer.save(owner=user)#guardo el documento creado asignandole a su campo owner el user 
        
class GetDocument(generics.RetrieveAPIView):
    serializer_class=DocumentSerializer
    
class DeleteDocument(generics.DestroyAPIView):
    serializer_class=DocumentSerializer
    queryset=Documentos.objects.all()
    
class GetDocuments(generics.ListAPIView):
    queryset=Documentos.objects.all()
    serializer_class=Documents
    
class UpdateDocument(generics.UpdateAPIView):
    queryset=Documentos.objects.all()
    serializer_class=Documents
