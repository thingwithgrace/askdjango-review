# blog/admin.py
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ['make_published']

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{} sucessfully marked as published'.format(updated_count))
    make_published.short_description = 'Mark selected stories as published'

    list_display = ['id', 'title', 'content', 'status']

    def content_size(self, post):
        return '{}글자'.format(len(post))
    content_size.short_description = '내용 글자수'