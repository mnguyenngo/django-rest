# Installation

## Procedure

### Prerequisites

This code was tested with Python 3.6.3

### Create a Virtual Environment

```bash
virtualenv env
```

#### Activating the virtual environment

```bash
source env/bin/activate
```

#### Deactivating the virtual environment

```bash
deactivate
```

### Install Django and Django-Rest-Framework

```bash
pip install Django
pip install djangorestframework
```

#### Record package installation in `requirements.txt` file

```bash
pip freeze -l > requirements.txt
```

If you open the requirements.txt file, you will see the following:

```bash
Django==2.1.2
djangorestframework==3.8.2
pytz==2018.5
```

### Project Setup

```bash
django-admin.py startproject my-api .
```

```bash
cd my-api
django-admin.py startapp my-app
```

### File Structure

By running the following command, you can check the file structure of your project:

```bash
tree -I env
```

This will ignore the directory for the virtual environment.

Expected output:

```bash
django-rest
├── LICENSE
├── README.md
├── my-api
│   ├── my-api
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── settings.cpython-36.pyc
│   │   │   └── urls.cpython-36.pyc
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── my-app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── manage.py
├── docs
│   ├── README.md
│   └── installation.md
├── env
└── requirements.txt
```

### Start up the database

```bash
python manage.py migrate
```

### Create a superuser

```bash
python manage.py createsuperuser --email admin@example.com --username admin
```

__This will prompt you to enter the password for the superuser.__

### Add 'rest_framework' and 'my-app' to 'INSTALLED_APPS' in my-api/settings.py

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'my-app'
]
```

### Add urls for the app

Import `include` from `django.urls` and add the paths for my-app to `urlpatterns`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my-app.urls'))
]
```

## References

1. [Let’s build an API with Django REST Framework — Part 1](https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5)
2. [Let’s build an API with Django REST Framework — Part 2](https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-part-2-cfb87e2c8a6c)