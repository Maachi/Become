from django.db import models
from clients.models import Client
from contracts.models import Contract
from django.contrib.auth.models import User
from invoices.utils import number_to_letter
from datetime import datetime

#The type is important since if there is a significant change in the invoice we are going to replicate
# the Invoice information. 
class Type(models.Model):
	name = models.CharField(max_length=100)
	active = models.BooleanField(default=True, db_index=True)

	def __unicode__(self):
		return self.name

#Invoice status
class Status(models.Model):
	name = models.CharField(max_length=100)
	active = models.BooleanField(default=True, db_index=True)

	def __unicode__(self):
		return self.name


#The Filed is the numeric represention when the invoice is finished
class File(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateTimeField(blank=True, null=True)
	file_id = models.IntegerField(default=0, blank=True, null=True)
	#Reference of the organization
	organization_id = models.IntegerField(default=0, blank=True, null=True)
	# Override save to generate and keep the file updated
	def save(self, *args, **kwargs):
		if self.organization_id:
			count = 1
			try:
				count = File.objects.filter(organization_id=self.organization_id).count()
				count = count+1
			except File.DoesNotExist:
				count = 1
			from organizations.models import Organization
			organization = Organization.objects.get(pk=self.organization_id)
			organization_name = organization.name
			self.name = "Invoice " + organization_name + " Number " + str(count)
			self.file_id = count
		self.date = datetime.now()
		super(File, self).save(*args, **kwargs)

	def __unicode__(self):
		return unicode(self.name)


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

	# Override save for the project to add special dato to the register
	def save(self, *args, **kwargs):
		if not self.id:
			self.status = Status.objects.get(pk=1)
		if not self.type:
			self.type = Type.objects.get(pk=1)
		super(Invoice, self).save(*args, **kwargs)

	#Get the member associated with the invoice
	def _member(self):
		from organizations.models import Member
		return Member.get_member_with_user(self.owner)

	#Get the member associated with the invoice
	def _calculate_tax(self):
		tax = 0
		return tax

	def _calculate_total(self):
		total = 0
		return total

	def _value_letters(self):
		return unicode(number_to_letter.to_word(int(self.value), 'COP')).upper()

	def _invoice_number(self):
		file = self.file
		file_number = 0
		if file:
			file_number = file.file_id
		return file_number

	value_letters = property(_value_letters)
	owner_member = property(_member)
	number = property(_invoice_number)
	tax = property(_calculate_tax)
	total = property(_calculate_total)
	

#The log represents when the user changes the model or admin perform a change to the status
class InvoiceLog(models.Model):
	action = models.CharField(max_length=200)
	user = models.ForeignKey(User, blank=True, null=True, default=None)
	invoice = models.ForeignKey(Invoice, blank=True, null=True, default=None)
	date = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return unicode(self.action)