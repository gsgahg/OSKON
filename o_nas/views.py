from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('o_nas/index.html')
    context = {}
    return render(request, 'o_nas/index.html', context)

def kontakt(request):
    template=loader.get_template('o_nas/kontakt.html')
    context = {}
    return render(request, 'o_nas/kontakt.html', context)

def galerie(request):
    template=loader.get_template('o_nas/galerie.html')
    context = {}
    return render(request, 'o_nas/galerie.html', context)
