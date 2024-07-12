from rest_framework import serializers
from app.models import Documentos

class DocumentSerializer(serializers.Serializer):
    class Meta:
        Model=Documentos
        fields="__all__"