import datetime
from django.db import models
from django.utils import timezone


class Pregunta(models.Model):
    textPregunta = models.CharField(max_length=200)
    dataPubli = models.DateTimeField('Fecha de publicacion')
    def __str__(self):
        return self.textPregunta
        def was_published_recently(self):
        	return self.dataPubli >= timezone.now() - datetime.timedelta(days=1)

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    textRespuesta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.textRespuesta

