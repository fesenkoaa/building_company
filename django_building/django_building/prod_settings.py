import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-afxic5t3oabm3wq%%42+ik6%ln_8ecxg6j%8gg_j^ft50-4wg%'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1:8000', '46.101.244.154']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ttc_building',
        'USER': 'fesenkoaa',
        'PASSWORD': '231105',
        'HOST': 'localhost',
        'POST': ''
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')