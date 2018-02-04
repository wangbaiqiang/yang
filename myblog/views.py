from django.shortcuts import render
from django.http import HttpResponse
from myblog.apps import MyblogConfig
# Create your views here.
def index(request):

    return HttpResponse('nihao world')