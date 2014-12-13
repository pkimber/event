# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from event.models import Permission


def init_app_event():
    Permission.objects.init_permission(Permission.PUBLIC, 'Public', 'public')
    Permission.objects.init_permission(Permission.STAFF, 'Staff only', 'staff')
    Permission.objects.init_permission(Permission.USER, 'User', 'user')
