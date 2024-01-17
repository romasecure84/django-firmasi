from django.http import Http404
from django.shortcuts import render
from .fake_db.products import FAKE_DB_PRODUCTS

def product_list_view(request):
    page_title = 'Products'
    context = dict(
        page_title = page_title,
        products = FAKE_DB_PRODUCTS,
    )
    return render(request, 'product/products.html', context)

def product_detail_view(request, id):
    #page_title = 'Product'
    result = list(filter(lambda x:(x['id'] == id), FAKE_DB_PRODUCTS))
    if result:
        context = dict(
            page_title = 'Product_id',
            item = result[0],
            products=FAKE_DB_PRODUCTS,
            detail= result[0]['detail'],
        )
        return render(request, 'product/product_detail.html', context)
    raise Http404