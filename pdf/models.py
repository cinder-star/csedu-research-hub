from django.db import models

from accounts.models import User

# Create your models here.
class PdfFile(models.Model):
    pdf_name = models.CharField(max_length=100)
    pdf_description = models.TextField()
    pdf_uploaded_at = models.DateTimeField(auto_now_add=True)
    pdf_path = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pdf_name
