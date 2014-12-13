# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

from event.models import Event


class HomeView(TemplateView):

    template_name = 'example/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update(dict(
            events=Event.objects.public_calendar(),
        ))
        return context
