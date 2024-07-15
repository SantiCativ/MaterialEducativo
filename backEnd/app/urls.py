from django.urls import path, include
from rest_framework import routers
from app import views
from .views import *


router= routers.DefaultRouter()
#router.register(r'Usuarios',views.UsuariosViewSet)
urlpatterns= [
    path('',include(router.urls)),
    path('registro/', CreateUser.as_view(), ), 
    path('update/<int:pk>/',UpdatedUser.as_view()),
    path('delete/<int:pk>/', DeleteUser.as_view()), 
    path('user/<int:pk>/', GetUser.as_view()), 
    path('users/', GetUsers.as_view()), 
    ]