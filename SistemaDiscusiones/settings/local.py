__author__ = 'soporte'
from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [*]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'discusiones',
		'USER' : 'cursodjango',
		'PASSWORD' : 'pass',
		'HOST' : 'localhost',
		'PORT' : '5432',
	}
}
 
STATIC_URL = '/static/'
 
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '1422409964680771'
SOCIAL_AUTH_FACEBOOK_SECRET = '640df1ac8fcb8da6dbc59209f3635069'

SOCIAL_AUTH_TWITTER_KEY = 'qWHWMSKEnshW2gukH5MQ'
SOCIAL_AUTH_TWITTER_SECRET = 'jviFtewE4lDhXIR54M61Ni8tyDlrVPpRbTjOj4NRVqU'