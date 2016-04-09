"""
Django settings for eduraam project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mv%_^@v)e70q$4g&3@+q&q!roa(swq*ys5@*bo)#(d%25q17$e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'compressor',
    'corsheaders',
    'kb.events',
    'kb.apps',
    'kb.inbox',
    'kb.collections',
    'kb.groups',
    'kb.lvs',
    'kb.settings',
    'kb.permissions',
    'kb.badges',
    'kb.questions',
    'kb.skills.apps.SkillsConfig',
    'kb.releases',
    'kb',
    'launch',
    'accounts',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.openid',
    'connectors.apps.ConnectorsConfig',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'kb.middleware.ContextTokenProcessingMiddleware',
    'subdomains.middleware.SubdomainURLRoutingMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

CONNECTORS = {
    'codeorg': 'connectors.codeorg.Connector',
    'scratch': 'connectors.scratch.Connector'
}

SCRATCH_SIGNUP_EMAIL = "butler.melvin+scratch@perceptum.nl"
SCRATCH_SIGNUP_COUNTRY = "Netherlands"

ROOT_URLCONF = 'eduraam.urls'

SUBDOMAIN_URLCONFS = {
    None: ROOT_URLCONF,
    "accounts": "accounts.urls",
    "api": "kb.urls",
    "launch": "launch.urls"
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

import logging
LOG_LEVEL = os.getenv('GENERAL_LOG_LEVEL', 20 if DEBUG else 30)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'coded': {
            'format': '{%(name)s:[%(code)s]} %(message)s',
        },
        'basic': {
            'format': '{%(name)s} %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': int(os.getenv('H_CONSOLE_LOG_LEVEL', LOG_LEVEL)),
            'formatter': 'basic',
        },
        'coded-console': {
            'class': 'logging.StreamHandler',
            'level': int(os.getenv('H_CONSOLE_LOG_LEVEL', LOG_LEVEL)),
            'formatter': 'coded',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': int(os.getenv('DJANGO_LOG_LEVEL', LOG_LEVEL)),
        },
        'connectors': {
            'handlers': ['coded-console'],
            'level': int(os.getenv('CONNECTORS_LOG_LEVEL', LOG_LEVEL)),
        },
        'kb.events': {
            'handlers': ['coded-console'],
            'level': int(os.getenv('EVENT_LOG_LEVEL', LOG_LEVEL)),
        }
    }
}

"""
LOG_CODES Tables
================

The log codes table contains a mapping from shorthand log codes to
verbose descriptions. The log code itself is constructed as follows:

    <Log level (1 digit)><Log code (2 digits)>

Log categories
--------------
The log categories are inspired by both HTTP status codes and the python logger
module, for more information see: https://docs.python.org/3.5/howto/logging.html

    1xx :   log level DEBUG
    2xx :   log level INFO
    3xx :   log level WARNING
    4xx :   log level ERROR
    5xx :   log level CRITICAL

Example
-------
    501 would mean a critical error (01)
"""
LOG_CODES = {
    100: "Routed %(url)s to %(routed_url)s",
    101: "Network package debug",

    110: "Login parameters %(params)s",
    111: "Signup successful for %(user)s",
    112: "Login sucessfull with %(token)s",
    113: "Login failed with %(token)s",
    114: "Already logged in with %(token)s",

    201: "Signals registered",

    302: "Token doesn't match current user",

    410: "Unexpected login failure with %(token)s",
    411: "Signup failed for %(user)s",
    412: "Could not set language to %(lang)s for %(user)s",
    420: "Could not create event",

    501: "Something unexpected happened: %(error)s",
    502: "Unknown debug log code: %(code)s",
    503: "Error constructing log message: %(error)s",

    509: "Cannot unpack token",

    510: "Cannot extract %(field)s from HTML document",
    511: "Unknown login parameter %(param)s:%(value)s",
    512: "Login called with invalid credentials object",
}
SHOW_LOG_CODE_DESCRIPTION = os.getenv('SHOW_LOG_CODE_DESCRIPTION', True)

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.auth_backends.ExtendedAuthenticationBackend',
]
ACCOUNT_ADAPTER = "accounts.adapter.EduraamAccountAdapter"
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[Codecult] "

DEFAULT_FROM_EMAIL = "info@codecult.nl"

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
]

APPSTATIC = None

WSGI_APPLICATION = 'eduraam.wsgi.application'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication'
    ]
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'nl-NL'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True
