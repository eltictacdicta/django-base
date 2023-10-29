# Django proyecto inicial

Esqueleto de Django con algunas modificaciones algunas cosas utiles como un gitignore configurado para Django y un sistema de generación de clave secreta para poder publicar tu proyecto sin problemas de seguridad.

## Configuración del entorno

1. Asegúrese de tener instalado Python y Django en su sistema.
2. Clone este repositorio en su sistema local.
3. Para que funcione tienes que crear una clave secreta, para ello crea un archivo llamado en app/secret.py con: SECRET_KEY = '' y entre comillas pegas el resultado de ejecutar python generador_django.py
4. Instale las dependencias del proyecto utilizando el comando `pip install -r requirements.txt`.
5. Inicie el servidor Django con el comando `python manage.py runserver`.
6. Ejecuta `python manage.py migrate` para completar la configuración de la base de datos.

## Uso

Para iniciar el scraping web, navegue a la URL `http://localhost:8000/`.

## Contribuir

Las contribuciones son bienvenidas. Por favor, haga un "Fork" del proyecto y proponga cambios a través de un "Pull Request".
