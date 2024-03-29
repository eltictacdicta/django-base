# Proyecto inicial de Django

Aquí tienes un esqueleto de Django con algunas modificaciones y cosillas útiles, como:

- .gitignore ya configurado para Django
- Sistema para generar claves secretas que permite publicar tu proyecto en Github sin preocuparte por la seguridad
- Plantilla base con Bootstrap 5
- Configurado el directorio de archivos estáticos de Django

Hice este proyecto para usarlo como base y ahorrar tiempo en futuros proyectos.

## ¿Cómo poner todo en marcha?


1. Asegúrate de tener Python. Si tienes Windows, puedes seguir esta guía: [https://misterdigital.es/instalando-python-3-en-windows/](https://misterdigital.es/instalando-python-3-en-windows/)
2. Clona este repositorio en tu ordenador.
3. Una vez en la carpeta del proyecto desde la terminal, crea el entorno virtual con `python -m venv ./venv`
4. Para que todo funcione, necesitas crear una clave secreta. Para ello ejecutar python generador_django.py esto te generará un archivo .env con la clave privada
5. Instala las dependencias del proyecto con `pip install -r requirements.txt`.
6. Ejecuta `python manage.py migrate` para terminar de configurar la base de datos.

## ¿Cómo lo uso?


Arranca el entorno virtual con `.\venv\Scripts\activate`.
Inicia el servidor Django con `python manage.py runserver`.
Para iniciar el scraping web, ve a la URL `http://localhost:8000/`.

## ¿Quieres contribuir?

¡Genial! Las contribuciones son bienvenidas. Haz un "Fork" del proyecto y propón tus cambios a través de un "Pull Request".
