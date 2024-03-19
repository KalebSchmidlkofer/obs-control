
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'obs.settings')

application = get_wsgi_application()
bind = "localhost:8000"
workers = 3
