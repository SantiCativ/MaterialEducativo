
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.serializers.User_serializer import *
from app.models import Usuarios
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
# USUARIOS
# para cruds basicos
# class UsuariosViewSet (viewsets.ModelViewSet):
#     queryset=Usuarios.objects.all()
#     serializer_class= UsuariosSerializers



class ResetPasswordConfirm(generics.GenericAPIView):
    serializer_class =resetPasswordConfirm

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contraseña actualizada exitosamente."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPassword(generics.GenericAPIView):
    serializer_class=resetPassword

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        # Validar los datos
        if serializer.is_valid():
            email=serializer.validated_data['email']
            try:
                user=Usuarios.objects.get(email=email)
                token = default_token_generator.make_token(user)
                return Response({
                    "token": token,
                    "email": email 
                }, status=status.HTTP_200_OK)
            except user.DoesNotExist:
                return Response({
                    "error": "No existe ningún usuario con este email."
                }, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       



class CreateUser(generics.CreateAPIView):
    serializer_class = createUser

    # este metodo create pertenece ala vista y lo sobreescribo para que me imprima los errores que suceden
    # el serializador tiene su propio metodo create, no son el mismo, este solo pertenece ala vista CreateApiview
    def create(self, request, *args, **kwargs):
        print("Datos recibidos:", request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        if not serializer.is_valid():
            print("Errores de validación:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # ste método llama internamente al método create del serializer, creando así el usuario en la base de datos.
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Usuario registrado exitosamente."},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class UpdatedUser(generics.UpdateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = updatedUser


class UpdatedEstado(generics.UpdateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = updatedEstado


class DeleteUser(generics.DestroyAPIView):
    queryset = Usuarios.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Customize the response here
        return HttpResponse(
            {"mensaje": "Usuario eliminado exitosamente."},
            status=status.HTTP_204_NO_CONTENT,
        )


class GetUser(generics.RetrieveAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = getUser
    permission_classes=[IsAuthenticated]

class GetUsers(generics.ListAPIView):
    queryset = Usuarios.objects.all().order_by("-id")
    serializer_class = getUsers
    # permission_classes=[IsAdminUser]
    

