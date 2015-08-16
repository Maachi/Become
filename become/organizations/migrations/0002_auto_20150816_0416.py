# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import organizations.models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='users',
        ),
        migrations.AddField(
            model_name='member',
            name='is_owner',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AddField(
            model_name='member',
            name='photo',
            field=models.FileField(default=None, null=True, upload_to=organizations.models.upload_photo_to, blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(to='organizations.Member', blank=True),
        ),
    ]
