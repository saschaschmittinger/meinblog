from django.contrib import admin
from .models import BlogContentModel


class BlogContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}

admin.site.register(BlogContentModel, BlogContentAdmin)