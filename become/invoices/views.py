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


def create_invoice(request):
	con = user_session(request)
	page = 'pages/create-invoice.html'
	con.update(csrf(request))
	return render_to_response(page, con)