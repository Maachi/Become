from django.contrib import admin
from locations.models import *

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	list_display = ['name']
	search_fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	list_display = ['name']
	search_fields = ['name']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	list_display = ['name']
	search_fields = ['name', 'city__name', 'country__name']