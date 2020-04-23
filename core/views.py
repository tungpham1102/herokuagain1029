import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import Product, Order


# Create your views here.


def simple_checkout(request):
    return render(request, 'simple_checkout.html')


def store(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store.html', context)


def checkout(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'checkout.html', context)


def complete(request):
    body = json.loads(request.body)
    print('BODY: ', body)
    product = Product.objects.get(id=body['productId'])
    Order.objects.create(
        product=product
    )
    return JsonResponse('Payment completed!', safe=False)
