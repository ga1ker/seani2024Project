# Generated by Django 5.0.2 on 2024-02-27 18:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
        ('library', '0004_alter_question_question_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0.0, verbose_name='Puntaje')),
                ('modules', models.ManyToManyField(to='library.module', verbose_name='Módulo')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.stage', verbose_name='Estado')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ExamModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('score', models.FloatField(default=0.0, verbose_name='Puntaje')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam', verbose_name='Examen')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.module', verbose_name='Modulo')),
            ],
        ),
    ]
