from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices

from libraryproject.books.models import Book

# Create your models here.


class Ticket(models.Model):
    TICKET_STATUS = Choices(
        (0, 'submitted', _('Enviada')),
        (1, 'rejected', _('Rechazada')),
        (2, 'approved', _('Aprobada')),
        (3, 'canceled', _('Cancelada')),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='TicketDescription')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    status = models.IntegerField(
        choices=TICKET_STATUS, default=TICKET_STATUS.submitted)
    status_notes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self):
        return "%s" % (self.pk)

    def get_absolute_url(self):
        return reverse('tickets:ticket-detail', kwargs={'pk': self.pk})


class TicketDescription(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Descripcion de la Ticket"
        verbose_name_plural = "Descripciones de la ticket"
