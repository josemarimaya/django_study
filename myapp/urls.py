
from django.urls import path, include
from . import views # Importamos las views directamente desde la app

urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello),
    path('hello/<int:id>', views.hello_id),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.go_project, name='detail'),
    path('tasks/', views.tasks_signout, name='tasks'),
    path('tasks_completed/', views.completed_tasks_list, name='completed_task_list'),
    path('tasks_user/', views.tasks_sigin, name='tasks_user'),
    path('tasks_user/<int:task_id>', views.tasks_detail_user, name='tasks_user_detail'),
    #path('tasks/<str:title>', views.task_title),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.task_completed, name='task_completed'),
    path('tasks/<int:task_id>/delete', views.task_deleted, name='task_delete'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project'),
    path('signin/', views.sig_in, name='sign_in'),
    path('signup/', views.sign_up, name='sign_up'),
    path('signout/', views.signout, name='sign_out'),

]
