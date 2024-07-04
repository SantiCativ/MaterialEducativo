from django.urls import path, include
from rest_framework import routers
from app import views
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)


router= routers.DefaultRouter()
#router.register(r'Usuarios',views.UsuariosViewSet)
urlpatterns= [
    path('',include(router.urls)),
    path('registro/', CreateUserController.as_view(), ), 
    path('update/<int:pk>/',UpdatedUserController.as_view()),
    path('delete/<int:pk>/', DeleteUserController.as_view()), 
    path('user/<int:pk>/', GetUser.as_view()), 
    path('list/', ListUsersController.as_view()), 
    #estas vistas estan provistas por django rest, ya estan definidas en el modlo importado
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#esta vista recibe el usuario y contraseña y si
    #son correctos(los busca en la BD) devuelve un token de acceso y otro de refresh
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #--
    ]