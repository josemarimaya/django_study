# Imports del proyecto
from .models import Project, Task
from .forms import CreateNewProject, CreateTaskForm

# Imports de django
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Importamos un formulario de Django ya creado
from django.contrib.auth.models import User # Importamos un modelo ya creado de usuarios de Django
from django.contrib.auth import login, logout, authenticate # Creación de cookies para los usuarios, Logout de usuario, Autentificación...
from django.db import IntegrityError # Para trabajar con manejo de errores concretos



def index(request):
    title = "Welcome to DJANGO"
    # Podemos pasarle la variable de title que hemos creado como parámetro en el tercer componente, el diccionario
    return render(request, 'index.html', {
        'title': title
    })

def sig_in(request):

    if request.method == 'GET':
        print('Enviando formulario')
    else:
        print(request.POST)

        user_authenticate = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user_authenticate is None: # Si el usuario no se encuentra en la base de datos lo devuelve vacío

            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña es incorrecta'
            })
        else:
            login(request, user_authenticate) # Si el usuario existe le guardo la autentificación
            return redirect('tasks')

    return render(request, 'signin.html', {
            'form': AuthenticationForm
    })

def sign_up(request):

    if request.method == 'GET':
        print('Enviando formulario')
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            # manejo de errores con try/catch
            try: 
                user = User.objects.create_user(username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()                
                login(request, user) # Creación de cookies para el usuario
                return redirect('tasks')
            
            except IntegrityError: # Usamos excepciones con errores específicos
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden'
            })
        
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })

def signout(request):
    logout(request)
    return redirect('main')
        
def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello %s</h2>" %username)

def hello_id(request, id):
    print(type(id))
    result = id + 100 * 2
    return HttpResponse("<h2>Hello %i</h2>" %result)

def about(request):
    username = "Josemari"
    return render(request, 'about.html', {
        'username' : username
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    #return HttpResponse("Projects:")
    #return JsonResponse(projects, safe=False)
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks_sigin(request):
    #task = Task.objects.get(id=id)
    #tasks = Task.objects.all()
    tasks = Task.objects.filter(user = request.user, # Para filtrar por el usuario iniciado
                                datecompleted__isnull=True) # Y filtramos por aquellas que no están completadas
    # task = get_object_or_404(Task, id=id)
    #return HttpResponse("Task: %s" % task.title)
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def tasks_signout(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def task_detail(request, task_id): # Nos traemos el task_id de la urls.py en el que los hemos invocado
    #task = Task.objects.get(pk=task_id)

    if request.method == 'GET':

        task = get_object_or_404(Task, pk=task_id)
        form = CreateTaskForm(instance=task)
        return render(request, 'tasks/task_detail.html',{
            'task': task,
            'form': form
        })
    
    else:
        try:

            task = get_object_or_404(Task, pk=task_id)
            form = CreateTaskForm(request.POST, instance= task)
            form.save()
            return redirect('tasks_user')
        
        except ValueError:

            return render(request, 'tasks/task_detail.html', {
                'form': CreateTaskForm(),
                'error': 'Fallo al actualizar'
            })



def task_title(request, title):
    task = get_object_or_404(Task, title=title)
    return HttpResponse("Task: %s" % task.title)

def create_task(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'tasks/create_task.html', {
            'form': CreateTaskForm()
        })
    else:
        """Task.objects.create(title=request.POST['title'], description=request.POST['description'], 
        # Al poner project_id le estamos señalando al proyecto al que pertenece
        project_id=2)
        
        return redirect('tasks') # Ahora redirigimos con el name de la url"""

        try:
            form = CreateTaskForm(request.POST)
            new_task = form.save(commit=False) # Obtenemos la tarea que estamos haciendo sin hacerle post
            new_task.user = request.user # Como sabemos que cada tarea necesita un usuario por su fk cogemos el del usuario que está con la sesión iniciada
            new_task.save() # Finalmente almacenamos la tarea
            print(form) 
            return redirect('tasks_user')
        
        except ValueError:
            return render(request, 'tasks/create_task.html', {
                'form': CreateTaskForm(),
                'error': 'Por favor provee valores válidos'
            })
        

'''
Pruebas con GET
def create_task(request):
    Task.objects.create(title=request.GET['title'], description=request.GET['description']
        , projectkey=2)
    return render(request, 'create_task.html', {
        'form': CreateNewTask()
    })
'''

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    

def go_project(request, id):
    project = get_object_or_404(Project, id=id) # Si no existe el proyecto con el id se devuelve un 404
    #tasks = Task.objects.all()
    tasks = Task.objects.filter(project_id=id) # Filtramos por id del proyecto
    return render(request, 'projects/details.html', {
        'project_name':project.name,
        'tasks':tasks
    })





    
