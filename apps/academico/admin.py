from django.contrib import admin
#from .models import Alumnos, Docentes, SistemaEvaluacion, Cursos, CiclosAcademicos
from .models import *

# Register your models here.
admin.site.register(Alumnos)
admin.site.register(Docentes)
admin.site.register(SistemaEvaluacion)
admin.site.register(Cursos)
admin.site.register(CiclosAcademicos)

