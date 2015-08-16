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
from clients.models import *
from locations.models import *
from datetime import datetime


def create_client(request):
	save_client(request)
	con = user_session(request)
	con["type_clients"] = Type.objects.filter(active=True);
	con["cities"] = City.objects.filter(active=True);
	page = 'pages/create-client.html'
	con.update(csrf(request))
	return render_to_response(page, con)


def save_client(request):
	client = None
	personal = None
	company_email = None
	if request.method == 'POST':
		organization = Organization.objects.filter(members__id=request.user.pk)[:1][0]
		print organization
		client = Client()
		if request.POST['type']:
			client.type = Type.objects.get(pk=int(request.POST['type'])) 
		if request.POST['name']:
			client.name = request.POST['name']
		if request.POST['last_name']:
			client.last_name = request.POST['last_name']
		if request.POST['identification_number']:
			client.identification_number = request.POST['identification_number']
		if request.POST['company_name']:
			client.company_name = request.POST['company_name']
		if request.POST['company_identification_number']:
			client.company_identification_number = request.POST['company_identification_number']
		if request.POST['address']:
			client.address = request.POST['address']
		if request.POST['phone']:
			client.phone = request.POST['phone']
		if request.POST['cell_phone']:
			client.cell_phone = request.POST['cell_phone']
		if request.POST['city']:
			client.city = City.objects.get(pk=int(request.POST['city']))
		if request.POST['client_email']:
			personal = Email()
			personal.name = "Personal email"
			personal.email = request.POST['client_email']
			personal.save()
		if request.POST['client_company_email']:
			company_email = Email()
			company_email.name = "Company email"
			company_email.email = request.POST['client_company_email']
			company_email.save()
		client.date = datetime.now()
		client.save()
		if personal:
			client.emails.add(personal)
		if company_email:
			client.emails.add(company_email)
		organization.clients.add(client)
	return client