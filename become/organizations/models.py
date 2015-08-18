from django.db import models
from invoices.models import Invoice
from clients.models import Client
from contracts.models import Contract
from django.contrib.auth.models import User, AbstractUser
import hashlib
import time
import os


def upload_photo_to(instance, filename):
	name, extension = os.path.splitext(filename)
	encoded_name = hashlib.md5(str(time.time())).hexdigest() + extension
	return os.path.join("uploads/members/%s" % hashlib.md5(str(instance.id)).hexdigest(), encoded_name)


class Member(User):
	identification_number = models.CharField(max_length=200, blank=True, null=True)
	photo = models.FileField(upload_to=upload_photo_to, blank=True, null=True, default=None)
	is_owner = models.BooleanField(default=False, db_index=True)

	@staticmethod
	def get_member_with_user(user):
		try:
			member = Member.objects.get(pk=user.pk)
			return member
		except Member.DoesNotExist:
			return None


class Type(models.Model):
	name = models.CharField(max_length=100)
	active = models.BooleanField(default=True, db_index=True)

	def __unicode__(self):
		return self.name


class BankAccount(models.Model):
	name = models.CharField(max_length=200, unique=True)
	account_number = models.CharField(max_length=200, blank=True, null=True)
	type = models.ForeignKey(Type, blank=True, null=True)
	is_main = models.BooleanField(default=False, db_index=True)

	def __unicode__(self):
		return self.name



class Organization (models.Model):
	name = models.CharField(max_length=200, unique=True)
	identification_number = models.CharField(max_length=200, unique=True, blank=True, null=True)
	society_name = models.CharField(max_length=200, blank=True, null=True)
	invoices = models.ManyToManyField(Invoice, blank=True)
	clients = models.ManyToManyField(Client, blank=True)
	contracts = models.ManyToManyField(Contract, blank=True)
	members = models.ManyToManyField(Member, blank=True)
	bank_accounts = models.ManyToManyField(BankAccount, blank=True)
	date = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return self.name
