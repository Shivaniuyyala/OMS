# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from member.decorators import login_required
from django.utils.decorators import method_decorator
from product.models import *


class ViewAllProducts(ListView):
    template_name = 'view_all_products.html'

    @login_required
    def get_context_data(self, **kwargs):
        return super(ViewAllProducts, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        products_list = Product.objects.all()
        total_products = products_list.count()
        paginator = Paginator(products_list, 2)

        page = request.GET.get('page')
        products = []
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            products = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            products = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'products': products, 'total_products': total_products,
                                                    'message': "products not found" if not
        products else ""})



