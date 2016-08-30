from django.contrib import admin
from Shoppingapp.models import *
# Register your models here.
admin.site.register(Customer);
admin.site.register(Category);
admin.site.register(Brand);
admin.site.register(Product);
admin.site.register(ProductDetail);