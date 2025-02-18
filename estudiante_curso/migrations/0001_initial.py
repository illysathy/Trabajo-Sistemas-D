# Generated by Django 5.1.2 on 2024-10-14 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curso', '0001_initial'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstudianteCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('fechaFinal', models.DateField()),
                ('estado', models.CharField(max_length=100)),
                ('notaFinal', models.DecimalField(decimal_places=2, max_digits=3)),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='curso.curso')),
                ('estudiante', models.ForeignKey(limit_choices_to={'rol': 'Estudiante'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cursos', to='persona.persona')),
            ],
            options={
                'db_table': 'Estudiantes_Cursos',
            },
        ),
    ]
