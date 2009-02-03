#!/usr/bin/env python
#-*-coding:utf-8-*-
# ---------------------------------
# create-time:      <2009/01/23 14:51:28>
# last-update-time: <halida 02/03/2009 20:08:54>
# ---------------------------------
# 
from django import http
from testproject.myblog.models import *
from django.shortcuts import render_to_response,get_object_or_404
from django.forms.models import modelformset_factory
from django.http import Http404
from django.contrib.auth.decorators import login_required

TOP_ARTICLE_NUM = 10

def render_with_header(request,template,dict):
    """渲染页面头部的部分"""
    dict['islogin'] = request.user.is_authenticated()
    dict['username'] = request.user.username
    dict['next'] = request.path
    return render_to_response(template,dict)

def mainpage(request):
    return render_with_header(request,'myblog_mainpage.html',
                              {'message':'welcome to myblog!'})    

def message(request,message=None):
    """show message"""
    return render_with_header(request,'myblog_message.html',
                              {'message':message})

def show(request,blog_name,article_id=None):
    #find blog
    blog = get_object_or_404(Blog, name=blog_name)
    #query articles
    articles = Article.objects.filter(blog=blog)
    if not article_id:
        articles = articles.order_by('-create_time')[:TOP_ARTICLE_NUM]
    else:
        articles = articles.filter(pk=article_id)
    #show articles
    return render_with_header(request,'myblog_blog.html',
                              {'articles':articles,
                               'blog_name':blog_name})

def check_blog(request,name):
    """检查博客拥有者"""
    try:
        blog = Blog.objects.get(name=name)
        if blog.author.username != request.user.username:
            return message('这不是你的博客!')
    except Blog.DoesNotExist:
        blog = None
    return blog

@login_required
def manage_blog(request,blog_name=None):
    """博客管理"""
    #显示当前博客
    blogs = Blog.objects.filter(author=request.user)
    #新增博客
    if request.method == "POST":
        blog = check_blog(request,request.POST['name'])
        form = BlogForm(request.POST,instance=blog)
        #修改博客的人是当前用户
        form.instance.author = User.objects.get(username=request.user.username)
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect('/myblog/manage/')
    else:
        if blog_name==None:#建立博客
            form = BlogForm(initial={'desc':'这个人很懒,没有留下任何信息.'})
        else:#修改博客
            blog = get_object_or_404(Blog, name=blog_name)
            form = BlogForm(instance=blog)

    return render_with_header(request,'myblog_manage_blog.html',
                              {'blogs':blogs,
                               'form':form,})

@login_required
def delete_blog(request,blog_name,confirm):
    if confirm == "notconfirmed":
        return render_with_header(request,'myblog_delete.html',
                                  {'blog_name':blog_name})
    else:
        blog = check_blog(request,blog_name)
        blog.delete()
        return http.HttpResponseRedirect('/myblog/manage/')

def check_article(request,blog_name,article_id):
    """检查文章"""
    try:
        article = Article.objects.get(pk=article_id)
        if article.blog.name<>blog_name:
            return message('该文章不在博客:%s中!',blog_name)
    except Article.DoesNotExist:
        article = None
    return article

@login_required
def manage_article(request,blog_name,article_id=None):
    """博客管理"""
    #显示文章
    blog = check_blog(request,blog_name)
    if not blog:raise http.Http404
    articles = Article.objects.filter(blog=blog)
    articles = articles.order_by('-create_time')
    #新增文章
    if request.method == "POST":
        article = check_article(request,blog_name,article_id)
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.instance.blog = blog
            form.save()
            return http.HttpResponseRedirect('/myblog/%s/manage/' % blog_name)
    else:
        if article_id==None:#建立文章
            form = ArticleForm()
        else:#修改文章
            article = get_object_or_404(Article,pk=article_id)
            form = ArticleForm(instance=article)
    return render_with_header(request,'myblog_manage_article.html',
                              {'articles':articles,
                               'blog_name':blog_name,
                               'form':form,})

@login_required
def delete_article(request,blog_name,article_id,confirm):
    if confirm == "notconfirmed":
        return render_with_header(request,'myblog_delete.html',
                                  {'blog_name':blog_name,
                                   'article_id':article_id})
    else:
        article = check_article(request,blog_name,article_id)        
        article.delete()
        return http.HttpResponseRedirect('/myblog/%s/manage/' % blog_name)

