# Create your views here.
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


def home(request):
    category_list = Category.objects.filter(category_status=1)
    brand_list = Brand.objects.filter(brand_status=1)
    return render(request,'index.html',{'category_list':category_list,'brand_list':brand_list})

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact-us.html')        

def product(request):
    return render(request, 'product-details.html')

def shop(request):
    return render(request, 'shop.html')    

def product_detail(request):
    return render(request, 'product-details.html')    

def blog_single(request):
    return render(request, 'blog-single.html')     

def page_not_found(request):
    return render(request, '404.html')      

def login(request):
	return render(request, 'login.html')      
