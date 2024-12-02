from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from elasticsearch_dsl import Q
from PyPDF2 import PdfReader
from .documents import PdfDocumentDocument
from .models import *
from .serializers import *
from .utils import extract_pdf_content


#view for uploading files
class UploaderView(APIView):
    def post(self, request):
        print(request.data)
        serializer = PdfSerializer(data=request.data)
        if serializer.is_valid():
            pdf_instance = serializer.save()
            pdf_file_path = pdf_instance.file.path
            try:
                pdf_content = extract_pdf_content(pdf_file_path)
                if not pdf_content:
                    return Response(
                        {"error": "No content extracted from PDF."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                pdf_instance.pdf_content = pdf_content
                pdf_instance.indexed = True
                pdf_instance.save()
                
                PdfDocumentDocument.init()  
                document = PdfDocumentDocument(meta={'id': pdf_instance.id})
                document.title = pdf_instance.title
                document.file_path = pdf_instance.file.url
                document.pdf_content = pdf_content
                document.save()
                
            except Exception as e:
                pdf_instance.indexed = False
                pdf_instance.save()
                return Response(
                    {"error": "Failed to extract or index PDF content.", "details": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#view for searching files
class SearchView(APIView):
   def get(self, request):
        query = request.query_params.get('query', None)
        title = request.query_params.get('title', None)
        print(f"Received query: {query}")
        print(f"Received title: {title}")

        if not query or not title:
            return Response(
                {"error": "Both 'query' and 'title' parameters are required."},
                status=400
            )
            
        search_query = Q("bool", must=[
            Q("match", pdf_content=query),
            Q("term", title__raw=title)   
        ])

        search = PdfDocumentDocument.search().query(search_query).highlight('pdf_content')

        response = search.execute()

        results = []
        for hit in response:
            highlights = list(hit.meta.highlight.pdf_content) if 'pdf_content' in hit.meta.highlight else []

            results.append({
                'id': str(hit.meta.id),      
                'title': hit.title,           
                'file_url': hit.file_path,   
                'highlights': highlights     
            })

        return Response({"results": results})
        
        
