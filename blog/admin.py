from django.contrib import admin
from .models import Post, Category
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','status',)
    readonly_fields = ('created_at','updated_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('created_at','updated_at',)

