# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from base.form_utils import RequiredFieldForm

from .models import Event


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
            'event_date',
            'description',
            'start_time',
            'end_time',
            'location',
            'notes',
        )
