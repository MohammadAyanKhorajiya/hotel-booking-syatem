# hotel_project/wsgi.py - Production deployment के लिए
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_project.settings')
application = get_wsgi_application()
