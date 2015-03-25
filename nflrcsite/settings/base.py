# base.py
"""
Django BASE settings for nflrcsite project.
"""
import os
from unipath import Path

PROJECT_DIR = Path(__file__).ancestor(3) # Points to top level directory
DOC_ROOT = ''

ADMINS = (
     ('Admin', 'llcit@hawaii.edu'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Pacific/Honolulu'

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

# MEDIA_ROOT = '/media/'

MEDIA_URL = '/media/nflrc/'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nflrcapp.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'nflrcsite.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',

    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.webdesign',

    
    
	'haystack',
    'braces',
    'crispy_forms',

    'badge_site',
    'nflrcapp',

    # 'south',
)

GRAPPELLI_ADMIN_TITLE = 'NFLRC Site Administration'
GRAPPELLI_INDEX_DASHBOARD = 'nflrcsite.dashboard.CustomIndexDashboard'


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'nflrc_stack',
    },
}

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 1000

# local dev -> /usr/local/bin/elasticsearch


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

ISSUER_REPO = 'badge-docs/issuer'
BADGES_REPO = 'badge-docs/badges'
AWARDS_REPO = 'badge-docs/earned'
REVOKE_REPO = 'badge-docs/revoke'


