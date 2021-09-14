from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'   