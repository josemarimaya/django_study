
from django.urls import path, include
from . import views # Importamos las views directamente desde la app

urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello),
    path('hello/<int:id>', views.hello_id),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<str:title>', views.task_title),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project')
]
