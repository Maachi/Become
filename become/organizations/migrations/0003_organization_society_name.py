# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20150816_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='society_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
