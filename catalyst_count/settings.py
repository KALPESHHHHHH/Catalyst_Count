"""
Django settings for catalyst_count project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os 
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n=d0*s$bnjz@nn*213)k&f7^i35w!cqhc2!a36d9kaq@qz2=7x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


CORS_ALLOW_ALL_ORIGINS = True  # or specify allowed origins



# settings.py
CSRF_COOKIE_SECURE = False  # Set to True if using HTTPS
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = 'Lax'  # or 'Strict', depending on your needs





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
     'corsheaders',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'company',  
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',  
    'django_celery_results', 
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add the following line:
    'allauth.account.middleware.AccountMiddleware',
]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Ensure this line is present
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

WSGI_APPLICATION = 'catalyst_count.wsgi.application'



import os
import environ

# Initialize environment variables
env = environ.Env()

# Read the environment variables from the .env file (if present)
environ.Env.read_env(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Check if you're running in Docker
IS_DOCKER = env.bool('RUNNING_IN_DOCKER', default=False)

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB', default='catalyst_count_db'),
        'USER': env('POSTGRES_USER', default='catalyst_user'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='catalyst_pass'),
        'HOST': 'db' if IS_DOCKER else 'localhost',
        'PORT': env('POSTGRES_PORT', default='5432'),
    }
}

# Authentication
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
import os

# Assuming BASE_DIR is already defined above this code
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'

# Directory where static files will be collected
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Directories where Django will also look for static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Celery settings for background processing
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'django-db'


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SITE_ID = 1


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kiljekalpesh1999@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'kuey pasb iglq ripf'  # Your app password
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1 


# Allauth configuration
LOGIN_REDIRECT_URL = 'home' 
LOGOUT_REDIRECT_URL = 'logout_page' 
ACCOUNT_LOGOUT_ON_GET = True  
# Email verification and requirements
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Change to 'mandatory' if you want email verification
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True  # Redirect authenticated users

# Additional settings
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ROOT_URLCONF = 'catalyst_count.urls'  # URL configuration for the project

# settings.py

# Allow large file uploads
DATA_UPLOAD_MAX_MEMORY_SIZE = 1048576000 
FILE_UPLOAD_MAX_MEMORY_SIZE = 1048576000  

# File upload handlers
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
   
]
# settings.py

# Celery Configuration Options
CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'
CELERY_RESULT_BACKEND = 'django-db'  # You can also use 'rpc://' or other backends if needed.
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'  # Adjust to your preferred timezone

# settings.py

INSTALLED_APPS += ['django_q',]
# settings.py

Q_CLUSTER = {
    'name': 'DjangoQ',
    'workers': 4,  
    'recycle': 500,  
    'timeout': 60, 
    'retry': 120, 
    'bulk': 10, 
    'orm': 'default', 
}
