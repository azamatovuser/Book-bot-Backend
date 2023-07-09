from django.urls import path
from .views import BookListAPIView, get_book_file


urlpatterns = [
    path('list/', BookListAPIView.as_view()),
    path('detail/', get_book_file),
]