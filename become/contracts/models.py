from django.db import models
from clients.models import *

class Contract (models.Model):
	name = models.CharField(max_length=100)
	client = models.ForeignKey(City, blank=True, null=True)
	creation_date = models.DateTimeField(blank=True, null=True)
	description = models.TextField(blank=True, null=True, default=None)

	from_date = models.DateTimeField(blank=True, null=True)
	to_date = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return self.name
