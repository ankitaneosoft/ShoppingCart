from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control
from django.contrib import auth
from Shoppingapp.models import *
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import pdb
from datetime import date, timedelta
import json
# Create your views here.

@csrf_exempt
def signup(request):
	try:
		user_obj = Customer(
		username = request.POST.get('email'),	
		customer_first_name = request.POST.get('name'),
		customer_email = request.POST.get('email')
		)
		user_obj.set_password(request.POST.get('password'))
		user_obj.save()
		#login(request,user)
		request.session['user_id'] = user_obj.customer_id
		request.session['first_name'] = user_obj.customer_first_name 
		data = {
		'success': 'true',
		}

	except Exception, e:
		print e		
		data = {
		'success': 'false',
		'message': 'User with same emailid already exists'
		}
	return HttpResponse(json.dumps(data), content_type='application/json')

def sign_out(request):
	request.session['user_id'] = ''
	request.session['first_name'] = '' 
	logout(request)
	return redirect('/home/')

@csrf_exempt
def signin(request):
	print '--------request--------',request.POST
	try:
		user = authenticate(username=request.POST.get('email'), password= request.POST.get('password'))
		print '----user-----',user
		if user is not None:
			cust_obj = Customer.objects.get(username=user)
			if cust_obj.customer_status=="1":
				request.session['user_id'] = cust_obj.customer_id
				request.session['first_name'] = cust_obj.customer_first_name 
				login(request,user)
				data= { 'success' : 'true'}
			else:
				data= { 'success' : 'false', 'message' :'User Is Not Active'}
		else:
			data= { 'success' : 'false', 'message' :'Invalid Username or Password'}

	except Exception, e:
		print 'Exception ', e
		data= { 'success' : 'false', 'message':'Invalid Username or Password'}
	print '------------data-------',data
	return HttpResponse(json.dumps(data), content_type='application/json')
