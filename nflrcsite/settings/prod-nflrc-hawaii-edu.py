# prod.py
from .base import *

SECRET_KEY = 'su!r1r&_kq+03a8(y3*@z23=7zi@j!-w8gpv!&79xl7jql17q+'

DOC_ROOT = '/web'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# ! DO NOT EDIT THESE IN DEVELOPMENT!
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'nflrcpydb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'nflrcpydbuser',
        'PASSWORD': 'uN05inco3',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}

# Append apps needed only in production.
# #INSTALLED_APPS += (,)

# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(DOC_ROOT, 'media/nflrc/')

# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(DOC_ROOT, 'static/nflrc/')

# ! END SACRED DO NOT EDIT THESE IN DEVELOPMENT!

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

