import os
from pathlib import Path

# Создайте пути внутри проекта следующим образом: BASE_DIR/'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Настройки быстрого старта разработки - непригодны для производства
# См. https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/.

# ПРЕДУПРЕЖДЕНИЕ О БЕЗОПАСНОСТИ: храните секретный ключ, используемый в производстве, в тайне!
SECRET_KEY = 'django-insecure-u_9e3ba5(z(i@p196sh_cn$pmx6%(p_!tlcg5@1rq+vzl34!2z'

# ПРЕДУПРЕЖДЕНИЕ БЕЗОПАСНОСТИ: не запускайте с включенной отладкой в рабочей среде!
DEBUG = True

ALLOWED_HOSTS = []

# Определение приложения

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'catalog',
    'blog',
    'users',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

# База данных
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dz_22_2',
        'USER': 'postgres',
        'PASSWORD': '1q2w3e',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# Проверка пароля
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Интернационализация
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Статические файлы (CSS, JavaScript, изображения)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Тип поля первичного ключа по умолчанию
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

STATICFILES_DIRS = (BASE_DIR / 'static',)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'  # dz_20.1
MEDIA_ROOT = BASE_DIR / 'media'  # dz_20.1

AUTH_USER_MODEL = 'users.Users'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "vanya1928ivanov@yandex.ru"
EMAIL_HOST_PASSWORD = "jncywffoxzdmdsho"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
