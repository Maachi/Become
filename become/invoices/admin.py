from django.contrib import admin
from invoices.models import *

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
	list_display = ('client', 'status')
	search_fields = ['client__name']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
	list_display = ['name']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
	list_display = ['name']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
	list_display = ['name']

@admin.register(InvoiceLog)
class InvoiceLogAdmin(admin.ModelAdmin):
	list_display = ['action']