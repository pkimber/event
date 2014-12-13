# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from dateutil.relativedelta import relativedelta

from django.test import TestCase
from django.utils import timezone

from event.models import (
    Event,
    Permission,
)

from .factories import (
    CategoryFactory,
    EventFactory,
    PermissionFactory,
    StatusFactory,
)


class TestEvent(TestCase):

    def test_public_calendar(self):
        publish = StatusFactory(publish=True)
        public = PermissionFactory(slug=Permission.PUBLIC)
        user = PermissionFactory(slug=Permission.USER)
        staff = PermissionFactory(slug=Permission.STAFF)
        EventFactory(description='a', status=publish, permission=public)
        EventFactory(description='b', status=publish, permission=user)
        EventFactory(description='c', status=publish, permission=staff)
        EventFactory(description='d', status=publish, permission=public)
        events = Event.objects.public_calendar()
        self.assertEquals(
            ['a', 'd'],
            [e.description for e in events]
        )

    def test_public_calendar_date(self):
        """Select published events within the next two months."""
        today = timezone.now().date()
        b4 = today + relativedelta(days=-1)
        one = today + relativedelta(days=7)
        two = today + relativedelta(days=14)
        year = today + relativedelta(years=1)
        public = PermissionFactory(slug=Permission.PUBLIC)
        publish = StatusFactory(publish=True)
        start = timezone.now().time()
        EventFactory(
            description='a', start_date=one, start_time=start, status=publish,
            permission=public,
        )
        EventFactory(
            description='b', start_date=two, start_time=start, status=publish,
            permission=public,
        )
        # do NOT include this one because it is older than two months
        EventFactory(
            description='c', start_date=year, start_time=start, status=publish,
            permission=public,
        )
        # do NOT include this one because it for yesterday
        EventFactory(
            description='d', start_date=b4, start_time=start, status=publish,
            permission=public,
        )
        events = Event.objects.public_calendar()
        self.assertEquals(
            ['a', 'b'],
            [e.description for e in events]
        )

    def test_public_delete(self):
        today = timezone.now().date()
        one = today + relativedelta(days=7)
        public = PermissionFactory(slug=Permission.PUBLIC)
        publish = StatusFactory(publish=True)
        start = timezone.now().time()
        EventFactory(
            description='a', start_date=one, start_time=start, status=publish,
            permission=public,
        )
        # do NOT include this one because it is deleted
        EventFactory(
            description='b', start_date=one, start_time=start, status=publish,
            permission=public, deleted=True,
        )
        events = Event.objects._public()
        self.assertEquals(
            ['a',],
            [e.description for e in events]
        )

    def test_public_promoted(self):
        """Promoted events are between two and eight months."""
        today = timezone.now().date()
        one = today + relativedelta(days=7)
        six = today + relativedelta(months=6)
        year = today + relativedelta(years=1)
        public = PermissionFactory(slug=Permission.PUBLIC)
        publish = StatusFactory(publish=True)
        pending = StatusFactory(publish=False)
        promote = CategoryFactory(promote=True)
        routine = CategoryFactory(promote=False, routine=True)
        start = timezone.now().time()
        # do NOT include this one because it is less than 2 months
        EventFactory(
            description='a', start_date=one, start_time=start, status=publish,
            permission=public,
        )
        EventFactory(
            description='b', start_date=six, start_time=start, status=publish,
            permission=public, category=promote,
        )
        # do NOT include this one because it is a routine event (not promoted)
        EventFactory(
            description='c', start_date=six, start_time=start, status=publish,
            permission=public, category=routine,
        )
        # do NOT include this one because it is older than 8 months
        EventFactory(
            description='d', start_date=year, start_time=start, status=publish,
            permission=public,
        )
        # do NOT include this one because it is deleted
        EventFactory(
            description='e', start_date=six, start_time=start, status=publish,
            permission=public, deleted=True,
        )
        # do NOT include this one because it is not published
        EventFactory(
            description='e', start_date=six, start_time=start, status=pending,
            permission=public,
        )
        events = Event.objects.public_promoted()
        self.assertEquals(
            ['b',],
            [e.description for e in events]
        )

    def test_public_status(self):
        today = timezone.now().date()
        one = today + relativedelta(days=7)
        public = PermissionFactory(slug=Permission.PUBLIC)
        publish = StatusFactory(publish=True)
        pending = StatusFactory(publish=False)
        start = timezone.now().time()
        EventFactory(
            description='a', start_date=one, start_time=start, status=pending,
            permission=public,
        )
        EventFactory(
            description='b', start_date=one, start_time=start, status=publish,
            permission=public,
        )
        events = Event.objects._public()
        self.assertEquals(
            ['b',],
            [e.description for e in events]
        )
