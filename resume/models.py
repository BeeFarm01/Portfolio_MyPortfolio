from django.db import models

# Create your models here.
class Education (models.Model):
    icon = models.ImageField(upload_to = "media/resume/")
    level = models.CharField(max_length=250)
    passed_year = models.CharField(max_length=200)
    discription = models.TextField(null = True, blank= True)
    grade = models.CharField(max_length=200)


class WorkedHistory (models.Model):
    icon = models.ImageField(upload_to= "media/resume/")
    company_name = models.CharField(max_length=250)
    about_work = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_currently_working_here = models.BooleanField(default=False)

class Skills (models.Model):
    icon = models.ImageField(upload_to= "media/resume/")
    skill_name = models.CharField(max_length=250)
    about_skill = models.TextField(max_length=250)
    







