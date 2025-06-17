from django.contrib import admin

# Register your models here.
#from import_export.admin import ImportExportModelAdmin

# Nuevos modelos importados con sus nombres actualizados
from .models import *

# Registro en el admin con soporte para import/export

class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 1
    verbose_name = 'Inscripcion'
    verbose_name_plural = 'Inscripciones'

class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'departamento', 'instructor')
    list_filter = ('departamento', 'instructor')
    search_fields = ['nombre']
    inlines = [InscripcionInline]



class EntegaInline(admin.TabularInline):
    model = Entrega
    extra = 1
    verbose_name = 'Entrega'
    verbose_name_plural = 'Entregas'

class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso')
    list_filter = ('curso',)
    search_fields = ['titulo']
    inlines = [EntegaInline]


admin.site.register(Departamento)
admin.site.register(Instructor)
#admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Tarea,TareaAdmin)
admin.site.register(Entrega)
admin.site.register(Curso, CursoAdmin)