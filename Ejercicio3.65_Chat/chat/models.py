from django.db import models

class Mensaje(models.Model):
    usuario = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario}: {self.contenido}"
