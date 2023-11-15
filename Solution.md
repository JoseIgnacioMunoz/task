Activamos virtualenvwrapper para, posteriormente, crear un entorno virtual: 

```bash
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
```

Creamos un entorno virtual dentro del directorio "entornoVirtual" de este repositorio:

```bash 
mkvirtualenv <nombreEntorno>  
```
Actualizar pip

```bash
python -m pip install --upgrade pip
```
Usamos el archivo requirements.txt para instalar las dependencias (Django~=3.2.10):
```bash
pip install -r requirements.txt
```
Una vez instalado Django, ahora crearemos la estructura de directorios inicial iniciando un proyecto con startproject:
```bash
django-admin startproject taskSite
```
He tenido un problema con la rama local y la remota porque cuando quise hacer el push, tenía cambios hechos en la rama remota que no tenía en local y viceversa. Así que tuve que hacer un merge entre las dos ramas: 
```bash
git config pull.rebase false
```
```bash
git pull origin main
```

Continuando con el proyecto, ahora lo que debemos hacer es modificar el archivo settings.py para que contenga las siguientes sentencias:

```python
TIME_ZONE = ‘Europe/Madrid’

LANGUAGE_CODE = ‘es-es’

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
```

En el mismo archivo, enlazamos la base de datos db.sqlite3: 

```python
DATABASES = {

'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',

}
}
```

A continuación, aseguramos que el esquema de la base de datos esté actualizado con los modelos y cambios en el esquema del proyecto con: 

```bash
python manage.py migrate
```

 Arrancamos el servidor: 

 ```bash
python manage.py runserver
 ```

 Comprobamos navegando hacia http://localhost:8000

Creamos la estructura de la aplicación task

```bash
python manage.py startapp task
```

Como hemos creado la aplicación task, vamos a registrarla en el archivo settings.py de taskSite:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task',
]
```

Para crear un modelo, dirígete hacia models.py y pon lo siguiente: 

```python
from django.db import models

class Task(models.Model):

    nomTarea = models.CharField(max_length=250)
    descrip = models.CharField(max_length=250)
    hecha = models.BooleanField(default=False)
    
    def __str__(self):

        return self.nomTarea
```

Acabamos de cambiar el modelo, así que vamos a registrar los cambios en la base de datos: 

```bash
python manage.py makemigrations task
```

Después ejecutamos el migrate:

```bash
python manage.py migrate task
```

Modificamos el archivo admin.py: 

```python
from django.contrib import admin
from .models import Task

admin.site.register(Task)
```

Creamos la cuenta de administrador: 

```bash
python manage.py createsuperuser
```

Comprobamos que lo hemos hecho bien navegando hacia : http://127.0.0.1:8000/admin/
-Nota: comprobar que en ALLOWED_HOSTS de settings está así ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.pythonanywhere.com']

## URLs

Para que Django redirija todo lo que entre a 'http://127.0.0.1:8000/' hacia task.urls, escribimos en el archivo taskSite/urls.py lo siguiente:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),
]
```

A continuación, creamos otro archivo vacío urls.py en el directorio task de nuestro proyecto y escribimos lo siguiente:

```python
from django.urls import path
from . import views

urlpatterns = [
 path('', views.post_list, name='post_list'),
]
```

## Views

En el archivo views.py de /task, ponemos lo siguiente para importar las vistas: 

```python
from django.shortcuts import render
from .models import Task

def post_list(request):
    tareas = Task.objects.all()
    return render(request, 'task/tareas.html', {'task': task})
```

## Templates

Para crear los templates, antes organizamos la estructura de carpetas: task/templates/task

Después, dentro del último directorio task creado, creamos un archivo tareas.html:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tareas J Ignacio Muñoz Sotelo</title>
</head>
<body>

    {%for tarea in tareas%}
        Nombre: {{tarea.nomTarea}} <br>
        Descripcion: {{tarea.descrip}} <br>
        Hecho: {{tarea.hecha}} <br>
        <br>
        {%empty%}
        No hay tareas para realizar.
    {%endfor%}
    
</body>
</html>
```
