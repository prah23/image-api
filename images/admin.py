from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Image)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', '_id', 'status', 'slug')
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(models.Category)