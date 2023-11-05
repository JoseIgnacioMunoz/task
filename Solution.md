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
from django.conf import settings

from django.db import models

from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)

    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):

        self.published_date = timezone.now()

        self.save()

    def __str__(self):

        return self.title
```

Acabamos de cambiar el modelo, así que vamos a registrar los cambios en la base de datos: 

```bash
python manage.py makemigrations task
```

Después ejecutamos el migrate:

```bash
python manage.py migrate blog
```

Modificamos el archivo admin.py: 

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Creamos la cuenta de administrador: 

```bash
python manage.py createsuperuser
```

