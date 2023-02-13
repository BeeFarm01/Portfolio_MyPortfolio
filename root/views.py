from django.views.generic import TemplateView
from blog.models import Blog
from resume.models import Education, WorkedHistory, Skills
from contact.forms import ContactForm
from about.models import AboutMe, AboutScroll
from header.models import Navigation, Hero


class IndexPage(TemplateView): 
     template_name = 'index.html'

     def get_context_data(self, **kwargs): 
          context = super().get_context_data(**kwargs)
          context["blog_list"] = Blog.objects.all()
          context["education_list"] = Education.objects.all()
          context["work_history_list"] = WorkedHistory.objects.all()
          context["skills_list"] = Skills.objects.all()
          context["contact_form"] = ContactForm()
          context["about_me"] = AboutMe.objects.first()
          context["about_scroll"] = AboutScroll.objects.all()
          context["navigation"] = Navigation.objects.first()
          context["hero"] = Hero.objects.first()
          


          return context
     


