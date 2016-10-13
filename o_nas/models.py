from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=128, unique=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField('date published', null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Reference(models.Model):
    name = models.CharField(max_length=128, unique=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
