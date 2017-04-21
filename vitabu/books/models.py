from __future__ import unicode_literals

import datetime

from django.db import models


class Book(models.Model):

    YEAR_CHOICES = [(r, r)
                    for r in range(1984, datetime.date.today().year + 1)]

    title = models.CharField(max_length=50)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True)
    editor = models.CharField(max_length=255, blank=True)
    edition = models.CharField(max_length=255, blank=True)
    year = models.IntegerField('year',
                               choices=YEAR_CHOICES,
                               default=datetime.datetime.now().year)
    pages = models.IntegerField(blank=True, null=True)
    condition = models.CharField(max_length=255)
    shelf_location = models.CharField(max_length=50)
    notes = models.TextField()
