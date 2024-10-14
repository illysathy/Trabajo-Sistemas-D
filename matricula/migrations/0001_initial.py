# Generated by Django 5.1.2 on 2024-10-14 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudiante_curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=150)),
                ('fecha_inicio', models.DateField()),
                ('costo', models.DecimalField(decimal_places=1, max_digits=8)),
                ('estudiante_curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='estudiante_curso.estudiantecurso')),
            ],
            options={
                'db_table': 'Matriculas',
            },
        ),
    ]
