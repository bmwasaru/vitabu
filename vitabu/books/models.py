from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone


CONDITION = (
    ('New', 'New'),
    ('Good', 'Good'),
    ('Old', 'Old'),
)

SHELF_LOCATION = (
    ('Business & I.T', 'Business & I.T'),
    ('Economics', 'Economics'),
    ('I.T', 'I.T'),
    ('Law', 'Law'),
    ('Mathematics', 'Mathematics'),
    ('Medicine', 'Medicine'),
    ('Scialogy', 'Socialogy'),
)


class Book(models.Model):

    YEAR_CHOICES = [(r, r)
                    for r in range(1984, datetime.date.today().year + 1)]

    title = models.CharField(max_length=50)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField(
        blank=False, null=False, help_text='dd/mm/yy')
    author = models.CharField(max_length=255, blank=False)
    editor = models.CharField(max_length=255, blank=False)
    edition = models.CharField(max_length=255, blank=False)

    year = models.IntegerField('year',
                               choices=YEAR_CHOICES,
                               default=datetime.datetime.now().year)

    pages = models.IntegerField(blank=False, null=False)

    condition = models.CharField('condition',
                                 max_length=10,
                                 choices=CONDITION,
                                 default='choose condition')

    shelf_location = models.CharField('shelf_location',
                                      max_length=100,
                                      choices=SHELF_LOCATION,
                                      default='choose location')

    notes = models.TextField()
    copies = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, null=False)
    ISBN = models.CharField(max_length=255, null=False)
