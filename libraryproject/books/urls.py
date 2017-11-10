from django.conf.urls import url

from .views import BooksList, GenreList, GenreBooksList, AuthorList, \
    AuthorBooksList

urlpatterns = [
    url(r'^$', BooksList.as_view(), name='book-list'),
    url(r'^genres/$', GenreList.as_view(), name='genre-list'),
    url(r'^genres/(?P<id>\d+)/$', GenreBooksList.as_view(),
        name='per-genre-books'),
    url(r'^authors/$', AuthorList.as_view(), name='author-list'),
    url(r'^authors/(?P<id>\d+)/$',
        AuthorBooksList.as_view(), name='per-author-books'),
]
