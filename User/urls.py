from django.conf.urls import include, url
from django.views.generic import TemplateView
from Shoppingapp import views
from ShoppingCart import settings
from django.conf.urls.static import static

user_urlpattern = [
    url(r'^signup/', 'User.views.signup',name='signup'),
    url(r'^signout/', 'User.views.sign_out',name='sign_out'),
    url(r'^signin/', 'User.views.signin',name='signin'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)