from django.db import models

class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField() 
    indexed = models.BooleanField(default=False) 
    pdf_content = models.TextField(blank=True, null=True)
    
    def __str__(self):
            return self.title