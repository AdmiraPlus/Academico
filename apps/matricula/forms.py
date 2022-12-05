from django import forms


# -- Solicitud de código --------------------------------------------------------------------------------------------
class CodigoAlumnoForm(forms.Form):
	codigo_alumno = forms.CharField(label="Código del Alumno", max_length=9)
	
	widgets = {
		'codigo_alumno': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
	}