from django import forms
from django.forms import ModelForm
from .models import Task


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, 
            widget=forms.TextInput(attrs={'class': 'input'})) # Llamamos a una clase que hemos creado nosotros directamente desde el css
    description= forms.CharField(label="descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200,
        widget=forms.TextInput(attrs={'class': 'input'}))
    

# Creación de formularios con soporte en Django
class CreateTaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
