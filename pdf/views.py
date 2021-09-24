from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from core.classes import FileManager
from .utils import extract_zip, make_pdf

# Create your views here.


class UploadZip(APIView):
    def post(self, request):
        file = request.FILES["file"]
        main_tex_file = request.POST["main_tex_file"]
        if file.content_type != "application/zip":
            return Response(
                {"status": "Error", "message": "Invalid file type"}, status=400
            )
        filemanager = FileManager()
        zip_file_path = filemanager.save_file(file, "zip", "zips")
        build_dir = extract_zip(zip_file_path)
        make_pdf(build_dir, build_dir.split("/")[-1], main_tex_file)
        return Response({"status": "Ok", "message": "File uploaded successfully"})
