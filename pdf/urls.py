from django.urls import path

from .views import UploadZip

urlpatterns = [
    path('zip_upload/', UploadZip.as_view()),
]
