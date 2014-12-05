# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import factory

from event.models import Event


class EventFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Event
