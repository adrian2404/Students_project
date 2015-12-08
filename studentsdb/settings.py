"""
Django settings for studentsdb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# PORTAL_URL = 'http://localhost:8000'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e_$$pt-t!f+63e)4pvtsr5qb291za3)l4t*iq#9nznh74+h68!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


#MEDIA STUFF
MEDIA_URL = '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR, '..', 'media')

# Application definition

INSTALLED_APPS = (
    'django_pdb',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_extensions',
    'registration',
    'students',
    'studentsdb'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django_pdb.middleware.PdbMiddleware',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

ROOT_URLCONF = 'studentsdb.urls'

WSGI_APPLICATION = 'studentsdb.wsgi.application'

REGISTRATION_OPEN = True
LOGIN_URL = 'users:auth_login'
LOGOUT_URL = 'users:auth_logout'
# LOGIN_REDIRECT_URL = 'home'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'studentsdb', 'templates'),
    )

from .db import DATABASES



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

from django.conf import global_settings

TEMPLATE_CONTEXT_PROCESSORS = \
    global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
    "studentsdb.context_processors.students_proc",
    "students.context_processors.groups_processor",
    'django.contrib.messages.context_processors.messages',
    )

# email settings
 # please, set here you smtp server details and your admin email
ADMIN_EMAIL = 'adrian.yavorski@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'adrian.yavorski@gmail.com'
EMAIL_HOST_PASSWORD = 'adrian_yavorski'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True