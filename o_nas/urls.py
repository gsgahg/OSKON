from django.conf.urls import url

from . import views

app_name = 'o_nas'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
    url(r'^galerie/$', views.galerie, name='galerie'),
    url(r'^reference/$', views.reference, name='reference'),
]
