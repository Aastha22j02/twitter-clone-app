from pathlib import Path

from django.urls import reverse_lazy

from environs import Env

# Set up environs
env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = [ 'localhost', '127.0.0.1', '10.0.1.109', 'twitter.os3.com']



# Application definition

INSTALLED_APPS = [
    # 'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # serving static files
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # For full-text search
    'django.contrib.postgres',
    'sslserver',
    # 3RD PARTY

    # For user account management
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # github
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.facebook',


    # django otp
 
    # For widget tweaking
    'widget_tweaks',
    # For debugging
    #'debug_toolbar',

    # LOCAL

    # For about and home page
    'pages.apps.PagesConfig',
    
    'mobile_otp',

    # For user profiles
    'profiles.apps.ProfilesConfig',

    # For activity stream
    'actions.apps.ActionsConfig',

    # For tweet functionality
    'tweets.apps.TweetsConfig',

    # # For Chat
    # 'mychatapp.apps.MychatappConfig'
    'chat',
 
  

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    
    # For debug_toolbar
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Custom context processor for follow suggestion section on right sidebar of site.
                'profiles.context_processors.follow_suggestion',

            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#---------------------------------------------------------------------------
# For allauth
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 3

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env.str("DJANGO_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.str("DJANGO_EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT = 'home'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
DEFAULT_FROM_EMAIL = 'os3noreply'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SESSION_REMEMBER = True
#--------------------------------------------------------------------------------
# Canonical url for users
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('profile', args=[u.username])
}
#---------------------------------------------------------------------------------
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
# MESSAGE_STORAGE = 'django.contrib.messages.storage.base.BaseStorage'
#provider auth
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         }
#     }
# }

#provider github
# SOCIALACCOUNT_PROVIDERS = {
#     'github': {
#         'APP': {
#             'client_id': 'cd077d77842fa53beebb',
#             'secret': '0179f2cb26a9a637a2254e33ab1f1aba54bc8f08',
#             'key': ''
#         }
#     }
# }

# settings.py

TWILIO_ACCOUNT_SID = 'ACa15c520f3c63eb4745384784262cd38d'
TWILIO_AUTH_TOKEN = 'b36c3bef11f957dc63ec7a7ec4e50e99'
TWILIO_PHONE_NUMBER = '+12316248749'

# CORS_ALLOWED_ORIGINS = [

# "http://localhost:8000",
# "http://127.0.0.1:8000"
# ]

# CORS_ALLOW_METHODS = [
# 'DELETE',
# 'GET',
# 'OPTIONS',
# 'PATCH',
# 'POST',
# 'PUT',
# ]

# CORS_ALLOW_HEADERS = [
# 'accept',
# 'accept-encoding',
# 'authorization',
# 'content-type',
# 'dnt',
# 'origin',
# 'user-agent',
# 'x-csrftoken',
# 'x-requested-with',
# ]
