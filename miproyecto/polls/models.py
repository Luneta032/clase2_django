from django.db import models

# Create your models here.
class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField('Fecha de Publicacion')

    def __str__(self):
       return self.texto_pregunta
   