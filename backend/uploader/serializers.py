from rest_framework import serializers
from .models import *

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFDocument
        fields = ['title', 'file'] 