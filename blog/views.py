from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog

# Create your views here.
class BlogListView(ListView):
    queryset = Blog.objects.all()
    template_name = "blog_list.html"
    model = Blog
