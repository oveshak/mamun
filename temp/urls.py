from django.urls import path

from temp.views import CheckOut, Index, Shop, SinglePage, add_to_cart

urlpatterns = [
    path('',Index.as_view(),name='index'),
path('shop/',Shop.as_view(),name='shop'),
   path('checkout/',CheckOut.as_view(),name='checkout'),
path('single-product/<slug>/',SinglePage.as_view(), name='single-product'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
]