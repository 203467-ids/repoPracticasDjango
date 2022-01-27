# Ambientación del back Django

## Instalación de los recuros de restframework librerias 
```bash
pip install djangorestframework
```
```bash
pip install markdown 
```
```bash
pip install django-filter  
```

## Agregar la libreria a INSTALLED_APPS en settings
```bash
'rest_framework',
```
## Instalacion para el manejo de variables de entorno 
```bash
pip install python-dotenv
```
## Agregar a settings.py
```bash
from dotenv import load_dotenv
import os 
load_dotenv() 
```