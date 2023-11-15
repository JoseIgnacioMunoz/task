from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='post_list'),
    path('tasks/completadas/', views.CompletedTaskList.as_view(), name='completadas'),
    path('tasks/pendientes/', views.PendingTaskList.as_view(), name='pendientes'),
    path('tasks/completadas/<int:pk>/', views.DetalleTareaView.as_view(), name='detalle_tarea'),  # Agregamos para completadas
    path('tasks/pendientes/<int:pk>/', views.DetalleTareaView.as_view(), name='detalle_tarea'),  # Agregamos para pendientes
    path('tasks/editarTarea/<int:pk>/', views.EditarTareaView.as_view(), name='editarTarea'),
    path('eliminarTarea/<int:pk>/', views.EliminarTareaView.as_view(), name='eliminarTarea'),

]
