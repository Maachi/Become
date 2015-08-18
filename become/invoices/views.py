from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.template.loader import get_template
from django.template import Context, Template
from django.views.decorators.csrf import csrf_exempt
from organizations.views import *
from invoices.models import *
from organizations.views import *
from clients.models import *
from locations.models import *
from datetime import datetime


def create_invoice(request, client_name, client_id):
	if not request.user.is_authenticated():
		return redirect_to_member_home(request)
	invoice = save_invoice(request, client_id)
	if invoice and request.method == 'POST':
		return HttpResponseRedirect("/clients/"+client_name+"/"+client_id+"/")
	con = user_session(request)
	con["client"] = Client.objects.get(pk=client_id)
	page = 'pages/create-invoice.html'
	con.update(csrf(request))
	return render_to_response(page, con)



def view_invoice(request, client_name, client_id, invoice_id):
	if not request.user.is_authenticated():
		return redirect_to_member_home(request)
	con = user_session(request)
	con["client"] = Client.objects.get(pk=client_id)
	con["invoice"] = Invoice.objects.get(pk=invoice_id)
	page = 'pages/invoice.html'
	con.update(csrf(request))
	return render_to_response(page, con)


def save_invoice(request, client_id):
	invoice  = None
	organization = Organization.objects.filter(members__id=request.user.pk)[:1][0]
	if request.method == 'POST':
		client = Client.objects.get(pk=client_id)
		invoice = Invoice()
		if request.POST['value']:
			invoice.value = request.POST['value']
		if request.POST['sales_tax']:
			invoice.sales_tax = request.POST['sales_tax']
		if request.POST['description']:
			invoice.description = request.POST['description']
		invoice.creation_date = datetime.now()
		if request.POST['contract']:
			invoice.contract = Contract.objects.get(pk=request.POST['contract'])
		invoice.client = client
		invoice.owner = request.user
		invoice.save()
		organization.invoices.add(invoice)
	return invoice