from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .models import Product, PubFile
from . import queries
import pandas as pd

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

def settings(request):
    return render(request, "settings.html", {
        "user": queries.get_user(1),
    })

@csrf_exempt
def uploadCSV(request):
    if request.method == "POST":
        try:
            raw_csv_file = request.FILES['csvFile']
            csv_file = pd.read_csv(raw_csv_file)
        except Exception as e:
            return redirect("/")
        
        if raw_csv_file.name == "append.csv":
            try:
                for i in range(len(csv_file)):
                    p = Product(
                        name=csv_file["name"][i],
                        number=csv_file["number"][i],
                        off=csv_file["off"][i],
                        price=csv_file["price"][i]
                    )
                    p.save()
                return redirect("/")
            except Exception as e:
                return HttpResponse(e)

        elif raw_csv_file.name == "delete.csv":
            try:
                for i in range(len(csv_file)):
                    Product.objects.get(id=csv_file["ids"][i]).delete()
                return redirect("/")
            except Exception as e:
                return HttpResponse(e)

        else:
            return redirect("/")

@csrf_exempt
def uploadPUB(request):
    if request.method == "POST":
        try:
            pub_file = request.FILES['pubFile']
            p = PubFile(
                name=pub_file.name,
                category="test",
                file=pub_file
            )
            p.save()
            return redirect("/")
        except Exception as e:
            return HttpResponse(e)

def signup(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def forgotPassword(request):
    return render(request, "password.html")
