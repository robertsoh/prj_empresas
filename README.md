## Instalación:

- Instalar pip y virtualenv `sudo apt-get install python-pip python-virtualenv`
- Crear entorno virtual: `virtualenv --no-site-package --distribute`
- Activar el entorno virtual: `source bin/activate`
- Instalar dependencias: `pip install -r requirements/dev.txt`

- Configuración de variables de entorno para el sistema:
```sh
    DJANGO_SETTINGS_MODULE
    SECRET_KEY
    DB_USER
    DB_NAME
    DB_HOST
    DB_PASSWORD
```

- Instalar dependencias: tesseract-ocr, python-lxml
```
    sudo apt-get install tesseract-ocr
    sudo apt-get install python-lxml
```

- Ejecutar las migraciones: `python manage.py migrate`
- Crear superusuario de django : `python manage.py createsuperuser`
- Ejecutar Django: `python manage.py runserver`
- Ingresar con el usuario creado
