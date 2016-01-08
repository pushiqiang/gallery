"""
WSGI config for gallery project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
from os.path import join,dirname,abspath

PROJECT_DIR = '/home/pushiqiang/gallery'#dirname(dirname(abspath(__file__)))
import sys
if PROJECT_DIR not in sys.path:
    sys.path.insert(0,PROJECT_DIR)

os.environ["DJANGO_SETTINGS_MODULE"] = "gallery.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
