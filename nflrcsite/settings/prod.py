# prod.py
from .base import *

DOC_ROOT = '<ABS PATH TO WEB DOCUMENT ROOT HERE>'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# ! DO NOT EDIT THESE IN DEVELOPMENT!
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}

# Append apps needed only in production.
# #INSTALLED_APPS += (,)

# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(DOC_ROOT, 'media/nflrc/')

# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(DOC_ROOT, 'static/nflrc/')

