# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import contracts.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(null=True, blank=True)),
                ('description', models.TextField(default=None, null=True, blank=True)),
                ('contract_file', models.FileField(default=None, null=True, upload_to=contracts.models.upload_file_to, blank=True)),
                ('from_date', models.DateTimeField(null=True, blank=True)),
                ('to_date', models.DateTimeField(null=True, blank=True)),
                ('client', models.ForeignKey(blank=True, to='clients.Client', null=True)),
                ('owner', models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
