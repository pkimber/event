# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from base.form_utils import RequiredFieldForm

from .models import (
    Event,
    EventLocation,
    EventStatus,
    EventType,
)


class EventForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for name in ('description', 'location', 'notes'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = Event
        fields = (
            'status',
            'event_type',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'description',
            'location',
            'notes',
        )


class EventLocationForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(EventLocationForm, self).__init__(*args, **kwargs)
        for name in ('description', 'url', 'url_map', 'notes'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = EventLocation
        fields = (
            'description',
            'url',
            'url_map',
            'notes',
        )


class EventStatusForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(EventStatusForm, self).__init__(*args, **kwargs)
        for name in ('description',):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = EventStatus
        fields = (
            'description',
            'publish',
        )


class EventTypeForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(EventTypeForm, self).__init__(*args, **kwargs)
        for name in ('description', 'css_class_name'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = EventType
        fields = (
            'description',
            'promote',
            'routine',
            'css_class_name',
        )
