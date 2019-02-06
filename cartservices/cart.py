import datetime
from cartservices.models import *

CART_ID = 'CART-ID'


class ItemAlreadyExists(Exception):
    pass


class ItemDoesNotExist(Exception):
    pass


class CartServices:
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = Cart.objects.get(id=cart_id, checked_out=False)
            except Cart.DoesNotExist:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def new(self, request):
        cart = Cart(creation_date=datetime.datetime.now())
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product, quantity=1):
        try:
            item = Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except Item.DoesNotExist:
            item = Item()
            item.cart = self.cart
            item.product = product
            if product.stock >= item.quantity:
                item.quantity = quantity
            else:
                pass
            item.save()
        else: #ItemAlreadyExists
            item.quantity += int(quantity)
            item.save()

    def remove(self, product):
        try:
            item = Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except Item.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()

    def update(self, product, quantity):
        try:
            item = Item.objects.get(
                cart=self.cart,
                product=product,
            )
        except Item.DoesNotExist:
            raise ItemDoesNotExist
        else: #ItemAlreadyExists
            if quantity == 0:
                item.delete()
            else:
                item.quantity = int(quantity)
                item.save()

    def count(self):
        result = 0
        for item in self.cart.item_set.all():
            result += 1 * item.quantity
        return result

    def clear(self):
        for item in self.cart.item_set.all():
            item.delete()

