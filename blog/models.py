from django.db import models

# Create your models here.
class Blog(models.Model):
	icon = models.ImageField(upload_to = "media/blog/")
	name = models.CharField(max_length = 200)
	published_date = models.DateField()
	author_name = models.CharField(max_length = 200, blank = True, null = True)
	category = models.CharField(max_length = 200, blank = True, null = True)
	slug = models.SlugField()
	content = models.TextField()


