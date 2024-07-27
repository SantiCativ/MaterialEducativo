from rest_framework import serializers
from app.models import Documentos

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Documentos
        fields=["title", "created_date","file", "owner_id", "state"]
        
    def create(self, validated_data):
        return Documentos.objects.create(**validated_data)
    
class Documents(serializers.ModelSerializer):
    class Meta:
        model=Documentos
        fields='__all__'