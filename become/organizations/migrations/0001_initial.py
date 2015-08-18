# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import organizations.models
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('clients', '0001_initial'),
        ('contracts', '0001_initial'),
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('account_number', models.CharField(max_length=200, null=True, blank=True)),
                ('is_main', models.BooleanField(default=False, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('identification_number', models.CharField(max_length=200, null=True, blank=True)),
                ('photo', models.FileField(default=None, null=True, upload_to=organizations.models.upload_photo_to, blank=True)),
                ('is_owner', models.BooleanField(default=False, db_index=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('identification_number', models.CharField(max_length=200, unique=True, null=True, blank=True)),
                ('society_name', models.CharField(max_length=200, null=True, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('bank_accounts', models.ManyToManyField(to='organizations.BankAccount', blank=True)),
                ('clients', models.ManyToManyField(to='clients.Client', blank=True)),
                ('contracts', models.ManyToManyField(to='contracts.Contract', blank=True)),
                ('invoices', models.ManyToManyField(to='invoices.Invoice', blank=True)),
                ('members', models.ManyToManyField(to='organizations.Member', blank=True)),
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
            model_name='bankaccount',
            name='type',
            field=models.ForeignKey(blank=True, to='organizations.Type', null=True),
        ),
    ]
