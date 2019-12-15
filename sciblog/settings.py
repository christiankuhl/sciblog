"""
Django settings for sciblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os
from sciblog.private import SECRETKEY, DEBUG_FLAG

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETKEY

# Set DEBUG = False in production. Set DEBUG = True in localhost development
# This flag is set in an external file private.py
DEBUG = DEBUG_FLAG

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','www.musicofreason.de','musicofreason.de']

DESCR_LONG = 'Music of Reason - A blog about math, finance and the universe'

# Application definition
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
    'disqus', # for comments
    'ckeditor', # for managing text,images and formulas
    'ckeditor_uploader',
)
SITE_ID = 3

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

#list of IPs able to see the toolbar
INTERNAL_IPS=('127.0.0.1','localhost',)

ROOT_URLCONF = 'sciblog.urls'

WSGI_APPLICATION = 'sciblog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'img')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/img/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'blog','static'),
)

TEMPLATE_LOADERS = ['django_mobile.loader.Loader']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'blog',)],
        'APP_DIRS': False,
        'OPTIONS': {'loaders': ['django_mobile.loader.Loader',
                                'django.template.loaders.app_directories.Loader'],
                    'context_processors': ["django.contrib.auth.context_processors.auth",
                                            "django_mobile.context_processors.flavour"]
                    }
    },
]

# Disqus configuration (for managing comments)
# To install disqus http://django-disqus.readthedocs.org/en/latest/index.html
DISQUS_API_KEY = 'ELxieP8XDmv4l7A14ptjFiTgMkOTcnIpDMj6BBJpbetwwBcMIMgFQQ2JvjFemIHT'
DISQUS_WEBSITE_SHORTNAME = 'musicofreason'

# Http protocol with (https://) or without SSL (http://)
# NOTE: You need to have a SSL certificate installed before setting this flag to True
HTTPS = True

# Social Networks
FACEBOOK_ID = '1452207144803935' #for Facebook tracking
FACEBOOK_URL = ''
TWITTER_URL = 'https://twitter.com/musicofreason'
TWITTER_HANDLE = 'musicofreason'
LINKEDIN_URL = ''
GOOGLE_PLUS_URL = ''
PINTEREST_URL = ''
INSTAGRAM_URL = ''
RSS_URL = ''

# Google Analytics
GA_TRACKING_ID = ''

# Ckeditor
CKEDITOR_UPLOAD_PATH = "upload/"
CKEDITOR_IMAGE_BACKEND = "pillow"