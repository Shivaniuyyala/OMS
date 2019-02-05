from django.conf.urls import include, url
from product.views import *

urlpatterns = [

    url('product/', include(([
        url('view_all_products/$', ViewAllProducts.as_view(), name='view_all_products'),
    ], 'product'), namespace='product')),
]