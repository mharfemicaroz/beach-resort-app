from django.urls import re_path
from .views import login, booking_list, room_list, room_delete, booking_delete, leisure_list, transaction_list, transactionitem_list, booking_status_counts, transaction_filter, transactionitem_filter, transactionitem_delete

urlpatterns = [
    re_path(r'^login/$', login, name='login'),
    re_path(r'^bookings/$',booking_list , name='booking-list'),
    re_path(r'^bookings/stats/$', booking_status_counts, name='booking-stats'),
    re_path(r'^bookings/(?P<pk>\d+)/$', booking_list, name='booking-detail'), 
    re_path(r'^bookings/delete/(?P<pk>\d+)/$', booking_delete, name='booking-delete'),    
    re_path(r'^rooms/$', room_list, name='room-list'),
    re_path(r'^rooms/(?P<pk>\d+)/$', room_list, name='room-detail'), 
    re_path(r'^rooms/delete/(?P<pk>\d+)/$', room_delete, name='room-delete'), 
    re_path(r'^leisures/$', leisure_list, name='leisure-list'),
    re_path(r'^transaction/$', transaction_list, name='transaction-list'),
    re_path(r'^transaction/(?P<pk>\d+)/$', transaction_list, name='transaction-detail'), 
    re_path(r'^transaction/filter/$', transaction_filter, name='transaction-filter'),
    re_path(r'^transaction/item/$', transactionitem_list, name='transactionItem-list'),
    re_path(r'^transaction/item/(?P<pk>\d+)/$', transactionitem_list, name='transactionItem-detail'),
    re_path(r'^transaction/item/delete/(?P<pk>\d+)/$', transactionitem_delete, name='transactionItem-delete'),
    re_path(r'^transaction/item/filter/$', transactionitem_filter, name='transactionItem-list'),
]
