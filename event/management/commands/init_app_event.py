# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand

from event.service import init_app_event


class Command(BaseCommand):

    help = "Initialise 'event' application"

    def handle(self, *args, **options):
        init_app_event()
        print("Initialised 'event' app...")
