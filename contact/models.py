from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length = 255, null = True, blank= True)
    message = models.TextField(max_length=1000)

    