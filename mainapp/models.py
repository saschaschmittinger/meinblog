from django.db import models


class BlogContentModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField(blank=True)
    image = models.ImageField(upload_to='images',default=False)
    
    class Meta:
        verbose_name_plural = 'Markdown content'
        
    def __str__(self):
        return self.title