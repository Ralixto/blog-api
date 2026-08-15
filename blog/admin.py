from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Post, Comment

admin.site.register(User, UserAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'published']

admin.site.register(Category)
admin.site.register(Comment)