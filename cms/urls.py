from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("charts/", views.charts, name="charts"),
    path("tables/", views.tables, name="tables"),
]