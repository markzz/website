from datetime import datetime as dt

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import Http404, HttpResponseRedirect, render

from root.views import gen_navbar, is_admin
from root.models import Page, SocialMediaButton

from .forms import CommentForm, PostForm
from .models import Post, Comment

# Create your views here.


def index(request):
    navbar = gen_navbar()
    blog_page = Page.objects.get(name='blog')
    posts = Post.objects.order_by('-created')[:10]
    social_media = SocialMediaButton.objects.all()
    page = 1
    next = 2
    prev = 0

    if blog_page.header_image[0] == '&':
        blog_page.header_image = blog_page.header_image[1:]
    else:
        blog_page.header_image = "url('%s');" % (blog_page.header_image,)

    return render(request, 'index.html', locals())


def index_pages(request, page):
    navbar = gen_navbar()
    blog_page = Page.objects.get(name='blog')

    first = (int(page) - 1) * 10
    last = (int(page) - 1) * 10 + 10

    posts = Post.objects.order_by('-created')[first:last]
    social_media = SocialMediaButton.objects.all()
    next = int(page) + 1
    prev = int(page) - 1

    if blog_page.header_image[0] == '&':
        blog_page.header_image = blog_page.header_image[1:]
    else:
        blog_page.header_image = "url('%s')" % (blog_page.header_image,)

    return render(request, 'index.html', locals())


def post(request, post_id):
    navbar = gen_navbar()
    selected_post = Post.objects.get(id=post_id)
    social_media = SocialMediaButton.objects.all()

    if selected_post.header_image[0] == '&':
        selected_post.header_image = selected_post.header_image[1:]
    else:
        selected_post.header_image = "url('%s');" % (selected_post.header_image,)

    if not selected_post:
        raise Http404('Post not found!')

    if selected_post.comments_enabled:
        comments = Comment.objects.filter(post=selected_post).order_by('-timestamp')
        comment_form = CommentForm(request.POST or None)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.timestamp = dt.now()
            new_comment.post = selected_post
            new_comment.save()

            return HttpResponseRedirect('')

    return render(request, 'post.html', locals())


@user_passes_test(is_admin)
def new(request):
    navbar = gen_navbar()
    post_form = PostForm(request.POST or None)
    social_media = SocialMediaButton.objects.all()

    if post_form.is_valid():
        new_post = post_form.save(commit=False)
        new_post.user = request.user
        new_post.created = dt.now()
        new_post.save()

        return HttpResponseRedirect('/blog/post/%d/' % (new_post.id,))

    return render(request, 'edit-post.html', locals())


@user_passes_test(is_admin)
def edit(request, post_id):
    navbar = gen_navbar()
    post_form = PostForm(request.POST or None, instance=Post.objects.get(id=post_id))
    social_media = SocialMediaButton.objects.all()

    if post_form.is_valid():
        edited_post = post_form.save(commit=False)
        edited_post.edited = dt.now()
        edited_post.save()

        return HttpResponseRedirect('/blog/post/%d/' % (post_id,))

    return render(request, 'edit-post.html', locals())
