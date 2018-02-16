import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings



class Pregunta(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
	textPregunta = models.CharField(max_length=200)
	dataPubli = models.DateTimeField('Fecha de publicacion')
	def __str__(self):
		return self.textPregunta
	def was_published_recently(self):
		return self.dataPubli >= timezone.now() - datetime.timedelta(days=1)

class Respuesta(models.Model):
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	textRespuesta = models.CharField(max_length=200)

	def __str__(self):
		return self.textRespuesta
	def sum(self):
		return Voto.objects.filter(respuesta=self).count()
	def user(self):
		return self.author


class Voto(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
	respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE)
	def Id(self):
		return self.id
	