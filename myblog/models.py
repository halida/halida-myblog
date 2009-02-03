#!/usr/bin/env python
#-*-coding:utf-8-*-
# ---------------------------------
# create-time:      <2009/01/23 14:51:28>
# last-update-time: <halida 01/24/2009 19:06:31>
# ---------------------------------
# 
from django.db import models
import django.forms
from django.forms import ModelForm
from django.contrib.auth.models import User
#from tinymce.widgets import TinyMCE

TITLE_MAX_LENGTH = 100
NAME_MAX_LENGTH = 20

class Blog(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    desc = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.name

class Article(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.title

#form
class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'desc')
        
class ArticleForm(ModelForm):
    #text = django.forms.CharField(widget=TinyMCE())#attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Article
        fields = ('title','text')
