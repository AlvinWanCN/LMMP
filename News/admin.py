#coding:utf8
from django.contrib import admin

# Register your models here.
from News.models import *     #导入

admin.site.register(News)