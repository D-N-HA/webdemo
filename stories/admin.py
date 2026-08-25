from django.contrib import admin
from .models import Category, Story

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'views', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')

