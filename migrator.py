# -*- coding: utf-8 -*-
import django

from django.conf import settings
from django.core.management import call_command

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'ibantools',
    ),
)

django.setup()
call_command('makemigrations', 'ibantools')
