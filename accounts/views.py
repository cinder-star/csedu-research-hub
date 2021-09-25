from rest_framework.generics import ListAPIView

from pdf.serializers import PdfSerializer
from pdf.models import PdfFile

# Create your views here.


class ProfilePdfList(ListAPIView):
    serializer_class = PdfSerializer

    def get_queryset(self):
        return PdfFile.objects.filter(user=self.request.user)
