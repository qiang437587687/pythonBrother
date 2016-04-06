from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import date
from blog.models import *
# 在urls 里面进行绑定  之后 启动服务器 console python3 manage.py runserver

def hello(request, number):
    return HttpResponse('<h1>Hello Zhang: %s</h1>' % number)
    # return render(request, 'hello.html')


def hello1(request):
    name = 'handabao'
    age = 18
    # return HttpResponse('<h1>Hello Zhang: %s</h1>' % number)
    return render(request, 'hello.html', locals()) # 按照 价值对的形式 传入这个函数全部的变量


def index(request):
    d = date.today()
    articles = Article.objects.all()
    return render(request, 'index.html', locals())
