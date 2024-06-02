from django.urls import path, include
from rest_framework import routers
from app import views
from .views import *


router= routers.DefaultRouter()
#router.register(r'Usuarios',views.UsuariosViewSet)
urlpatterns= [
    path('',include(router.urls)),
    path('registro/', CreateUserController.as_view(), ), 
    path('update/<int:pk>/',UpdatedUserController.as_view()),
    path('delete/<int:pk>/', DeleteUserController.as_view()), 
    path('user/<int:pk>/', GetUser.as_view()), 
    path('list/', ListUsersController.as_view()), 
    ]