from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        username = data.get('username')
        password = data.get('password')
        try:
            user = CustomUser.objects.get(username=username, password=password)
            response_data = {'status': True,'role':user.role,'fName':user.FirstName,'lName':user.LastName,'username':user.username,'isActive':user.isActive,'id':user.id, 'route':user.route}
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
            dt= o.objects.all()
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
def restotables_list(request, pk=None):
    return generic_list(request, RestoTables, RestoTablesSerializer, pk)

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