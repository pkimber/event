# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from django.utils import timezone

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from login.tests.scenario import default_scenario_login

from .factories import (
    EventFactory,
    EventLocationFactory,
    EventStatusFactory,
    EventTypeFactory,
)


class TestViewPerm(PermTestCase):

    def setUp(self):
        self.setup_users()

    def test_event_create(self):
        self._assert_staff(reverse('event.create'))

    def test_event_list(self):
        self._assert_staff(reverse('event.list'))

    def test_event_update(self):
        event = EventFactory(
            event_date=date(2013, 3, 30),
            start_time=timezone.now().time(),
        )
        url = reverse(
            'event.update',
            kwargs=dict(pk=event.pk)
        )
        self._assert_staff(url)

    def test_event_location_create(self):
        self._assert_staff(reverse('event.create'))

    def test_event_location_list(self):
        self._assert_staff(reverse('event.list'))

    def test_event_location_update(self):
        event_location = EventLocationFactory()
        url = reverse(
            'event.location.update',
            kwargs=dict(pk=event_location.pk)
        )
        self._assert_staff(url)

    def test_event_status_create(self):
        self._assert_staff(reverse('event.create'))

    def test_event_status_list(self):
        self._assert_staff(reverse('event.list'))

    def test_event_status_update(self):
        event_status = EventStatusFactory()
        url = reverse(
            'event.status.update',
            kwargs=dict(pk=event_status.pk)
        )
        self._assert_staff(url)

    def test_event_type_create(self):
        self._assert_staff(reverse('event.create'))

    def test_event_type_list(self):
        self._assert_staff(reverse('event.list'))

    def test_event_type_update(self):
        event_type = EventTypeFactory()
        url = reverse(
            'event.type.update',
            kwargs=dict(pk=event_type.pk)
        )
        self._assert_staff(url)
