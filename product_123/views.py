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
def add_review(request):
	try:
		review_obj = ProductReviews(
		product_id = Product.objects.get(product_id=request.POST.get('email')),	
		user_name = request.POST.get('name'),
		user_email = request.POST.get('email'),
		user_review = request.POST.get('review')
		)
		review_obj.save()
		data = {
		'success': 'true',
		'message': 'Your review have been added successfully'
		}

	except Exception, e:
		print e		
		data = {
		'success': 'false',
		'message': 'Error in adding reviews'
		}
	return HttpResponse(json.dumps(data), content_type='application/json')
