from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class UploadZip(APIView):
    def post(self, request):
        return Response({"message": "Zip file uploaded successfully"})