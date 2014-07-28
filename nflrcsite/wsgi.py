"""
WSGI config for nflrcsite project.
"""

import os, sys

sys.path.insert(0, '/pythonweb/nflrcpydev/')

os.environ["DJANGO_SETTINGS_MODULE"] = "nflrcsite.settings.prod-nflrc-hawaii-edu"

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nflrcsite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

