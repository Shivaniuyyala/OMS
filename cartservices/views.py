# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, redirect
from django.contrib import messages
from cartservices.cart import Cart
from product.models import Product
from member.decorators import login_required


@login_required
def add_to_cart(request, product_id, quantity=1):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    try:
        cart.add(product, quantity)
    except:
        pass
    return redirect('product:view_all_products')

@login_required
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    try:
        cart.remove(product)
    except:
        pass
    return redirect('product:view_all_products')


@login_required
def get_cart(request):
    cart = Cart(request)
    is_empty = False
    if not cart.count():
        is_empty = True
    return render(request, 'view_cart.html', {"cart": cart, 'is_empty': is_empty})