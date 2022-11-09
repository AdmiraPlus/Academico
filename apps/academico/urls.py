# URLs particulares de la aplicación

from django.urls import path

from .views import alumnos_listar, alumnos_agregar, alumnos_editar, alumnos_eliminar
from .views import docentes_listar, docentes_agregar, docentes_editar, docentes_eliminar
from .views import sis_evaluacion_listar, sis_evaluacion_agregar, sis_evaluacion_editar, sis_evaluacion_eliminar
from .views import cursos_listar, cursos_agregar, cursos_editar, cursos_eliminar
from .views import ciclos_listar, ciclos_agregar, ciclos_editar, ciclos_eliminar


urlpatterns = [
	path('alumnos/listar/', alumnos_listar, name='alumnos_listar'),
	path('alumnos/agregar/', alumnos_agregar, name="alumnos_agregar"),
	path('alumnos/editar/<int:id>/', alumnos_editar, name="alumnos_editar"),
	path('alumnos/eliminar/<int:id>/', alumnos_eliminar, name="alumnos_eliminar"),
	
	path('docentes/listar/', docentes_listar, name='docentes_listar'),
	path('docentes/agregar/', docentes_agregar, name='docentes_agregar'),
	path('docentes/editar/<int:id>/', docentes_editar, name='docentes_editar'),
	path('docentes/eliminar/<int:id>/', docentes_eliminar, name='docentes_eliminar'),
	
	path('sis_evaluacion/listar/', sis_evaluacion_listar, name='sis_evaluacion_listar'),
	path('sis_evaluacion/agregar/', sis_evaluacion_agregar, name='sis_evaluacion_agregar'),
	path('sis_evaluacion/editar/<int:id>/', sis_evaluacion_editar, name='sis_evaluacion_editar'),
	path('sis_evaluacion/eliminar/<int:id>/', sis_evaluacion_eliminar, name='sis_evaluacion_eliminar'),
	
	path('cursos/listar/', cursos_listar, name='cursos_listar'),
	path('cursos/agregar/', cursos_agregar, name='cursos_agregar'),
	path('cursos/editar/<int:id>/', cursos_editar, name='cursos_editar'),
	path('cursos/eliminar/<int:id>/', cursos_eliminar, name='cursos_eliminar'),
	
	path('ciclos/listar/', ciclos_listar, name='ciclos_listar'),
	path('ciclos/agregr', ciclos_agregar, name='ciclos_agregar'),
	path('ciclos/editar/<int:id>/', ciclos_editar, name='ciclos_editar'),
	path('ciclos/eliminar/<int:id>/', ciclos_eliminar, name='ciclos_eliminar'),
]