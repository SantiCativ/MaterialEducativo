from django.shortcuts import get_object_or_404
from rest_framework import generics
from app.serializers.Documents_serializer import *
from app.models import Documentos,Comentario,Favorito
from rest_framework.permissions import IsAuthenticated

class CreateDocument(generics.CreateAPIView):
    serializer_class=DocumentSerializer
    permission_classes = [IsAuthenticated]
    #sobreescribo el metodo perform para que le asigne la instancia del user que hizo la peticion al campo owner
    def perform_create(self, serializer):
        user=self.request.user#asigno a user la instancia del usuario que esta en request.user
        serializer.save(owner=user)#guardo el documento creado asignandole a su campo owner el user 
    
class DeleteDocument(generics.DestroyAPIView):
    serializer_class=DocumentSerializer
    queryset=Documentos.objects.all()
    
class GetDocuments(generics.ListAPIView):#este controlador esta hecho para la zona admin, ya que trae documentos con la info de sus propietarios
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
#NUEVO
class UserFavoritesDocuments(generics.ListAPIView):
    serializer_class=userDocuments
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id=self.kwargs['id']
        return Documentos.objects.filter(favorito__usuario_id=user_id)
        
        
#NUEVO
class UserDocuments(generics.ListAPIView):#este controlador es destinado para el uso del usuario para recuperar sus documentos
    serializer_class=userDocuments
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user_id=self.kwargs['id']  # Asumiendo que el user_id se pasa como parte de la URL
        user=get_object_or_404(Usuarios,id=user_id)  # Obtiene el usuario o lanza un 404
        return Documentos.objects.filter(owner=user)
    
#NUEVO
class UserFolders(generics.ListAPIView):#este controlador es para el uso del user para mostar sus carpetas
    serializer_class=Folders
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user_id=self.kwargs['id']  # Asumiendo que el user_id se pasa como parte de la URL
        user=get_object_or_404(Usuarios,id=user_id)  # Obtiene el usuario o lanza un 404
        return Carpeta.objects.filter(usuario=user)

#NUEVO
class UserFolder(generics.RetrieveAPIView):
    queryset=Carpeta.objects.all()
    serializer_class=Folders
    permission_classes=[IsAuthenticated]
    def get_object(self):
        user=self.request.user
        carpeta_id=self.kwargs.get('id')
        return Carpeta.objects.get(id=carpeta_id,usuario=user)
    
#NUEVO
class CreateFolderUser(generics.CreateAPIView):
    serializer_class = newFolder
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)#le asigno el usuario autenticado al campo usuario de la carpeta para establecer la relacion
        
#NUEVO
class GetDocument(generics.RetrieveAPIView):
    serializer_class=DocumentSerializer
    queryset=Carpeta.objects.all()
    permission_classes=[IsAuthenticated]
    def get_object(self):
        user=self.request.user
        document_id=self.kwargs.get('id')
        return Documentos.objects.get(id=document_id,usuario=user)
