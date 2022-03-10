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
```bash
pip install python-dotenv
```
```bash
pipenv install django Pillow
```
## Agregar la libreria a INSTALLED_APPS en settings
```bash
'rest_framework',
'rest_framework.authtoken',
```
## Instalar django-cors-headers
```bash
pip instalar django-cors-headers 
```
## Agregar corsheaders a la sección de aplicaciones instaladas
```bash
'corsheders',
```
## Agregar corsheaders middleware
```bash
'django.middleware.security.SecurityMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'corsheaders.middleware.CorsMiddleware',
```
## Agregar especificar el acceso a las peticiones 
```bash
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST =(
  'http: // localhost: 8000',
)
```