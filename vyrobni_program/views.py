from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product
from django.template import loader



def index(request):
    latest_products = Product.objects.order_by('-pub_date')[:27]
    template = loader.get_template('vyrobni_program/vyrobni_program.html')
    context = {'latest_products': latest_products}
    return render(request, 'vyrobni_program/vyrobni_program.html', context)


def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404('Product does not exist')
    return render(request, 'vyrobni_program/detail.html',
    {'product': product})
