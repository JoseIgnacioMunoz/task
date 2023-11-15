from django.shortcuts import render, redirect, get_object_or_404
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
    
class EditarTareaView(View):
    template_name = 'task/editarTarea.html'

    def get(self, request, pk):
        tarea = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=tarea)
        return render(request, self.template_name, {'tarea': tarea, 'form': form})

    def post(self, request, pk):
        tarea = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=tarea)

        if form.is_valid():
            form.save()
            return redirect('detalle_tarea', pk=pk)

        return render(request, self.template_name, {'tarea': tarea, 'form': form})
    
class EliminarTareaView(View):
    template_name = 'task/eliminarTarea.html'

    def get(self, request, pk):
        # Obtener la tarea específica que se va a eliminar usando el identificador de la tarea (pk)
        tarea = get_object_or_404(Task, pk=pk)
        
        # Renderizar la plantilla eliminarTarea.html y pasar la tarea como contexto
        return render(request, self.template_name, {'tarea': tarea})

    def post(self, request, pk):
        # Obtener la tarea específica que se va a eliminar usando el identificador de la tarea (pk)
        tarea = get_object_or_404(Task, pk=pk)
        
        # Llamar al método delete() en el objeto de tarea para eliminar la tarea de la base de datos
        tarea.delete()
        
        # Redirigir al usuario a la lista de tareas (post_list) después de eliminar la tarea
        return redirect('post_list')

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