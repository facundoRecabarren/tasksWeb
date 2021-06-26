from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tasks-home'),
    path('tasks/', views.tareas, name='tasks-tareas'),
    path('tasks/<int:pk>/delete/',views.deleteTaskView.as_view(), name="delete-task"),
    path('tasks/<int:pk>/update/',views.updateTaskView.as_view(), name="update-task"),
    path('tasks/<int:pk>/start/',views.start_task, name="start-task"),
    path('tasks/<int:pk>/end/',views.end_task, name="start-task")
]