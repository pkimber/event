# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from dateutil.relativedelta import relativedelta

from django.test import TestCase
from django.utils import timezone

from event.models import Event

from .factories import (
    EventFactory,
    EventStatusFactory,
    EventTypeFactory,
)


class TestEvent(TestCase):

    def test_promoted(self):
        """Promoted events are between two and eight months."""
        today = timezone.now().date()
        one = today + relativedelta(days=7)
        six = today + relativedelta(months=6)
        year = today + relativedelta(years=1)
        publish = EventStatusFactory(publish=True)
        pending = EventStatusFactory(publish=False)
        promote = EventTypeFactory(promote=True)
        routine = EventTypeFactory(promote=False, routine=True)
        start = timezone.now().time()
        # do NOT include this one because it is less than 2 months
        EventFactory(
            description='a', event_date=one, start_time=start, status=publish
        )
        EventFactory(
            description='b', event_date=six, start_time=start, status=publish,
            event_type=promote,
        )
        # do NOT include this one because it is a routine event (not promoted)
        EventFactory(
            description='c', event_date=six, start_time=start, status=publish,
            event_type=routine,
        )
        # do NOT include this one because it is older than 8 months
        EventFactory(
            description='d', event_date=year, start_time=start, status=publish
        )
        # do NOT include this one because it is deleted
        EventFactory(
            description='e', event_date=six, start_time=start, status=publish,
            deleted=True,
        )
        # do NOT include this one because it is not published
        EventFactory(
            description='e', event_date=six, start_time=start, status=pending,
        )
        events = Event.objects.promoted()
        self.assertEquals(
            ['b',],
            [e.description for e in events]
        )

    def test_published_date(self):
        today = timezone.now().date()
        b4 = today + relativedelta(days=-1)
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
        # do NOT include this one because it for yesterday
        EventFactory(
            description='d', event_date=b4, start_time=start, status=publish
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
        # do NOT include this one because it is deleted
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
