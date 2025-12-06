from rest_framework import viewsets
from .models import Mensaje
from .serializers import MensajeSerializer
from django.shortcuts import render

# API: Para leer/escribir mensajes automáticamente
class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all().order_by('-fecha')
    serializer_class = MensajeSerializer

# WEB: Para ver la pantalla del chat
def sala_chat(request):
    return render(request, 'chat/index.html')
