from django import forms
from .models import Task


class TaskForm (forms.ModelForm): 
    class Meta:
        model=Task
        fields = ('nomTarea', 'descrip', 'hecha')
        labels = {
            'nomTarea': 'Nombre',
            'descrip': 'Descripción',
            'hecha': 'Hecho',
        }


"""
class TaskForm (forms.Form): 
    Nombre = forms.CharField(label="Nombre", max_length=100)
    Descripción = forms.CharField(label="Descripción", widget=forms.Textarea)
    Hecha = forms.BooleanField(label="Hecha", required=False)
"""
