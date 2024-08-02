from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject
from django.contrib.auth.forms import UserCreationForm # Importamos un formulario de Django ya creado
# Create your views here.

def index(request):
    title = "Welcome to DJANGO"
    # Podemos pasarle la variable de title que hemos creado como parámetro en el tercer componente, el diccionario
    return render(request, 'index.html', {
        'title': title
    })

def sig_in(request):
    return render(request, 'signin.html')

def sign_up(request):
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })


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

def tasks(request):
    #task = Task.objects.get(id=id)
    tasks = Task.objects.all()
    # task = get_object_or_404(Task, id=id)
    #return HttpResponse("Task: %s" % task.title)
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def task_title(request, title):
    task = get_object_or_404(Task, title=title)
    return HttpResponse("Task: %s" % task.title)

def create_task(request):
    if request.method == 'GET':
        # show interface
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], 
        # Al poner project_id le estamos señalando al proyecto al que pertenece
        project_id=2) 
        return redirect('tasks') # Ahora redirigimos con el name de la url
        

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





    
