# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView,
    ListView,
    TemplateView,
    UpdateView,
)

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin

from .forms import (
    EventForm,
    EventLocationForm,
    EventStatusForm,
    EventTypeForm,
)
from .models import (
    Event,
    EventLocation,
    EventStatus,
    EventType,
)


class EventCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, CreateView):

    form_class = EventForm
    model = Event

    def get_success_url(self):
        return reverse('event.list')


class EventListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = Event


class EventUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, UpdateView):

    form_class = EventForm
    model = Event

    def get_success_url(self):
        return reverse('event.list')


class EventLocationCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, CreateView):

    form_class = EventLocationForm
    model = EventLocation

    def get_success_url(self):
        return reverse('event.location.list')


class EventLocationListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = EventLocation


class EventLocationUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, UpdateView):

    form_class = EventLocationForm
    model = EventLocation

    def get_success_url(self):
        return reverse('event.location.list')


class EventStatusCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, CreateView):

    form_class = EventStatusForm
    model = EventStatus

    def get_success_url(self):
        return reverse('event.status.list')


class EventStatusListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = EventStatus
    template_name = 'dash/event_status.html'


class EventStatusUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, UpdateView):

    form_class = EventStatusForm
    model = EventStatus

    def get_success_url(self):
        return reverse('event.status.list')


class EventTypeCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, CreateView):

    form_class = EventTypeForm
    model = EventType

    def get_success_url(self):
        return reverse('event.type.list')


class EventTypeListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = EventType
    template_name = 'dash/event_types.html'


class EventTypeUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, UpdateView):

    form_class = EventTypeForm
    model = EventType

    def get_success_url(self):
        return reverse('event.type.list')
