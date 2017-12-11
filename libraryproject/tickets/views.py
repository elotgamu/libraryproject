# from django.shortcuts import redirect
from django.views.generic.edit import CreateView, ModelFormMixin
from django.views.generic import ListView
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import Ticket, TicketDescription
from .forms import TicketForm, TicketInlineForm

# Create your views here.


class TicketCreate(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = "tickets/new_ticket.html"
    success_url = reverse_lazy('tickets:ticket-list')

    def get_context_data(self, **kwargs):
        context = super(TicketCreate, self).get_context_data(**kwargs)

        if self.request.POST:
            context['inline_form'] = TicketInlineForm(self.request.POST)
        else:
            context['inline_form'] = TicketInlineForm()

        return context

    def get_form_kwargs(self):
        kwargs = super(TicketCreate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        context = self.get_context_data()
        inline_form = context['inline_form']

        with transaction.atomic():
            self.object = form.save()

            if inline_form.is_valid():
                inline_form.instance = self.object
                inline_form.save()

        return super(TicketCreate, self).form_valid(form)


class TicketList(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = "tickets/list_ticket.html"
    context_object_name = 'ticket_list'

    def get_queryset(self, **kwargs):
        self.tickets = Ticket.objects.filter(user=self.request.user)
        return self.tickets
