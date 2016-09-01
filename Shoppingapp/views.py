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
from ShoppingCart.settings import MEDIA_ROOT, MEDIA_URL

def home(request):
    try:
        user_name = request.session['first_name']
    except Exception, e:
        print e     
        user_name = ''
    category_list = Category.objects.filter(category_status=1)
    brand_list = Brand.objects.filter(brand_status=1)
    product_list = ProductDetail.objects.filter(product_status=1)
    return render(request,'index.html',{'media_root': MEDIA_ROOT, 'media_url': MEDIA_URL,'product_list':product_list,'user_name':user_name,'category_list':category_list,'brand_list':brand_list})

def blog(request):
    try:
        user_name = request.session['first_name']
    except Exception, e:
        print e     
        user_name = ''    
    return render(request, 'blog.html',{'user_name': user_name})

def cart(request):
    try:
        user_name = request.session['first_name']
    except Exception, e:
        print e     
        user_name = ''   
    return render(request, 'cart.html',{'user_name': user_name})

def checkout(request):
    try:
        user_name = request.session['first_name']
    except Exception, e:
        print e     
        user_name = ''   
    return render(request, 'checkout.html',{'user_name': user_name})

def contact(request):
    try:
        user_name = request.session['first_name']
    except Exception, e:
        print e     
        user_name = ''   
    return render(request, 'contact-us.html',{'user_name': user_name})        

def product(request):
    try:
        user_name = request.session['first_name']
    except Exception, e:
        print e     
        user_name = ''   
    return render(request, 'product-details.html',{'user_name': user_name})

def shop(request):
    try:
        user_name = request.session['first_name']
    except Exception, e:
        print e     
        user_name = ''
    category_list = Category.objects.filter(category_status=1)
    brand_list = Brand.objects.filter(brand_status=1)
    product_list = ProductDetail.objects.filter(product_status=1)       
    return render(request, 'shop.html',{'media_root': MEDIA_ROOT, 'media_url': MEDIA_URL,'product_list':product_list,'user_name':user_name,'category_list':category_list,'brand_list':brand_list})    

def product_detail(request):
    try:
        user_name = request.session['first_name']
    except Exception, e:
        print e     
        user_name = ''

    category_list = Category.objects.filter(category_status=1)
    brand_list = Brand.objects.filter(brand_status=1)
    product_list = ProductDetail.objects.filter(product_status=1)       
    product_obj = ProductDetail.objects.get(product_detail_id=request.GET.get('product_id'))       
    review_list = ProductReviews.objects.filter(product_id=request.GET.get('product_id'))
    return render(request, 'product-details.html',{'review_list':review_list,'product_list':product_list,'brand_list':brand_list,'category_list':category_list,'user_name': user_name,'product_obj':product_obj})    

def blog_single(request):
    try:
        user_name = request.session['first_name']
    except Exception, e:
        print e     
        user_name = ''   
    return render(request, 'blog-single.html',{'user_name': user_name})     

def page_not_found(request):
    try:
        user_name = request.session['first_name']
    except Exception, e:
        print e     
        user_name = ''   
    return render(request, '404.html',{'user_name': user_name})      

def signin(request):
    try:
        user_name = request.session['first_name']
    except Exception, e:
        print e     
        user_name = ''   
	return render(request, 'login.html',{'user_name': user_name})      
