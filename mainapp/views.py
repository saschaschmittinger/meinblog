from django.shortcuts import render
from django.views import generic  



class BlogContent_view(generic.TemplateView):
    template_name = 'blog/index.html'
 

