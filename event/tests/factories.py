# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import factory
from django.utils import timezone

from event.models import (
    Category,
    Event,
    Location,
    Permission,
    Status,
)


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category


class LocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Location


class PermissionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Permission


class StatusFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Status


class EventFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Event

    category = factory.SubFactory(CategoryFactory)
    location = factory.SubFactory(LocationFactory)
    permission = factory.SubFactory(PermissionFactory)
    start_date = timezone.now().date()
    status = factory.SubFactory(StatusFactory)
