# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from event.management.commands import init_app_event


class TestCommand(TestCase):

    def test_init_app(self):
        """ Test the management command """
        command = init_app_event.Command()
        command.handle()
