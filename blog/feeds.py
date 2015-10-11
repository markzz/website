from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.html import strip_tags as st
from .models import Post

def truncate_words(content, length=100, suffix='...'):
  if len(content) <= length:
    return content
  else:
    return content[:length].rsplit(' ',1)[0] + suffix

class PostFeed(Feed):
  title = "Mark Weiman's Blog"
  link = "/blog/"
  description = "Changes on new post"
  
  def items(self):
    return Post.objects.order_by('-created')
  
  def item_title(self, item):
    return item.title
  
  def item_description(self, item):
    return truncate_words(st(item.body))
  
  def item_link(self, item):
    return 'https://markzz.com/blog/post/' + str(item.id)
