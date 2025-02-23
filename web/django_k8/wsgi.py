"""
WSGI config for django_k8 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import pathlib
import dotenv

from django.core.wsgi import get_wsgi_application


CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE = BASE_DIR / '.env'
dotenv.read_dotenv(ENV_FILE)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_k8.settings')

application = get_wsgi_application()
