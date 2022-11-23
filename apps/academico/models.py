from django.db import models

# Create your models here.

# -- Tabla Alumnos -----------------------------------------------------------------------------------------
class Alumnos(models.Model):
	codigo_uni = models.CharField(
		max_length=9, 
		verbose_name="Código UNI"
	)
	numero_dni = models.CharField(
		max_length=9, 
		verbose_name="Número de DNI"
	)
	apellido_p = models.CharField(
		max_length=20, 
		verbose_name="Apellido Paterno"
	)
	apellido_m = models.CharField(
		max_length=20, 
		verbose_name="Apellido Materno"
	)
	nombres = models.CharField(
		max_length=40, 
		verbose_name="Nombres"
	)
	
	def __str__(self):
		return f"{self.apellido_p} {self.apellido_m}, {self.nombres}"
	
	class Meta:
		db_table = "Alumnos"
		verbose_name = "Alumno"
		ordering = [
			"apellido_p",
			"apellido_m",
			"nombres"
		]

# -- Tabla Docentes ----------------------------------------------------------------------------------------
class Docentes(models.Model):
	nro_dni = models.CharField(
		max_length=9, 
		verbose_name="Número de DNI"
	)
	apellido_p = models.CharField(
		max_length=20, 
		verbose_name="Apellido Paterno"
	)
	apellido_m = models.CharField(
		max_length=20, 
		verbose_name="Apellido Materno"
	)
	nombres = models.CharField(
		max_length=40, 
		verbose_name="Nombres"
	)
	
	def __str__(self):
		return f"{self.apellido_p} {self.apellido_m}, {self.nombres}"
	
	class Meta:
		db_table = "Docentes"
		verbose_name = "Docente"
		ordering = [
			"apellido_p", 
			"apellido_m", 
			"nombres"
		]

# -- Tabla SistemaEvaluacion -------------------------------------------------------------------------------
class SistemaEvaluacion(models.Model):
	sistema_evaluacion = models.CharField(
		max_length=1, 
		verbose_name="Sist. de Evaluación",
		null=True
	)
	
	def __str__(self):
		return self.sistema_evaluacion
	
	class Meta:
		db_table = "SistemasEvaluacion"
		verbose_name = "SistemaEvaluacion"
		ordering = ["sistema_evaluacion"]

# -- Tabla Cursos ------------------------------------------------------------------------------------------
class Cursos(models.Model):
	codigo = models.CharField(
		max_length=5, 
		verbose_name="Código del Curso"
	)
	curso = models.CharField(
		max_length=40, 
		verbose_name="Curso"
	)
	ciclo = models.CharField(
		max_length=1, 
		verbose_name="Ciclo"
	)
	creditos = models.PositiveSmallIntegerField(
		verbose_name="Créditos"
	)
	sistema_evaluacion = models.ForeignKey(
		SistemaEvaluacion, 
		on_delete=models.SET_NULL, 
		null=True, 
		verbose_name="Sist. de Evaluación", 
		db_column="id_sistema_evaluacion"
	)
	pre_requisitos = models.CharField(
		max_length=20, 
		null=True,
		verbose_name="Pre-requisitos"
	)
	
	def __str__(self):
		return self.curso
	
	class Meta:
		db_table = "Cursos"
		verbose_name = "Curso"
		ordering = [
			"curso", 
			"codigo"
		]

# -- Tabla CiclosAcademicos --------------------------------------------------------------------------------
class CiclosAcademicos(models.Model):
	CICLOS = ( 
		("1","1"),
		("2","2"),
		("3","3"),
	)
	
	TIPO =  (
		("N", "Normal"),
		("V", "Vacacional"),
	)
	
	anno = models.CharField(
		max_length=4, 
		verbose_name="Año"
	)
	ciclo = models.CharField(
		max_length=1, 
		choices=CICLOS, 
		verbose_name="Ciclo"
	)
	tipo = models.CharField(
		max_length=1, 
		choices=TIPO, 
		verbose_name="Tipo"
	)
	
	def __str__(self):
		return f"{self.anno}{self.ciclo}"
	
	class Meta:
		db_table = "CiclosAcademicos"
		verbose_name = "CiclosAcademico"
		ordering = ["anno", "ciclo"]

# -- Tabla ClasificacionPrediccion -------------------------------------------------------------------------
class ClasificacionPrediccion(models.Model):
	codigo_prediccion = models.CharField(
		max_length=1, 
		verbose_name="Código de Predicción"
	)
	descripcion_prediccion = models.CharField(
		max_length=10, 
		verbose_name="Descripción de Predicción"
	)
	
	def __str__(self):
		return f"{self.codigo_prediccion} - {self.descripcion_prediccion}"
	
	class Meta:
		db_table = "ClasificacionPrediccion"
		verbose_name = "ClasificacionPrediccion"
		ordering = ["codigo_prediccion"]

