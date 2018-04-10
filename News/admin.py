#coding:utf8
from django.contrib import admin

# Register your models here.
from News.models import *     #导入

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','author','date']
    search_fields = ['author','title']
admin.site.register(News,NewsAdmin)