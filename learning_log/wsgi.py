"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# Add voor Heroku
from dj_static import Cling                         

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')
# Add voor Heroku
application = Cling(get_wsgi_application())

application = get_wsgi_application()
