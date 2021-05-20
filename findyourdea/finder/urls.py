from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("details", views.details, name="details"),
    path("user/", views.user, name="user"),
    path("", views.index, name="index"),
    path("listado/", views.listado, name="listado"),
    path("contact/", views.contact, name="contact")
]