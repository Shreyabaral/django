from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Authors,blogPost


# Create your views here.
class index(ListView):
    context_object_name = 'blogpost'
    model = blogPost
    template_name = 'Blog/blogpost_list.html/'

class authors(DetailView):
    context_object_name = 'authors'
    model = Authors
    template_name = 'Blog/author_detail.html/'