from django.db import models

# Create your models here.
class Navigation (models.Model):
    icon = models.ImageField(upload_to= "media/navigation/", null= True, blank=True)
    home = models.TextField(max_length=1000)
    about = models.TextField(max_length=1000)
    portfolio = models.TextField(max_length=1000)
    blog = models.TextField(max_length=1000)
    dropdown = models.TextField(max_length=1000, null= True, blank=True)
    contact = models.TextField(max_length=1000)
    

class Hero (models.Model):
    heroImg = models.ImageField(upload_to= "media/hero/")
    intro = models.CharField(max_length=250)
    skill1 = models.TextField(max_length=1000)
    skill2 = models.TextField(max_length=1000, null= True, blank=True)