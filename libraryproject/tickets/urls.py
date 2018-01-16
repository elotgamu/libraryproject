from django.conf.urls import url

from .views import TicketCreate, TicketList, CancelTicketView, TicketDetails

urlpatterns = [
    url(r'^$', TicketList.as_view(), name='ticket-list'),
    url(r'^new-ticket/$', TicketCreate.as_view(), name='new-ticket'),
    url(r'^cancel/(?P<pk>\d+)/$', CancelTicketView.as_view(),
        name='cancel-ticket'),
    url(r'^detail/(?P<pk>\d+)/$', TicketDetails.as_view(),
        name='ticket-detail'),
]
