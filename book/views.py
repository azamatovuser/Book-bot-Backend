from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


def get_book_file(request):
    book_title = request.GET.get('title')

    try:
        book = Book.objects.get(title=book_title)
        file_path = book.file.path
        return JsonResponse({'file': file_path})
    except ObjectDoesNotExist:
        return JsonResponse({'message': 'Book not found'}, status=404)


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer