# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(max_length=100, null=True, blank=True)),
                ('identification_number', models.CharField(max_length=200, null=True, blank=True)),
                ('company_name', models.CharField(max_length=100, null=True, blank=True)),
                ('company_identification_number', models.CharField(max_length=200, null=True, blank=True)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('cell_phone', models.CharField(max_length=20, null=True, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('city', models.ForeignKey(blank=True, to='locations.City', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True, db_index=True)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='emails',
            field=models.ManyToManyField(to='clients.Email', blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='type',
            field=models.ForeignKey(to='clients.Type'),
        ),
    ]
