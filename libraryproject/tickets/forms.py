from django import forms

from .models import Ticket, TicketDescription


class TicketForm(forms.ModelForm):
    user = forms.CharField(label='Prestamo realizado por: ')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = self.request.user.name
        self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = Ticket
        fields = ('user',)

    def clean(self):
        cleaned_data = super(TicketForm, self).clean()
        cleaned_data['user'] = self.request.user


class DescriptionTicketForm(forms.ModelForm):

    class Meta:
        model = TicketDescription
        fields = ('book',
                  'quantity',)


TicketInlineForm = forms.inlineformset_factory(
    Ticket, Ticket.books.through, fields=('book', 'quantity'), extra=1)
