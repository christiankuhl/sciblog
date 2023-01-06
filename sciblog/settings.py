"""
Django settings for sciblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ.get("SECRET_KEY", "0")
DEBUG = bool(os.environ.get("DEBUG"))

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','www.musicofreason.de','musicofreason.de', 'musicofreason.herokuapp.com']

DESCR_LONG = 'Music of Reason - A blog about math, finance and the universe'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'django_mobile',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.syndication',
    'django.contrib.sitemaps',
    'ckeditor',
    'ckeditor_uploader',
)

SITE_ID = 3

MIDDLEWARE= ('django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    )

INTERNAL_IPS=('127.0.0.1','localhost',)

ROOT_URLCONF = 'sciblog.urls'

WSGI_APPLICATION = 'sciblog.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False

MEDIA_ROOT = os.path.join(BASE_DIR, 'img')
MEDIA_URL = '/img/'

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'blog','static'),
)

TEMPLATE_LOADERS = []

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'blog',)],
        'APP_DIRS': False,
        'OPTIONS': {'loaders': ['django_mobile.loader.Loader',
                                'django.template.loaders.app_directories.Loader'],
                    'context_processors': ["django.contrib.auth.context_processors.auth",
                                            "django_mobile.context_processors.flavour",
                                            "django.contrib.messages.context_processors.messages",]
                    }
    },
]

HTTPS = bool(os.environ.get("HTTPS"))

X_FRAME_OPTIONS = 'SAMEORIGIN'

FACEBOOK_ID = '1452207144803935'
FACEBOOK_URL = ''
TWITTER_URL = 'https://twitter.com/musicofreason'
TWITTER_HANDLE = 'musicofreason'
LINKEDIN_URL = 'https://www.linkedin.com/in/christian-kuhl-01b058120/'

CKEDITOR_UPLOAD_PATH = "upload/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
   'default': {
       'skin': 'moono',
       'toolbar_Custom': [
           {'name': 'math', 'items': ['Mathjax', ]},
       ],
       'extraPlugins': 'mathjax',
   },
}

if not os.environ.get("DEV"):
    import django_heroku
    django_heroku.settings(locals())
