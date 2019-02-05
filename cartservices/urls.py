from django.conf.urls import include, url
from cartservices.views import *

urlpatterns = [

    url('cart/', include(([
        url('view_cart/$', get_cart, name='view_cart'),
        url('add_to_cart/(?P<product_id>\d+)/$', add_to_cart, name='add_to_cart'),
        url('remove_from_cart/(?P<product_id>\d+)/$', remove_from_cart, name='remove_from_cart'),
    ], 'cart'), namespace='cart')),
]