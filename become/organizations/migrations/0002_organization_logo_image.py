# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import organizations.models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='logo_image',
            field=models.FileField(default=None, null=True, upload_to=organizations.models.upload_logo_to, blank=True),
        ),
    ]
