#!/usr/bin/env python
import os
import sys
from django.core.management.commands.runserver import Command as runserver


def main():
    runserver.default_port = "80"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-user-management-project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
