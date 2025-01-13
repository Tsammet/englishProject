from django.contrib import admin
from .models import Category, Words

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    ordering = ('id',)


class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'word', 'meaning')
    search_fields = ('word',)
    ordering = ('id',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Words, WordAdmin)