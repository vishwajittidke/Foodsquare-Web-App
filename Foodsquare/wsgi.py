# """
# WSGI config for Foodsquare project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Foodsquare.settings')

# application = get_wsgi_application()



"""
WSGI config for Foodsquare project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import dotenv

# ✅ Load environment variables from .env file
dotenv.load_dotenv()

from django.core.wsgi import get_wsgi_application

# ✅ Set the default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Foodsquare.settings')

# ✅ Create the WSGI application
application = get_wsgi_application()
