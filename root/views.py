from datetime import datetime as dt
import re
import os

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect, render

from .forms import PageForm
from .models import Page, SocialMediaButton

# Create your views here.


def is_admin(user):
    return user.is_staff or user.is_superuser


def check_body_for_execute(text):
    matches = re.findall(r'@execute (.*?) @execute', text, re.I|re.DOTALL)

    for m in matches:
        text = text.replace('@execute %s @execute' % (m,),
                            '%s' % (os.popen(m).read()))

    return text


def gen_navbar(extras=[]):
    # this function generates the navbar at the top of the page
    pages = Page.objects.all().exclude(name='').exclude(name='blog')

    nav_objects = ['home', 'blog']
    for p in pages:
        nav_objects.append('%s' % (p.name,))
    nav_objects = nav_objects + extras

    return nav_objects


def index(request):
    navbar = gen_navbar()
    page_content = Page.objects.get(name='')
    social_media = SocialMediaButton.objects.all()

    if page_content.header_image[0] == '&':
        page_content.header_image = page_content.header_image[1:]
    else:
        page_content.header_image = "url('%s');" % (page_content.header_image,)

    page_content.body = check_body_for_execute(page_content.body)

    return render(request, 'page.html', locals())


@user_passes_test(is_admin)
def edit_index(request):
    navbar = gen_navbar()
    page_edit = PageForm(request.POST or None, instance=Page.objects.get(name=''))
    social_media = SocialMediaButton.objects.all()

    if page_edit.is_valid():
        print("IM HERE")
        edited_page = page_edit.save(commit=False)
        edited_page.edited = dt.now()
        edited_page.save()

        return HttpResponseRedirect('/')

    return render(request, 'edit.html', locals())


def page(request, path):
    navbar = gen_navbar()
    page_content = Page.objects.get(name=path)
    social_media = SocialMediaButton.objects.all()

    if page_content.header_image[0] == '&':
        page_content.header_image = page_content.header_image[1:]
    else:
        page_content.header_image = "url('%s');" % (page_content.header_image,)

    return render(request, 'page.html', locals())


@user_passes_test(is_admin)
def edit(request, path):
    navbar = gen_navbar()
    page_edit = PageForm(request.POST or None, instance=Page.objects.get(name=path))
    social_media = SocialMediaButton.objects.all()

    if page_edit.is_valid():
        edited_page = page_edit.save(commit=False)
        edited_page.edited = dt.now()
        edited_page.save()

        return HttpResponseRedirect('/%s/' % (edited_page.name,))

    return render(request, 'edit.html', locals())


@user_passes_test(is_admin)
def add(request):
    navbar = gen_navbar()
    page_edit = PageForm(request.POST or None)

    if page_edit.is_valid():
        added_page = page_edit.save(commit=False)
        added_page.edited = dt.now()
        added_page.save()

        return HttpResponseRedirect('/%s/' % (added_page.name,))

    return render(request, 'edit.html', locals())

def home(request):
    return HttpResponseRedirect('/')
