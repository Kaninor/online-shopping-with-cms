from django.contrib import admin
from .models import Product
from .adminModels import ProductAdminModel

admin.site.register(Product, ProductAdminModel)
