# settings/dev.py

# Example use with manage.py:
# $ python manage.py runserver --settings=nflrcsite .settings.dev


from .base import *

# Secret key stored in environment variable not here.
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nflrc_pg',
        'USER': 'postgres',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Append apps used in development not production.

MEDIA_ROOT = PROJECT_DIR.child('media', 'nflrc')

# FILEBROWSER SETTINGS
from django.conf import settings

FILEBROWSER_DIRECTORY = ''
FILEBROWSER_VERSIONS_BASEDIR = getattr(settings, 'FILEBROWSER_VERSIONS_BASEDIR', '_versions')
FILEBROWSER_ADMIN_VERSIONS = getattr(settings, 'FILEBROWSER_ADMIN_VERSIONS', ['thumbnail', 'small', 'medium', 'big', 'large'])
FILEBROWSER_EXTENSIONS = getattr(settings, "FILEBROWSER_EXTENSIONS", {
    'Folder': [''],
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
    'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
    'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm'],
    'Audio': ['.mp3','.mp4','.wav','.aiff','.midi','.m4p']
})

FILEBROWSER_SELECT_FORMATS = getattr(settings, "FILEBROWSER_SELECT_FORMATS", {
    'file': ['Folder','Image','Document','Video','Audio'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video','Audio'],
})

FILEBROWSER_ADMIN_THUMBNAIL = getattr(settings, 'FILEBROWSER_ADMIN_THUMBNAIL', 'admin_thumbnail')

FILEBROWSER_VERSIONS = getattr(settings, "FILEBROWSER_VERSIONS", {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 230, 'height': '', 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 230, 'height': '', 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
})
FILEBROWSER_CONVERT_FILENAME = getattr(settings, "FILEBROWSER_CONVERT_FILENAME", False)
# END FILEBROWSER SETTINGS

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/logout'

LOGIN_REDIRECT_URL = '/'

# EMAIL_HOST = os.environ['EMAIL_HOST']
# EMAIL_PORT = os.environ['EMAIL_PORT']
# EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
# EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']

# SITE_HOST = os.environ['SITE_HOST']

# SENDFILE settings
SENDFILE_BACKEND = 'sendfile.backends.development'
#SENDFILE_BACKEND = 'sendfile.backends.xsendfile'
#SENDFILE_BACKEND = 'sendfile.backends.nginx'
SENDFILE_ROOT = os.path.join(PROJECT_DIR, 'protected-dev')
SENDFILE_URL = '/protected-dev'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': '',
    },
}

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 1000

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

