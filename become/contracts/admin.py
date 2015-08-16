from django.contrib import admin
from contracts.models import *

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
	list_display = ('name', 'client')
	search_fields = ['name', 'client__name']