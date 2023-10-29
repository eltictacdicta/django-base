# Proyecto inicial de Django

Aquí tienes un esqueleto de Django con algunas modificaciones y cosillas útiles, como un gitignore ya configurado para Django y un sistema para generar claves secretas. Así puedes publicar tu proyecto sin preocuparte por la seguridad. 
Hice este proyecto para usarlo como base y ahorrar tiempo en futuros proyectos.

## ¿Cómo poner todo en marcha?


1. Asegúrate de tener Python. Si tienes Windows, puedes seguir esta guía: [https://misterdigital.es/instalando-python-3-en-windows/](https://misterdigital.es/instalando-python-3-en-windows/)
2. Clona este repositorio en tu ordenador.
3. Una vez en la carpeta del proyecto desde la terminal, crea el entorno virtual con `python -m venv ./venv`
4. Para que todo funcione, necesitas crear una clave secreta. Para ello, crea un archivo en app/secret.py con: SECRET_KEY = '' y entre comillas pega el resultado de ejecutar python generador_django.py
5. Instala las dependencias del proyecto con `pip install -r requirements.txt`.
6. Ejecuta `python manage.py migrate` para terminar de configurar la base de datos.

## ¿Cómo lo uso?


Arranca el entorno virtual con `.\venv\Scripts\activate`
Inicia el servidor Django con `python manage.py runserver`.
Para iniciar el scraping web, ve a la URL `http://localhost:8000/`.

## ¿Quieres contribuir?

¡Genial! Las contribuciones son bienvenidas. Haz un "Fork" del proyecto y propón tus cambios a través de un "Pull Request".
