# google ccbv
from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


class ListCreateBookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer
    

