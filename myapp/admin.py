from django.contrib import admin
from .models import Project, Task

# Register your models here.

# Este archivo es para poder ver y usar los modelos en modo administrador de django

admin.site.register(Project)
admin.site.register(Task)
