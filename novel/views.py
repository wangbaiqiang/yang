# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import models


def index(request):
    # 在这里调用model 然后render渲染 到我们的模版html上面 通过第三个参数传递
    return render(request, 'novel/index.html', {'hello': 'hello Blog'})


def detail(request):
    return render(request, 'novel/detail/detail.html', {'zhenyu': 'woshiwuzhenyu'})


def article(request):
    article = models.Article.objects.get(pk=1)
    return render(request, 'novel/article.html', {'article': article})


def articles(request):
    # 这里返回的是 集合对象 queryset
    articles = models.Article.objects.all()
    return render(request, 'novel/articles.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'novel/article_page.html', {'article': article})


# 编辑界面
def edit_page(request, article_id):
    if (str(article_id) == '0'):
        return render(request, 'novel/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'novel/edit_page.html', {'article': article})


# edit的表单action
def edit_action(request):
    userName = request.POST.get('userName', 'USERNAME')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        models.Article.objects.create(userName=userName, content=content)
        articles = models.Article.objects.all()
        return render(request, 'novel/articles.html', {'articles': articles})
    else:
        # 这里就是更新数据库，实际操作的就是对象
        article = models.Article.objects.get(pk=article_id)
        article.userName = userName
        article.content = content
        article.save()
        return render(request, 'novel/article_page.html', {'article': article})
