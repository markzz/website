from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.package_index, name='package-index'),
    url(r'^(?P<os>[a-z]+)/(?P<repo>[a-z]+)', views.repository, name='repo-index'),
]
