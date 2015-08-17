# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import contracts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contracts', '0002_auto_20150817_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_file',
            field=models.FileField(default=None, null=True, upload_to=contracts.models.upload_file_to, blank=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='owner',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
