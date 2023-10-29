# Django proyecto inicial

Esqueleto de Django con algunas modificaciones algunas cosas utiles como un gitignore configurado para Django y un sistema de generación de clave secreta para poder publicar tu proyecto sin problemas de seguridad. 
Este proyecto lo hago para tenerlo como base para cualquier proyecto y partir de el para ahorrar tiempo

## Configuración del entorno

1. Crear el entorno virtual con el comando `python -m venv ./venv`
1. Asegúrese de tener instalado Python y Django en su sistema.
2. Clone este repositorio en su sistema local.
3. Para que funcione tienes que crear una clave secreta, para ello crea un archivo llamado en app/secret.py con: SECRET_KEY = '' y entre comillas pegas el resultado de ejecutar python generador_django.py
4. Instale las dependencias del proyecto utilizando el comando `pip install -r requirements.txt`.
5. Ejecuta `python manage.py migrate` para completar la configuración de la base de datos.

## Uso


Ejecutar el entorno virtual con el comando `.\venv\Scripts\activate`
Inicie el servidor Django con el comando `python manage.py runserver`.
Para iniciar el scraping web, navegue a la URL `http://localhost:8000/`.

## Contribuir

Las contribuciones son bienvenidas. Por favor, haga un "Fork" del proyecto y proponga cambios a través de un "Pull Request".
