from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Employee

def rth(request):
    return redirect("/cms")

def home(request):
    employees = Employee.objects.all()
    return render(request, "home.html", {"employees": employees, "title": "Home"})

def employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        return HttpResponse(f"<h1>{employee.firstName} {employee.lastName}</h1>")
    except:
        return HttpResponse("NOT FOUND")

@csrf_exempt
def delete(request, id):
    if request.method == "DELETE":
        try:
            employee = Employee.objects.get(id=id)
            employee.delete()
            return HttpResponse("deleted")
        except:
            return HttpResponse("error")
    elif request.method == "POST":
        return HttpResponse("post")

@csrf_exempt
def add(request):
    employee = Employee(
        firstName="Dariush", 
        lastName="Rouhifard", 
        age=16, 
        email="dariushroouhifard@gmail.com", 
        phoneNumber="09109770784"
    )
    employee.save()
    return redirect("/")