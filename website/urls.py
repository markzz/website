# website URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/1.8/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# Including another URLconf
#     1. Add an import:  from blog import urls as blog_urls
#     2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))

from django.conf.urls import include, url
from django.contrib import admin

import website.settings as settings

urlpatterns = [
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', 'root.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'packages/', include('repos.urls')),
    url(r'^home/', 'root.views.home', name='home'),
    url(r'^add/$', 'root.views.add', name='page-add'),
    url(r'^edit/$', 'root.views.edit_index', name='index-edit'),
    url(r'^(?P<path>[a-zA-Z0-9]+)/$', 'root.views.page', name='page'),
    url(r'^(?P<path>[a-zA-Z0-9]+)/edit/$', 'root.views.edit', name='page-edit'),
]

