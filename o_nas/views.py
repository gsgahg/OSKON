from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Gallery

def index(request):
    template = loader.get_template('o_nas/index.html')
    context = {}
    return render(request, 'o_nas/index.html', context)

def kontakt(request):
    template=loader.get_template('o_nas/kontakt.html')
    context = {}
    return render(request, 'o_nas/kontakt.html', context)

def about(request):
    template=loader.get_template('o_nas/about.html')
    context = {}
    return render(request, 'o_nas/about.html', context)

def galerie(request):
    list_of_images = Gallery.objects.order_by('-pub_date')
    template=loader.get_template('o_nas/galerie.html')
    context = {'list_of_images': list_of_images}
    return render(request, 'o_nas/galerie.html', context)
