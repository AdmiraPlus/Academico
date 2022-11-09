from django import forms
from .models import Alumnos, CiclosAcademicos, Docentes, SistemaEvaluacion, Cursos, CiclosAcademicos

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# -- Alumnos ----------------------------------------------------------------------------------------------------------
class AlumnosForm(forms.ModelForm):
	
    class Meta:
        model = Alumnos
		
        fields = [
            'codigo_uni',
            'numero_dni',
            'apellido_p',
            'apellido_m',
            'nombres'
        ]
		
        labels = {
            'codigo_uni': 'Código UNI',
            'numero_dni': 'Nro. de D.N.I.',
            'apellido_p': 'Apellido Paterno',
            'apellido_m': 'Apellido Materno',
            'nombres': 'Nombre(s)',
        }
		
        widgets = {
            'codigo_uni': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'numero_dni': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'apellido_p': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'apellido_m': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control form-control-sm'})
        }

# -- Docentes----------------------------------------------------------------------------------------------------------
class DocentesForm(forms.ModelForm):
	
    class Meta:
        model = Docentes
		
        fields = [
            'nro_dni',
            'apellido_p',
            'apellido_m',
            'nombres'
        ]
		
        labels = {
            'nro_dni': 'Nro. de D.N.I.',
            'apellido_p': 'Apellido Paterno',
            'apellido_m': 'Apellido Materno',
            'nombres': 'Nombre(s)',
        }
		
        widgets = {
            'nro_dni': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'apellido_p': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'apellido_m': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control form-control-sm'})
        }

# -- Sistemas de Evaluación -------------------------------------------------------------------------------------------
class SistemaEvaluacionForm(forms.ModelForm):
	
    class Meta:
        model = SistemaEvaluacion
		
        fields = [
            'sistema_evaluacion',
        ]
		
        labels = {
            'sistema_evaluacion': 'Sistema de Evaluación',
        }
		
        widgets = {
            'sistema_evaluacion': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }

# -- Cursos -----------------------------------------------------------------------------------------------------------
class CursosForm(forms.ModelForm):
	
    class Meta:
        model = Cursos
		
        fields = [
            'codigo',
            'curso',
            'sistema_evaluacion'
        ]
		
        labels = {
            'codigo': 'Código Curso',
            'curso': 'Nombre del Curso',
            'sistema_evaluacion': 'Sistema de Evaluación'
        }
		
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'curso': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'sistema_evaluacion': forms.Select(attrs={'class': 'form-control form-control-sm'}),
        }

# -- Ciclos Académicos ------------------------------------------------------------------------------------------------
class CiclosForm(forms.ModelForm):
	
    class Meta:
        model = CiclosAcademicos
		
        fields = [
			'anno',
    	    'ciclo',
	    	'tipo'
        ]
		
        labels = {
			'anno': 'Año',
    	    'ciclo': 'Ciclo',
	    	'tipo': 'Tipo'
        }
		
        widgets = {
			'anno': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
    	    'ciclo': forms.Select(attrs={'class': 'form-control form-control-sm'}),
	    	'tipo': forms.Select(attrs={'class': 'form-control form-control-sm'})
        }


# -- User -------------------------------------------------------------------------------------------------------------
class RegistroForm(UserCreationForm):
	
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		]
	