# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class User(AbstractUser):
    is_member = models.BooleanField(blank=True, default=False)


    def __unicode__(self):
        return u'%s' % self.username


