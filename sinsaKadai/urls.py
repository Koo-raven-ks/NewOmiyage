from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("overview/", views.overview, name="overview"),
    path("list/", views.list_view, name="list"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("contact/", views.contact, name="contact"),
]
