# Empty fullstack project
Stack: django, django REST framework, vue.js 3, axios

_Junior cheat sheet for fullstack_

---

## Preparing tools
```bash
pip3 install poetry --upgrade --user
pip3 install virtualenv --upgrade --user

npm install vue@next
npm install -g @vue/cli
vue upgrade --next
```


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
	gunicorn backend.wsgi

django-shell:
	cd backend ; \
	poetry run python manage.py shell

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
backend % poetry add django-cors-headers
backend % poetry add environs
backend % poetry add flake8 --dev
backend % poetry add gunicorn --dev

backend % poetry show

django              2.2.10 A high-level Python Web framework that encourages rapid development and clean, pragma...
django-cors-headers 3.7.0  django-cors-headers is a Django application for handling the server headers required ...
djangorestframework 3.12.4 Web APIs for Django, made easy.
environs            9.3.2  simplified environment variable parsing
flake8              3.9.2  the modular source code checker: pep8 pyflakes and co
gunicorn            20.1.0 WSGI HTTP Server for UNIX
marshmallow         3.12.2 A lightweight library for converting complex datatypes to and from native Python data...
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
backend % tree -aL 2

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

### 13. Add apps *CORS*, *Django REST*, *api* and *vue_app* to settings

`backend/backend/settings.py`

```python
<...>
# Application definition
INSTALLED_APPS = [
     <...>,
    'corsheaders',
    'rest_framework',
    'api',
    'vue_app',
]
<...>

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    <...>
]

<...>

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

<...>

# CORS setup
# https://pypi.org/project/django-cors-headers/

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
       'http://localhost:8080',
)


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
% vue create frontend
% cd frontend
```

### 2. Setup Makefile
```bash
frontend % rm README.md # I don't need it
frontend % nano Makefile
```

`frontend/Makefile`
```bash
install:
	npm install

run:
	npm run serve

build:
	rm -rf ../backend/backend/vue_app/static/* ; \
	rm -rf ../backend/backend/vue_app/templates/* ; \
	npm run build ; \
	cp public/static/* ../backend/backend/vue_app/static

lint:
	npm run lint
```

### 3. Add axios
```bash
frontend % npm install axios --save
```

### 4. Setup build settings
```bash
frontend % nano vue.config.js
```

`frontend/vue.config.js`
```js
module.exports = {
    outputDir : '../backend/backend/vue_app',
    assetsDir : 'static',
    indexPath : 'templates/index.html',
}
```

Also we don't need to remove 'dest' directory, so we need add tag ```--no-clean``` for build command in 
`frontend/package.json`
```js
<...>
"build": "vue-cli-service build --no-clean",
<...>
```

### 5. favicon as static file [?]
Remove `public/favicon.ico`
```bash
frontend % rm public/favicon.ico
```

Make ```static``` directory in ```frontend/public```

Place image ```favicon.png``` to ```frontend/public/static```

```frontend/public/static/favicon.png```

<img src="https://s166vla.storage.yandex.net/rdisk/bf6ceacbfc23cf7a60b069a9a7dbd8c09bb34ef44065fd6c87b35828e8b3193b/60f591dd/YuF1AkqY7vFrwwvnnznVKVgQdXaY6aVykGyQom3fPDGcBQwE0k-Fgtb2UfoSCm1Mswwep1zoSAWoW9do6hwUaQ==?uid=0&filename=favicon.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&fsize=1864&hid=9f42e7b85affce806b90be0ce40c6be3&media_type=image&tknv=v2&etag=87fb134c6791e9a90e79ab92b2865377&rtoken=qlGf6AtlWpUG&force_default=no&ycrid=na-b2ef2bb8db8d26a6a30fc65156e4bd84-downloader14e&ts=5c77b18f27140&s=2e5934f223abf117eb9463a2f57111a31a98a633a6bcf2e9424f66bec475cabf&pb=U2FsdGVkX19LehIkB8E9U9F6WEldIKhZ1HaeJmYEsIqYM04fyRiOJ-RaaIKemWSUhtkRYClqHx1DKVfjuN7CrYlSzS_4jF6-Sq-YcXetHwE"/>

Edit src in `public/index.html`
```html
<...>
    <link rel="icon" type="image/png" href="/static/favicon.png">
<...>
```

### 6. Check structure
```bash
frontend % tree -L 3

.
├── Makefile
├── README.md
├── babel.config.js
├── node_modules
│   └── <..>
├── package-lock.json
├── package.json
├── public
│   ├── index.html
│   └── static
│       └── favicon.png
├── src
│   ├── App.vue
│   ├── assets
│   │   └── logo.png
│   ├── components
│   │   └── HelloWorld.vue
│   └── main.js
├── subl
└── vue.config.js
```

### 7. Try to run and build
1. Let's run dev server
```bash
frontend % make run
```
Check out url [http://127.0.0.1:8080](http://127.0.0.1:8080)

2. Let's build for prod and run from Django server
```bash
frontend % make build
frontend % cd ../backend
backend % make run
```
Check out url [http://127.0.0.1:8000/vue](http://127.0.0.1:8000/vue)

Go back to frontend
```bash
backend % cd ../frontend
frontend %
```

### 8. Setup _axios_ for _dev_ and _prod_ api urls
If you run vue app with `make run` your base url will be `http://127.0.0.1:8000`. If you
build vue app with `make build` your base url will be `/`

`frontend/src/main.js`
```js
import { createApp } from 'vue'
import App from './App.vue'
import axios from "axios"

// Setup dev and prod base urls for axios
let dev_mode = process.env.NODE_ENV === 'development'
axios.defaults.baseURL = dev_mode ? 'http://127.0.0.1:8000' : '/'

createApp(App).mount('#app')
```

---
### TBC