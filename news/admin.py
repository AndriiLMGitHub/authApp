from django.contrib import admin
from news.models import PostNew

from .models import PostNew, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment, CommentAdmin)
# Register your models here.
admin.site.register(PostNew)
