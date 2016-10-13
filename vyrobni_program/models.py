from django.db import models
from ckeditor.fields import RichTextField
from django.utils.encoding import python_2_unicode_compatible


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    short_description = models.CharField(max_length=250, null=True, blank=True)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    long_description = RichTextField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField()
    description2 = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.title

class Picture(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True, unique=True)
    picture = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    popis = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return str(self.name)
