# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_auto_20150527_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='subtitle',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
    ]
