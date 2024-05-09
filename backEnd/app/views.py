from rest_framework import viewsets
from .serializer import *
from .models import *


# trae todos los alumnos
class AlumnosViewSet (viewsets.ModelViewSet):
    queryset=Alumnos.objects.all()
    serializer_class= AlumnosSerializers


