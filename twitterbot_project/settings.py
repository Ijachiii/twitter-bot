"""
Django settings for twitterbot_project project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-%37&rss7-v9ep57#hga3qdj3b5_k6_z5x$3$va4+(rcj^bcw$6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # local apps
    "twitterbot.apps.TwitterbotConfig",
    "accounts.apps.AccountsConfig",
    "api.apps.ApiConfig",
    # 3rd party apps
    "crispy_forms",
    "crispy_bootstrap5",
    "django.contrib.sites",
    "allauth",
    "allauth.socialaccount",
    "allauth.account",
    "social_django",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "drf_spectacular",

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = "twitterbot_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ BASE_DIR / "templates" ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "twitterbot_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"

SOCIAL_AUTH_TWITTER_KEY = "nkP9VwbfMZzKtpgwigFVr7D61"
SOCIAL_AUTH_TWITTER_SECRET = "fdo8ZxNUYqgRhuZLwnS6bduoieuDsmCmmT51MY6pS80K00OfEt"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "login"

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "social_core.backends.twitter.TwitterOAuth",
)

# sending mails
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "smtp2go_django.email_backend.Smtp2goEmailBackend"

# DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
# EMAIL_HOST = env("EMAIL_HOST")
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = env.int("EMAIL_PORT")
# EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")

# allauth authentication
#ACCOUNT_EMAIL_REQUIRED = False
#ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
#ACCOUNT_USERNAME_REQUIRED = False
#ACCOUNT_AUTHENTICATION_METHOD = "username"
#ACCOUNT_UNIQUE_EMAIL = True
#ACCOUNT_EMAIL_VERIFICATION = "none"


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        "rest_framework.authentication.SessionAuthentication",
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticated',
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8000"]
CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "http://localhost:8000",
)

SPECTACULAR_SETTINGS = {
    "TITLE": "Twitter Bot",
    "DESCRIPTION": "Api endpoints for project Twitter Bot",
    "VERSION": "1.0.0",
}

# REST_AUTH = {
#     'JWT_AUTH_COOKIE': 'my-app-auth',
#     'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
# }

# USE_JWT = True