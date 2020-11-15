from django.contrib import admin
from .models import Book, Category
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title",'slug',"created_at","author_full_name","email_author",'is_publicado')
    readonly_fields = ("slug", "created_at", "updated_at")
    list_filter = ('author__email',)
    search_fields = ('title','slug','author__email')


    def author_full_name(self, obj):
        return obj.author.first_name + " " + obj.author.last_name

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
