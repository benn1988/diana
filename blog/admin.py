from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """
    Changing the template for the post edit on the admin page
    """
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['content', 'author', 'date_posted']})
    ]
    list_display = ['title', 'author', 'date_posted', 'date_updated']
    list_filter = ['date_posted', 'date_updated']
    search_fields = ['content', 'title']


admin.site.register(Post, PostAdmin)
