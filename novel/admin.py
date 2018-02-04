# coding:utf-8
from django.contrib import admin
from models import Article
# Register your models here.
admin.site.site_header = "文章管理"
admin.site.register(Article)