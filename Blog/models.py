# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BlogEntry(models.Model):
    entryDate = models.DateField(auto_created=True)
    entryTitle = models.CharField(max_length=500)
    entryText = models.TextField()

    def __str__(self):
        return self.entryTitle
