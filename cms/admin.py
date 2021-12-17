from django.contrib import admin
from .models import Product, PubFile
from .adminModels import ProductAdminModel

admin.site.register(Product, ProductAdminModel)
#admin.site.register(PubFile)
