from django.contrib import admin
from .models import Article 

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'teaser', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'teaser': ('title',)}
  
class CategoryAdmin (admin.ModelAdmin):
    list_display = (
        'blog_category',
        'title',
        'image',
    )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Blog_category, CategoryAdmin)