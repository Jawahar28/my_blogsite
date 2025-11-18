from django.urls import path
from . import views

app_name = "likes"

urlpatterns = [
    path("toggle/", views.toggle_like, name="toggle-like"),
]
