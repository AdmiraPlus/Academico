from django.urls import path

from .views import *

urlpatterns = [
	path('buscar/', BuscarAlumno, name='buscar'),
	
	path('pre_matricula/<str:codigo>/', PreMatricula, name='pre_matricula'),
	#path('pre_matricula/', PreMatricula, {'datos':'alumno'}, name='pre_matricula'),
	
]