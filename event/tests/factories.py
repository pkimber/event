# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import factory

from event.models import (
    Event,
    EventLocation,
    EventStatus,
    EventType,
)


class EventFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Event


class EventLocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = EventLocation


class EventStatusFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = EventStatus


class EventTypeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = EventType
