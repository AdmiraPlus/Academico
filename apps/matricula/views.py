from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from apps.academico.models import Alumnos, Matricula, DetalleMatricula

from .forms import *


# Create your views here.
@login_required
def BuscarAlumno(request):
	mensaje = ''
	if request.method == 'POST':
		#alumno = Alumnos.objects.get(codigo_uni__iexact=request.POST["codigo_alumno"])
		codigo_alumno = request.POST["codigo_alumno"]
		if codigo_alumno:
			try:
				alumno = Alumnos.objects.get(codigo_uni__iexact=codigo_alumno)
				return redirect('pre_matricula', codigo=codigo_alumno)
				#return redirect('pre_matricula', codigo=alumno.codigo_uni)
			except ObjectDoesNotExist:
				form = CodigoAlumnoForm(request.POST)
				mensaje = 'No se encontró ningún alumno con ese código.'
		else:
			form = CodigoAlumnoForm(request.POST)
			mensaje = 'Debe indicar un código de alumno, por favor.'
	else:
		form = CodigoAlumnoForm()
	
	return render(request, 'matricula/buscar.html', {'form': form, 'mensaje':mensaje})

""" 
def PreMatricula(request, codigo):
	if request.method == 'POST':
		pass
	else:
		alumno = Alumnos.objects.get(codigo_uni=codigo)
		matricula = Matricula.objects.get(id_alumno=alumno.id) # Funciona!
		#matricula = Matricula.objects.filter(alumno)
		#detalle = DetalleMatricula.objects.filter(matricula)
		detalle = DetalleMatricula.objects.filter(id_matricula=matricula.id)
		
		context = {
			'alumno':alumno,
			'matricula':matricula,
			'detalle':detalle,
			'CursosSeleccionados':0,
			'CreditosSeleccionados':0
		}
	return render(request, 'matricula/pre_matricula.html', context)
 """
def PreMatricula(request, codigo):
	alumno = Alumnos.objects.get(codigo_uni=codigo)
	matricula = Matricula.objects.get(id_alumno=alumno.id) # Funciona!
	#matricula = Matricula.objects.filter(alumno)
	#detalle = DetalleMatricula.objects.filter(matricula)
	detalle = DetalleMatricula.objects.filter(id_matricula=matricula.id)
	
	context = {
		'alumno':alumno,
		'matricula':matricula,
		'detalle':detalle,
		'CursosSeleccionados':0,
		'CreditosSeleccionados':0,
		'codigo': codigo
	}
	if request.method == 'POST':
		return render(request, 'matricula/pre_matricula.html', context)
	else:
		return render(request, 'matricula/pre_matricula.html', context)

