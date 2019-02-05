# -*- coding: utf-8 -*-
import django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from member.models import User
import datetime


class BaseClass(models.Model):
    created_on = models.DateTimeField(editable=False, default=datetime.datetime.now)
    updated_on = models.DateTimeField(editable=False, auto_now=True)
    created_by = models.ForeignKey(User, editable=False, blank=True, null=True,
                                   related_name="%(class)s_created_by")
    updated_by = models.ForeignKey(User, editable=False, blank=True, null=True,
                                   related_name="%(class)s_updated_by")

    class Meta:
        abstract = True

    @classmethod
    def table_name(cls):
        return cls._meta.db_table


class OrderItem(BaseClass):
    product = models.ForeignKey("product.Product")
    quantity = models.IntegerField(default=1)


class Order(BaseClass):
    SUBMITTED = 1
    IN_PROGRESS = 2
    COMPLETE = 3
    CANCELLED = 4
    ORDER_STATUS = (
        (SUBMITTED, 'Submitted'),
        (IN_PROGRESS, 'In-progress'),
        (COMPLETE, 'Complete'),
        (CANCELLED, 'Cancelled'),)

    ORDER_STATUS_DICT = dict(ORDER_STATUS)

    order_id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User)
    status = models.IntegerField(default=1, choices=ORDER_STATUS)
    items = models.ManyToManyField(OrderItem, blank=True, editable=False)
    user_comment = models.TextField(blank=True, null=True)
    admin_comment = models.TextField(blank=True, null=True)

    def get_order_status(self):
        order_status_dict = Order.ORDER_STATUS_DICT
        return order_status_dict[self.status]

    def is_order_eligible_for_cancellation(self):
        if self.status in [Order.SUBMITTED, Order.IN_PROGRESS]:
            return True
        return False

