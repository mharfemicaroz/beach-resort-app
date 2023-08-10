# Generated by Django 4.1.7 on 2023-08-10 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=50)),
                ('isAvailable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('clientemail', models.EmailField(blank=True, max_length=254, null=True)),
                ('clientaddress', models.CharField(blank=True, max_length=255, null=True)),
                ('clientnationality', models.CharField(max_length=50)),
                ('clientType', models.CharField(max_length=50)),
                ('checkinDate', models.CharField(max_length=50)),
                ('checkoutDate', models.CharField(max_length=50)),
                ('room_name', models.CharField(max_length=255)),
                ('room_type', models.CharField(max_length=255)),
                ('room_price', models.CharField(max_length=20)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('contactNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(max_length=50)),
                ('itemID', models.CharField(max_length=128)),
                ('actualCheckoutDate', models.CharField(blank=True, max_length=50)),
                ('cancellationDate', models.CharField(blank=True, max_length=50)),
                ('isPaid', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('partialPayment', models.DecimalField(decimal_places=2, max_digits=8)),
                ('processedBy', models.CharField(max_length=128)),
                ('groupkey', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BugReports',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('screenshot_file_name', models.CharField(max_length=256)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128, null=True)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('lastAccessed', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=False)),
                ('route', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GuestCounter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('counter', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItemRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_id', models.IntegerField(blank=True, null=True)),
                ('supplier_name', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('purchase_id', models.IntegerField(blank=True, null=True)),
                ('sales_id', models.IntegerField(blank=True, null=True)),
                ('stock_id', models.IntegerField()),
                ('stock_sku', models.CharField(max_length=50)),
                ('stock_name', models.CharField(max_length=255)),
                ('priceRate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchaseQty', models.IntegerField()),
                ('totalCost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_type', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeisureItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('priceRate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('counter', models.CharField(max_length=32)),
                ('isAvailable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_id', models.IntegerField()),
                ('supplier_name', models.CharField(max_length=255)),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestoItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('imageUrl', models.TextField(blank=True, null=True)),
                ('imageFileName', models.TextField(blank=True, null=True)),
                ('category', models.CharField(max_length=255)),
                ('stocks', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('isAvailable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestoOnholds',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestoOrders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_type', models.CharField(max_length=255)),
                ('table_id', models.IntegerField()),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('items', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=255)),
                ('processedBy', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestoTables',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('isAvailable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestoTakeouts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestoTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('taxValue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discountType', models.TextField(blank=True, null=True)),
                ('discountValue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('totalCharge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('totalPay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payMethod', models.TextField(blank=True, null=True)),
                ('nonCashref', models.TextField(blank=True, null=True)),
                ('items', models.TextField(blank=True, null=True)),
                ('processedBy', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('isAvailable', models.BooleanField(default=True)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sku', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('isAvailable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=255)),
                ('tinno', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('isAvailable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('taskname', models.CharField(max_length=255)),
                ('actualStartTime', models.CharField(max_length=50)),
                ('startDate', models.CharField(max_length=50)),
                ('endDate', models.CharField(max_length=50)),
                ('person_name', models.CharField(max_length=255)),
                ('person_role', models.CharField(max_length=255)),
                ('dept', models.CharField(max_length=255)),
                ('taskdesc', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(max_length=50)),
                ('itemID', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('processedBy', models.CharField(max_length=128)),
                ('groupkey', models.CharField(blank=True, max_length=128, null=True)),
                ('states', models.TextField(blank=True, null=True)),
                ('isCompleted', models.BooleanField(default=False)),
                ('isNotify', models.BooleanField(default=False)),
                ('completionDate', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TasksRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('actor', models.CharField(max_length=255)),
                ('task', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('clientname', models.CharField(max_length=255)),
                ('clientemail', models.EmailField(blank=True, max_length=254, null=True)),
                ('clientcontact', models.CharField(blank=True, max_length=20, null=True)),
                ('clientaddress', models.CharField(blank=True, max_length=255, null=True)),
                ('clientnationality', models.CharField(max_length=50)),
                ('clientType', models.CharField(max_length=50)),
                ('transaction_date', models.DateTimeField(auto_now=True)),
                ('totalAmountToPay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paymentMethod', models.CharField(max_length=50)),
                ('nonCashReference', models.CharField(blank=True, max_length=128, null=True)),
                ('cashAmountPay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payStatus', models.CharField(max_length=50)),
                ('discountMode', models.CharField(blank=True, max_length=50)),
                ('discountValue', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('bookingID', models.CharField(max_length=255)),
                ('processedBy', models.CharField(max_length=128)),
                ('groupkey', models.CharField(blank=True, max_length=128, null=True)),
                ('cashRemarks', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bookingID', models.CharField(max_length=255)),
                ('itemName', models.CharField(max_length=255)),
                ('itemType', models.CharField(max_length=50)),
                ('itemPriceRate', models.CharField(max_length=255)),
                ('purchaseQty', models.IntegerField()),
                ('totalCost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=50)),
                ('itemOption', models.CharField(max_length=50)),
                ('transid', models.CharField(blank=True, max_length=255, null=True)),
                ('groupkey', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionRecord',
            fields=[
                ('transactionrecord_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction', models.IntegerField()),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('paymentMethod', models.CharField(max_length=50)),
                ('nonCashReference', models.CharField(blank=True, max_length=128, null=True)),
                ('totalAmountToPay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cashAmountPay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discountMode', models.CharField(blank=True, max_length=50)),
                ('discountValue', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('processedBy', models.CharField(max_length=128)),
                ('payStatus', models.CharField(max_length=50)),
            ],
        ),
    ]
