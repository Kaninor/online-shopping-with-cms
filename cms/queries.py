from .models import CMSUser, Product

def get_user(id):
    return CMSUser.objects.get(id=id)

def get_products():
    return Product.objects.all().order_by("id").reverse()