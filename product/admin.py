# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from product.models import *


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id', 'product_description', 'availability', 'stock', 'created_on', 'updated_on')


class ProductDescriptionAdmin(admin.ModelAdmin):
    model = ProductDescription
    list_display = ('id', 'description', 'brand', 'weight', 'name', 'updated_on', 'created_on',)


class ProductBrandAdmin(admin.ModelAdmin):
    model = ProductBrand
    list_display = ('internal_name', 'name', 'slug', 'updated_on', 'created_on',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDescription, ProductDescriptionAdmin)
admin.site.register(ProductBrand, ProductBrandAdmin)
