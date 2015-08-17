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
	con = user_session(request)
	con["client"] = Client.objects.get(pk=client_id)
	page = 'pages/create-invoice.html'
	con.update(csrf(request))
	return render_to_response(page, con)