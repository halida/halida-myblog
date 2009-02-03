#!/usr/bin/env python
#-*-coding:utf-8-*-
# ---------------------------------
# create-time:      <2009/01/23 14:51:28>
# last-update-time: <halida 02/03/2009 20:35:00>
# ---------------------------------
# 
from django import http
from django.shortcuts import render_to_response,get_object_or_404
from django.forms.models import modelformset_factory
from django.http import Http404
import django.contrib.auth 
import django.contrib.auth.views

def message(request,msg):
    return render_to_response('accounts_message.html',
                              {'message':msg})    

def login(request):
    return django.contrib.auth.views.login(request,template_name="accounts_login.html")

def logout(request):
    django.contrib.auth.logout(request)
    next = request.REQUEST['next']
    if next<>None:
        return http.HttpResponseRedirect(next)
    else:
        return message(request,"用户已登出!")

def register(request):
    return message(request,"暂时不开启注册功能.")

def test_login(request):
    if request.user.is_authenticated():
        result = "user exists!"
    else:
        result = "not login!"
    message(request,result)
    
