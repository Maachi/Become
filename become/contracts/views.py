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


def create_contract(request, client_name, client_id):
	if not request.user.is_authenticated():
		return redirect_to_member_home(request)
	contract = save_contract(request, client_id)
	if contract and request.method == 'POST':
		return HttpResponseRedirect("/clients/"+client_name+"/"+client_id+"/")
	con = user_session(request)
	con["client"] = Client.objects.get(pk=client_id)
	page = 'pages/create-contract.html'
	con.update(csrf(request))
	return render_to_response(page, con)


def save_contract(request, client_id):
	contract  = None
	personal = None
	company_email = None
	organization = Organization.objects.filter(members__id=request.user.pk)[:1][0]
	if request.method == 'POST':
		client = Client.objects.get(pk=client_id)
		contract = Contract()
		if request.POST['name']:
			contract.name = request.POST['name']
		contract.client = client
		contract.creation_date = datetime.now()
		if request.POST['description']:
			contract.description = request.POST['description']
		if request.POST['from_date']:
			contract.from_date = datetime.strptime(request.POST['from_date'], '%m/%d/%Y').date()
		if request.POST['to_date']:
			contract.to_date = datetime.strptime(request.POST['to_date'], '%m/%d/%Y').date() 
		contract.owner = request.user
		contract.save()
		organization.contracts.add(contract)
		if request.FILES:
			if "contract_file" in request.FILES:
				contract.contract_file = request.FILES["contract_file"]
				contract.save()
	return contract

