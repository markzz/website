from django.db import models

# Create your models here.


class Arch(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False, blank=False)
    agnostic = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PackageType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    operating_system = models.CharField(max_length=50, null=False, blank=False)
    codename = models.CharField(max_length=50, null=False, blank=True)
    library = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.codename,)


class Repository(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    package_type = models.ForeignKey(PackageType)
    arches = models.ManyToManyField(Arch)
    location = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return '%s - %s' % (self.name, self.package_type.codename,)


class Package(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    repo = models.ForeignKey(Repository)
    arch = models.ForeignKey(Arch)
    description = models.TextField()
    pkgver = models.CharField(max_length=255, null=False, blank=False)
    pkgrel = models.IntegerField()
    updated = models.DateField()
    download = models.URLField()

    def __str__(self):
        return '%s %s-%d' % (self.name, self.pkgver, self.pkgrel,)
