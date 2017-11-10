from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)
    descrition_text = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


class Book(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField(blank=True)
    genre = models.ForeignKey(Genre, related_name='books')
    author = models.ForeignKey(Author, related_name='books')
    added_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.name

    def clean(self):
        if Book.objects.filter(name=self.name).exists() and  \
                Book.objects.filter(author=self.author).exists():
            raise ValidationError('Este libro ya ha sido agregado')
