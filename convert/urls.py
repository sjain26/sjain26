from django.urls import path
from . import views
urlpatterns = [
    path("",views.upload,name="upload"),
    path("index1",views.index1,name="index1"),
    path("in",views.download_file,name="download")
]