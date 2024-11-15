"""
WSGI config for reportcard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
# Owned by Yash Jangid 
# github_id = yash-jangid-21
# linkeldn_id = yash-21-yash

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reportcard.settings')

application = get_wsgi_application()
