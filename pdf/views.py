import os
from django.shortcuts import render
from django.http import FileResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from core.classes import FileManager
from csedu_research_hub.settings import MEDIA_ROOT
from .utils import extract_zip, make_pdf
from .models import PdfFile
from .serializers import PdfSerializer, PdfDetailSerializer

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
        pdf_path = make_pdf(build_dir, build_dir.split("/")[-1], main_tex_file)
        user = request.user
        PdfFile.objects.create(
            pdf_name=request.POST["pdf_name"],
            user=user,
            pdf_description=request.POST["pdf_description"],
            pdf_path=pdf_path,
        )
        return Response({"status": "Ok", "message": "File uploaded successfully"})


class PdfFileList(ListAPIView):
    queryset = PdfFile.objects.all().order_by("-pdf_uploaded_at")
    serializer_class = PdfSerializer


class PdfFileDetail(RetrieveAPIView):
    queryset = PdfFile.objects.all()
    serializer_class = PdfDetailSerializer


def PdfView(request, pdf_name):
    file = open(os.path.join(MEDIA_ROOT, "pdf", pdf_name), "rb")
    return FileResponse(file)