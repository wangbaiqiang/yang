# coding:utf-8
"""yang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from novel import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 配置novel app的url来管理自己的url映射
    url(r'^novel/', include('novel.urls',namespace='novel')),
    #这里要用到views 而不是在''字符串中 如果是字符串的化 上面的包也会是灰色的说明我们没有用到该函数
    url(r'^$', views.index),
]
