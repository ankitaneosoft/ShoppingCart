"""ShoppingCart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from User.urls import user_urlpattern

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include(user_urlpattern)),    
    url(r'^$', 'Shoppingapp.views.home',name='home'),
    url(r'^home/', 'Shoppingapp.views.home',name='home'),
    url(r'^blog/', 'Shoppingapp.views.blog',name='blog'),
    url(r'^cart/', 'Shoppingapp.views.cart',name='cart'),
    url(r'^checkout/', 'Shoppingapp.views.checkout',name='checkout'),
    url(r'^contact/', 'Shoppingapp.views.contact',name='contact'),
    url(r'^product/', 'Shoppingapp.views.product',name='product'),
    url(r'^shop/', 'Shoppingapp.views.shop',name='shop'),
    url(r'^product-details/', 'Shoppingapp.views.product_detail',name='product_detail'),
    url(r'^blog-single/', 'Shoppingapp.views.blog_single',name='blog_single'),
    url(r'^page-not-found/', 'Shoppingapp.views.page_not_found',name='page_not_found'),
    url(r'^signin/', 'Shoppingapp.views.signin',name='signin'),
]