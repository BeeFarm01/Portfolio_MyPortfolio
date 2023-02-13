from django.db import models

# Create your models here.


class AboutMe (models.Model):
    icon = models.ImageField(upload_to= "media/about/", null= True, blank=True)
    title = models.TextField(max_length=1000)
    discription = models.TextField(null = True, blank= True)

class AboutScroll (models.Model):
    icon = models.ImageField(upload_to= "media/resume/")
    title = models.CharField(max_length=250, null= True, blank=True)
    about_work = models.TextField(max_length=1000)

