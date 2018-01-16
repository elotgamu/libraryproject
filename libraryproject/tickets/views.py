from django.views.generic.edit import CreateView, UpdateView, BaseUpdateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.detail import SingleObjectTemplateResponseMixin

from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import JsonResponse

from django.template.loader import render_to_string

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Ticket
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


class TicketDetails(DetailView):
    model = Ticket
    template_name = "tickets/ticket_details.html"
    context_object_name = 'ticket'


class JSONResponseMixin(object):
    """Mixin to handle the JSON response"""

    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context),
                            safe=False,
                            **response_kwargs
                            )

    def get_data(self, context):
        context = render_to_string(self.template_name, context, self.request)
        return context


class CancelTicketView(
        JSONResponseMixin,
        SingleObjectTemplateResponseMixin,
        BaseUpdateView):
    """CancelTicketView"""

    model = Ticket
    fields = ('status',)
    template_name = "tickets/cancel_ticket_partial.html"

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super(CancelTicketView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """Getting the ticket using its pk"""
        obj = Ticket.objects.get(pk=self.kwargs['pk'])
        return obj

    def render_to_response(self, context):
        # checking if the request is a json format

        # it seems that format json in the GET
        # request is not being recognized
        # we tried the is_ajax method instead
        # if self.request.GET.get('format') == 'json:

        if self.request.is_ajax():
            return self.render_to_json_response(context)
        else:
            return super(CancelTicketView, self).render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = Ticket.TICKET_STATUS.canceled
        self.object.status_notes = 'Ya no deseo hacer este prestamo'
        self.object.save()

        if request.is_ajax():
            """The context of the request is not needed
            here we pass a new dictionary that acts as context"""

            context = dict()
            context['form_is_valid'] = 'The Ticket was canceled successfully'

            updated_tickets = Ticket.objects.filter(
                user=self.request.user)

            context['html'] = render_to_string(
                'tickets/ticket_list_partial.html', {
                    'ticket_list': updated_tickets
                })

            return JsonResponse(context)

        else:
            return super(CancelTicketView, self).post(request, *args, **kwargs)


class TicketCancelView(UpdateView):
    model = Ticket
    template_name = "tickets/cancel_ticket_partial.html"
    context_object_name = 'ticket'
    fields = ('status',)
    success_url = reverse_lazy('tickets')

    def get_object(self, queryset=None):
        """Getting the ticket using its pk"""
        obj = Ticket.objects.get(pk=self.kwargs['pk'])
        return obj

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            data = dict()
            # ticket = self.get_object()
            data['html'] = render_to_string(
                'tickets/cancel_ticket_partial.html',
                context=self.get_context_data(), request=request
            )
            return JsonResponse(data)

    def render_to_response(self, context):
        # getting to know the json type reponse
        if self.request.GET.get('format') == 'json':
            return self.render_to_json_response(context)

    def form_valid(self, form):
        ticket = self.get_object()
        ticket.status = Ticket.status.rejected
        ticket.save()
        return super(TicketCancelView, self).form_valid(form)

    def form_invalid(self, form):
        return super(TicketCancelView, self).form_invalid(form)
