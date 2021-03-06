"""
Django settings for eagletrack_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)

STATIC_PATH = os.path.join(PROJECT_PATH, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uv&%c3o0=ux5b!@kxmql+@l@5uk$ihw%ks+ygvn1-kui2g&obv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

ALLOWED_HOSTS = []

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pt',
    'personnel',
    'rest_framework',
    # 'attendance',
    # 'gear',
    'stronghold',
    'bootstrapform'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'stronghold.middleware.LoginRequiredMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

ROOT_URLCONF = 'eagletrack_project.urls'

WSGI_APPLICATION = 'eagletrack_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eagletrack_demo',
        'USER': 'charles',
        'PASSWORD': 'shorefish',
        'HOST': 'eagletrack.cnkdqqk3dlt2.us-west-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'eagletrack',
#         'USER': 'root',
#        # 'PASSWORD': '',
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#A setting to allow django debug toolbar to work with wsgi interface
DEBUG_TOOLBAR_PATCH_SETTINGS = False

STRONGHOLD_PUBLIC_NAMED_URLS = ('cadet_registration', 'report', 'thanks', 'organize_staff', 'organize_staff_save')

STATIC_ROOT = PROJECT_PATH + '/../static'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
               STATIC_PATH,
               )

REST_FRAMEWORK = {
    'PAGE_SIZE': 5
}