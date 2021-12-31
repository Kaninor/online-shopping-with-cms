from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Product

def dashboard(request):
    products = Product.objects.all().order_by('id').reverse()
    return render(request, 'dashboard.html', {'products': products})
