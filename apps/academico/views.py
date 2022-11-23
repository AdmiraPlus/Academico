# Vistas Particulares de la Aplicación

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from . import models
from . import forms

# =====================================================================================================================

# -- Alumnos ----------------------------------------------------------------------------------------------------------

@login_required
def alumnos_listar(request):
	# Filtrado de los datos -------------
	text = request.GET.get('buscar', '')
	alumnos_filtrados = models.Alumnos.objects.filter(
		Q(codigo_uni__icontains=text) |
		Q(numero_dni__icontains=text) |
		Q(apellido_p__icontains=text) |
		Q(apellido_m__icontains=text) |
		Q(nombres__icontains=text)
	)
	
	# Paginado de los datos -------------
	alumnos_paginados = Paginator(alumnos_filtrados, 7)
	page = request.GET.get('page', 1)
	alumnos = alumnos_paginados.get_page(page)  # El objeto "page_obj"
	
	# Renderizado de los datos ----------
	return render(request, 'academico/alumnos_listar.html', {'data': alumnos, 'paginator': alumnos_paginados, 'buscar': text})

@login_required
def alumnos_agregar(request):
	if request.method == 'POST':
		form = forms.AlumnosForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('alumnos_listar')
	else:
		form = forms.AlumnosForm()
	return render(request, 'academico/alumnos_form.html', {'form': form})

@login_required
def alumnos_editar(request, id):
	alumno = models.Alumnos.objects.get(id=id)
	if request.method == 'GET':
		form = forms.AlumnosForm(instance=alumno)
	else:
		form = forms.AlumnosForm(request.POST, instance=alumno)
		if form.is_valid():
			form.save()
		return redirect('alumnos_listar')
	return render(request, 'academico/alumnos_form.html', {'form': form})

@login_required
def alumnos_eliminar(request, id):
	alumno = models.Alumnos.objects.get(id=id)
	if request.method == 'POST':
		alumno.delete()
		return redirect('alumnos_listar')
	return render(request, 'academico/alumnos_eliminar.html', {'alumno': alumno})

# -- Docentes ----------------------------------------------------------------------------------------------------------

@login_required
def docentes_listar(request):
	text = request.GET.get('buscar', '')
	docentes_lst = models.Docentes.objects.filter(
		Q(nro_dni__icontains=text) |
		Q(apellido_p__icontains=text) |
		Q(apellido_m__icontains=text) |
		Q(nombres__icontains=text)
	)
	docentes_paginados = Paginator(docentes_lst, 7)  # Paginator
	page = request.GET.get('page', 1)
	docentes = docentes_paginados.get_page(page)  # page_obj
	return render(request, 'academico/docentes_listar.html', {'data': docentes, 'paginator': docentes_paginados})

@login_required
def docentes_agregar(request):
	if request.method == 'POST':
		form = forms.DocentesForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('docentes_listar')
	else:
		form = forms.DocentesForm()
	return render(request, 'academico/docentes_form.html', {'form': form})

@login_required
def docentes_editar(request, id):
	docente = models.Docentes.objects.get(id=id)
	if request.method == 'GET':
		form = forms.DocentesForm(instance=docente)
	else:
		form = forms.DocentesForm(request.POST, instance=docente)
		if form.is_valid():
			form.save()
		return redirect('docentes_listar')
	return render(request, 'academico/docentes_form.html', {'form': form})

@login_required
def docentes_eliminar(request, id):
	docente = models.Docentes.objects.get(id=id)
	if request.method == 'POST':
		docente.delete()
		return redirect('docentes_listar')
	return render(request, 'academico/docentes_eliminar.html', {'docente': docente})

# -- Sistemas de Evaluación -------------------------------------------------------------------------------------------

@login_required
def sis_evaluacion_listar(request):
	text = request.GET.get('buscar', '')
	sis_eval_lst = models.SistemaEvaluacion.objects.filter(
		sistema_evaluacion__icontains=text
	)
	sis_eval_paginados = Paginator(sis_eval_lst, 7)  # Paginator
	page = request.GET.get('page', 1)
	sis_evals = sis_eval_paginados.get_page(page)  # page_obj
	return render(request, 'academico/sis_evaluacion_listar.html', {'data': sis_evals, 'paginator': sis_eval_paginados})

