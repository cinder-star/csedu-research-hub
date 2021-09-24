from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from core.classes import FileManager

# Create your views here.


class UploadZip(APIView):
    def post(self, request):
        file = request.FILES["file"]
        if file.content_type != "application/zip":
            return Response(
                {"status": "Error", "message": "Invalid file type"}, status=400
            )
        filemanager = FileManager()
        filemanager.save_file(file, "zip", "zips")
        return Response({"status": "Ok", "message": "File uploaded successfully"})
