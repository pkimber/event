# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand

from event.models import Permission


class Command(BaseCommand):

    help = "Initialise 'event' application"

    def handle(self, *args, **options):
        Permission.objects.init_permission(
            Permission.PUBLIC, 'Public', 'public'
        )
        Permission.objects.init_permission(
            Permission.STAFF, 'Staff only', 'staff'
        )
        Permission.objects.init_permission(
            Permission.USER, 'User', 'user'
        )
        print("Initialised 'event' app...")
