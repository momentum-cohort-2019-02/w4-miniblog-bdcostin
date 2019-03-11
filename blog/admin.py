from django.contrib import admin
from blog.models import BlogPost, Topic, Author, Comment
# Register your models here.

# admin.site.register(BlogPost)
# admin.site.register(Topic)
# admin.site.register(Author)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_topic')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


