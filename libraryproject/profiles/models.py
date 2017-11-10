from django.db import models

from django.conf import settings
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=8, blank=True, null=True)
    id_card = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        abstract = True


class Student(Profile):
    student_number = models.CharField(max_length=6)
    school_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return self.user.name


class Visitor(Profile):

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"

    def __str__(self):
        return self.user.name


class Librarian(Profile):

    class Meta:
        verbose_name = "Bibliotecario"
        verbose_name_plural = "Bibliotecarios"

    def __str__(self):
        return self.user.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.user.is_staff = True
            self.user.save()

        super(Librarian, self).save(*args, **kwargs)
