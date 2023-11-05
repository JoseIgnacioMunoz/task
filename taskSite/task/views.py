from django.shortcuts import render
from .models import Task

def post_list(request):
    tareas = Task.objects.all()
    return render(request, 'task/tareas.html', {'tareas': tareas})