from django.urls import path, include
from rest_framework import routers
from app.views import *
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)


router= routers.DefaultRouter()
#router.register(r'Usuarios',views.UsuariosViewSet)
urlpatterns= [
    path('',include(router.urls)),
    path('registro/', CreateUser.as_view(), ), 
    path('documents_create/',CreateDocument.as_view(),),
    path('update/<int:pk>/',UpdatedUser.as_view()),
    path('delete/<int:pk>/', DeleteUser.as_view()), 
    path('user/<int:pk>/', GetUser.as_view()), 
    path('users/', GetUsers.as_view()), 
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#esta vista recibe el usuario y contraseña y si
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('documents/', GetDocuments.as_view()), 
    ]