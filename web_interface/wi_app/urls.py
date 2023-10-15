from django.urls import path
from . import views

app_name = "wi_app"

urlpatterns = [
    path("", views.index, name="index"), # index path
    path("recording/", views.recording, name="recording"),
    path("record/detail/<uuid:id>", views.recording_detail, name="recording_detail")
]