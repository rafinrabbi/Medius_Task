from django.urls import path
from django.views.generic import TemplateView
from django.db.models import Q

from product.views.product import CreateProductView
from product.views.variant import VariantView, VariantCreateView, VariantEditView

from .models import *

app_name = "product"

from django.shortcuts import render

def product_list(request):
    # 
    product = Product.objects.all()
    product_and_pvps = []

    serial = 1
    for p in product:
        # product_variant = ProductVariant.objects.filter(product = p)
        product_var_price = ProductVariantPrice.objects.filter(product = p)
        dp  ={
            "serial":serial,
            "product":p,
            "pvps":product_var_price
        }
        serial+=1
        product_and_pvps.append(dp)

    print(product_and_pvps)
   
    return render(request, 'products/list.html', {'product_and_pvps': product_and_pvps})

urlpatterns = [
    path('list/', product_list,  name='list.product'),
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    # path('list/', TemplateView.as_view(template_name='products/list.html', extra_context={
    #     'product': Product.objects.all(), 'variant': Variant.objects.all(), 'product_variant': ProductVariant.objects.all()
    # }), name='list.product'),
]
