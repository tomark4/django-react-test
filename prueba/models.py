from django.db import models
from django.contrib.auth.models import User
# comment in model
# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Entrada(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    categories = models.ManyToManyField(Categoria)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


