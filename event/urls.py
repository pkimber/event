# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)

from .views import (
    EventCreateView,
    EventListView,
    EventLocationCreateView,
    EventLocationListView,
    EventLocationUpdateView,
    EventStatusCreateView,
    EventStatusListView,
    EventStatusUpdateView,
    EventTypeCreateView,
    EventTypeListView,
    EventTypeUpdateView,
    EventUpdateView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^event/$',
        view=EventListView.as_view(),
        name='event.list'
        ),
    url(regex=r'^event/create/$',
        view=EventCreateView.as_view(),
        name='event.create'
        ),
    url(regex=r'^event/(?P<pk>\d+)/update/$',
        view=EventUpdateView.as_view(),
        name='event.update'
        ),
    url(regex=r'^location/$',
        view=EventLocationListView.as_view(),
        name='event.location.list'
        ),
    url(regex=r'^location/create/$',
        view=EventLocationCreateView.as_view(),
        name='event.location.create'
        ),
    url(regex=r'^location/(?P<pk>\d+)/update/$',
        view=EventLocationUpdateView.as_view(),
        name='event.location.update'
        ),
    url(regex=r'^status/$',
        view=EventStatusListView.as_view(),
        name='event.status.list'
        ),
    url(regex=r'^status/create/$',
        view=EventStatusCreateView.as_view(),
        name='event.status.create'
        ),
    url(regex=r'^status/(?P<pk>\d+)/update/$',
        view=EventStatusUpdateView.as_view(),
        name='event.status.update'
        ),
    url(regex=r'^type/$',
        view=EventTypeListView.as_view(),
        name='event.type.list'
        ),
    url(regex=r'^type/create/$',
        view=EventTypeCreateView.as_view(),
        name='event.type.create'
        ),
    url(regex=r'^type/(?P<pk>\d+)/update/$',
        view=EventTypeUpdateView.as_view(),
        name='event.type.update'
        ),
)
