from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Gallery, Reference
from form.models import Contact
from form.forms import ContactForm
from django.contrib import messages

def index(request):
    template = loader.get_template('o_nas/index.html')
    context = {}
    return render(request, 'o_nas/index.html', context)

def kontakt(request):
    template = loader.get_template('o_nas/kontakt.html')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            messages.success(request, 'Thank you for your message.')
            return HttpResponseRedirect('/kontakt/')
    else:
        form = ContactForm()
    context = {'form':form}
    return render(request, 'o_nas/kontakt.html', context)





def galerie(request):
    list_of_images = Gallery.objects.order_by('-pub_date')
    template=loader.get_template('o_nas/galerie.html')
    context = {'list_of_images': list_of_images}
    return render(request, 'o_nas/galerie.html', context)

def reference(request):
    list_of_references = Reference.objects.order_by('-pub_date')
    template=loader.get_template('o_nas/reference.html')
    context = {"list_of_references": list_of_references}
    return render(request, 'o_nas/reference.html', context)
