#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns,url

urlpatterns = patterns('blog.views',
    url(r'^bloglist/$', 'blog_list', name='bloglist'),
    url(r'^(?P<id>\d+)/$', 'blog_show', name='detailblog'),
    url(r'^tag/(?P<id>\d+)/$', 'blog_filter', name='filtrblog'),
    url(r'^add/$', 'blog_add', name='addblog'),
    url(r'^(?P<id>\w+)/update/$', 'blog_update',name='updateblog'),
    url(r'^(?P<id>\w+)/del/$', 'blog_del', name='delblog'),
    url(r'^(?P<id>\d+)/commentshow/$', 'blog_show_comment', name='showcomment'),
)

urlpatterns += patterns('blog.views',
    url(r'^foo/$','foobar',{'template':'foo.html'}),
    url(r'^bar/$','testform',{'template':'bar.html'}),
)