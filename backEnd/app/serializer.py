from rest_framework import serializers
from .models import *

class AlumnosSerializers(serializers.ModelSerializer):
    class Meta:
        model=Alumnos
        fields= "__all__"
