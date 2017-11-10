from django.contrib import admin

# Register your models here.
from .models import Ticket, TicketDescription


class TicketDescriptionInline(admin.StackedInline):
    '''
        StackedInline def for the m2m
    '''
    model = TicketDescription


class TicketAdmin(admin.ModelAdmin):
    '''
        Admin View for the Ticket
    '''
    inlines = [TicketDescriptionInline]
    list_filter = ['status']
    list_display = ['pk', 'user', ]


admin.site.register(Ticket, TicketAdmin)
