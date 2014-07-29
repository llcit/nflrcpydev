"""
WSGI config for nflrcsite project.
NOTE: This config is NOT set up for production use. See production server setup for production use.
"""

import os, sys

sys.path.insert(0, 'PATH HERE')

os.environ["DJANGO_SETTINGS_MODULE"] = "DOTTED PATH HERE"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

