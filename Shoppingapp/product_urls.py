from django.conf.urls import include, url
from django.views.generic import TemplateView
from Shoppingapp import views
from ShoppingCart import settings
from django.conf.urls.static import static

product_urlpattern = [
    url(r'^add-review/', 'Shoppingapp.product.add_review',name='add_review'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)