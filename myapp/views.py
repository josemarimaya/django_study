from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
# Create your views here.

def index(request):
    title = "Welcome to DJANGO"
    # Podemos pasarle la variable de title que hemos creado como parámetro en el tercer componente, el diccionario
    return render(request, 'index.html', {
        'title': title
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
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    #task = Task.objects.get(id=id)
    tasks = Task.objects.all()
    # task = get_object_or_404(Task, id=id)
    #return HttpResponse("Task: %s" % task.title)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def task_title(request, title):
    task = get_object_or_404(Task, title=title)
    return HttpResponse("Task: %s" % task.title)
