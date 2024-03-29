# Generated by Django 4.1.1 on 2022-11-22 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0004_alter_matricula_id_alumno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallematricula',
            name='id_codigo_prediccion',
            field=models.ForeignKey(db_column='id_codigo_prediccion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='academico.clasificacionprediccion', verbose_name='Código de Predicción'),
        ),
        migrations.AlterField(
            model_name='detallematricula',
            name='id_curso',
            field=models.ForeignKey(db_column='id_curso', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='academico.cursos', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='detallematricula',
            name='id_seccion',
            field=models.ForeignKey(db_column='id_seccion', on_delete=django.db.models.deletion.DO_NOTHING, to='academico.secciones', verbose_name='Sección'),
        ),
    ]
