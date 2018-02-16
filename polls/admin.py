from django.contrib import admin

# Register your models here.
from .models import Pregunta,Respuesta,Voto

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 3

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('textRespuesta','pregunta','sum')
    search_fields = ['textoRespuesta']
    def get_ordering(self, request):
        if request.user.is_superuser:
            return ['pregunta']
        else:
            return ['pregunta']
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('textPregunta', 'dataPubli')
    inlines = [RespuestaInline]
    list_filter = ['dataPubli']
    search_fields = ['textPregunta']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

class VotoAdmin(admin.ModelAdmin):
    list_display = ('author','respuesta','Id')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)



admin.site.register(Pregunta,QuestionAdmin)
admin.site.register(Respuesta,RespuestaAdmin)
admin.site.register(Voto,VotoAdmin)