from django.urls import path

from .views import UploadZip, PdfFileList, PdfFileDetail

urlpatterns = [
    path("zip_upload/", UploadZip.as_view()),
    path("", PdfFileList.as_view()),
    path("<int:pk>/", PdfFileDetail.as_view()),
]
