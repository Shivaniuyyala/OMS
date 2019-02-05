from django.conf.urls import include, url
from order.views import *

urlpatterns = [

    url('order/', include(([
        url('view_all_order_history/$', ViewAllOrders.as_view(), name='all_orders_history'),
        url('create_order/$', create_order, name='create_order'),
        url('view_order_items/(?P<order_id>\d+)/$', viewOrderDetails, name='view_order_items'),
        url('cancel_order/(?P<order_id>\d+)/$', cancel_order, name='cancel_order'),
    ], 'order'), namespace='order')),
]