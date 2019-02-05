# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from member.models import *


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('id', 'email', 'is_active', 'is_staff', 'is_superuser', 'is_member', 'date_joined')

admin.site.register(User, UserAdmin)

