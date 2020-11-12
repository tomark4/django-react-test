from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    STATUS = (
        ('published','Published'),
        ('draft','Draft')
    )

    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique_for_date='created_at')
    status = models.CharField(max_length=255, choices=STATUS)
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    postobjects = PostObjects()

    def __str__(self):
        return self.title

    class Meta():
        ordering = ("-created_at",)
        verbose_name = 'post'
        verbose_name_plural = 'posts'

