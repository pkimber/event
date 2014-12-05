# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)

from .views import (
    EventCreateView,
    EventListView,
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
)
