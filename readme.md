# Sistema de Gestión Empresarial

## Descripción del proyecto

Aplicación cliente para sistemas de Rocola. Permite explorar música y gestionar listas de reproducción, interactuando directamente con el backend de la Rocola. 

Las tecnologías y herramientas ocupadas son las siguientes:
- Python
- Django
- PostgreSQL
- Bootstrap

## Instalación 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Pre-requisitos 📋

Que cosas necesitas para instalar el software.

```
Visual Studio Code, Node, Git, Github
```

### Instalación 🔧
Realizar un fork o clon del proyecto.
Importar proyecto al IDE de preferencia para ejecutar.
Para ejecutar en consola realizar el build (empaquetado) de la aplicación.

```bash
git clone https://github.com/VictorPenafiel/Django_Rocola.git
cd proyecto
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

## Construido con 🛠️

* [Python](https://www.python.org/django)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Git](https://git-scm.com/)
* [GitHub](https://github.com/)

## Contribuye 🖇️

```bash
# Fork → Crea rama → Cambios → Commit → Pull Request
```

## Autores ✒️

https://github.com/victorpenafiel

## Licencia 📄

Ningún Derecho Reservado.  [Creative Commons Atribución/Reconocimiento 4.0 ](https://creativecommons.org/licenses/by/4.0/deed.es).

Este proyecto está bajo la Licencia - mira el archivo [LICENSE.md](LICENSE.md) para detalles