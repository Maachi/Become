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
from organizations.models import *
import time

#Displays the index page for all type of users not login required 
def index (request):
	if request.user.is_authenticated():
		return redirect_to_member_home(request)
	else :
		return HttpResponseRedirect("/login/")

def login_page(request):
	authenticate_user_to_system(request)
	if request.user.is_authenticated():
		return redirect_to_member_home(request)
	auth_hash = str(time.time())
	con = {
		"auth_hash" : auth_hash,
	}
	page = 'pages/login.html'
	con.update(csrf(request))
	return render_to_response(page, con)


def user_session(request):
	organizations = []
	member = None
	try:
		member = Member.objects.get(pk=request.user.pk)
	except ObjectDoesNotExist:
		member = []
	try:
		organizations = Organization.objects.filter(members__id=request.user.pk)
	except ObjectDoesNotExist:
		organizations = []
	return {
		"member" : member,
		"organizations" : organizations,
	}


def dashboard(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/login/")
	con = user_session(request)
	page = 'pages/dashboard.html'
	con.update(csrf(request))
	return render_to_response(page, con)


def logout_request(request):
	if request.user.is_authenticated():
		logout(request)
	return redirect_to_member_home(request)



def authenticate_user_to_system(request):
	user = None
	if request.method == 'POST':
		if len(request.POST['user']) < 30:
			user = authenticate(username=request.POST['user'], password=request.POST['password'])
		else :
			user = authenticate(username=request.POST['user'][:20], password=request.POST['password'])
			#if not user.email.index(request.POST['user']):
				#user = None
		#This will validate the user user the user identification id cc, nit, etc
		if not user:
			try:
				#Try the login with user's identification number
				if request.POST['user']:
					#if is_number(request.POST['user']):
					member = Member.objects.get(identification_number=request.POST['user'])
					user = authenticate(username=member.username, password=request.POST['password'])
			except ObjectDoesNotExist:
				user = None

		if user is not None:
			if user.is_active:
				login(request, user)
				if request.POST.get('remember', None):
					#The session will expire in 5 years
					request.session.set_expiry(31536000)
	return user


def redirect_to_member_home(request):
	return HttpResponseRedirect("/dashboard/")