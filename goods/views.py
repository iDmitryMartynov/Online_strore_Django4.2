from django.shortcuts import render

from .models import Products


def catalog(request):
    goods = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_id):
    product = Products.objects.get(id=product_id)

    context = {
        'product': product
    }

    return render(request, "goods/product.html", context)
