from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices


@python_2_unicode_compatible
class User(AbstractUser):

    TYPE_OF_USER = Choices(
        (0, 'bibliotecario', _('bibliotecario')),
        (1, 'estudiante', _('estudiante')),
        (2, 'visitante', _('visitante')),
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    type_of_user = models.IntegerField(choices=TYPE_OF_USER,
                                       default=TYPE_OF_USER.visitante)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def is_visitor(self):
        return self.type_of_user == self.TYPE_OF_USER.visitante

    def is_student(self):
        return self.type_of_user == self.TYPE_OF_USER.estudiante

    def is_librarian(self):
        return self.type_of_user == self.TYPE_OF_USER.bibliotecario

    def has_visitor_profile(self):
        return hasattr(self, 'visitor')

    def has_student_profile(self):
        return hasattr(self, 'student')

    def has_librarian_profile(self):
        return hasattr(self, 'librarian')
