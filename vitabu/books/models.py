from __future__ import unicode_literals

import datetime

from django.db import models


CONDITION = (
    ('New', 'New'),
    ('Good', 'Good'),
    ('Old', 'Old'),
    )

SHELF_LOCATION = (
    ('1A', '1A'),
    ('1B', '1B'),
    ('1C', '1C'),
    )

class Book(models.Model):

    YEAR_CHOICES = [(r, r)
                    for r in range(1984, datetime.date.today().year + 1)]

    title = models.CharField(max_length=50)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField(blank=True, null=True, help_text='dd/mm/yy')
    author = models.CharField(max_length=255, blank=True)
    editor = models.CharField(max_length=255, blank=True)
    edition = models.CharField(max_length=255, blank=True)

    year = models.IntegerField('year',
                               choices=YEAR_CHOICES,
                               default=datetime.datetime.now().year)

    pages = models.IntegerField(blank=True, null=True)

    condition = models.CharField('condition',
                                  max_length=10,
                                  choices=CONDITION,
                                  default='choose condition')

    shelf_location = models.CharField('shelf_location', 
                                       max_length=10, 
                                       choices=SHELF_LOCATION, 
                                       default='choose location')

    notes = models.TextField()
    copies = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
