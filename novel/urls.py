# -*- coding:utf-8 -*-
from django.conf.urls import url
from novel import views
#相当于子路径 r'^index/$' 这里的／很重要不然会找不到
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^detail/$', views.detail),
    url(r'^article/$', views.article),
    url(r'^articles/$', views.articles),
    #正则表达式来表示传参的id值 与值绑定 注：这个名字要和我们在views.py中写的参数名保持相同
    # http://127.0.0.1:8000/novel/article_page/1 网页只要传数字即可
    url(r'^article_page/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page,name='edit_page'),
    url(r'^edit/action$', views.edit_action,name='edit_action'),
]