from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("contactos/", views.lista_contactos, name="lista_contactos"),
    path("contacto/nuevo/", views.nuevo_contacto, name="nuevo_contacto"),
    path("contacto/editar/<int:id>/", views.editar_contacto, name="editar_contacto"),
    path("contacto/eliminar/<int:id>/", views.eliminar_contacto, name="eliminar_contacto"),
]
