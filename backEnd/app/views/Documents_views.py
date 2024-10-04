from django.shortcuts import get_object_or_404
from rest_framework import generics
from app.serializers.Documents_serializer import *
from app.models import Documentos,Comentario
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
    
class UpdateState(generics.UpdateAPIView):
    queryset=Documentos.objects.all()
    serializer_class=updateState
    
    
    
class DocumentosSugeridos(generics.ListAPIView):
    serializer_class = DocumentSerializer
    

    def get_queryset(self):
        idUser = self.kwargs['idUser']  # ID del usuario desde la URL
        
        # Obtener todos los comentarios realizados por el usuario
        comentarios = Comentario.objects.filter(usuario_id=idUser)
        
        # Extraer los documentos de esos comentarios
        documentos_comentados = comentarios.values_list('documento_id', flat=True)
        
        # Obtener las materias asociadas a esos documentos
        materias = Documentos.objects.filter(id__in=documentos_comentados).values_list('materia_id', flat=True).distinct()
        
        # Filtrar los documentos de esas materias, limitando el resultado a 5
        documentos_sugeridos = Documentos.objects.filter(materia_id__in=materias).order_by('-created_at')[:5]
        
        return documentos_sugeridos
