from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import *
from .serializer import *
from .models import *


# USUARIOS
class UsuariosViewSet (viewsets.ModelViewSet):
    queryset=Usuarios.objects.all()
    serializer_class= UsuariosSerializers
    
class CreateUserController(generics.CreateAPIView):
    serializer_class=CreateUserSerializer
    
class UpdatedUserController(generics.UpdateAPIView):#esta vista se usara para que los usuarios editen su perfil
    queryset = Usuarios.objects.all()
    permission_classes = [IsAuthenticated] #significa que solo los usuarios que estan autenticados(iniciaron sesion)pueden usar esta vista
    serializer_class=UpdatedUserSerializer
    
class DeleteUserController(generics.DestroyAPIView):
    queryset=Usuarios.objects.all()#aqui usa el metodo get_object para buscar el usuario con su id entre todos los users
    serializer_class=UsuariosSerializers
    permission_classes=[IsAdminUser]#esta accion solo la puede hacer un admin
    
class GetUser(generics.RetrieveAPIView):
    queryset=Usuarios.objects.all()
    serializer_class=UsuariosSerializers
    permission_classes=[IsAdminUser]
    
class ListUsersController(generics.ListAPIView):
    queryset=Usuarios.objects.all()
    serializer_class=UsuariosSerializers
    permission_classes=[IsAdminUser]
    
    



