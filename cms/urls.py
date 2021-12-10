from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("charts/", views.charts, name="charts"),
    path("tables/", views.tables, name="tables"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("forgotpassword/", views.forgotPassword, name="forgotPassword"),
    path("upload/csv/", views.uploadCSV, name="uploadCSV"),
    path("upload/pub/", views.uploadPUB, name="uploadPUB"),
]