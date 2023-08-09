from django.db import models

# Create your models here.


class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128, null=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    lastAccessed = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=False)
    route = models.CharField(max_length=50)


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    clientemail = models.EmailField(null=True, blank=True)
    clientaddress = models.CharField(max_length=255, null=True, blank=True)
    clientnationality = models.CharField(max_length=50)
    clientType = models.CharField(max_length=50)
    checkinDate = models.CharField(max_length=50)
    checkoutDate = models.CharField(max_length=50)
    room_name = models.CharField(max_length=255)
    room_type = models.CharField(max_length=255)
    room_price = models.CharField(max_length=20)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    contactNumber = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=50)
    itemID = models.CharField(max_length=128)
    actualCheckoutDate = models.CharField(max_length=50, blank=True)
    cancellationDate = models.CharField(max_length=50, blank=True)
    isPaid = models.CharField(max_length=50, blank=True)
    created_at = models.DateField(auto_now_add=True)
    totalPrice = models.DecimalField(max_digits=8, decimal_places=2)
    partialPayment = models.DecimalField(max_digits=8, decimal_places=2)
    processedBy = models.CharField(max_length=128)
    groupkey = models.CharField(max_length=128, null=True, blank=True)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    taskname = models.CharField(max_length=255)
    actualStartTime = models.CharField(max_length=50)
    startDate = models.CharField(max_length=50)
    endDate = models.CharField(max_length=50)
    person_name = models.CharField(max_length=255)
    person_role = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    taskdesc = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50)
    itemID = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    processedBy = models.CharField(max_length=128)
    groupkey = models.CharField(max_length=128, null=True, blank=True)
    states = models.TextField(null=True, blank=True)
    isCompleted = models.BooleanField(default=False)
    completionDate = models.CharField(max_length=50, blank=True, null=True)


class Assign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    isAvailable = models.BooleanField(default=True)


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    isAvailable = models.BooleanField(default=True)
    status = models.CharField(max_length=100)


class LeisureItem(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    priceRate = models.DecimalField(max_digits=10, decimal_places=2)
    counter = models.CharField(max_length=32)
    isAvailable = models.BooleanField(default=True)


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    clientname = models.CharField(max_length=255)
    clientemail = models.EmailField(null=True, blank=True)
    clientcontact = models.CharField(max_length=20, null=True, blank=True)
    clientaddress = models.CharField(max_length=255, null=True, blank=True)
    clientnationality = models.CharField(max_length=50)
    clientType = models.CharField(max_length=50)
    transaction_date = models.DateTimeField(auto_now=True)
    totalAmountToPay = models.DecimalField(max_digits=10, decimal_places=2)
    paymentMethod = models.CharField(max_length=50)
    nonCashReference = models.CharField(max_length=128, null=True, blank=True)
    cashAmountPay = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    payStatus = models.CharField(max_length=50)
    discountMode = models.CharField(max_length=50, blank=True)
    discountValue = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    bookingID = models.CharField(max_length=255)
    processedBy = models.CharField(max_length=128)
    groupkey = models.CharField(max_length=128, null=True, blank=True)
    cashRemarks = models.CharField(max_length=255, null=True, blank=True)


class TransactionRecord(models.Model):
    transactionrecord_id = models.AutoField(primary_key=True)
    transaction = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    paymentMethod = models.CharField(max_length=50)
    nonCashReference = models.CharField(max_length=128, null=True, blank=True)
    totalAmountToPay = models.DecimalField(max_digits=10, decimal_places=2)
    cashAmountPay = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    discountMode = models.CharField(max_length=50, blank=True)
    discountValue = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    processedBy = models.CharField(max_length=128)
    payStatus = models.CharField(max_length=50)


class TransactionItem(models.Model):
    id = models.AutoField(primary_key=True)
    bookingID = models.CharField(max_length=255)
    itemName = models.CharField(max_length=255)
    itemType = models.CharField(max_length=50)
    itemPriceRate = models.CharField(max_length=255)
    purchaseQty = models.IntegerField()
    totalCost = models.DecimalField(max_digits=10, decimal_places=2)
    dateCreated = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    itemOption = models.CharField(max_length=50)
    transid = models.CharField(max_length=255, null=True, blank=True)
    groupkey = models.CharField(max_length=128, null=True, blank=True)


class StockItem(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    isAvailable = models.BooleanField(default=True)


class RestoItem(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    imageUrl = models.TextField(null=True, blank=True)
    imageFileName = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255)
    stocks = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    isAvailable = models.BooleanField(default=True)


class RestoTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    taxValue = models.DecimalField(max_digits=10, decimal_places=2)
    discountType = models.TextField(null=True, blank=True)
    discountValue = models.DecimalField(max_digits=10, decimal_places=2)
    subTotal = models.DecimalField(max_digits=10, decimal_places=2)
    totalCharge = models.DecimalField(max_digits=10, decimal_places=2)
    totalPay = models.DecimalField(max_digits=10, decimal_places=2)
    payMethod = models.TextField(null=True, blank=True)
    nonCashref = models.TextField(null=True, blank=True)
    items = models.TextField(null=True, blank=True)
    processedBy = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)


class RestoOrders(models.Model):
    id = models.AutoField(primary_key=True)
    order_type = models.CharField(max_length=255)
    table_id = models.IntegerField()
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    items = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255)
    processedBy = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class RestoTables(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    isAvailable = models.BooleanField(default=True)


class RestoTakeouts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class RestoOnholds(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    tinno = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    isAvailable = models.BooleanField(default=True)


class Purchases(models.Model):
    id = models.AutoField(primary_key=True)
    supplier_id = models.IntegerField()
    supplier_name = models.CharField(max_length=255)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class InventoryItemRecord(models.Model):
    id = models.AutoField(primary_key=True)
    supplier_id = models.IntegerField(null=True, blank=True)
    supplier_name = models.CharField(max_length=255, null=True, blank=True)
    customer_name = models.CharField(max_length=255, null=True, blank=True)
    purchase_id = models.IntegerField(null=True, blank=True)
    sales_id = models.IntegerField(null=True, blank=True)
    stock_id = models.IntegerField()
    stock_sku = models.CharField(max_length=50)
    stock_name = models.CharField(max_length=255)
    priceRate = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseQty = models.IntegerField()
    totalCost = models.DecimalField(max_digits=10, decimal_places=2)
    stock_type = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)


class TasksRecord(models.Model):
    id = models.AutoField(primary_key=True)
    actor = models.CharField(max_length=255)
    task = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)


class GuestCounter(models.Model):
    id = models.AutoField(primary_key=True)
    counter = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class BugReports(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(null=True, blank=True)
    screenshot_file_name = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)
