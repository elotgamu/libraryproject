from django.contrib import admin


from .models import Genre, Author, Book
# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    '''
        Admin View for Genre
    '''
    list_display = ('name',)


admin.site.register(Genre, GenreAdmin)


class AuthorAdmin(admin.ModelAdmin):
    '''
        Admin View for Author
    '''
    list_display = ('first_name', 'last_name')


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    '''
        Admin View for Book
    '''
    list_display = ('name', 'author', 'genre')

    def autor(self, author):
        return "%s %s" % (author.first_name, author.last_name)

    def genre(self, genre):
        return genre.name


admin.site.register(Book, BookAdmin)
