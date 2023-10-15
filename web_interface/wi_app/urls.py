from django.urls import path
from . import views

app_name = "wi_app"

urlpatterns = [
    path("", views.index, name="index") # index path
]