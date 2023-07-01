from django.db import models


class User(models.Model):
    username = models.CharField("name", max_length=100)
    password = models.CharField("password", max_length=20)

    class Meta:
        db_table = 'user'

# Create your models here.
