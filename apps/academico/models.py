from django.db import models

# Create your models here.

# -- Tabla Alumnos -----------------------------------------------------------------------------------------
class Alumnos(models.Model):
    codigo_uni = models.CharField(max_length=9, verbose_name="Código UNI")
    numero_dni = models.CharField(max_length=9, verbose_name="Número de DNI")
    apellido_p = models.CharField(max_length=20, verbose_name="Apellido Paterno")
    apellido_m = models.CharField(max_length=20, verbose_name="Apellido Materno")
    nombres = models.CharField(max_length=40, verbose_name="Nombres")

    def __str__(self):
        return f"{self.apellido_p} {self.apellido_m}, {self.nombres}"
    
    class Meta:
        db_table = "Alumnos"
        verbose_name = "Alumno"
        ordering = ["apellido_p", "apellido_m", "nombres"]

# -- Tabla Docentes ----------------------------------------------------------------------------------------
class Docentes(models.Model):
    nro_dni = models.CharField(max_length=9, verbose_name="Número de DNI")
    apellido_p = models.CharField(max_length=20, verbose_name="Apellido Paterno")
    apellido_m = models.CharField(max_length=20, verbose_name="Apellido Materno")
    nombres = models.CharField(max_length=40, verbose_name="Nombres")
    
    def __str__(self):
        return f'{self.apellido_p} {self.apellido_m}, {self.nombres}'

    class Meta:
        db_table = "Docentes"
        verbose_name = "Docente"
        ordering = ["apellido_p", "apellido_m", "nombres"]

# -- Tabla SistemaEvaluacion -------------------------------------------------------------------------------
class SistemaEvaluacion(models.Model):
    sistema_evaluacion = models.CharField(max_length=1, verbose_name="Sist. de Evaluación")

    def __str__(self):
        return self.sistema_evaluacion

    class Meta:
        db_table = "SistemasEvaluacion"
        verbose_name = "SistemaEvaluacion"
        ordering = ["sistema_evaluacion"]

# -- Tabla Cursos ------------------------------------------------------------------------------------------
class Cursos(models.Model):
    codigo = models.CharField(max_length=5, verbose_name="Código del Curso")
    curso = models.CharField(max_length=40, verbose_name="Curso")
    sistema_evaluacion = models.ForeignKey(SistemaEvaluacion, on_delete=models.DO_NOTHING, verbose_name="Sist. de Evaluación")

    def __str__(self):
        return self.curso

    class Meta:
        db_table = "Cursos"
        verbose_name = "Curso"
        ordering = ["curso", "codigo"]

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
    
    anno = models.CharField(max_length=4, verbose_name="Año")
    ciclo = models.CharField(max_length=1, choices=CICLOS, verbose_name="Ciclo")
    tipo = models.CharField(max_length=1, choices=TIPO, verbose_name="Tipo")
	
    def __str__(self):
        return f"{self.anno}{self.ciclo}"
	
    class Meta:
        db_table = "CiclosAcademicos"
        verbose_name = "CiclosAcademico"
        ordering = ["anno", "ciclo"]

# ----------------------------------------------------------------------------------------------------------

