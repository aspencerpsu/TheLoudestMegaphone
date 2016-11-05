"""
Django settings for NewYorkFatalities project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os, psycopg2, sys, gettext, locale

sys.dont_write_bytecode

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_%v%9+_&lda3c4=qh(c0dnl5*0i!9#rs!bs6h*)9#tp%te*dw9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#Tweepy Account Settings

Twitter_Consumer_Key = 	'Axt0mv2kupxboLs30wSlWy73s'
Twitter_Consumer_Secret = '	JCBmN0ykBiHr7XFSVFJI1JGrfwtXlWnGNFA56tXIdx1aXXxAET'
Twitter_Access_Token = '781216035936538625-tsdTVa15PPxts0bWcJaABAm43HewBCg'
Twitter_Access_Secret = '9kkCjBXXhROi1gXvxWxZgHlhn1iMPFg0DZI7Jj2ZApq76'
Owner_ID = 781216035936538625
Owner = 'theloudestmega1'



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #All Third Party Applications
     'tweepy',
     'NewYorkFatalities',
     'tweets'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NewYorkFatalities.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
	    'debug': False,
        },
    },
]

WSGI_APPLICATION = 'NewYorkFatalities.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'loudestmegaphone',
	'USER': 'loudestone',
	'PASSWORD': 'changetheworld',
	'HOST': 'localhost',
	'POST': '',
	'BROKER_URL': 'django://'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_DIRS = [ os.path.abspath(BASE_DIR)+"NewYorkFatalities/static/", ]


MEDIA_URL="/media/"

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")
