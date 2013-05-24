from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newblog.views.home', name='home'),
    # url(r'^newblog/', include('newblog.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^newblog/', include('blog.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/home/wxj/workspace/newblog/static'}),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
