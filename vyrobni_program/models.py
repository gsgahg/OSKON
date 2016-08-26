from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    short_description = models.CharField(max_length=250, null=True, blank=True)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    long_description = models.CharField(max_length=5000, null=True, blank=True)

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
    picture = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
