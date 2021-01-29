from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog_category(models.Model):

    class Meta:
        verbose_name_plural = 'blog Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    url = models.SlugField(max_length=200, unique=True)

    teaser = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    blog_category = models.ForeignKey('blog_category', null=True, blank=True, on_delete=models.SET_NULL)

    image = models.FileField(default="", null=True, blank=True, upload_to='articles/img')
    additionalImages = models.FileField(default="", null=True, blank=True, upload_to='articles/additional')

    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title