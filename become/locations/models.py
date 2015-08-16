from datetime import datetime
from django.db import models

# Create your models here.

#Country
class Country(models.Model):
	
	class Meta:
			verbose_name_plural = "Countries"	
	name = models.CharField(max_length=100)
	register_date = models.DateTimeField()
	active = models.BooleanField(default=True, db_index=True)
	
	def __unicode__(self):
		return self.name


#City
class City(models.Model):
	class Meta:
		verbose_name_plural = "Cities"

	name = models.CharField(max_length=100)
	country = models.ForeignKey(Country)
	register_date = models.DateTimeField()
	active = models.BooleanField(default=True, db_index=True)
	geo_name_id = models.IntegerField(blank=True, null=True)
	latitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True, default=None)
	longitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True, default=None)


	def __unicode__(self):
		return self.name



#Location, the location model references a physical/non physical location
class Location(models.Model):
	class Meta:
		verbose_name_plural = "Locations"

	name = models.CharField(max_length=100, blank=True, null=True)
	city = models.ForeignKey(City, blank=True, null=True)
	country = models.ForeignKey(Country, blank=True, null=True)
	latitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True, default=None)
	longitude = models.DecimalField(max_digits=20, decimal_places=17, blank=True, null=True, default=None)
	active = models.BooleanField(default=True, db_index=True)

	def __unicode__(self):
		return self.name


	@staticmethod
	def get_location_query (latitude, longitude, distance, limit = 20):
		return 'SELECT *, ( 3959 * acos(cos( radians('+str(latitude)+')) * cos(radians( latitude )) \
		* cos( radians( longitude ) - radians(' + str(longitude) + ') ) + sin( radians('+str(latitude)+') ) * sin(radians(latitude)) ) ) AS distance\
		FROM locations_location\
		HAVING distance < '+str(distance)+' \
		ORDER BY distance\
		LIMIT 0 , '+str(limit)+';'


	@staticmethod
	#@param latitude 
	#@param logintude 
	#@param distance in miles 
	def near_locations(latitude, longitude, distance = 20):
		query = Location.get_location_query(latitude, longitude, distance)
		locations = []
		for location in Location.objects.raw(query):
			locations.append(location)
		return locations