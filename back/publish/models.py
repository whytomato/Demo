from django.db import models


class Author(models.Model):
    username = models.CharField("name", max_length=100)
    password = models.CharField("password", max_length=20)

# Create your models here.
