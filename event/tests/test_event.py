# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from dateutil.relativedelta import relativedelta

from django.test import TestCase
from django.utils import timezone

from event.models import Event

from .factories import (
    EventFactory,
    EventStatusFactory,
)


class TestEvent(TestCase):

    def test_published_date(self):
        today = timezone.now().date()
        one = today + relativedelta(days=7)
        two = today + relativedelta(days=14)
        year = today + relativedelta(years=1)
        publish = EventStatusFactory(publish=True)
        start = timezone.now().time()
        EventFactory(
            description='a', event_date=one, start_time=start, status=publish
        )
        EventFactory(
            description='b', event_date=two, start_time=start, status=publish
        )
        # do NOT include this one because it is older than two months
        EventFactory(
            description='c', event_date=year, start_time=start, status=publish
        )
        events = Event.objects.published()
        self.assertEquals(
            ['a', 'b'],
            [e.description for e in events]
        )

    def test_published_delete(self):
        today = timezone.now().date()
        one = today + relativedelta(days=7)
        publish = EventStatusFactory(publish=True)
        start = timezone.now().time()
        EventFactory(
            description='a', event_date=one, start_time=start, status=publish
        )
        EventFactory(
            description='b', event_date=one, start_time=start, status=publish,
            deleted=True
        )
        events = Event.objects.published()
        self.assertEquals(
            ['a',],
            [e.description for e in events]
        )

    def test_published_status(self):
        today = timezone.now().date()
        one = today + relativedelta(days=7)
        publish = EventStatusFactory(publish=True)
        pending = EventStatusFactory(publish=False)
        start = timezone.now().time()
        EventFactory(
            description='a', event_date=one, start_time=start, status=pending
        )
        EventFactory(
            description='b', event_date=one, start_time=start, status=publish,
        )
        events = Event.objects.published()
        self.assertEquals(
            ['b',],
            [e.description for e in events]
        )
