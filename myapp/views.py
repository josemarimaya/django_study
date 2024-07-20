from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    return HttpResponse("<h2>Index page</h2>")


def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello %s</h2>" %username)

def hello_id(request, id):
    print(type(id))
    result = id + 100 * 2
    return HttpResponse("<h2>Hello %i</h2>" %result)

def about(request):
    return HttpResponse("<h1> About </h1>")

def projects(request):
    projects = list(Project.objects.values())
    #return HttpResponse("Projects:")
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    #task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse("Task: %s" % task.title)

def task_title(request, title):
    task = get_object_or_404(Task, title=title)
    return HttpResponse("Task: %s" % task.title)
