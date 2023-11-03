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
