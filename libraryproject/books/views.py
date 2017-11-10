# from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Book, Genre, Author

# Create your views here.


class Home(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['recentbooks'] = Book.objects.order_by('-added_at')[:3]
        context['genres'] = Genre.objects.order_by('-added_at')[:3]
        context['authors'] = Author.objects.order_by('-added_at')[:3]
        return context


class BooksList(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = 'books'
    paginate_by = 3

    def get_queryset(self):
        books = super(BooksList, self).get_queryset()
        get_search = self.request.GET.get('search-field')
        filter_criteria = self.request.GET.get('filter-type')

        if get_search is None:
            books = Book.objects.all()

        else:

            if filter_criteria == '2':
                ''' Here the user wants to show book of the authors '''
                authors_name = Author.objects.filter(
                    first_name__icontains=get_search)

                if authors_name.exists():
                    authors = authors_name
                else:
                    authors_last_name = Author.objects.filter(
                        last_name__istartswith=get_search)
                    authors = authors_last_name

                books = Book.objects.filter(author__in=authors)

            else:
                books = Book.objects.filter(name__icontains=get_search)

        return books


class GenreList(ListView):
    model = Genre
    template_name = "books/genres.html"
    context_object_name = 'genres'


class GenreBooksList(ListView):
    model = Book
    template_name = "books/per_genre_books.html"
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(genre=self.kwargs['id'])


class AuthorList(ListView):
    model = Author
    template_name = "books/authors.html"
    context_object_name = 'authors'


class AuthorBooksList(ListView):
    model = Book
    template_name = "books/per_author_books.html"
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(author=self.kwargs['id'])
