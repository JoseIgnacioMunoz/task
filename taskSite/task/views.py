from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views import View

"""
def post_list(request):
    tareas = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form=TaskForm() 
    return render(request, 'task/tareas.html', {'tareas': tareas, 'form': form})
"""

class TaskList(View):
    template_name = 'task/tareas.html'

    def get(self, request):
        tareas = Task.objects.all()
        form=TaskForm()
        return render(request, self.template_name, {'tareas': tareas, 'form': form})
    
    def post(self, request):
        form = TaskForm(request.POST)
        tareas = Task.objects.all()
        if form.is_valid():
            form.save()
            return redirect('post_list')
        return render(request, self.template_name, {'tareas': tareas, 'form': form})

class CompletedTaskList(View):
    template_name = 'task/completadas.html'

    def get(self, request):
        tareasCompletadas = Task.objects.filter(hecha=True)
        return render(request, self.template_name, {'completadas': tareasCompletadas})

    def post(self, request):
        form = TaskForm(request.POST)
        tareasCompletadas = Task.objects.filter(hecha=True)
        if form.is_valid():
            form.save()
            return redirect('completadas')
        return render(request, self.template_name, {'completadas': tareasCompletadas, 'form': form})


class PendingTaskList(View):
    template_name = 'task/pendientes.html'

    def get(self, request):
        tareasPendientes = Task.objects.filter(hecha=False)
        return render(request, self.template_name, {'pendientes': tareasPendientes})

    def post(self, request):
        form = TaskForm(request.POST)
        tareasPendientes = Task.objects.filter(hecha=False)
        if form.is_valid():
            form.save()
            return redirect('pendientes')
        return render(request, self.template_name, {'pendientes': tareasPendientes, 'form': form})
    
class DetalleTareaView(View):
    template_name = 'task/detalleTarea.html'  

    def get(self, request, pk):
        tarea = Task.objects.get(pk=pk)
        return render(request, self.template_name, {'tarea': tarea})

"""
class TaskList(View):
    def post_list(request):
        tareas = Task.objects.all()

        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                nomTarea = form.cleaned_data['nomTarea']
                descrip = form.cleaned_data['descrip']
                hecha = form.cleaned_data['hecha']

                Task.objects.create(nomTarea=nomTarea, descrip=descrip, hecha=hecha)
                return redirect('post_list')
        else:
            form=TaskForm() 
        return render(request, 'task/tareas.html', {'tareas': tareas, 'form': form})
"""