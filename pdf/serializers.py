from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import PdfFile


class PdfSerializer(ModelSerializer):
    user = SerializerMethodField()

    def get_user(self, pdf: PdfFile):
        return pdf.user.username

    class Meta:
        fields = [
            "id",
            "pdf_name",
            "user",
            "pdf_description",
            "pdf_uploaded_at",
        ]
        model = PdfFile


class PdfDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    file = SerializerMethodField()

    def get_user(self, pdf: PdfFile):
        return pdf.user.username

    def get_file(self, pdf: PdfFile):
        return "/api/v1/pdf/media/"+pdf.pdf_path.split("/")[-1]

    class Meta:
        fields = [
            "id",
            "pdf_name",
            "user",
            "pdf_description",
            "pdf_uploaded_at",
            "file",
        ]
        model = PdfFile