from django.shortcuts import get_object_or_404
from rest_framework import generics
from app.serializers.Documents_serializer import *
from app.models import Documentos


class GetDocument(generics.RetrieveAPIView):
    serializer_class=DocumentSerializer
    
class DeleteDocument(generics.DestroyAPIView):
    serializer_class=DocumentSerializer
    queryset=Documentos.objects.all()
    
class ListDocuments(generics.ListAPIView):
    queryset=Documentos.objects.all()
    serializer_class=DocumentSerializer
    
class UpdateDocument(generics.UpdateAPIView):
    queryset=Documentos.objects.all()
    serializer_class=DocumentSerializer
