# Vistas Comunes o Generales

from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from apps.academico.forms import RegistroForm
from django.contrib.auth.models import User

from datetime import date

# =====================================================================================================================
def inicio(request):
	return render(request, 'inicio.html', {'fecha': date.today()})

""" 
def registrar_usuario(request):
	if request.method == "GET":
		return render(request, 'registrar_usuario.html', {'form': UserCreationForm})
	else:
		if request.POST["password1"] == request.POST["password2"]:
			try:
				usuario = User.objects.create_user(
					username=request.POST["username"], 
					password=request.POST["password1"]
				)
				usuario.save()
				login(request, usuario)
				return redirect('inicio')
			except:
				return render(request, 'registrar_usuario.html', {
					'form': UserCreationForm,
					'error': 'El usuario ya existe.'
				})
		return render(request, 'registrar_usuario.html', {
			'form': UserCreationForm,
			'error': 'La contraseña no coincide'
		})


def registro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
	else:
		form = UserCreationForm()
	
	context = { 'form':form }
	return render(request, 'registro.html', context)
"""

def registrar_usuario(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			form.save()
			usuario = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
			"""usuario = User.objects.create_user(
				username=request.POST["username"], 
				password=request.POST["password1"],
				email=request.POST['email']
			)"""
			login(request, usuario)
			return redirect('inicio')
	else:
		form = RegistroForm()
	
	context = { 'form':form }
	return render(request, 'registrar_usuario.html', context)



@login_required
def cerrar_sesion(request):
	logout(request)
	return redirect('iniciar_sesion')

def iniciar_sesion(request):
	if request.method == "GET":
		return render(request, 'iniciar_sesion.html', {
			'form': AuthenticationForm
		})
	else:
		user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
		if user is None:
			return render(request, 'iniciar_sesion.html', {
				'form': AuthenticationForm,
				'error': 'Usuario/Clave incorrecto o no existe el usuario.'
			})
		else:
			login(request, user)
			return redirect('inicio')





# =====================================================================================================================
def xxx_registrar_usuario(request):
	if request.method == "GET":
		return render(request, 'bak/xxx_registrar_usuario.html', {'form': UserCreationForm})
	else:
		if request.POST["password1"] == request.POST["password2"]:
			try:
				usuario = User.objects.create_user(
					username=request.POST["username"], password=request.POST["password1"])
				usuario.save()
				login(request, usuario)
				return redirect('inicio')
			except:
				return render(request, 'bak/xxx_registrar_usuario.html', {
					'form': UserCreationForm,
					'error': 'El usuario ya existe.'
				})
		return render(request, 'bak/xxx_registrar_usuario.html', {
			'form': UserCreationForm,
			'error': 'La contraseña no coincide'
		})
 