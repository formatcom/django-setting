"""
Django settings for pruebas project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY       = 'CODEHERE' #CHANGES TO THE ORIGINAL CODE.
ROOT_URLCONF     = 'PROJECTNAME.urls' #PLACE PROJECT NAME.
WSGI_APPLICATION = 'PROJECTNAME.wsgi.application' #PLACE PROJECT NAME.


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = ()

LOCAL_APPS = (
    'django_extensions',
)

BASE_APPS = ()

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + BASE_APPS

if DEBUG:
    INSTALLED_APPS  += LOCAL_APPS

########## END APP CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES_DJANGO = (
    # Default Django milddleware:
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

MIDDLEWARE_CLASSES_THIRD_PARTY = ()

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES_DJANGO + MIDDLEWARE_CLASSES_THIRD_PARTY
########## END MIDDLEWARE CONFIGURATION

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL  = '/static/'
MEDIA_URL   = '/media/'

MEDIA_ROOT  = 'media/'   
STATIC_ROOT = 'static/'

TEMPLATE_DIRS = (
    'templates/',
)

if DEBUG:
    STATIC_ROOT = 'static/'
    MEDIA_ROOT  = 'media/'
    TEMPLATE_DIRS = (
        'templates/',
    )

########## END GENERAL CONFIGURATION
