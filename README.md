# Empty fullstack project
Stack: Django, Django REST framework (DRF), Vue.js 3, Axios, Vue Router

_Junior cheat sheet for fullstack_

---
## Look around
1. [Prepare tools](#Prepare-tools)
2. [Create a project](#Create-a-project)
3. [Backend](#Backend)
4. [Roadmap](#Roadmap)
5. [Resources](#Resources)

---
## Prepare tools
```bash
pip3 install poetry --upgrade --user
pip3 install virtualenv --upgrade --user

npm install vue@next
npm install -g @vue/cli
vue upgrade --next
```

---

## Create a project
### 1. Create project directory and README.md

```bash
mkdir empty_project
cd empty_project
% touch README.md
```

### 2. Create git

```bash
% git init
```
* `/.gitignore`
  
  ```gitignore
  .idea
  .DS_Store
  ```

### 3. Create master Makefile
* `/Makefile`
  
  ```Makefile
  make install:
      cd backend ; \
      make install ; \
      mv .env_example .env ; \
      make migrations ; \
      make migrate ; \
      make load-demo-data ; \
      cd ../frontend ; \
      make install
  
  make run:
      cd frontend ; \
      make build ; \
      cd ../backend ; \
      make run
  ```

---

## Backend

### 1. Create dir for backend

```bash
% mkdir backend
% cd backend
```

### 2. Make `.gitignore`

```bash
backend % touch .gitignore
```

* `backend/.gitignore`

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

> *if there is no `backend/.venv`:*
> 
> ```bash
> backend % virtualenv .venv
> backend % poetry env use .venv/bin/python
> ```
> check env setup
> ```bash
> backend % poetry env list --full-path
> 
> <..>/empty_project/backend/.venv (Activated)
> ```

### 4. Create Makefile

```bash
backend % touch Makefile
```

* `backend/Makefile`

    ```makefile
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
    
    load-demo-data:
        poetry run python backend/manage.py loaddata backend/memo_api/fixtures/01_sections.yaml ; \
        poetry run python backend/manage.py loaddata backend/memo_api/fixtures/02_notes.yaml
    ```

### 5. Add packages

```bash
backend % poetry add django@2.2.10
backend % poetry add djangorestframework
backend % poetry add django-cors-headers
backend % poetry add environs
backend % poetry add pyyaml
backend % poetry add flake8 --dev
backend % poetry add gunicorn --dev

backend % poetry show

django              2.2.10 A high-level Python Web framework that encourage...
django-cors-headers 3.7.0  django-cors-headers is a Django application for ...
djangorestframework 3.12.4 Web APIs for Django, made easy.
environs            9.3.2  simplified environment variable parsing
flake8              3.9.2  the modular source code checker: pep8 pyflakes a...
gunicorn            20.1.0 WSGI HTTP Server for UNIX
marshmallow         3.12.2 A lightweight library for converting complex dat...
mccabe              0.6.1  McCabe checker, plugin for flake8
pycodestyle         2.7.0  Python style guide checker
pyflakes            2.3.1  passive checker of Python programs
python-dotenv       0.18.0 Read key-value pairs from a .env file and set th...
pytz                2021.1 World timezone definitions, modern and historical
pyyaml              5.4.1  YAML parser and emitter for Python
sqlparse            0.4.1  A non-validating SQL parser.
```

### 6. Start Django project

```bash
backend % poetry run django-admin startproject backend
backend % tree -aL 2 -I .venv

.
├── .gitignore
├── Makefile
├── backend
│   ├── backend
│   └── manage.py
├── poetry.lock
└── pyproject.toml
```

### 7. Setup WSGI

```bash
backend % source .venv/bin/activate
backend % export DJANGO_SETTINGS_MODULE=backend.settings
backend % deactivate
```

Try to run using *Django [?]*

```bash
backend % make run
```

Try to run using Gunicorn

```bash
backend % make gunicorn-run
```

### 8. Setup secret keys

Create .env

```bash
backend % touch .env
```

* `backend/.env` 

  ```
  SECRET_KEY='strong key'
  ```

*Also I created file `.env_example`. If you clone this repo - rename `.env_example` to `.env`. You don't need to create it.*

Update key in settings

* `backend/backend/settings.py`

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

### 10. Create superuser
*We don't need superuser here. You can skip this step.*

```bash
backend % poetry run python backend/manage.py createsuperuser
```

### 11. Add apps to project

This app will return Vue app.
```bash
backend % cd backend

backend/backend % poetry run django-admin startapp vue_app
backend/backend % touch vue_app/urls.py
backend/backend % mkdir vue_app/templates
backend/backend % mkdir vue_app/static
backend/backend % cd ..
```

This app will work as random API.
```bash
backend % cd backend

backend/backend % poetry run django-admin startapp random_api
backend/backend % touch random_api/urls.py
backend/backend % cd ..
```

### 12. Check structure

```bash
backend % tree -aL 2 -I .venv

.
├── .env
├── .env_example
├── .gitignore
├── Makefile
├── backend
│   ├── backend
│   ├── random_api
│   ├── db.sqlite3
│   ├── manage.py
│   └── vue_app
├── poetry.lock
└── pyproject.toml
```

```bash
backend % tree backend

backend
├── backend
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── random_api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── vue_app
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── static
    ├── templates
    ├── tests.py
    ├── urls.py
    └── views.py
```

### 13. Add apps *CORS*, *Django REST*, *api* and *vue_app* to settings

* `backend/backend/settings.py`

    ```python
    <...>
    # Application definition
    INSTALLED_APPS = [
         <...>,
        'corsheaders',
        'rest_framework',
        'random_api',
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
│   └── <..>
├── Makefile
├── backend
│   ├── backend
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── random_api
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── db.sqlite3
│   ├── manage.py
│   └── vue_app
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations
│       ├── models.py
│       ├── static
│       ├── templates
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── poetry.lock
└── pyproject.toml
```

### 15. Add some features to backend

* `backend/backend/urls.py`
    ```python
    <...>
    from django.urls import path, include
  
  
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/random/', include('random_api.urls')),
        path('', include('vue_app.urls')),
    ]
    ```

* `backend/vue_app/urls.py`
    ```python
    from django.urls import re_path

    from .views import MainView
    
    
    urlpatterns = [
        # path("", MainView.as_view()),
        re_path(r'^.*$', MainView.as_view()),  # TODO: using this url make mistakes
    ]
    ```

* `backend/vue_app/views.py`
    ```python
    from django.shortcuts import render
    from django.views import View
  
  
    class MainView(View):
        def get(self, request, *args, **kwargs):
            return render(request, 'index.html')
    ```

* `backend/random_api/urls.py`
    ```python
    from django.urls import path, re_path
    
    from .views import RandomSequenceView
    
    
    urlpatterns = [
        path('sequence/', RandomSequenceView.as_view()),
    ]
    ```

* `backend/random_api/views.py`
    ```python
    import random

    from rest_framework.views import APIView
    from rest_framework.response import Response
    
    
    class RandomSequenceView(APIView):
        """Random sequence View."""
    
        def get(self, request, *args, **kwargs):
            """This is test function. Returns random sequence. Max length - 10."""
    
            count = int(request.GET.get('count', 10))
            count = 10 if count > 10 else count
            random_range = {i: random.randint(0, 100) for i in range(1, count + 1)}
            return Response(random_range)
    ```

### 18. Add demo page
*After frontend is set up we will overwrite this page.*

* `backend/vue_app/templates/index.html`
  
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

* check address [http://127.0.0.1:8000](http://127.0.0.1:8000/vue/). There you will see page with title and text
```
Hello, World!
```
* check address [http://127.0.0.1:8000/api/random/sequence/?count=5](http://127.0.0.1:8000/api/random/sequence/?count=5). You will see the answer:
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

## Frontend

### 1. Start Vue app
```bash
% vue create frontend
% cd frontend
```

### 2. Setup Makefile
```bash
frontend % rm README.md # I don't need it
frontend % touch Makefile
```

* `frontend/Makefile`
  
    ```Makefile
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

### 3. Add axios and vue-router
```bash
frontend % npm install axios --save
frontend % npm install vue-router@next --save
```

### 4. Set up build settings
```bash
frontend % touch vue.config.js
```
Set up `dest` directory 

* `frontend/vue.config.js`
  
    ```js
    module.exports = {
        outputDir : '../backend/backend/vue_app',
        assetsDir : 'static',
        indexPath : 'templates/index.html',
    }
    ```

We don't need to remove `dest` directory, so we need to add tag ```--no-clean``` to `build` command
* `frontend/package.json`
  
    ```js
    <...>
    "build": "vue-cli-service build --no-clean",
    <...>
    ```

### 5. Favicon as static file [?]
Remove `public/favicon.ico`
```bash
frontend % rm public/favicon.ico
```

Make `static` directory in `frontend/public`.

Place image `favicon.png` to `frontend/public/static`.

* `frontend/public/static/favicon.png`
  
  <img src="https://s166vla.storage.yandex.net/rdisk/bf6ceacbfc23cf7a60b069a9a7dbd8c09bb34ef44065fd6c87b35828e8b3193b/60f591dd/YuF1AkqY7vFrwwvnnznVKVgQdXaY6aVykGyQom3fPDGcBQwE0k-Fgtb2UfoSCm1Mswwep1zoSAWoW9do6hwUaQ==?uid=0&filename=favicon.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&fsize=1864&hid=9f42e7b85affce806b90be0ce40c6be3&media_type=image&tknv=v2&etag=87fb134c6791e9a90e79ab92b2865377&rtoken=qlGf6AtlWpUG&force_default=no&ycrid=na-b2ef2bb8db8d26a6a30fc65156e4bd84-downloader14e&ts=5c77b18f27140&s=2e5934f223abf117eb9463a2f57111a31a98a633a6bcf2e9424f66bec475cabf&pb=U2FsdGVkX19LehIkB8E9U9F6WEldIKhZ1HaeJmYEsIqYM04fyRiOJ-RaaIKemWSUhtkRYClqHx1DKVfjuN7CrYlSzS_4jF6-Sq-YcXetHwE"/>

* Edit `src` in `frontend/public/index.html`
    ```html
    <...>
        <link rel="icon" type="image/png" href="/static/favicon.png">
    <...>
    ```

### 6. Check structure
```bash
frontend % tree -I node_modules

.
├── Makefile
├── README.md
├── babel.config.js
├── package-lock.json
├── package.json
├── public
│   ├── index.html
│   └── static
│       └── favicon.png
├── src
│   ├── App.vue
│   ├── assets
│   │   └── logo.png
│   ├── components
│   │   └── HelloWorld.vue
│   └── main.js
└── vue.config.js
```

### 7. Try to run and build
1. Run dev server
```bash
frontend % make run
```
Check out url [http://127.0.0.1:8080](http://127.0.0.1:8080).

2. Build Vue app for `production` and run it via Django _server [?]_
```bash
frontend % make build
frontend % cd ../backend
backend % make run
```
Check out url [http://127.0.0.1:8000](http://127.0.0.1:8000).

Go back to frontend.
```bash
backend % cd ../frontend
frontend %
```

### 8. Setup _axios_ for `development` and `production` api urls
If you run Vue app with `make run`, your base url will be `http://127.0.0.1:8000`. If you
build Vue app with `make build`, your base url will be `/`.

* `frontend/src/main.js`
  
    ```js
    import { createApp } from 'vue'
    import App from './App.vue'
    import axios from "axios"
  
    // Setup development and production base urls for axios
    let dev_mode = process.env.NODE_ENV === 'development'
    axios.defaults.baseURL = dev_mode ? 'http://127.0.0.1:8000' : '/'
  
    createApp(App).mount('#app')
    ```

### 9. Add functionality
This app will have:
* One main app: `App.vue`
* Three **components**:
    1. `NavigationComponent.vue`
    2. `FooterComponent.vue`
    3. `RandomSequenceComponent.vue`
* Three **views** *(for `vue-router`)*:
    1. `HomeView.vue`
    2. `RandomSequenceView.vue`
    3. `PageNotFoundView.vue`

```plain
App.vue  
  ├─ NavigationComponent.vue
  ├─ router-view (by 'vue-router') 
  │    ├─ HomeView.vue (on path '/')
  │    ├─ RandomSequenceView.vue (on path '/rasq/')
  │    │    └─ RandomSequenceComponent.vue
  │    └─ PageNotFoundView.vue (on any other path)
  └─ FooterComponent.vue
```

**Start with `components`.**
* `frontend/src/components/FooterComponent.vue`
    ```js
    <template>
        <div id="footer-component">
          <span>Created  with</span>
          <img alt="Vue logo" src="../assets/logo.png" height="20">
        </div>
    </template>
  
    <script>
    export default { name: "FooterComponent", }
    </script>
  
    <style scoped>
      #footer-component {
        position: absolute;
        bottom: 1rem;
        right: 1rem;
        font-size: small;
      }
    </style>
    ```

* `frontend/src/components/NavigationComponent.vue`
    ```js
    <template>
      <div id="navigation-component">
        <router-link to="/">home</router-link>
        <router-link to="/rasq/">rasq</router-link>
        <router-link to="/new/not/developed/feature">nefe</router-link>
      </div>
    </template>
  
    <script>
    export default { name: "NavigationComponent", }
    </script>
  
    <style scoped>
      #navigation-component { margin: 1rem 0; }
      a { padding: 0 1rem; }
    </style>
    ```

* `frontend/src/components/RandomSequenceComponent.vue`
    ```js
    <template>
      <div id="random-sequence-component">
        <div>
          {{ msg }} with
          <input v-on:input="edit_count_of_elements($event)" value="10" type="number"/>
          numbers
        </div>
        <li v-for="(value, key) in elements" v-bind:key="key">
          {{ value }}
        </li>
      </div>
    </template>
  
    <script>
  
    import axios from 'axios'
  
    export default {
  
      name: 'RandomSequenceComponent',
  
      props: {
        msg: String
      },
  
      data: () => ({
        elements_count: 10,
        elements: [],
      }),
  
      mounted() {
        this.get_random_sequence()
      },
  
      methods: {
        edit_count_of_elements: function (event) {
          let event_value = Number(event.target.value)
  
          if (event_value > 10) {
            event.target.value = 10
            event_value = 10
          } else if (event_value < 0) {
            event.target.value = 0
            event_value = 0
          }
  
          if (event_value !== this.elements_count) {
            this.elements_count = event_value
            this.get_random_sequence()
          }
        },
  
        get_random_sequence: function () {
          axios({
                method: 'get',
                url: "api/random/sequence/",
                params: {
                  count: this.elements_count
                }
              }).then(response => {
                this.elements = response.data
              })
        }
      }
    }
    </script>
  
    <style scoped>
  
      input {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
  
        font-size: medium;
        border: none;
        width: 2em;
      }
  
      input:focus { outline: none; }
  
      input::-webkit-outer-spin-button,
      input::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
      }
  
      li {
        display: inline-block;
        padding: 0.5em;
        margin: 10px 10px;
      }
  
      li:hover {
        background-color: #2c3e50;
        color: white;
      }
  
    </style>
  
    ```

**Then `views`.**
* `frontend/src/views/HomeView.vue`
    ```js
    <template>
      <div id="home-view">
        <span>Home page</span>
      </div>
    </template>
  
    <script>
    export default { name: "HomeView.vue", }
    </script>
    ```

* `frontend/src/views/PageNotFoundView.vue`
    ```js
    <template>
      <div id="not-found-view">
        <span>404 | Page not found</span>
      </div>
    </template>
  
    <script>
    export default { name: "NotFoundView", }
    </script>
  
    <style scoped>
      span { font-size: x-large; }
    </style>
    ```

* `frontend/src/views/RandomSequenceView.vue`
    ```js
    <template>
      <div id="random-sequence-view">
        <RandomSequenceComponent msg="Generate random sequence"/>
      </div>
    </template>
  
    <script>
    import RandomSequenceComponent from '@/components/RandomSequenceComponent.vue'
  
    export default {
      name: 'RandomSequenceView',
      components: { RandomSequenceComponent, }
    }
    </script>
    ```

**Now `App.vue`.**
* `frontend/src/App.vue`
  
    ```js
    <template>
      <div id="home-app">
        <NavigationComponent/>
        <router-view/>
        <FooterComponent/>
      </div>
    </template>
  
    <script>
    import NavigationComponent from "./components/NavigationComponent.vue"
    import FooterComponent from "./components/FooterComponent.vue"
  
    export default {
      name: "App.vue",
      components: {
        NavigationComponent,
        FooterComponent,
      }
    }
    </script>
  
    <style scoped>
      #home-app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
      }
    </style>
    ```

Don't try to run...

### 9. Setup router
* `frontend/src/router/index.js`
    ```js
    import { createWebHistory, createRouter } from 'vue-router'
  
    const routes = [
        {
            path: '/',
            name: 'Home',
            component: () => import("@/views/HomeView.vue"),
        },
        {
            path: '/rasq/',
            name: 'RandomSequenceGenerator',
            component: () => import("@/views/RandomSequenceView.vue"),
        },
        {
            path: '/:catchAll(.*)',
            name: "Page not found",
            component: () => import("@/views/PageNotFoundView.vue"),
        },
    ]
  
    const router = createRouter({
        history: createWebHistory(),
        routes,
    })
  
    export default router
    ```

* `frontend/src/main.js`
    ```js
    import { createApp } from 'vue'
    import axios from "axios"
    import router from './router'
  
    import App from "./App.vue"
  
    // Setup dev and prod base urls for axios
    let dev_mode = process.env.NODE_ENV === 'development'
    axios.defaults.baseURL = dev_mode ? 'http://127.0.0.1:8000' : '/'
  
    // Setup url routing
    createApp(App).use(router).mount('#app')
    ```

### 10. Check structure
```bash
frontend % tree -I node_modules

.
├── Makefile
├── README.md
├── babel.config.js
├── package-lock.json
├── package.json
├── public
│   ├── index.html
│   └── static
│       └── favicon.png
├── src
│   ├── App.vue
│   ├── assets
│   │   └── logo.png
│   ├── components
│   │   ├── FooterComponent.vue
│   │   ├── NavigationComponent.vue
│   │   └── RandomSequenceComponent.vue
│   ├── main.js
│   ├── router
│   │   └── index.js
│   └── views
│       ├── HomeView.vue
│       ├── PageNotFoundView.vue
│       └── RandomSequenceView.vue
└── vue.config.js
```
---
## Roadmap

**Backend**
* [x] [Django](https://www.djangoproject.com)
* [x] [Django ORM](https://docs.djangoproject.com/en/3.2/topics/db/queries/) @ describe
* [x] [Django REST Framework](https://www.django-rest-framework.org)
* [x] [DRF Serializer](https://www.django-rest-framework.org/api-guide/serializers/) @ describe
* [ ] Authentication _*check source_
* [ ] Tests

**Frontend**
* [x] [Vue.js 3](https://v3.vuejs.org)
* [x] [axios](https://axios-http.com)
* [ ] ~~Setup axios for post requests (csrf-token)~~ ¯\\\_(ツ)_/¯
* [x] [Vue Router](https://router.vuejs.org)
* [ ] [Vuex](https://vuex.vuejs.org)
* [ ] Tests

**Dev part**
* [ ] [PostgreSQL](https://www.postgresql.org)
* [ ] CI/CD
* [ ] [Docker](https://www.docker.com)
* [ ] [nginx](https://nginx.org)
* [ ] CI/CD/CD

**Backend 2**
* [ ] Django / Django ORM / DRF -> 
[Fast API](https://fastapi.tiangolo.com) 
/ [SQLAlchemy](https://www.sqlalchemy.org) 
/ [pydantic](https://pydantic-docs.helpmanual.io)

---
## Resources
1. [Poetry](https://python-poetry.org/docs/)
2. [Django start guide](https://www.djangoproject.com/start/)
3. [Django REST Framework quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
4. [Django CORS](https://github.com/adamchainz/django-cors-headers)
5. [Vue.js introduction](https://v3.vuejs.org/guide/introduction.html)
6. [About vue.config.js](https://cli.vuejs.org/config/)
7. ~~[Vue.js routing](https://v3.vuejs.org/guide/routing.html#official-router)~~
8. ~~[Github example Vue.js routing](https://github.com/phanan/vue-3.0-simple-routing-example)~~
9. [Vue Router](https://router.vuejs.org/guide/)

## Unsorted


### New app with models
```bash
backend/backend % poetry run django-admin startapp memo_api
```

### Cookie setup for frontend
```bash
frontend % npm install js-cookie --save
```


1. https://www.django-rest-framework.org/api-guide/authentication/
2. https://www.django-rest-framework.org/api-guide/permissions/
3. https://stackoverflow.com/questions/35970970/django-rest-framework-permission-classes-of-viewset-method
4. https://pythonru.com/uroki/django-rest-api
5. https://auth0.com/blog/building-modern-applications-with-django-and-vuejs/
6. https://vue-loader-v14.vuejs.org/ru/configurations/pre-processors.html
