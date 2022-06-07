from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Book
from .serializers import BookSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect


# Create your views here.


@api_view(['GET'])
def latest_books_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request, pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(books, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):

    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def edit(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()

    return Response("Deleted")

