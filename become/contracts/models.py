from django.db import models
from django.contrib.auth.models import User
from clients.models import *
import hashlib
import time
import os


def upload_file_to(instance, filename):
	name, extension = os.path.splitext(filename)
	encoded_name = hashlib.md5(str(time.time())).hexdigest() + extension
	return os.path.join("uploads/contracts/%s" % hashlib.md5(str(instance.id)).hexdigest(), encoded_name)


class Contract (models.Model):
	name = models.CharField(max_length=100)
	client = models.ForeignKey(Client, blank=True, null=True)
	creation_date = models.DateTimeField(blank=True, null=True)
	description = models.TextField(blank=True, null=True, default=None)
	contract_file = models.FileField(upload_to=upload_file_to, blank=True, null=True, default=None)
	owner = models.ForeignKey(User, blank=True, null=True, default=None)

	from_date = models.DateTimeField(blank=True, null=True)
	to_date = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return self.name
