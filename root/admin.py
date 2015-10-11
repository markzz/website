from django.contrib import admin

from .models import Page, SocialMediaButton

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    class Meta:
        model = Page

admin.site.register(Page, PageAdmin)


class SocialMediaButtonAdmin(admin.ModelAdmin):
    class Meta:
        model = SocialMediaButton

admin.site.register(SocialMediaButton, SocialMediaButtonAdmin)
