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
class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = { # Estilizamos importando el modelo inyectando los estilos de boostrap
            'title': forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Escribe el titulo de la tarea'}),
            'description': forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Agrega una descripción para la tarea realizada'}),
            'important': forms.CheckboxInput(attrs={'class' : 'form-check-input py-2'})
        }
