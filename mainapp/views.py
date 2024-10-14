from django.shortcuts import render
from .models import BlogContentModel
from django.views import generic  




class BlogContent_view(generic.ListView):
    template_name = 'blog/index.html'
    queryset = BlogContentModel.objects.all() 
    context_object_name = 'blogContent'

