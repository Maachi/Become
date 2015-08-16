from django.db import models
from locations.models import City

#IdentificationType
#This class defines the different types of participant 
class Type(models.Model):
	name = models.CharField(max_length=100)
	active = models.BooleanField(default=True, db_index=True)

	def __unicode__(self):
		return self.name


class Email(models.Model):
	#Reference name
	name = models.CharField(max_length=100, blank=True, null=True)
	email = models.CharField(max_length=200)

	def __unicode__(self):
		return self.email


class Client (models.Model):
	#There are only two types of users, let's keep the relation if we need to add more types
	type = models.ForeignKey(Type)
	name = models.CharField(max_length=100, blank=True, null=True)
	last_name = models.CharField(max_length=100, blank=True, null=True)
	identification_number = models.CharField(max_length=200, blank=True, null=True)
	emails = models.ManyToManyField(Email, blank=True)
	# If the client is a company 
	company_name = models.CharField(max_length=100, blank=True, null=True)
	company_identification_number = models.CharField(max_length=200, blank=True, null=True)
	# Common and required information
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=20)
	cell_phone = models.CharField(max_length=20, blank=True, null=True)
	city = models.ForeignKey(City, blank=True, null=True)
	# Creation date
	date = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return self.name

	def _client_name(self):
		if self.type.pk == 1:
			return self.company_name
		return self.name + " " + self.last_name

	client_name = property(_client_name)
