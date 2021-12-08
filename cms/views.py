from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import CMSUser
from . import queries

def dashboard(request):
    return render(request, "index.html", {"user": queries.get_user(1)})

def charts(request):
    return render(request, "charts.html", {"user": queries.get_user(1)})

def tables(request):
    return render(request, "tables.html", {"user": queries.get_user(1)})
