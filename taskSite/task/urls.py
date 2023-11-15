from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='post_list'),
    path('tasks/completadas/', views.CompletedTaskList.as_view(), name='completadas'),
    path('tasks/pendientes/', views.PendingTaskList.as_view(), name='pendientes'),
    path('tasks/completadas/<int:pk>/', views.DetalleTareaView.as_view(), name='detalle_tarea_completada'),  # Agregamos para completadas
    path('tasks/pendientes/<int:pk>/', views.DetalleTareaView.as_view(), name='detalle_tarea_pendiente'),  # Agregamos para pendientes
]