@login_required
def sis_evaluacion_agregar(request):
	if request.method == 'POST':
		form = forms.SistemaEvaluacionForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('sis_evaluacion_listar')
	else:
		form = forms.SistemaEvaluacionForm()
	return render(request, 'academico/sis_eval_form.html', {'form': form})

@login_required
def sis_evaluacion_editar(request, id):
	sis_eval = models.SistemaEvaluacion.objects.get(id=id)
	if request.method == 'GET':
		form = forms.SistemaEvaluacionForm(instance=sis_eval)
	else:
		form = forms.SistemaEvaluacionForm(request.POST, instance=sis_eval)
		if form.is_valid():
			form.save()
		return redirect('sis_evaluacion_listar')
	return render(request, 'academico/sis_eval_form.html', {'form': form})

@login_required
def sis_evaluacion_eliminar(request, id):
	sis_eval = models.SistemaEvaluacion.objects.get(id=id)
	if request.method == 'POST':
		sis_eval.delete()
		return redirect('sis_evaluacion_listar')
	return render(request, 'academico/sis_evaluacion_eliminar.html', {'sis_eval': sis_eval})

# -- Cursos -----------------------------------------------------------------------------------------------------------

@login_required
def cursos_listar(request):
	text = request.GET.get('buscar', '')
	cursos_lst = models.Cursos.objects.filter(
		Q(codigo__icontains=text) |
		Q(curso__icontains=text) |
		Q(sistema_evaluacion__sistema_evaluacion__icontains=text)
	)
	cursos_paginados = Paginator(cursos_lst, 7)
	page = request.GET.get('page', 1)
	cursos = cursos_paginados.get_page(page)
	return render(request, 'academico/cursos_listar.html', {'data': cursos, 'paginator': cursos_paginados})

@login_required
def cursos_agregar(request):
	if request.method == 'POST':
		form = forms.CursosForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('cursos_listar')
	else:
		form = forms.CursosForm()
	return render(request, 'academico/cursos_form.html', {'form': form})

@login_required
def cursos_editar(request, id):
	curso = models.Cursos.objects.get(id=id)
	if request.method == 'GET':
		form = forms.CursosForm(instance=curso)
	else:
		form = forms.CursosForm(request.POST, instance=curso)
		if form.is_valid():
			form.save()
		return redirect('cursos_listar')
	return render(request, 'academico/cursos_form.html', {'form': form})

@login_required
def cursos_eliminar(request, id):
	curso = models.Cursos.objects.get(id=id)
	if request.method == 'POST':
		curso.delete()
		return redirect('cursos_listar')
	return render(request, 'academico/cursos_eliminar.html', {'curso': curso})

# -- Ciclos Académicos ------------------------------------------------------------------------------------------------

@login_required
def ciclos_listar(request):
	text = request.GET.get('buscar', '')
	ciclos_lst = models.CiclosAcademicos.objects.filter(
		Q(anno__icontains=text) |
		Q(ciclo__icontains=text) |
		Q(tipo__contains=text)
	)
	ciclos_paginados = Paginator(ciclos_lst, 7)
	page = request.GET.get('page', 1)
	ciclos = ciclos_paginados.get_page(page)
	return render(request, 'academico/ciclos_listar.html', {'data': ciclos, 'paginator': ciclos_paginados})

@login_required
def ciclos_agregar(request):
	if request.method == 'POST':
		form = forms.CiclosForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('ciclos_listar')
	else:
		form = forms.CiclosForm()
	return render(request, 'academico/ciclos_form.html', {'form': form})

@login_required
def ciclos_editar(request, id):
	ciclo = models.CiclosAcademicos.objects.get(id=id)
	if request.method == 'GET':
		form = forms.CiclosForm(instance=ciclo)
	else:
		form = forms.CiclosForm(request.POST, instance=ciclo)
		if form.is_valid():
			form.save()
		return redirect('ciclos_listar')
	return render(request, 'academico/ciclos_form.html', {'form': form})

@login_required
def ciclos_eliminar(request, id):
	ciclo = models.CiclosAcademicos.objects.get(id=id)
	if request.method == 'POST':
		ciclo.delete()
		return redirect('ciclos_listar')
	return render(request, 'academico/ciclos_eliminar.html', {'ciclo': ciclo})
