from django.views.generic.edit import CreateView, ModelFormMixin
from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import Ticket, TicketDescription
from .forms import TicketForm, TicketInlineForm

# Create your views here.


class TicketCreate(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = "tickets/new_ticket.html"
    success_url = reverse_lazy('home')

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
        print(self.request)
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(TicketCreate, self).form_valid(form)


class TicketCreate1(LoginRequiredMixin, CreateView):
    '''This class just show a multiselct with existing book,
    doesnot help since we need to specify a quantity field '''

    model = Ticket
    # form_class = NewTicketForm
    template_name = "tickets/new_ticket.html"
    success_url = reverse_lazy('home')
    fields = ('books',)

    def form_valid(self, form):
        user = self.request.user
        form.instace.user = user

        self.object = form.save(commit=True)

        for book in form.cleaned_data['books']:
            ticket_description = TicketDescription()
            ticket_description.ticket = self.object
            ticket_description.books = book
            ticket_description.save()

        super(ModelFormMixin, self).form_valid(form)


class TicketList(ListView):
    model = Ticket
    template_name = "tickets/list_ticket.html"
    context_object_name = 'ticket_list'
