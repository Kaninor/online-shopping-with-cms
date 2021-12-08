from django.urls import path
from . import views

urlpatterns = [
    path("", views.rth),
    path("home/", views.home),
    path("home/<int:id>", views.employee),
    path("home/delete/<id>", views.delete),
    path("home/add/", views.add),
]