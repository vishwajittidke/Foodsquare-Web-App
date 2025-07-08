#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv

# ✅ Load environment variables from a .env file
dotenv.load_dotenv()

def main():
    # ✅ Set default settings module for Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Foodsquare.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # ✅ Run the management command
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
