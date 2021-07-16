# DJANGO + VUE 
Junior cheat sheet for fullstack

---

## Create project
### 1. Create project dir and README.md

```bash
mkdir empty_project
cd empty_project
% touch README.md
```

### 2. Create git

```bash
% git init
% touch .gitignore
```

---

## Backend (Django + Django Rest Framework)

### 1. Create dir for backend

```bash
% mkdir backend
% cd backend
```

### 2. Make `.gitignore`

```bash
backend % nano .gitignore
```

`backend/.gitignore`

```
__pycache__
.venv
.env
dist
snippets
.vscode
.idea
.DS_Store
.github/.DS_Store
.coverage
coverage.xml
*.pyc
db.sqlite3

```

### 3. Init virtual environment

```bash
backend % poetry init
backend % tree -aL 1

.
├── .gitignore
├── .venv
├── poetry.lock
└── pyproject.toml
```

*if there no `backend/.venv`:*

```bash
backend % virtualenv .venv
backend % poetry env use .venv/bin/python
```
check env setup
```bash
backend % poetry env list --full-path

<..>/empty_project/backend/.venv (Activated)
```

### 4. Create Makefile

```
backend % nano Makefile
```

`backend/Makefile`

```
install:
	poetry install

run:
	poetry run python backend/manage.py runserver

gunicorn-run:
	source .venv/bin/activate ; \
	cd backend ; \
	gunicorn backend.wsgi ; \

django-shell:
	cd backend ; \
	poetry run python manage.py shell ; \

migrations:
	poetry run python backend/manage.py makemigrations

migrate:
	poetry run python backend/manage.py migrate

lint:
	poetry run flake8 backend

```

### 5. Add packages

```bash
backend % poetry add django@2.2.10
backend % poetry add djangorestframework
backend % poetry add environs
backend % poetry add flake8 --dev
backend % poetry add gunicorn --dev

backend % poetry show

django              2.2.10 A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
djangorestframework 3.12.4 Web APIs for Django, made easy.
environs            9.3.2  simplified environment variable parsing
flake8              3.9.2  the modular source code checker: pep8 pyflakes and co
gunicorn            20.1.0 WSGI HTTP Server for UNIX
marshmallow         3.12.2 A lightweight library for converting complex datatypes to and from native Python datatypes.
mccabe              0.6.1  McCabe checker, plugin for flake8
pycodestyle         2.7.0  Python style guide checker
pyflakes            2.3.1  passive checker of Python programs
python-dotenv       0.18.0 Read key-value pairs from a .env file and set them as environment variables
pytz                2021.1 World timezone definitions, modern and historical
sqlparse            0.4.1  A non-validating SQL parser.
```

### 6. Start Django project

```bash
backend % poetry run django-admin startproject backend
backend % tree -aL 1

.
├── .gitignore
├── .venv
│   └── <..>
├── Makefile
├── backend
│   ├── backend
│   └── manage.py
├── poetry.lock
└── pyproject.toml
```

### 7. Setup WSGI

```bash
backend % source .venv/bin/activate
backend % export DJANGO_SETTINGS_MODULE=backend.settings
backend % deactivate
```

Try to run with *Django [?]*

```bash
backend % make run
```

Try to run with Gunicorn

```bash
backend % make gunicorn-run
```

### 8. Setup secrets keys

Create .env

```python
backend % touch .env
```

`backend/.env` 

```
SECRET_KEY='strong key'
```

*Also I created file .env_example if you clone this repo rename .env_exmple to .env. You don't need to create it.*

Update key in settings

`backend/backend/settings.py`

```python
<...>
from environs import Env

# Setup environment
env = Env()
env.read_env(override=True)

<...>
SECRET_KEY = env.str('SECRET_KEY')
<...>
```

### 9. Setup database *sqlite*

```bash
backend % make migrations
backend % make migrate
```

### 10. Create superuser.
*We don't need superuser here. You can pass this step* 

```bash
backend % poetry run python backend/manage.py createsuperuser
```

### 11. Add apps to project

This app will return Vue app
```bash
backend % cd backend

backend/backend % poetry run django-admin startapp vue_app
backend/backend % touch vue_app/urls.py
backend/backend % mkdir vue_app/templates
backend/backend % mkdir vue_app/static
backend/backend % cd ..
```

This app will work as API
```bash
backend % cd backend

backend/backend % poetry run django-admin startapp api
backend/backend % touch api/urls.py
backend/backend % cd ..
```

### 12. Check structure

```bash
backend % tree -aL 2

.
├── .env
├── .env_example
├── .gitignore
├── .venv
│   └── <..>
├── Makefile
├── backend
│   ├── api
│   ├── backend
│   ├── db.sqlite3
│   ├── manage.py
│   └── vue_app
├── poetry.lock
└── pyproject.toml
```

```bash
backend % tree backend        
backend
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── backend
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── vue_app
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── static
    ├── templates
    ├── tests.py
    ├── urls.py
    └── views.py
```

### 13. Add apps *api*, *vue_app* and *Django REST* to settings

`backend/backend/settings.py`

```python
<...>
# Application definition
INSTALLED_APPS = [
     <...>,
    'rest_framework',
    'api',
    'vue_app',
]
<...>

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
<...>
```

### 14. Total structure

```python
backend % tree -aL 3

.
├── .env
├── .env_example
├── .gitignore
├── .venv
│   └── <..>
├── Makefile
├── backend
│   ├── api
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── backend
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── manage.py
│   └── vue_app
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations
│       ├── models.py
│       ├── static
│       ├── templates
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── poetry.lock
└── pyproject.toml
```

### 15. Add some features to backend

`backend/backend/urls.py`

```python
<...>
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vue/', include('vue_app.urls')),
    path('api/', include('api.urls')),
]
```

`backend/vue_app/urls.py`

```python
from django.urls import path

from .views import MainView


urlpatterns = [
    path('', MainView.as_view())
]
```

`backend/vue_app/views.py`

```python
from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
```

`backend/api/urls.py`
```python
from django.urls import path

from .views import RandomView


urlpatterns = [
    path('random', RandomView.as_view())
]
```

`backend/api/views.py`

```python
import random

from rest_framework.views import APIView
from rest_framework.response import Response


class RandomView(APIView):
    def get(self, request, *args, **kwargs):
        """This is test function. Returns random sequence. Max length - 10."""

        count = int(request.GET.get('count', 10))
        count = 10 if count > 10 else count
        random_range = {i: random.randint(0, 100) for i in range(1, count + 1)}
        return Response(random_range)
```

### 18. Add demo page.
*After setup frontend we will overwrite it.*

`backend/vue_app/templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello, World!</title>
</head>
<body>
    Hello, World!
</body>
</html>
```

### 19. Check out

```bash
backend % make run
```

* check address [http://127.0.0.1:8000/vue/](http://127.0.0.1:8000/vue/). There you must see page with title and text
```
Hello, World!
```
* cehck address [http://127.0.0.1:8000/random?count=5](http://127.0.0.1:8000/random?count=5). You must see answer:
```JSON
{
    "1": 46,
    "2": 23,
    "3": 65,
    "4": 22,
    "5": 10
}
```

### 20. Return to main project directory
```bash
backend % cd ..
```

---

## Frontend (Vue 3)

### 1. Start Vue app
```bash
vue create frontend
cd frontend
```

