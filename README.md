# SIA
'remake' del repositorio https://github.com/Ballena0/SIA-Botilleria con postgres, juegos de azar y mujerzuelas. Requiere Python 3 y una versión compatible de PIP.
## Pasos para levantar la aplicación
* Situarse en la carpeta `SIA`
* Crear un entorno virtual de Python (recomiendo virtualenv)
* En la línea de comandos, ejecutar `pip install -r requirements.txt`
* Ejecutar seguidamente: `python manage.py makemigrations`, `python manage.py migrate` y `python manage.py createsuperuser` (crear un superusuario)
* Finalmente `python manage.py runserver` y la aplicación estará disponible en `http://localhost:8000/`

Nótese que si se tiene instalado Python2 y Python3 simultáneamente (como en sistemas Linux), el comando `python` se reemplaza por `python3` y `pip` por `pip3`.
