from .production import *

DEBUG = True
TEMPLATE_DEBUG = True
DJANGO_SERVE_PUBLIC = True
USE_DJANGO_DEBUG_TOOLBAR = True
PREPEND_WWW = False
SEND_BROKEN_LINK_EMAILS = False
SESSION_ENGINE = 'django.contrib.sessions.backends.file'

if USE_DJANGO_DEBUG_TOOLBAR:
    MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
    INSTALLED_APPS += ("debug_toolbar",)
    DEBUG_TOOLBAR_CONFIG = { 'INTERCEPT_REDIRECTS': False, }

TEMPLATE_CONTEXT_PROCESSORS += [
    'django.core.context_processors.debug'
]
