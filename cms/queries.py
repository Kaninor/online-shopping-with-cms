from .models import Product
from django.contrib.auth.models import User

def get_user(id):
    return User.objects.get(id=id)

def get_products():
    return Product.objects.all().order_by("id").reverse()