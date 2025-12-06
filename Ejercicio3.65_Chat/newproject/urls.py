from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from chat import views

# Router de la API (crea las URLs automáticamente)
router = routers.DefaultRouter()
router.register(r'mensajes', views.MensajeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),           # Ruta para los datos (JSON)
    path('chat/', views.sala_chat, name='chat'),  # Ruta para la web (HTML)
]
