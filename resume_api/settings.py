"""
Django settings for resume_api project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


if DEBUG:
    ALLOWED_HOSTS = [
        "127.0.0.1",
        "localhost",
        # "diverse-intense-whippet.ngrok-free.app",
        "osamaaslam.pythonanywhere.com",
    ]
else:
    ALLOWED_HOSTS = ["osamaaslam.pythonanywhere.com"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "resume",
    "api_auth",
    "rest_framework",
    "corsheaders",
    "django_extensions",
    "formtools",
    "crispy_forms",
    "crispy_bootstrap5",
    "rest_framework_simplejwt",
    # "rest_framework_simplejwt.token_blacklist",
    "drf_spectacular",
]

MIDDLEWARE = [
    # "resume_api.cors.CustomCorsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "resume_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "resume_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# if not DEBUG:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Cache configuration
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    "alternate": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "my_cache_table",
    },
}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


##################################---------- CORS settings---------------##################################
CORS_ALLOWED_ORIGINS = [
    "https://osama11111.pythonanywhere.com",
    "https://osamaaslam.pythonanywhere.com",
    "https://web.postman.co",
    "https://diverse-intense-whippet.ngrok-free.app",
    "http://127.0.0.1:5500",
    "https://resume-builder-integrated-with-resume-api.vercel.app",
    "https://resume-builder-pwa.vercel.app/",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "X-RateLimit-Limit",
    "X-RateLimit-Remaining",
]


if DEBUG:
    CSRF_TRUSTED_ORIGINS = [
        "http://127.0.0.1:5500",
        "https://web.postman.co",
        "https://diverse-intense-whippet.ngrok-free.app",
        "https://osamaaslam.pythonanywhere.com",
        "https://osama11111.pythonanywhere.com",
        "https://resume-builder-integrated-with-resume-api.vercel.app",
    ]
else:
    # authenticate teh request only, checking if it has CSRF token comming here from django-e-commrace
    CSRF_TRUSTED_ORIGINS = [
        "http://127.0.0.1:5500",
        "https://osamaaslam.pythonanywhere.com",
        "https://osama11111.pythonanywhere.com",
        "https://web.postman.co",
        "https://diverse-intense-whippet.ngrok-free.app",
        "https://resume-builder-integrated-with-resume-api.vercel.app",
    ]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# crispy form
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"


# User Model
AUTH_USER_MODEL = "api_auth.CustomUser"


#  Stateless Authentication
# In stateless authentication, the server doesn't keep track of the user's state (session).
# Each request from the client must contain all the information necessary to authenticate the user,
# including the JWT token. The server verifies this token on every request to ensure the user is authenticated.
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_CLASSES": [
        "resume_api.custom_user_rated_throtle_class.CustomAnonRateThrottle",
        "resume_api.custom_user_rated_throtle_class.CustomUserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "200/hour",
        "user": "200/hour",
    },
    # "DATE_INPUT_FORMATS": ["%d-%m-%Y"],
    # "DATE_FORMAT": "%Y-%m-%d",
    # "DATETIME_FORMAT": "%Y-%m-%d %H",
}


SPECTACULAR_SETTINGS = {
    "TITLE": "Resume API",
    "DESCRIPTION": "API documentation for Resume API",
    "VERSION": "1.0.0",
    "COMPONENT_SPLIT_REQUEST": True,
    # Method: 1
    "PREPROCESSING_HOOKS": [
        "resume_api.excluded_path_drf_spectacular_schema.custom_preprocessing_hook",
    ],
    # Method 2: Use @extend_schema(exclude=True) by placing it on top of the View / Action
}

# Authorization: JWTs can contain claims (such as user roles or permissions)
# to authorize access to certain resources.
# JWTs consist of three parts: a header, a payload, and a signature.
# They are encoded as base64 strings and separated by dots (.).
from datetime import timedelta


# Disable DRF built-in session authentication
REST_SESSION_LOGIN = False

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=2500),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=10),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": "django-insecure-o_j80u+4owpa-&!$%&j&n@r0d6&)9kbutwi!m&j-v*b(ems*=d",
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "TOKEN_OBTAIN_SERIALIZER": "api_auth.serializers.TokenClaimObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
}
