from django.contrib import admin

# Register your models here.
from .models import Pregunta,Respuesta

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion de encuesta',  {'fields': ['textPregunta']}),
        ('Informacion de fecha',  {'fields': ['dataPubli']}),
    ]
    list_display = ('textPregunta', 'dataPubli')
    inlines = [RespuestaInline]
    list_filter = ['dataPubli']
    search_fields = ['textPregunta']

admin.site.register(Pregunta,QuestionAdmin)
admin.site.register(Respuesta)