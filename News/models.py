#coding:utf8
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    date = models.DateField()
    content = models.TextField()
    src = models.CharField(max_length=64)
    delete_flag = models.CharField(max_length=4)

class User(models.Model ):
    user = models.CharField(max_length=32)
    password = models.CharField( max_length=32)