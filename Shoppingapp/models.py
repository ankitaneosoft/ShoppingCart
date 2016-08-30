from django.db import models
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
#from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control
from django.contrib import auth
from django.db import models
#from constants import AppUserConstants, ExceptionLabel
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import datetime
# importing mysqldb and system packages

# Create your models here.
status = (
    ('1','1'),
    ('0','0'),
    
)


class Customer(User):
    customer_id			=       models.AutoField(primary_key=True, editable=False)
    customer_first_name =       models.CharField(max_length=45,null=True,blank=True)
    customer_last_name  =       models.CharField(max_length=45,null=True,blank=True)
    customer_email      =       models.CharField(max_length=45,null=True,blank=True)
    customer_status		=       models.CharField(max_length=1,default="1",choices=status)
    created_date       	=       models.DateTimeField(null=True,blank=True,default=datetime.datetime.now())
    fb_token			=       models.CharField(max_length=100,null=True,blank=True)
    twitter_token		=       models.CharField(max_length=100,null=True,blank=True)
    google_token		=       models.CharField(max_length=100,null=True,blank=True)

    def __unicode__(self):
    	return unicode(self.customer_id)


class Category(models.Model):
    category_id         =       models.AutoField(primary_key=True, editable=False)
    category_name       =       models.CharField(max_length=45,null=True,blank=True)
    created_date        =       models.DateTimeField(null=True,blank=True,default=datetime.datetime.now())
    category_status     =       models.CharField(max_length=1,default="1",choices=status)

    def __unicode__(self):
        return unicode(self.category_id)


class Brand(models.Model):
    brand_id         =       models.AutoField(primary_key=True, editable=False)
    brand_name       =       models.CharField(max_length=45,null=True,blank=True)
    created_date     =       models.DateTimeField(null=True,blank=True,default=datetime.datetime.now())
    brand_status     =       models.CharField(max_length=1,default="1",choices=status)

    def __unicode__(self):
        return unicode(self.brand_id)
