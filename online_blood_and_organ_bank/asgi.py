"""
ASGI config for online_blood_and_organ_bank project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_blood_and_organ_bank.settings') # chnage here

application = get_asgi_application()
