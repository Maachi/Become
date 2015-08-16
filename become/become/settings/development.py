from defaults import *

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'become',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

AWS_S3_SECURE_URLS = False
AWS_STORAGE_BUCKET_NAME = 'prowlist-dev'
SITE_URL = 'http://localhost:8000'
FROM_EMAIL = 'sebastian@maachi.com'