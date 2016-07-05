# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.
def index(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'index.html', {'post_list' : post_list})

def post_detail(request, post_title):
    post_list = Article.objects.all()
    for post in post_list:
        if post.title == post_title:
            return render(request, 'post.html', {'post': post})
        else:
            pass
def about(request):
    return render(request,'about.html')