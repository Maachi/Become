from django.contrib import admin
from organizations.models import *

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
	list_display = ['identification_number']
	search_fields = ['identification_number']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
	list_display = ['name']
	search_fields = ['name']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
	list_display = ['name']
	search_fields = ['name']


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
	list_display = ['name']
	search_fields = ['name']