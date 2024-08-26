from django.db import models
from django.contrib.auth.models import User # En vez de crear la tabla de User usamos la que nos facilita Django
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Relación con la tabla Project
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    done = models.BooleanField(default=False)

    # Añadiendo más campos

    created =models.DateTimeField(default=timezone.now) # A la hora de crearse se pone la fecha de ese instante
    datecompleted = models.DateTimeField(null=True, blank=True) # Inicialmente va a ser null porque es un campo que tendrá que rellenar el usuario
    important = models.BooleanField(default= False) # Inicialmente la tarea no será siempre importante
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) # Le indicamos que al crear el nuevo modelo todo lo anterior vaya al usuario 1 por defecto

    def __str__(self):
        return self.title + ' - ' + self.project.name + ' - by ' + self.user.username

