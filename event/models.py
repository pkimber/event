# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from dateutil.relativedelta import relativedelta

from django.db import models
from django.utils import timezone

import reversion

from base.model_utils import TimeStampedModel


class Category(TimeStampedModel):

    """This needs to have a level e.g. public, logged in and member of staff."""

    description = models.CharField(max_length=200)
    promote = models.BooleanField(default=False)
    routine = models.BooleanField(default=True)

    class Meta:
        ordering = ('description',)
        verbose_name = 'Event type'
        verbose_name_plural = 'Event types'

    def __str__(self):
        return '{}'.format(self.description)

reversion.register(Category)


class Location(TimeStampedModel):
    """
    Need some private notes so we can tell where the location is e.g. homegroup.
    Or... perhaps we need an option to contact us (using the enquiry form).
    So... if someone is not logged in, they get told to contact us....
    """

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

reversion.register(Location)


class PermissionManager(models.Manager):

    def create_permission(self, slug, description, css_class_name):
        permission = self.model(
            slug=slug,
            description=description,
            css_class_name=css_class_name,
        )
        permission.save()
        return permission

    def init_permission(self, slug, description, css_class_name):
        try:
            permission = self.model.objects.get(slug=slug)
            permission.description = description
            permission.css_class_name = css_class_name
            permission.save()
        except self.model.DoesNotExist:
            permission = self.create_permission(
                slug, description, css_class_name
            )
        return permission


class Permission(TimeStampedModel):

    PUBLIC = 'public'
    STAFF = 'staff'
    USER = 'user'

    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200)
    css_class_name = models.CharField(max_length=100, blank=True)
    objects = PermissionManager()

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'

    def __str__(self):
        return '{}'.format(self.description)

reversion.register(Permission)


class Status(TimeStampedModel):
    """Staff only for leaders meetings."""

    description = models.CharField(max_length=200)
    publish = models.BooleanField(default=False)

    class Meta:
        ordering = ('description',)
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return '{}'.format(self.description)

reversion.register(Status)


class EventManager(models.Manager):
    """
    Calendar on home page... just the next week + promoted events.

    Separate calendar page.

    We also have church member promotions e.g. Newquay... There don't need to
    be on the home page.

    And, we have events for the community e.g. Christmas Party

    Need to link an event to another page on the site... for more information.

    What about rotas etc?
    """

    def _eight_months(self):
        today = timezone.now().date()
        return today + relativedelta(months=8)

    def _two_months(self):
        today = timezone.now().date()
        return today + relativedelta(months=2)

    def _public(self):
        return self.model.objects.filter(
            permission__slug=Permission.PUBLIC,
            status__publish=True,
        ).exclude(
            deleted=True
        )

    def public_calendar(self):
        return self._public().filter(
            start_date__gte=timezone.now().date(),
            start_date__lte=self._two_months(),
        )

    def public_promoted(self):
        return self._public().filter(
            start_date__gt=self._two_months(),
            start_date__lte=self._eight_months(),
            category__promote=True,
        )


class Event(TimeStampedModel):
    """Extra info for members e.g. who is leading."""

    permission= models.ForeignKey(Permission)
    category = models.ForeignKey(Category)
    description = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    start_time = models.TimeField(
        blank=True, null=True,
        help_text="Please enter in 24 hour format e.g. 19:00",
    )
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(
        blank=True, null=True,
        help_text="Please enter in 24 hour format e.g. 21:00",
    )
    location = models.ForeignKey(Location)
    notes_public = models.TextField(blank=True)
    notes_user = models.TextField(blank=True)
    notes_staff = models.TextField(blank=True)
    status = models.ForeignKey(Status)
    deleted = models.BooleanField(default=False)
    objects = EventManager()

    class Meta:
        ordering = ('start_date', 'start_time')
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return '{}'.format(self.description)

reversion.register(Event)
