from django.conf.urls import url

from .views import TicketCreate, TicketList

urlpatterns = [
    url(r'^$', TicketList.as_view(), name='ticket-list'),
    url(r'^new-ticket/$', TicketCreate.as_view(), name='new-ticket'),
]
