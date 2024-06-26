from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['cloudymotion.com', '127.0.0.1', 'localhost', 'www.cloudymotion.com']
CURRENT_DOMAIN = 'https://cloudymotion.com/' if DEBUG is False else 'http://localhost:8000/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cm_site.apps.CmSiteConfig',
    # Надстройка для allauth
    'django.contrib.sites',
    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #API
    'rest_framework',
    'api',
    'corsheaders'
]

# django-allouth

# email обязателен
ACCOUNT_EMAIL_REQUIRED = True

# Дней на подтверждения email
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7

# Максимальная длина имени
ACCOUNT_USERNAME_MAX_LENGTH = 25

# Уникальный email
ACCOUNT_UNIQUE_EMAIL = True

# хз
ACCOUNT_EMAIL_VERIFICATION_METHOD = 'email'

# Задний привод allauth регестрации
AUTHENTICATION_BACKENDS = {
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    # 'social_core.backends.vk.VKOAuth2',
}

# Переменная 'django.contrib.sites'
SITE_ID = 1

# время хранения сессии (сейчас == 30 лет) ((60 * 60 * 24 * 30 * 12) *30)
SESSION_COOKIE_AGE = 31104000 * 30

# Дополнение к стандартной таблице User
AUTH_USER_MODEL = 'cm_site.CustomUser'  

# Перенаправление после входа
LOGIN_REDIRECT_URL = '/store/'

# Перенаправление после выхода
ACCOUNT_LOGOUT_REDIRECT_URL = '/store/'

# Перенаправление после подтверждения email
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/store/'

# подтверждение по email обязательно
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Метод подтверждения email
ACCOUNT_AUTHENTICATION_METHOD  = 'username_email'

# Настройки отправки писем
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Отправкой через Gmail SMTP сервер
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST_USER = 'inco.k.b.blizz@gmail.com' if DEBUG else 'cloudymotion4life@gmail.com'
EMAIL_HOST_PASSWORD = 'ltzw ivpx tqib lxnl' if DEBUG else 'lgkv yskm kkik lsup'

ROOT_URLCONF = 'www.urls'
#end django-allouth

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # middleware allauth
    'allauth.account.middleware.AccountMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

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

WSGI_APPLICATION = 'www.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True

# -------------------------------- FOR REG.RU --------------------------------#
STATIC_URL = '/static/'

STATIC_ROOT = '../static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = 'media/' if DEBUG is False else BASE_DIR / '../media/'
# -------------------------------- FOR REG.RU --------------------------------#

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

STRIPE_PUBLIC_KEY = os.getenv("STRIPE_TEST_PUBLIC_KEY") if DEBUG else os.getenv("STRIPE_PUBLIC_KEY")
STRIPE_SECRET_KEY = os.getenv("STRIPE_TEST_SECRET_KEY") if DEBUG else os.getenv("STRIPE_SECRET_KEY")

CORS_ORIGIN_WHITELIST = [
    'http://cloudymotion.com',
    'https://cloudymotion.com',
    'http://www.cloudymotion.com',
    'https://www.cloudymotion.com',
] if DEBUG is False else [
    'http://localhost:8000',
    'http://127.0.0.1:8000'
]

REPLACE_PATTERN_CONTRACTS = {
    'wav':{
        'date': { 'old': '{%DATE%}', 'new': ''},
        'date_full': {'old': '{%DATEFULL%}', 'new': ''},
        'track_name': {'old': '{%TRACKNAME%}', 'new': ''},
        'lic': {'old': '{%LIC%}', 'new': ''}
    },
    'unlimited':{
        'date': {'old': '{%DATE%}', 'new': ''},
        'date_full': {'old': '{%DATEFULL%}', 'new': ''},
        'track_name': {'old': '{%TRACKNAME%}', 'new': ''},
        'lic': {'old': '{%LIC%}', 'new': ''}
    },
    'exclusive':{
        'date': {'old': '{%DATE%}', 'new': ''},
        'customer_alias': {'old': '{%CUSTOMER_ALIAS%}', 'new': ''},
        'track_name': {'old': '{%TRACKNAME%}', 'new': ''},
        'customer_name': {'old': '{%CUSTOMER_NAME%}', 'new': ''}
    },
}