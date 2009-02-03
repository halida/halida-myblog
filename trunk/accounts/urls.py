#!/usr/bin/env python
#-*-coding:utf-8-*-
# ---------------------------------
# version:  1.0
#
# create-time:      <2009/01/23 11:54:50>
# last-update-time: <halida 02/03/2009 20:35:42>
# ---------------------------------
# module : urls

from django.conf.urls.defaults import *

urlpatterns = patterns('accounts.views',
                       #账户操作
                       (r'^login/$','login'),
                       (r'^logout/$','logout'),
                       (r'^register/$','register'),

                       (r'^testlogin/$','test_login'),                       
                       )

