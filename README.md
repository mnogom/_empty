# DJANGO + VUE

1. **Create project dir and README.md**

```bash
mkdir empty_project
cd empty_project
% touch README.md
```

2. **Create git**

```bash
% git init
% touch .gitignore
```

3. **Create dir for backend**

```bash
% mkdir backend
% cd backend
```

4. **Make `.gitignore`**

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

5. **Init virtual environment**

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
backend % poetry env list --full-path

<..>/empty_project/backend/.venv (Activated)
```

6. **Create Makefile**

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

7. **Add packages**

```bash
backend % poetry add django@2.2.10
backend % poetry add environs
backend % poetry add flake8 --dev
backend % poetry add gunicorn --dev

backend % poetry show

django        2.2.10 A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
environs      9.3.2  simplified environment variable parsing
flake8        3.9.2  the modular source code checker: pep8 pyflakes and co
gunicorn      20.1.0 WSGI HTTP Server for UNIX
marshmallow   3.12.2 A lightweight library for converting complex datatypes to and from native Python datatypes.
mccabe        0.6.1  McCabe checker, plugin for flake8
pycodestyle   2.7.0  Python style guide checker
pyflakes      2.3.1  passive checker of Python programs
python-dotenv 0.18.0 Read key-value pairs from a .env file and set them as environment variables
pytz          2021.1 World timezone definitions, modern and historical
sqlparse      0.4.1  A non-validating SQL parser.
```

8. **Start Django project**

```bash
backend % poetry run django-admin startproject backend
backend % tree -aL 1

.
├── .gitignore
├── .venv
│   ├── ..
│   ..
│   └── ..
├── Makefile
├── backend
│   ├── backend
│   └── manage.py
├── poetry.lock
└── pyproject.toml
```

9. **Setup WSGI**

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
backend % make gunicorn run
```

10. **Setup secrets keys**

Create .env

```python
backend % touch .env
```

`backend/.env` 

```
SECRET_KEY='strong key'
```

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

11. **Setup database *sqlite***

```bash
backend % make migrations
backend % make migrate
```

12. **Create superuser**

```bash
backend % poetry run python backend/manage.py createsuperuser
```

13. **Add app to project**

```bash
backend % cd backend
backend/backend % poetry run django-admin startapp **main_app**

backend/backend % touch main_app/urls.py
backend/backend % touch main_app/errors.py
backend/backend % touch main_app/selectors.py
backend/backend % touch main_app/services.py
backend/backend % touch main_app/serializers.py
backend/backend % mkdir main_app/templates
backend/backend % mkdir main_app/static

backend/backend % cd ..
```

14. **Check structure**

```bash
backend % tree -aL 2

.
├── .gitignore
├── .venv
│   ├── .gitignore
│   ├── bin
│   ├── lib
│   └── pyvenv.cfg
├── Makefile
├── backend
│   ├── backend
│   ├── db.sqlite3
│   ├── main_app
│   └── manage.py
├── poetry.lock
└── pyproject.toml
```

```bash
backend % tree backend/**main_app**

backend/main_app
├── __init__.py
├── admin.py
├── apps.py
├── errors.py
├── migrations
│   └── __init__.py
├── models.py
├── selectors.py
├── serializers.py
├── services.py
├── static
├── templates
├── tests.py
├── urls.py
└── views.py
```

15. **Add app to settings**

`backend/backend/settings.py`

```python
<...>
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '**main_app**',
]
<...>
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
<...>
```

16. **Total structure**

```python
backend % tree -aL 3

.
├── .gitignore
├── .venv
│   ├── ..
│   └── ..
├── Makefile
├── backend
│   ├── backend
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   ├── main_app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── errors.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── selectors.py
│   │   ├── serializers.py
│   │   ├── services.py
│   │   ├── static
│   │   ├── templates
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
├── poetry.lock
└── pyproject.toml
```

17. **Prepare for frontend**

`backend/backend/urls.py`

```python
<...>
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vue/', include('main_app.urls'))
]
```

`backend/main_app/urls.py`

```python
from django.urls import path

from .views import MainView

urlpatterns = [
    path('', MainView.as_view())
]
```

`backend/main_app/views.py`

```python
from django.shortcuts import render
from django.views import View

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
```

18. Add demo page `backend/main_app/templates/index.html`. After setup frontend we will overwrite it.

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

19. **Check out**

```bash
backend % make run
```

check address [http://127.0.0.1:8000/vue/](http://127.0.0.1:8000/vue/). There you must see page with title and text *"Hello, World!"*


**TBD**