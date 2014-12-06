# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import reversion

from base.model_utils import TimeStampedModel


class EventLocation(TimeStampedModel):

    description = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)
    url_map = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ('description',)
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return '{}'.format(self.description)

reversion.register(EventLocation)


class EventStatus(TimeStampedModel):

    description = models.CharField(max_length=200)
    publish = models.BooleanField(default=False)

    class Meta:
        ordering = ('description',)
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return '{}'.format(self.description)

reversion.register(EventStatus)


class EventType(TimeStampedModel):

    description = models.CharField(max_length=200)
    promote = models.BooleanField(default=False)
    routine = models.BooleanField(default=True)
    css_class_name = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ('description',)
        verbose_name = 'Event type'
        verbose_name_plural = 'Event types'

    def __str__(self):
        return '{}'.format(self.description)

reversion.register(EventType)


class Event(TimeStampedModel):

    event_date = models.DateField()
    event_type = models.ForeignKey(EventType)
    description = models.CharField(max_length=200, blank=True)
    start_time = models.TimeField(
        help_text="Please enter in 24 hour format e.g. 19:00",
    )
    end_time = models.TimeField(
        blank=True, null=True,
        help_text="Please enter in 24 hour format e.g. 21:00",
    )
    location = models.ForeignKey(EventLocation, blank=True, null=True)
    notes = models.TextField(blank=True)
    status = models.ForeignKey(EventStatus)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('event_date', 'start_time')
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return '{}'.format(self.description)

reversion.register(Event)
