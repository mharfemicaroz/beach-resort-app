from django.urls import re_path
from .views import *

urlpatterns = [ 
    re_path(r'^transactions_itemizer/$', get_transactions_with_items, name='transactions'),
    re_path(r'^login/$', login, name='login'),
    re_path(r'^restoorders/$',restoorders_list , name='restoorders-list'),
    re_path(r'^restoorders/(?P<pk>\d+)/$',restoorders_list, name='restoorders-detail'), 
    re_path(r'^restoorders/filter/$', restoorders_filter, name='restoorders-filter'),
    re_path(r'^restoonholds/$',restoonholds_list , name='restoonholds-list'),
    re_path(r'^restoonholds/(?P<pk>\d+)/$',restoonholds_list, name='restoonholds-detail'), 
    re_path(r'^restotakeouts/$',restotakeouts_list , name='restotakeouts-list'),
    re_path(r'^restotakeouts/(?P<pk>\d+)/$',restotakeouts_list, name='restotakeouts-detail'), 
    re_path(r'^restotakeouts/delete/(?P<pk>\d+)/$', restotakeouts_delete, name='restotakeouts-delete'),  
    re_path(r'^restotables/$',restotables_list , name='restotables-list'),
    re_path(r'^restotables/(?P<pk>\d+)/$',restotables_list, name='restotables-detail'), 
    re_path(r'^restotables/filter/$', restotables_filter, name='restotables-filter'),
    re_path(r'^restotransaction/$',restotransaction_list , name='restotransaction-list'),
    re_path(r'^restoitem/$',restoitem_list , name='restoitem-list'),
    re_path(r'^restoitem/(?P<pk>\d+)/$',restoitem_list, name='restoitem-detail'), 
    re_path(r'^restoitem/filter/$', restoitem_filter, name='restoitem-filter'),
    re_path(r'^task/record/$',tasksrecord_list , name='taskrecord-list'),
    re_path(r'^transaction/record/$', transactionrecord_list, name='transactionRecord-list'),
    re_path(r'^transaction/record/(?P<pk>\d+)/$', transactionrecord_list, name='transactionRecord-detail'),
    re_path(r'^transaction/record/delete/(?P<pk>\d+)/$', transactionrecord_delete, name='transactionrecord-delete'),
    re_path(r'^transaction/record/filter/$', transactionrecord_filter, name='transaction-record-filter'),
    re_path(r'^sales/$',sales_list , name='sales-list'),
    re_path(r'^sales/(?P<pk>\d+)/$',sales_list, name='sales-detail'), 
    re_path(r'^sales/filter/$', sales_filter, name='sales-filter'),
    re_path(r'^purchases/$',purchases_list , name='purchases-list'),
    re_path(r'^purchases/(?P<pk>\d+)/$',purchases_list, name='purchases-detail'), 
    re_path(r'^purchases/filter/$', purchases_filter, name='purchases-filter'),
    re_path(r'^inventory/item/$',inventoryitemrecord_list , name='inventoryitemrecord-list'),
    re_path(r'^inventory/item/(?P<pk>\d+)/$',inventoryitemrecord_list, name='inventoryitemrecord-detail'), 
    re_path(r'^inventory/item/filter/$', inventoryitemrecord_filter, name='inventoryitemrecord-filter'),
    re_path(r'^supplier/$',supplier_list , name='supplier-list'),
    re_path(r'^supplier/(?P<pk>\d+)/$',supplier_list, name='supplier-detail'), 
    re_path(r'^supplier/filter/$', supplier_filter, name='supplier-filter'), 
    re_path(r'^stockitem/$',stockitem_list , name='stockitem-list'),
    re_path(r'^stockitem/(?P<pk>\d+)/$',stockitem_list, name='stockitem-detail'), 
    re_path(r'^stockitem/filter/$', stockitem_filter, name='stockitem-filter'),
    re_path(r'^users/$',users_list , name='users-list'),
    re_path(r'^users/(?P<pk>\d+)/$',users_list, name='users-detail'), 
    re_path(r'^users/filter/$', users_filter, name='users-filter'),
    re_path(r'^user/delete/(?P<pk>\d+)/$', user_delete, name='user-delete'), 
    re_path(r'^bookings/$',booking_list , name='booking-list'),
    re_path(r'^bookings/filter/$', booking_filter, name='booking-filter'),
    re_path(r'^bookings/(?P<pk>\d+)/$', booking_list, name='booking-detail'), 
    re_path(r'^bookings/delete/(?P<pk>\d+)/$', booking_delete, name='booking-delete'),    
    re_path(r'^rooms/$', room_list, name='room-list'),
    re_path(r'^rooms/(?P<pk>\d+)/$', room_list, name='room-detail'), 
    re_path(r'^rooms/filter/$', rooms_filter, name='rooms-filter'),
    re_path(r'^rooms/delete/(?P<pk>\d+)/$', room_delete, name='room-delete'), 
    re_path(r'^leisures/$', leisure_list, name='leisure-list'),
    re_path(r'^leisures/(?P<pk>\d+)/$',leisure_list, name='leisure-detail'), 
    re_path(r'^leisures/filter/$', leisure_filter, name='leisure-filter'),
    re_path(r'^transaction/$', transaction_list, name='transaction-list'),
    re_path(r'^transaction/(?P<pk>\d+)/$', transaction_list, name='transaction-detail'), 
    re_path(r'^transaction/delete/(?P<pk>\d+)/$', transaction_delete, name='transaction-delete'), 
    re_path(r'^transaction/filter/$', transaction_filter, name='transaction-filter'),
    re_path(r'^transaction/item/$', transactionitem_list, name='transactionItem-list'),
    re_path(r'^transaction/item/(?P<pk>\d+)/$', transactionitem_list, name='transactionItem-detail'),
    re_path(r'^transaction/item/delete/(?P<pk>\d+)/$', transactionitem_delete, name='transactionItem-delete'),
    re_path(r'^transaction/item/filter/$', transactionitem_filter, name='transactionItem-list'),
]
