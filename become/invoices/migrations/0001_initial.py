# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=20, decimal_places=5)),
                ('sales_tax', models.DecimalField(max_digits=20, decimal_places=5)),
                ('description', models.TextField(default=None, null=True, blank=True)),
                ('creation_date', models.DateTimeField(null=True, blank=True)),
                ('completed', models.BooleanField(default=False, db_index=True)),
                ('client', models.ForeignKey(blank=True, to='clients.Client', null=True)),
                ('contract', models.ForeignKey(blank=True, to='contracts.Contract', null=True)),
                ('file', models.ForeignKey(default=None, blank=True, to='invoices.File', null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=200)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('invoice', models.ForeignKey(default=None, blank=True, to='invoices.Invoice', null=True)),
                ('user', models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True, db_index=True)),
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
            model_name='invoice',
            name='status',
            field=models.ForeignKey(default=None, blank=True, to='invoices.Status', null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='type',
            field=models.ForeignKey(default=None, blank=True, to='invoices.Type', null=True),
        ),
    ]
