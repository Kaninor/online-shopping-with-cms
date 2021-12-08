from .models import CMSUser

def get_user(id):
    return CMSUser.objects.get(id=id)