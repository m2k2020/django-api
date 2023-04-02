from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.TextField(max_length=100)
    author = models.TextField(max_length=100)


