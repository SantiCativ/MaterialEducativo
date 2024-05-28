from django.urls import path, include
from rest_framework import routers
from app import views
from .views import *


router= routers.DefaultRouter()
router.register(r'Usuarios',views.UsuariosViewSet)
urlpatterns= [
    path('',include(router.urls)),
    path('registro/', CreateUserController.as_view(), ), 
    ]