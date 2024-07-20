
from django.urls import path, include
from . import views # Importamos las views directamente desde la app

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('hello/<int:id>', views.hello_id),
    path('projects/', views.projects),
    path('tasks/<int:id>', views.tasks),
    path('tasks/<str:title>', views.task_title)
    
]
