# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arch',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('agnostic', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('pkgver', models.CharField(max_length=255)),
                ('pkgrel', models.IntegerField()),
                ('updated', models.DateField()),
                ('download', models.URLField()),
                ('arch', models.ForeignKey(to='repos.Arch')),
            ],
        ),
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('operating_system', models.CharField(max_length=50)),
                ('codename', models.CharField(blank=True, max_length=50)),
                ('library', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=255)),
                ('arches', models.ManyToManyField(to='repos.Arch')),
                ('package_type', models.ForeignKey(to='repos.PackageType')),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='repo',
            field=models.ForeignKey(to='repos.Repository'),
        ),
    ]
