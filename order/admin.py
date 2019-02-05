# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from order.models import *


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('order_id', 'user', 'status', 'user_comment', 'admin_comment', 'created_on',
                    'updated_on')
    filter_horizontal = ('items',)


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ('id', 'product', 'quantity', 'updated_on', 'created_on',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
