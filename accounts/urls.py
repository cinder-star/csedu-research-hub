from django.urls import path

from .views import ProfilePdfList

urlpatterns = [
    path("", ProfilePdfList.as_view(), name="profile-pdf-list"),
]
