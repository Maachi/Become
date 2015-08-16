from django.contrib import admin
from clients.models import *

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
	list_display = ['name']


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	search_fields = ['name', 'email']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ('name', 'last_name', 'identification_number')
	search_fields = ['name', 'company_name']