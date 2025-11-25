#!/usr/bin/env python
"""Django का management utility"""
import os
import sys

def main():
    """Django project के लिए command line utility"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django import नहीं हो सकी। क्या आपने pip install django किया है?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
