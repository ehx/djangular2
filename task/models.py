import os
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.utils import timezone
from redactor.fields import RedactorField

class Urgency(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return self.name

class Module(models.Model):
    tag = models.CharField(max_length=50, verbose_name="Nombre corto")
    name = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return self.tag + ' - ' + self.name

class Notification(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuario')
    ntype = models.CharField(max_length=50, verbose_name="Tipo de notificacion")
    notification = models.IntegerField(verbose_name="Notification")
    read = models.BooleanField(default=0, verbose_name="Leida?");
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.ntype

class Organization(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    address = models.CharField(max_length=50, verbose_name="Direccion")

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    lastname = models.CharField(max_length=50, verbose_name='Apellido')
    address = models.CharField(max_length=50, verbose_name='Direccion')
    telephone = models.IntegerField(verbose_name='Telefono')
    mail = models.EmailField(max_length=254, verbose_name='Mail')
    
    def __str__(self):
        return self.name + ' ' + self.lastname

class Task(models.Model):
    user = models.ForeignKey(User, null=True, verbose_name='Usuario')
    client = models.ForeignKey(User, null=True, verbose_name='Cliente', related_name="userR")
    title = models.CharField(max_length=100, verbose_name='Titulo de la tarea')
    turnover_code = models.CharField(default=0, max_length=50, verbose_name='Codigo en Turnover')
    priority = models.IntegerField(null=True, verbose_name='Orden')
    urgency = models.ForeignKey(Urgency, null=True, verbose_name='Urgencia')
    start_date = models.DateField(null=True, verbose_name='Fecha de Inicio')
    finish_date = models.DateField(null=True, verbose_name='Fecha Comprometida')
    estimation_hours = models.IntegerField(default=0, verbose_name='Horas Estimada')
    description = models.CharField(default='', max_length=255, verbose_name='Descripcion')
    sar = models.IntegerField(default=0, verbose_name='Incidente')
    done = models.BooleanField(default=0, verbose_name='Completado')
    module = models.ForeignKey(Module, null=True, verbose_name="Modulo")
    status = models.ForeignKey(Status, null=True, verbose_name="Estado")
    creation_date = models.DateField(null=True, blank=True,auto_now_add=True)

    def __str__(self):   
        return self.title

class TaskComment(models.Model):
    task = models.ForeignKey(Task, verbose_name="Tarea")
    user = models.ForeignKey(User, verbose_name="Usuario")
    comment = models.CharField(max_length= 5000, verbose_name="Comentario")
    docfile = models.FileField(upload_to='%Y-%m-%d', null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):   
        return self.user.first_name + ' ' + self.comment

    def delete(self,*args,**kwargs):
        if hasattr(self.docfile, 'path'):
            if os.path.isfile(self.docfile.path):
                os.remove(self.docfile.path)

        super(TaskComment, self).delete(*args,**kwargs)

class UserClient(models.Model):
    user = models.ForeignKey(User)
    userR = models.ForeignKey(User, related_name="userR")

    def __str__(self):   
        return self.user.last_name + ' / ' + self.userR.last_name

class Todo(models.Model):
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    user = models.ForeignKey(User, verbose_name="Usuario")
    task = models.ForeignKey(Task, null=True, verbose_name="Tarea")
    done = models.BooleanField(default=0, verbose_name='Completado')
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):   
        return self.user.first_name  + ' / ' + self.description 

class Message(models.Model):
    owner = models.OneToOneField(User, verbose_name="Usuario que envia", related_name="user_owner", unique=True)
    receptor = models.OneToOneField(User, verbose_name="Receptor", related_name="user_receptor", unique=True)
    message = models.CharField(max_length=255, verbose_name='Mensaje')
    read = models.BooleanField(default=0, verbose_name='Leido')
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):   
        return self.user.first_name  + ' / ' + self.client.name + ' @ ' + self.message

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, verbose_name="Usuario")
    organization = models.ForeignKey(Organization, verbose_name="Organizacion")
    online = models.BooleanField(default=1, verbose_name='Online')

    def __str__(self):   
        return self.user.first_name  + ' ' + self.user.last_name