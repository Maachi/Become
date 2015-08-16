from django.db import models
from clients.models import Client
from contracts.models import Contract
from django.contrib.auth.models import User

#The type is important since if there is a significant change in the invoice we are going to replicate
# the Invoice information. 
class Type(models.Model):
	name = models.CharField(max_length=100)
	active = models.BooleanField(default=True, db_index=True)

	def __unicode__(self):
		return self.name

class Status(models.Model):
	name = models.CharField(max_length=100)
	active = models.BooleanField(default=True, db_index=True)

	def __unicode__(self):
		return self.name


#The Filed is the numeric represention when the invoice is finished
class File(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return unicode(self.id)


class Invoice(models.Model):
	#When the invoice is completed the system should generate the file
	file = models.ForeignKey(File, blank=True, null=True, default=None)
	#The type of invoice represents if is a copy, duplicate
	type = models.ForeignKey(Type, blank=True, null=True, default=None)
	#The status represents if the invonce is in progres deleted or completed
	status = models.ForeignKey(Status, blank=True, null=True, default=None)
	# This keeps the value of the invoce
	value = models.DecimalField(max_digits=20, decimal_places=5)
	sales_tax = models.DecimalField(max_digits=20, decimal_places=5)
	description = models.TextField(blank=True, null=True, default=None)
	owner = models.ForeignKey(User)
	creation_date = models.DateTimeField(blank=True, null=True)
	contract = models.ForeignKey(Contract, blank=True, null=True)
	#The client is just a short hand to identify the invoice and the client, the client information is also
	#keep by the contract information
	client = models.ForeignKey(Client, blank=True, null=True)
	completed = models.BooleanField(default=False, db_index=True)

	def __unicode__(self):
		return unicode(self.value)
	

#The log represents when the user changes the model or admin perform a change to the status
class InvoiceLog(models.Model):
	action = models.CharField(max_length=200)
	user = models.ForeignKey(User, blank=True, null=True, default=None)
	invoice = models.ForeignKey(Invoice, blank=True, null=True, default=None)
	date = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return unicode(self.action)