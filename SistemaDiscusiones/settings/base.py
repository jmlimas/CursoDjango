from unipath import Path
BASE_DIR =  Path(__file__).ancestor(3)

SECRET_KEY = 'v_^vemp5f2)z#+v73=bfo(z^7!g1&pa*-4@2_xwsjv5)2*tgj0'

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    )

THIRD_PARTY_APPS = (
    'south',
     
    )

LOCAL_APPS = (
    'apps.home',

    )

INSTALLED_APPS =  DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SistemaDiscusiones.urls'

WSGI_APPLICATION = 'SistemaDiscusiones.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]