# -- Tabla Secciones ---------------------------------------------------------------------------------------
class Secciones(models.Model):
	seccion = models.CharField(
		max_length=1, 
		verbose_name="Sección"
	)
	
	def __str__(self):
		return self.seccion
	
	class Meta:
		db_table = "Secciones"
		verbose_name = "Sección"
		ordering = ["seccion"]

# -- Tabla Aulas -------------------------------------------------------------------------------------------
class Aulas(models.Model):
	aula = models.CharField(
		max_length=1, 
		verbose_name="Aula"
	)
	
	def __str__(self):
		return self.aula
	
	class Meta:
		db_table = "Aulas"
		verbose_name = "Aula"
		ordering = ["aula"]
	
# -- Tabla Matricula ---------------------------------------------------------------------------------------
class Matricula(models.Model):
	
	FACULTAD = (
		('1', 'FIIS'),
		('2', 'FIEE'),
		('3', 'FIM'),
		('4', 'FIA'),
		('5', 'FIC'),
		('6', 'FIGMM'),
		('7', 'FA'),
		('8', 'FIECS'),
	)
	
	id_alumno = models.ForeignKey(
		Alumnos, 
		on_delete=models.CASCADE, 
		verbose_name="Alumno", 
		db_column="id_alumno"
	)
	facultad = models.CharField(
		max_length=1, 
		choices=FACULTAD, 
		verbose_name="Facultad"
	)
	max_cred = models.PositiveSmallIntegerField(
		verbose_name="Cantidad de Créditos máx. a inscribir"
	)
	
	
	def __str__(self):
		return f"{self.id_alumno.codigo_uni}-{self.id_alumno.apellido_p} {self.id_alumno.apellido_m}, {self.id_alumno.nombres}"
	
	class Meta:
		db_table = "Matriculas"
		verbose_name = "Matricula"
		ordering = [
			"id_alumno__apellido_p",
			"id_alumno__apellido_m"
		]
	
# -- Tabla DetalleMatricula --------------------------------------------------------------------------------
class DetalleMatricula(models.Model):
	id_curso = models.ForeignKey(
		Cursos, 
		on_delete=models.DO_NOTHING, 
		verbose_name="Curso", 
		null=True, 
		db_column="id_curso"
	)
	repetido = models.PositiveSmallIntegerField(
		verbose_name="Repetido"
	)
	id_seccion = models.ForeignKey(
		Secciones, 
		on_delete=models.DO_NOTHING, 
		verbose_name="Sección", 
		db_column="id_seccion"
	)
	id_codigo_prediccion = models.ForeignKey(
		ClasificacionPrediccion, 
		on_delete=models.DO_NOTHING, 
		verbose_name="Código de Predicción", 
		null=True, 
		db_column="id_codigo_prediccion"
	)
	
	def __str__(self):
		return f"{self.id_curso__codigo}-{self.id_curso__curso}"
	
	class Meta:
		db_table = "DetalleMatricula"
		verbose_name = "DetalleMatricula"
		ordering = ["id_curso__curso"]
		
# -- Tabla CursoSeccion ------------------------------------------------------------------------------------
class CursoSeccion(models.Model):
	TIPO_CLASE = (
		('T', 'Teórica'),
		('P', 'Práctica'),
		('Lab', 'Laboratorio'),
	)
	
	DIA = (
		('LU', 'Lunes'),
		('MA', 'Martes'),
		('MI', 'Miércoles'),
		('JU', 'Jueves'),
		('VI', 'Viernes'),
		('SA', 'Sábados'),
	)
	
	id_curso = models.ForeignKey(
		Cursos, 
		on_delete=models.CASCADE, 
		verbose_name="Curso", 
		db_column="id_curso"
	)
	id_seccion = models.ForeignKey(
		Secciones, 
		on_delete=models.SET_NULL, 
		null=True, 
		verbose_name="Sección", 
		db_column="id_seccion"
	)
	tipo_clase = models.CharField(
		max_length=3, 
		choices=TIPO_CLASE, 
		verbose_name="Tipo de Clase"
	)
	dia = models.CharField(
		max_length=2, 
		choices=DIA, 
		verbose_name="Día"
	)
	hora_ini = models.PositiveSmallIntegerField(
		verbose_name="Hora Inicial"
	)
	hora_fin = models.PositiveSmallIntegerField(
		verbose_name="Hora Final"
	)
	id_docente = models.ForeignKey(
		Docentes, 
		on_delete=models.SET_NULL, 
		null=True, 
		verbose_name="Docente", 
		db_column="id_docente"
	)
	id_aula = models.ForeignKey(
		Aulas,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="Aula",
		db_column="id_aula"
	)
	vacantes = models.PositiveSmallIntegerField(
		verbose_name="Vancates"
	)
	inscritos = models.PositiveSmallIntegerField(
		verbose_name="Inscritos"
	)
	
	def __str__(self):
		return f"{self.id_curso__codigo}-{self.id_curso__curso} {self.id_seccion__seccion}"
	
	class Meta:
		db_table = "CursoSeccion"
		verbose_name = "CursosSeccion"
		ordering = ["id_curso__curso"]

# ----------------------------------------------------------------------------------------------------------
