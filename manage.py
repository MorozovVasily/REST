#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# import oauth2_provider.models


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineStore.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # oauth2_provider.models.Application.objects.all()
    # oauth2_app = oauth2_provider.models.Application()
    # oauth2_app.client_id = "id"
    # oauth2_app.client_secret = "secret"
    # oauth2_app.name = "name"
    # oauth2_app.client_type = "Confidential"
    # oauth2_app.authorization_grant_type = "Resource owner password-based"
    # oauth2_app.save()
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
