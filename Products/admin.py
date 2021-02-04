from django.contrib import admin

# Register your models here.
from Products.models import ProductModel, AddtoCartModel

admin.site.register(ProductModel)
admin.site.register(AddtoCartModel)
