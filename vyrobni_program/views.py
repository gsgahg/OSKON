from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product, Category, Picture
from django.template import loader



def index(request):
    list_of_categories = Category.objects.order_by('-pub_date')[:27]
    template = loader.get_template('vyrobni_program/vyrobni_program.html')
    context = {'list_of_categories': list_of_categories}
    return render(request, 'vyrobni_program/vyrobni_program.html', context)



def detail(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
        listofpictures = Picture.objects.filter(category_id=category_id)

    except Category.DoesNotExist:
        raise Http404('Category does not exist')
    return render(request, 'vyrobni_program/detail.html',
    {'category': category,
    'listofpictures': listofpictures})
