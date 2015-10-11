from django.conf.urls import url

from .feeds import PostFeed

from . import views

urlpatterns = [
    # show blog overview
    url(r'^$', views.index, name='blog-index'),

    # view for blog post (/blog/#/)
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post, name='blog-post'),

    # edit blog post
    url(r'^post/(?P<post_id>[0-9]+)/edit/$', views.edit, name='blog-edit'),

    # create new post
    url(r'^new/$', views.new, name='blog-new'),

    url(r'^page/(?P<page>[0-9]+)/$', views.index_pages, name='blog-pages'),
    
    url(r'^feed/$', PostFeed()),
]
