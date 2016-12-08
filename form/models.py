from django.db import models

# Create your models here.
class Contact(models.Model):
    subject = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)
    email = models.EmailField(null=True)
    telefon = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.subject
