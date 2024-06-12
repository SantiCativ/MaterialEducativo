from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import *
from .serializer import *
from .models import *
from django.http import HttpResponse
from rest_framework import status






# USUARIOS
#para cruds basicos
# class UsuariosViewSet (viewsets.ModelViewSet):
#     queryset=Usuarios.objects.all()
#     serializer_class= UsuariosSerializers
    
class CreateUserController(generics.CreateAPIView):
    serializer_class=CreateUserSerializer
    
    #este metodo create pertenece ala vista y lo sobreescribo para que me imprima los errores que suceden
    #el serializador tiene su propio metodo create, no son el mismo, este solo pertenece ala vista CreateApiview
    def create(self, request, *args, **kwargs):
        print("Datos recibidos:", request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        if not serializer.is_valid():
            print("Errores de validación:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class UpdatedUserController(generics.UpdateAPIView):#esta vista se usara para que los usuarios editen su perfil
    queryset = Usuarios.objects.all()
    #permission_classes = [IsAuthenticated] #significa que solo los usuarios que estan autenticados(iniciaron sesion)pueden usar esta vista
    serializer_class=UpdatedUserSerializer
    
class DeleteUserController(generics.DestroyAPIView):
    queryset = Usuarios.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Customize the response here
        return HttpResponse({
            "mensaje": "Usuario eliminado exitosamente."
        }, status=status.HTTP_204_NO_CONTENT)


    
class GetUser(generics.RetrieveAPIView):
    queryset=Usuarios.objects.all()
    serializer_class=UsuariosSerializers
    # permission_classes=[IsAdminUser]
    
class ListUsersController(generics.ListAPIView):
    queryset=Usuarios.objects.all()
    serializer_class=UsuariosSerializers
    # permission_classes=[IsAdminUser]
    
    



