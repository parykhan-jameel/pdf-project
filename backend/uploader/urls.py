from django.urls import path
from .views import *

urlpatterns = [
    path('upload/', UploaderView.as_view(), name='upload'),
    path('search/', SearchView.as_view(), name='search'),
]