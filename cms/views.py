from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import CMSUser
from . import queries

def dashboard(request):
    return render(request, "index.html", {
        "user": queries.get_user(1), 
        "products": queries.get_products(),
    })

def charts(request):
    return render(request, "charts.html", {
        "user": queries.get_user(1)
    })

def tables(request):
    return render(request, "tables.html", {
        "user": queries.get_user(1), 
        "products": queries.get_products()
    })

@csrf_exempt
def uploadCSV(request):
    if request.method == "POST":
        csv_file = request.POST['csvFile']
        return HttpResponse(csv_file)

@csrf_exempt
def uploadPUB(request):
    if request.method == "POST":
        pub_file = request.POST['pubFile']
        return HttpResponse(pub_file)

def signup(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def forgotPassword(request):
    return render(request, "password.html")
