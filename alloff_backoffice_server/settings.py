from pathlib import Path
from mongoengine.connection import connect
from datetime import timedelta
from django.contrib.staticfiles import handlers
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()  # take environment variables from .env.
env = dotenv_values(".env")
SERVICE_ENV_IS_DEV = env.get("SERVICE_ENV") != "prod"


# extend StaticFilesHandler to add "Access-Control-Allow-Origin" to every response
class CORSStaticFilesHandler(handlers.StaticFilesHandler):
    def serve(self, request):
        response = super().serve(request)
        response["Access-Control-Allow-Origin"] = "*"
        return response


# monkeypatch handlers to use our class instead of the original StaticFilesHandler
handlers.StaticFilesHandler = CORSStaticFilesHandler

"""
Django settings for alloff_backoffice_server project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-_*10%j5@a2i%)wx-*(6^a!wpar$e5jqce&hus=4dr_^(b9&2(q"
    if env.get("DJANGO_SECRET") is None
    else env.get("DJANGO_SECRET")
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = "*"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_mongoengine",
    "django_grpc_framework",
    "django_filters",
    "corsheaders",
    "drf_spectacular",
    "django_extensions",
    "office",
    "order",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "alloff_backoffice_server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "alloff_backoffice_server.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DB_ENV_IS_LOCAL = env.get("DB_ENV") == "local"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    if DB_ENV_IS_LOCAL
    else {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env.get("DB_HOST"),
        "NAME": f"order_{'dev' if SERVICE_ENV_IS_DEV else 'prod'}",
        "PASSWORD": env.get("DB_PASSWORD"),
        "USER": env.get("DB_USER"),
        "PORT": 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "office.drf.pagination.CustomPageNumberPagination",
    "PAGE_SIZE": 20,
}
STATIC_ROOT = "./static"
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        days=int(env.get("ACCESS_TOKEN_LIFETIME_IN_DAYS"))
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=int(env.get("REFRESH_TOKEN_LIFETIME_IN_DAYS"))
    ),
    "ACCESS_TOKEN_NAME": "Access-Token",
    "REFRESH_TOKEN_NAME": "Refresh-Token",
    "ROTATE_REFRESH_TOKENS": True,
}
ALIMTALK = {
    "APP_KEY": env.get("ALIMTALK_APP_KEY"),
    "SECRET": env.get("ALIMTALK_SECRET"),
    "SENDER_KEY": env.get("ALIMTALK_SENDER_KEY"),
    "URL": "https://api-alimtalk.cloud.toast.com/alimtalk/v2.1/appkeys/{}/messages",
}

PUSHSERVER = {
    "URL": env.get("PUSH_SERVER_URL"),
    "NAVIGATE_URL": env.get("PUSH_NAVIGATE_URL"),
}

connect(
    "outlet_dev" if SERVICE_ENV_IS_DEV else "outlet",
    host="mongodb://db.lessbutter.co",
    username=env.get("SERVICE_DB_USERNAME"),
    password=env.get("SERVICE_DB_PASSWORD"),
    authentication_source="admin",
)

AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_ACCESS_KEY_ID = env.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env.get("AWS_S3_REGION_NAME")
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = "public-read"
AWS_S3_VERIFY = True
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
SPECTACULAR_SETTINGS = {
    "COMPONENT_SPLIT_REQUEST": True,
    "ENUM_NAME_OVERRIDES": {
        "OrderStatusEnum": "order.models.order.OrderStatus.choices",
        "OrderItemStatusEnum": "order.models.order_item.OrderItemStatus.choices",
    },
    "SERVERS": [
        {"url": env.get("API_HOST") if "API_HOST" in env else "http://localhost:8000"}
    ],
}

LABEL_SERVER_URL = "https://memoji.jp.ngrok.io/print"
CODE_CHARSET = "346789ABCDEFGHJKLMNPQRTUVWXY"

GRPC_LOGISTICS_SERVER_URL = "ec2-13-209-64-30.ap-northeast-2.compute.amazonaws.com:9000"