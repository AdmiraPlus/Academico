# Generated by Django 4.1.1 on 2022-11-22 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0005_alter_detallematricula_id_codigo_prediccion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matricula',
            name='id_alumno',
        ),
        migrations.DeleteModel(
            name='DetalleMatricula',
        ),
        migrations.DeleteModel(
            name='Matricula',
        ),
    ]
