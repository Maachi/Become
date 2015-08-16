# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(null=True, blank=True)),
                ('description', models.TextField(default=None, null=True, blank=True)),
                ('from_date', models.DateTimeField(null=True, blank=True)),
                ('to_date', models.DateTimeField(null=True, blank=True)),
                ('client', models.ForeignKey(blank=True, to='locations.City', null=True)),
            ],
        ),
    ]
