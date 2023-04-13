from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'lastAccessed': {'read_only': True},
        }

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'        

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class LeisureItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeisureItem
        fields = '__all__'     

class TransactionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionRecord
        fields = '__all__'   

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        
class TransactionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionItem
        fields = '__all__'  

class StockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockItem
        fields = '__all__'  

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'  

class PurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = '__all__'  

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'  

class InventoryItemRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItemRecord
        fields = '__all__'  