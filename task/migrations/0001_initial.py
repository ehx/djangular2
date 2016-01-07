# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('lastname', models.CharField(max_length=50, verbose_name=b'Apellido')),
                ('address', models.CharField(max_length=50, verbose_name=b'Direccion')),
                ('telephone', models.IntegerField(verbose_name=b'Telefono')),
                ('mail', models.EmailField(max_length=254, verbose_name=b'Mail')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=255, verbose_name=b'Mensaje')),
                ('read', models.BooleanField(default=0, verbose_name=b'Leido')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.OneToOneField(related_name='user_owner', verbose_name=b'Usuario que envia', to=settings.AUTH_USER_MODEL)),
                ('receptor', models.OneToOneField(related_name='user_receptor', verbose_name=b'Receptor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=50, verbose_name=b'Nombre corto')),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ntype', models.CharField(max_length=50, verbose_name=b'Tipo de notificacion')),
                ('notification', models.IntegerField(verbose_name=b'Notification')),
                ('read', models.BooleanField(default=0, verbose_name=b'Leida?')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('address', models.CharField(max_length=50, verbose_name=b'Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Titulo de la tarea')),
                ('turnover_code', models.CharField(default=0, max_length=50, verbose_name=b'Codigo en Turnover')),
                ('priority', models.IntegerField(null=True, verbose_name=b'Orden')),
                ('start_date', models.DateField(null=True, verbose_name=b'Fecha de Inicio')),
                ('finish_date', models.DateField(null=True, verbose_name=b'Fecha Comprometida')),
                ('estimation_hours', models.IntegerField(default=0, verbose_name=b'Horas Estimada')),
                ('description', models.CharField(default=b'', max_length=255, verbose_name=b'Descripcion')),
                ('sar', models.IntegerField(default=0, verbose_name=b'Incidente')),
                ('done', models.BooleanField(default=0, verbose_name=b'Completado')),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(related_name='userClient', verbose_name=b'Cliente', to=settings.AUTH_USER_MODEL, null=True)),
                ('module', models.ForeignKey(verbose_name=b'Modulo', to='task.Module', null=True)),
                ('status', models.ForeignKey(verbose_name=b'Estado', to='task.Status', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=5000, verbose_name=b'Comentario')),
                ('docfile', models.FileField(null=True, upload_to=b'%Y-%m-%d')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(verbose_name=b'Tarea', to='task.Task')),
                ('user', models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255, verbose_name=b'Descripcion')),
                ('done', models.BooleanField(default=0, verbose_name=b'Completado')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(verbose_name=b'Tarea', to='task.Task', null=True)),
                ('user', models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Urgency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='UserClient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relation', models.CharField(max_length=1, verbose_name=b'Relacion Directa/Hereda')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('userR', models.OneToOneField(related_name='userR', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('online', models.BooleanField(default=1, verbose_name=b'Online')),
                ('organization', models.ForeignKey(verbose_name=b'Organizacion', to='task.Organization')),
                ('user', models.OneToOneField(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='urgency',
            field=models.ForeignKey(verbose_name=b'Urgencia', to='task.Urgency', null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(related_name='userTask', verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
