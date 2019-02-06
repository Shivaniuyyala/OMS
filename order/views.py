# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from member.decorators import login_required
from django.db import transaction
from django.contrib import messages
from order.models import *


class ViewAllOrders(ListView):
    template_name = 'view_order_history.html'

    @login_required
    def get_context_data(self, **kwargs):
        return super(ViewAllOrders, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        Orders_list = Order.objects.filter(user=request.user)
        paginator = Paginator(Orders_list, 2)

        page = request.GET.get('page')
        orders = []
        try:
            orders = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            orders = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            orders = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'orders': orders, 'message': "no order history found" if not
        orders else ""})



@login_required
def create_order(request):
    from cartservices.cart import CartServices
    from product.models import Product
    cart = CartServices(request)
    items_dict = dict(cart.cart.item_set.all().values_list('product', 'quantity'))
    try:
        with transaction.atomic():
            order = Order.objects.create(user=request.user)
            products = Product.objects.select_for_update().filter(id__in=items_dict.keys())
            for product in products:
                if product.stock >= items_dict[product.id]:
                    order.items.add(OrderItem.objects.create(product=product, quantity=items_dict[product.id]))
                    product.stock = product.stock - int(items_dict[product.id])
                    product.save()
        messages.success(request, "Order placed successfully")
    except:
        messages.error(request, "Error while placing order")
    cart.clear()
    return redirect("home")


@login_required
def viewOrderDetails(request, order_id):
    template_name = 'view_order_items.html'
    if request.method == "GET":
        order = Order.objects.get(order_id=order_id)
        items = order.items.all()
        return render(request, template_name, {'items': items})


@login_required
def cancel_order(request, order_id):
    from product.models import Product
    order = Order.objects.get(order_id=order_id)
    items_dict = dict(order.items.all().values_list('product', 'quantity'))
    try:
        with transaction.atomic():
            if not order.status == Order.CANCELLED:
                products = Product.objects.select_for_update().filter(id__in=items_dict.keys())
                for product in products:
                    product.stock = product.stock+items_dict[product.id]
                    product.save()
                order.status = Order.CANCELLED
                order.save()
        messages.success(request, "Order cancelled Successfully")
    except:
        messages.error(request, "Error while canceling order" )
    return redirect("home")




