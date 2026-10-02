from django.contrib import admin
from .models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'category', 'author', 'is_featured']
    list_editable=['is_featured']
    search_fields = (
        'id',
        'title',
        'author__username',
        'status',
        'category__category_name',
    )

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)