from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True, allow_unicode=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published  = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    visits = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title

    def is_publicado(self):
        if self.published == True:
            return f"Publicado"
        else:
            return f"El libro no ha sido publicado"

    @property
    def full_name_author(self):
        return f"{self.author.first_name} {self.author.last_name}"

    @property
    def email_author(self):
        return self.author.email

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)
        self.slug = slugify(f"{self.title}-{str(self.id)}")
        super(Book, self).save(*args, **kwargs)

