from typing import Generic
from django.views import generic
from books.models import Book
# Create your views here.

class BookListView(generic.ListView):
    model = Book
    template_name = 'books_list.html'
