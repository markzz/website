from django.shortcuts import render

from root.views import gen_navbar, is_admin
from root.models import Page, SocialMediaButton

from .models import *

# Create your views here.


def package_index(request):
    navbar = gen_navbar()
    package_page = Page.objects.get(name='packages')
    social_media = SocialMediaButton.objects.all()

    operating_systems = PackageType.objects.all().distinct()
    repositories = Repository.objects.all()

    if package_page.header_image[0] == '&':
        package_page.header_image = package_page.header_image[1:]
    else:
        package_page.header_image = "url('%s');" % (package_page.header_image,)

    return render(request, 'rindex.html', locals())


def repository(request, os, repo):
    navbar = gen_navbar()
    package_page = Page.objects.get(name='packages')
    social_media = SocialMediaButton.objects.all()
    packages = Package.objects.filter(repo=Repository.objects.get(package_type=PackageType.objects.filter(codename=os))).filter(repo=Repository.objects.get(name=repo))

    package_page.title = repo
    package_page.subtitle = os[0].upper() + os[1:] + ' Repository'

    if package_page.header_image[0] == '&':
        package_page.header_image = package_page.header_image[1:]
    else:
        package_page.header_image = "url('%s');" % (package_page.header_image,)

    return render(request, 'repo.html', locals())