from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload", views.upload, name="upload"),
    path("download/<str:file_name>", views.download, name="download"),
    path("confirmDownload/<str:file_name>", views.confirmDownload, name="confirmDownload"),
]