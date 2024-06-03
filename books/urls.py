from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDestroy

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='criar-lista-livros'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
]