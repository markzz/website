# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_auto_20150527_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaButton',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=150)),
                ('account', models.CharField(max_length=150)),
                ('url', models.URLField(max_length=255)),
            ],
        ),
    ]
