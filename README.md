# Django rest
start a virtual environment

`virtualenv venv`

`virtualenv --python=/usr/local/bin/python3 venv`

`pip install django`

`pip install django-rest-framework`

`pip freeze > requirements.txt`

`django-admin startproject <name>`

`django-admin startapp <name>`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`


```
INSTALLED_APPS = [
    'rest_framework',
    'apps.comments'
]
```
