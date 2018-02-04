# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#我们只需要创建一个类继承 models.Model就可以实现类 orm对数据的映射
class Article(models.Model):
    # 有的版本可能需要 __unicode__(self):
    def __str__(self):
        return self.userName
    # 属性对应的数据库字段是可以传参数的，参数可选和可不选 这里的参数是必选的
    userName=models.CharField(max_length=32, default='title')
    content=models.TextField(null=True)