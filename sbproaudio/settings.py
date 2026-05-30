from pathlib import Path
import os
from decouple import config
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sbproaudio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.site_settings',
                'core.context_processors.experience_video',
            ],
        },
    },
]

WSGI_APPLICATION = 'sbproaudio.wsgi.application'

DATABASE_URL = config('DATABASE_URL', default=None)

if DATABASE_URL:
    # Production (Railway) — uses PostgreSQL
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    # Local development — keeps using SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

JAZZMIN_SETTINGS = {
    "site_title": "GM SOUND",
    "site_header": "GM SOUND",
    "site_brand": "GM SOUND",
    "welcome_sign": "Welcome to GM SOUND Dashboard",
    "copyright": "GM SOUND",

    "show_sidebar": True,

    "navigation_expanded": True,

    "icons": {
        "core.Product": "fas fa-box",
        "core.ProductCategory": "fas fa-tags",
        "core.Service": "fas fa-tools",
        "core.Testimonial": "fas fa-star",
        "core.HeroSlide": "fas fa-image",
        "core.ContactSubmission": "fas fa-envelope",
        "core.SiteSettings": "fas fa-cogs",
        "core.QuoteRequest": "fas fa-file-invoice",
        "core.WhyChooseUs": "fas fa-check-circle",
        "core.HomeContent": "fas fa-home",
    },

    "topmenu_links": [
        {
            "name": "Visit Website",
            "url": "/",
            "new_window": True,
        }
    ],
}
