from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import PDFDocument

@registry.register_document
class PdfDocumentDocument(Document):
    title = fields.TextField(
        attr="title",
        fields={
            'raw': fields.KeywordField(), 
        }
    )
    file_path = fields.TextField(attr="file.url") 
    uploaded_at = fields.DateField()
    pdf_content = fields.TextField()
    
    
    class Index:
        name = 'pdfs'
        settings = {'number_of_shards':1,'number_of_replicas': 0}
    
    class Django:
        model = PDFDocument
        fields = []