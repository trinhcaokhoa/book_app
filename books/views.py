from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q 

# Create your views here.
class BookListView( LoginRequiredMixin ,ListView):
    model = Book
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView( LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'   
    login_url = 'account_login'
    permission_required = 'book.special_status'

class SearchResultsListView(ListView): 
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self): 
        if self.request.GET.get('q') != None:
            query = self.request.GET.get('q')
            return Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains="chess")
            )
