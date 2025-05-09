from django.contrib import admin
from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'slug', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'location',
                    'is_published', 'pub_date', 'created_at')
    list_filter = ('category', 'location', 'is_published')
    search_fields = ('title', 'text')
    list_editable = ('is_published',)
    date_hierarchy = 'pub_date'
