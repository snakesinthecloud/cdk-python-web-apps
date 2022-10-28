"""
ASGI config for mycdkdjangoapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from mangum import Mangum

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycdkdjangoapp.settings')

application = get_asgi_application()
handler = Mangum(application, lifespan='off')
