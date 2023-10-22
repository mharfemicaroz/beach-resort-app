from django.db.models import F, Func, Q
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from decimal import Decimal
from django.db.models import Sum
from datetime import datetime, time, date, timedelta
from dateutil import parser


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        username = data.get('username')
        password = data.get('password')
        try:
            user = CustomUser.objects.get(username=username, password=password)
            response_data = {'status': True, 'role': user.role, 'fName': user.FirstName, 'lName': user.LastName,
                             'username': user.username, 'isActive': user.isActive, 'id': user.id, 'route': user.route}
        except CustomUser.DoesNotExist:
            response_data = {'status': False}
        return JsonResponse(response_data)


@api_view(['POST'])
@csrf_exempt
def filter_model(request, o):
    if request.method == 'POST':
        data = request.data
        if isinstance(data, list):
            # multiple entries
            queryset = o.objects.all()
            for item in data:
                column_name = item.get('columnName')
                column_key = item.get('columnKey')
                if column_name and column_key:
                    queryset = queryset.filter(**{column_name: column_key})
                else:
                    return JsonResponse({'error': 'Invalid input data.'}, status=400)
            response_data = list(queryset.values())
        else:
            # single entry
            column_name = data.get('columnName')
            column_key = data.get('columnKey')
            if column_name and column_key:
                queryset = o.objects.filter(**{column_name: column_key})
                response_data = list(queryset.values())
            else:
                return JsonResponse({'error': 'Invalid input data.'}, status=400)
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@csrf_exempt
def generic_list(request, o, s, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                dt = o.objects.get(id=pk)
            except o.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            ds = s(dt)
            return Response(ds.data)
        else:
            dt = o.objects.all()
            ds = s(dt, many=True)
            return Response(ds.data)

    elif request.method == 'POST':
        ds = s(data=request.data)
        if ds.is_valid():
            ds.save()
            return Response(ds.data, status=status.HTTP_201_CREATED)
        return Response(ds.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            dt = o.objects.get(id=pk)
        except o.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ds = s(dt, data=request.data)
        if ds.is_valid():
            ds.save()
            return Response(ds.data)
        return Response(ds.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@csrf_exempt
def generic_delete(request, o, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                dt = o.objects.get(id=pk)
            except o.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            dt.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@csrf_exempt
def generic_deleter(request, o, pk=None):
    if request.method == 'GET':
        if pk is not None:
            try:
                dt = o.objects.get(id=pk)
            except o.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            dt.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
def generic_getitems(request, ref_model, item_model, item_serializer, identifier):
    if request.method == 'GET':
        o = ref_model.objects.all()
        o_data = item_serializer(o, many=True).data
        for item in o_data:
            id = item[identifier]
            items = item_model.objects.filter(**{identifier: id})
            items_data = item_serializer(items, many=True).data
            item['items'] = items_data
        return JsonResponse(o_data, safe=False)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
def get_transactions_with_items(request, prevday=0):
    today = date.today() - timedelta(days=int(prevday))
    current_month = today.month
    current_year = today.year

    transactions = Transaction.objects.all()

    if type == 'month':
        transactions = transactions.filter(
            transaction_date__year=current_year, transaction_date__month=current_month)
    elif type == 'day':
        current_day = today.day
        transactions = transactions.filter(
            transaction_date__year=current_year, transaction_date__month=current_month, transaction_date__day=current_day)

    transaction_data = TransactionSerializer(transactions, many=True).data

    booking_ids = [transaction['bookingID']
                   for transaction in transaction_data]
    trans_ids = [transaction['id'] for transaction in transaction_data]
    trans_gkeys = [transaction['groupkey']
                   for transaction in transaction_data if transaction['groupkey'] is not None]

    items = TransactionItem.objects.filter(bookingID__in=booking_ids)
    items2 = TransactionRecord.objects.filter(transaction__in=trans_ids)
    items_data = TransactionItemSerializer(items, many=True).data
    items2_data = TransactionRecordSerializer(items2, many=True).data

    transaction_item_dict = {}
    transaction_record_dict = {}

    for item in items_data:
        booking_id = item['bookingID']
        if booking_id not in transaction_item_dict:
            transaction_item_dict[booking_id] = []
        transaction_item_dict[booking_id].append(item)

    for item in items2_data:
        trans_id = item['transaction']
        if trans_id not in transaction_record_dict:
            transaction_record_dict[trans_id] = []
        transaction_record_dict[trans_id].append(item)

    for transaction in transaction_data:
        booking_id = transaction['bookingID']
        trans_id = transaction['id']
        trans_gkey = transaction['groupkey']
        transaction['items'] = transaction_item_dict.get(booking_id, [])
        transaction['items2'] = transaction_record_dict.get(trans_id, [])

        # Calculate actualIncomeOfThisDay
        transaction_date_str = transaction['transaction_date']
        transaction_date = parser.parse(transaction_date_str).date()
        transaction_date = datetime.combine(transaction_date, time.min)
        transaction_records = transaction_record_dict.get(trans_id, [])
        previous_income = sum([Decimal(record['cashAmountPay']) for record in transaction_records if parser.parse(
            record['transaction_date']) < transaction_date], Decimal('0'))
        cash_amount_pay = Decimal(transaction['cashAmountPay'])
        actual_income = cash_amount_pay - previous_income
        transaction['actualIncomeOfThisDay'] = actual_income

    return JsonResponse(transaction_data, safe=False)


@csrf_exempt
def itemcategory_list(request, pk=None):
    return generic_list(request, ItemCategory, ItemCategorySerializer, pk)


@csrf_exempt
def itemcategory_filter(request):
    return filter_model(request, ItemCategory)


@csrf_exempt
def package_list(request, pk=None):
    return generic_list(request, Package, PackageSerializer, pk)


@csrf_exempt
def package_filter(request):
    return filter_model(request, Package)


@csrf_exempt
def package_delete(request, pk=None):
    return generic_delete(request, Package, pk)


@csrf_exempt
def task_list(request, pk=None):
    return generic_list(request, Task, TaskSerializer, pk)


@csrf_exempt
def task_filter(request):
    return filter_model(request, Task)


@csrf_exempt
def task_delete(request, pk=None):
    return generic_delete(request, Task, pk)


@csrf_exempt
def agents_list(request, pk=None):
    return generic_list(request, Agents, AgentsSerializer, pk)


@csrf_exempt
def agents_filter(request):
    return filter_model(request, Agents)


@csrf_exempt
def agents_delete(request, pk=None):
    return generic_delete(request, Agents, pk)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


@csrf_exempt
def bugreports_list(request, pk=None):
    return generic_list(request, BugReports, BugReportsSerializer, pk)


@csrf_exempt
def guestcounter_list(request, pk=None):
    return generic_list(request, GuestCounter, GuestCounterSerializer, pk)


@csrf_exempt
def transactionrecord_delete(request, pk=None):
    return generic_delete(request, TransactionRecord, pk)


@csrf_exempt
def transaction_delete(request, pk=None):
    return generic_delete(request, Transaction, pk)


@csrf_exempt
def restoorders_list(request, pk=None):
    return generic_list(request, RestoOrders, RestoOrdersSerializer, pk)


@csrf_exempt
def restoorders_filter(request):
    return filter_model(request, RestoOrders)


@csrf_exempt
def restotables_filter(request):
    return filter_model(request, RestoTables)


@csrf_exempt
def restotakeouts_delete(request, pk=None):
    return generic_delete(request, RestoTakeouts, pk)


@csrf_exempt
def restotakeouts_list(request, pk=None):
    return generic_list(request, RestoTakeouts, RestoTakeoutsSerializer, pk)


@csrf_exempt
def restoonholds_list(request, pk=None):
    return generic_list(request, RestoOnholds, RestoOnholdsSerializer, pk)


@csrf_exempt
def restotables_list(request, pk=None):
    return generic_list(request, RestoTables, RestoTablesSerializer, pk)


@csrf_exempt
def restotransaction_filter(request):
    return filter_model(request, RestoTransaction)


@csrf_exempt
def restotransaction_delete(request, pk=None):
    return generic_delete(request, RestoTransaction, pk)


@csrf_exempt
def restotransaction_list(request, pk=None):
    return generic_list(request, RestoTransaction, RestoTransactionSerializer, pk)


@csrf_exempt
def restoitem_list(request, pk=None):
    return generic_list(request, RestoItem, RestoItemSerializer, pk)


@csrf_exempt
def restoitem_filter(request):
    return filter_model(request, RestoItem)


@csrf_exempt
def tasksrecord_list(request, pk=None):
    return generic_list(request, TasksRecord, TasksRecordSerializer, pk)


@csrf_exempt
def sales_list(request, pk=None):
    return generic_list(request, Sales, SalesSerializer, pk)


@csrf_exempt
def sales_filter(request):
    return filter_model(request, Sales)


@csrf_exempt
def purchases_list(request, pk=None):
    return generic_list(request, Purchases, PurchasesSerializer, pk)


@csrf_exempt
def purchases_filter(request):
    return filter_model(request, Purchases)


@csrf_exempt
def inventoryitemrecord_list(request, pk=None):
    return generic_list(request, InventoryItemRecord, InventoryItemRecordSerializer, pk)


@csrf_exempt
def inventoryitemrecord_filter(request):
    return filter_model(request, InventoryItemRecord)


@csrf_exempt
def supplier_list(request, pk=None):
    return generic_list(request, Supplier, SupplierSerializer, pk)


@csrf_exempt
def supplier_filter(request):
    return filter_model(request, Supplier)


@csrf_exempt
def stockitem_list(request, pk=None):
    return generic_list(request, StockItem, StockItemSerializer, pk)


@csrf_exempt
def stockitem_filter(request):
    return filter_model(request, StockItem)


@csrf_exempt
def transactionrecord_list(request, pk=None):
    return generic_list(request, TransactionRecord, TransactionRecordSerializer, pk)


@csrf_exempt
def transactionrecord_filter(request):
    return filter_model(request, TransactionRecord)


@csrf_exempt
def users_list(request, pk=None):
    return generic_list(request, CustomUser, CustomUserSerializer, pk)


@csrf_exempt
def user_delete(request, pk=None):
    return generic_delete(request, CustomUser, pk)


@csrf_exempt
def users_filter(request):
    return filter_model(request, CustomUser)


@csrf_exempt
def roomcategory_filter(request):
    return filter_model(request, RoomCategory)


@csrf_exempt
def roomcategory_list(request, pk=None):
    return generic_list(request, RoomCategory, RoomCategorySerializer, pk)


@csrf_exempt
def room_list(request, pk=None):
    return generic_list(request, Room, RoomSerializer, pk)


@csrf_exempt
def rooms_filter(request):
    return filter_model(request, Room)


@csrf_exempt
def room_delete(request, pk=None):
    return generic_delete(request, Room, pk)


@csrf_exempt
def booking_list(request, pk=None):
    return generic_list(request, Booking, BookingSerializer, pk)


# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @csrf_exempt
# def booking_lister(request, pk=None):
#     o = Booking
#     s = BookingSerializer
#     data = request.data
#     start_date_str = datetime.strptime(
#         data.get('start_date_str'), '%d/%m/%Y').date()
#     end_date_str = datetime.strptime(
#         data.get('end_date_str'), '%d/%m/%Y').date()

#     if request.method == 'POST':
#         if pk is not None:
#             try:
#                 dt = o.objects.get(id=pk)
#             except o.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#             ds = s(dt)
#             return Response(ds.data)
#         else:
#             dt = o.objects.annotate(
#                 checkin_as_date=Func(F('checkinDate'), function='STR_TO_DATE',
#                                      template='%(function)s(%(expressions)s, \'DD/MM/YYYY\')'),
#                 checkout_as_date=Func(F('checkoutDate'), function='STR_TO_DATE',
#                                       template='%(function)s(%(expressions)s, \'DD/MM/YYYY\')')
#             )
#             # Add filter to only get items within the date range
#             filtered_objects = dt.filter(
#                 Q(checkin_as_date__gte=start_date_str, checkin_as_date__lte=end_date_str) |
#                 Q(checkout_as_date__gte=start_date_str,
#                   checkout_as_date__lte=end_date_str)
#             )
#             ds = s(filtered_objects, many=True)
#             return Response(ds.data)


@csrf_exempt
def booking_filter(request):
    return filter_model(request, Booking)


@csrf_exempt
def booking_delete(request, pk=None):
    return generic_delete(request, Booking, pk)


@csrf_exempt
def leisure_list(request, pk=None):
    return generic_list(request, LeisureItem, LeisureItemSerializer, pk)


@csrf_exempt
def leisure_filter(request):
    return filter_model(request, LeisureItem)


@csrf_exempt
def transaction_list(request, pk=None):
    return generic_list(request, Transaction, TransactionSerializer, pk)


@csrf_exempt
def transaction_filter(request):
    return filter_model(request, Transaction)


@csrf_exempt
def transactionitem_list(request, pk=None):
    return generic_list(request, TransactionItem, TransactionItemSerializer, pk)


@csrf_exempt
def transactionitem_delete(request, pk=None):
    return generic_delete(request, TransactionItem, pk)


@csrf_exempt
def transactionitem_filter(request):
    return filter_model(request, TransactionItem)
