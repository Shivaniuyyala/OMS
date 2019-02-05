# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import  post_save
from django.db import models
from order.models import BaseClass


class ProductBrand(BaseClass):
    internal_name = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(_("Slug Name"), db_index=True, blank=True, null=True, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return "%s" % str(self.name)


class ProductDescription(BaseClass):
    id = models.AutoField(_("ProductDescription ID"), primary_key=True, editable=False)
    description = models.TextField(_("Description of product"), default='', blank=True)
    brand = models.ForeignKey(ProductBrand, blank=True, null=True, related_name="productdesc_brand")
    weight = models.CharField(_("Weight of product"), max_length=25, null=True, blank=False)
    name = models.CharField(_("Full Name"), max_length=255, blank=False)

    def __unicode__(self):
        brand_name = self.brand.name if self.brand else ''
        return "%s %s %s" % (brand_name, self.name, self.weight)


class Product(BaseClass):
    PRODUCT_AVAILABLE = 1
    PRODUCT_OUT_OF_STOCK = 2
    PRODUCT_UNAVAILABLE = 3

    PRODUCT_AVAILABILITY_CHOICES = (
        (PRODUCT_AVAILABLE, 'Available'),
        (PRODUCT_OUT_OF_STOCK, 'Out Of Stock'),
        (PRODUCT_UNAVAILABLE, 'Not Available')
    )

    PRODUCT_AVAILABILITY_CHOICES_DICT = dict(PRODUCT_AVAILABILITY_CHOICES)

    id = models.AutoField(_("Product ID"), primary_key=True, editable=False)
    product_description = models.ForeignKey(ProductDescription, related_name='productproductdesc')
    availability = models.IntegerField(choices=PRODUCT_AVAILABILITY_CHOICES, blank=True, default=2)
    stock = models.IntegerField(default=0, blank=True)

    def __unicode__(self):
        return "%s" % str(self.id)

    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.availability = Product.PRODUCT_OUT_OF_STOCK
        elif not self.availability == Product.PRODUCT_AVAILABLE:
            self.availability = Product.PRODUCT_AVAILABLE
        super(Product, self).save(*args, **kwargs)

