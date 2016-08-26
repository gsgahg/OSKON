from django.db import models

class Gallery(models.Model):
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
