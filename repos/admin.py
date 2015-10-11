from django.contrib import admin

from .models import *

# Register your models here.


class ArchAdmin(admin.ModelAdmin):
    class Meta:
        model = Arch


class PackageTypeAdmin(admin.ModelAdmin):
    class Meta:
        model = PackageType


class RepositoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Repository


class PackageAdmin(admin.ModelAdmin):
    class Meta:
        model = Package

admin.site.register(Arch, ArchAdmin)
admin.site.register(PackageType, PackageTypeAdmin)
admin.site.register(Repository, RepositoryAdmin)
admin.site.register(Package, PackageAdmin)