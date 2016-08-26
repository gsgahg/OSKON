from django.conf.urls import url

from . import views

app_name = 'vyrobni_program'
urlpatterns = [
    url(r'^$', views.index, name='vyrobni_program'),
    url(r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail'),
]
