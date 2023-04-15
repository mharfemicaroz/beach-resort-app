<template>
    <div class="container-fluid">
        <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm">
            <div class="container-fluid">
                <!-- Logo and Search Bar -->
                <a class="navbar-brand" href="#">
                    <img src="@/assets/pantukan-waterworld-logo.jpg" width="45" height="45" class="d-inline-block align-top"
                        alt="Pantukan Waterworld Logo">
                    Pantukan Waterworld Beach Resort
                </a>

                <!-- Navigation Links -->
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav me-auto">

                    </ul>
                    <ul class="navbar-nav">
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                                data-bs-toggle="dropdown" aria-expanded="false">
                                <img src="@/assets/user-avatar.png" class="rounded-circle" alt="User Avatar" height="32"
                                    width="32">
                                {{ userdata.fName }} {{ userdata.lName }}
                            </a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a class="dropdown-item" href="#" @click=logout()>Logout</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>


        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-12">
                    <ul class="nav nav-tabs justify-content-left">
                        <li class="nav-item">
                            <a class="nav-link active text-center" data-bs-toggle="tab" href="#inventory">
                                <i class="fas fa-warehouse fa-2x"></i>
                                <br>
                                Inventory
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link text-center" data-bs-toggle="tab" href="#supplier">
                                <i class="fas fa-truck fa-2x"></i>
                                <br>
                                Supplier
                            </a>
                        </li>

                        <li class="nav-item">
                            <a class="nav-link text-center" data-bs-toggle="tab" href="#purchases">
                                <i class="fas fa-cart-arrow-down fa-2x"></i>
                                <br>
                                Purchases
                            </a>
                        </li>

                        <li class="nav-item">
                            <a class="nav-link text-center" data-bs-toggle="tab" href="#sales">
                                <i class="fas fa-dollar-sign fa-2x"></i>
                                <br>
                                Sales
                            </a>
                        </li>

                    </ul>
                    <div class="tab-content">
                        <div id="inventory" class="tab-pane active">
                            <div id="inventory" class="tab-pane active">
                                <div class="row">
                                    <div class="col-md-3">
                                        <form @submit.prevent="saveInventory">
                                            <div class="mb-3">
                                                <label for="name" class="form-label">Name</label>
                                                <input type="text" class="form-control" id="name" v-model="stock.name"
                                                    required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="description" class="form-label">Description</label>
                                                <input type="text" class="form-control" id="description"
                                                    v-model="stock.description">
                                            </div>
                                            <div class="mb-3">
                                                <label for="sku" class="form-label">SKU</label>
                                                <input type="text" class="form-control" id="SKU" v-model="stock.sku"
                                                    required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="is-available" class="form-label">Category</label>
                                                <select class="form-select" id="is-available" v-model="stock.category"
                                                    required>
                                                    <option value="">-- Select --</option>
                                                    <option value="raw-materials">Raw materials</option>
                                                    <option value="finished-goods">Finished goods</option>
                                                    <option value="supplies">Supplies</option>
                                                    <option value="equipment">Equipment</option>
                                                    <option value="parts-and-components">Parts and components</option>
                                                </select>
                                            </div>

                                            <div class="mb-3">
                                                <label for="is-available" class="form-label">Availability</label>
                                                <select class="form-select" id="is-available" v-model="stock.isAvailable"
                                                    required>
                                                    <option value="">-- Select --</option>
                                                    <option value=true>Yes</option>
                                                    <option value=false>No</option>
                                                </select>
                                            </div>
                                            <button type="submit" class="btn btn-primary">{{ isUpdatingInventory ? 'Update'
                                                :
                                                'Save'
                                            }}</button>
                                        </form>
                                    </div>
                                    <div class="col-md-9"
                                        style=" height: 600px ;max-height: 600px;overflow-y: auto;overflow-x: hidden;padding-right: 1px;">
                                        <div class="input-group mt-2">
                                            <input type="text" class="form-control" placeholder="Search Inventory"
                                                v-model="searchInventory">
                                            <div class="input-group-append">
                                                <button class="btn btn-outline-secondary" type="button">
                                                    <i class="fa fa-search"></i>
                                                </button>
                                            </div>
                                        </div>
                                        <table class="table">
                                            <thead>
                                                <tr>
                                                    <th>Name</th>
                                                    <th>Description</th>
                                                    <th>SKU</th>
                                                    <th>Category</th>
                                                    <th>Qty</th>
                                                    <th>Is Available?</th>
                                                    <th>Action</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <template v-for="item in filteredstocks" :key="item.id">
                                                    <tr>
                                                        <td>{{ item.name }}</td>
                                                        <td>{{ item.description }}</td>
                                                        <td>{{ item.sku }}</td>
                                                        <td>{{ item.category }}</td>
                                                        <td>{{ item.quantity }}</td>
                                                        <td v-if="item.isAvailable">Yes</td>
                                                        <td v-else>No</td>
                                                        <td>
                                                            <button type="button" class="btn btn-primary btn-sm"
                                                                @click="editInventory(item.id)"><i
                                                                    class="fas fa-edit"></i></button>&nbsp;
                                                            <button type="button" @click="toggleTable3(item.id)"
                                                                    class="btn btn-primary btn-sm">
                                                                    <span v-if="!showTable3[item.id]">+</span>
                                                                    <span v-else>-</span>
                                                                </button>
                                                        </td>
                                                    </tr>

                                                    <tr v-if="showTable3[item.id]">
                                                        <td colspan="7">
                                                            <h5 class="bg-primary text-white">Records</h5>
                                                            <table class="table"
                                                                style="table-layout: fixed;word-wrap: break-word;">
                                                                <thead>
                                                                    <tr>
                                                                        
                                                                        <th>Status</th>
                                                                        <th>Price</th>
                                                                        <th>Qty</th>
                                                                        <th>Total</th>
                                                                        <th>Date</th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>
                                                                    <template v-for="(item, index) in item.items"
                                                                        :key="index">
                                                                        <tr>
                                                                            
                                                                            <td>{{ item.stock_type }}</td>
                                                                            <td>{{ item.priceRate }}</td>
                                                                            <td>{{ item.purchaseQty }}</td>
                                                                            <td>{{ item.totalCost }}</td>
                                                                            <td>{{ new Date(item.date_created).toLocaleDateString('en-GB') }}</td>
                                                                        </tr>
                                                                    </template>
                                                                </tbody>
                                                            </table>                                                            
                                                        </td>
                                                    </tr>
                                                </template>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>

                        </div>
                        <div id="supplier" class="tab-pane">
                            <div id="supplier" class="tab-pane">
                                <div class="row">
                                    <div class="col-md-3">
                                        <form @submit.prevent="saveSupplier">
                                            <div class="mb-3">
                                                <label for="name" class="form-label">Name</label>
                                                <input type="text" class="form-control" id="name" v-model="supplier.name"
                                                    required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="contact" class="form-label">Contact</label>
                                                <input type="text" class="form-control" id="contact"
                                                    v-model="supplier.contact" required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="email" class="form-label">Email</label>
                                                <input type="email" class="form-control" id="email" v-model="supplier.email"
                                                    required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="address" class="form-label">Address</label>
                                                <input type="text" class="form-control" id="address"
                                                    v-model="supplier.address" required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="tinno" class="form-label">TIN No.</label>
                                                <input type="text" class="form-control" id="tinno" v-model="supplier.tinno"
                                                    required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="is-available" class="form-label">Availability</label>
                                                <select class="form-select" id="is-available" v-model="supplier.isAvailable"
                                                    required>
                                                    <option value="">-- Select --</option>
                                                    <option value=true>Yes</option>
                                                    <option value=false>No</option>
                                                </select>
                                            </div>
                                            <button type="submit" class="btn btn-primary">{{ isUpdatingSupplier ? 'Update' :
                                                'Save' }}</button>
                                        </form>

                                    </div>
                                    <div class="col-md-9"
                                        style=" height: 600px ;max-height: 600px;overflow-y: auto;overflow-x: hidden;padding-right: 1px;">
                                        <div class="input-group mt-2">
                                            <input type="text" class="form-control" placeholder="Search Supplier"
                                                v-model="searchSupplier">
                                            <div class="input-group-append">
                                                <button class="btn btn-outline-secondary" type="button">
                                                    <i class="fa fa-search"></i>
                                                </button>
                                            </div>
                                        </div>
                                        <table class="table">
                                            <thead>
                                                <tr>
                                                    <th>Name</th>
                                                    <th>Contact</th>
                                                    <th>Email</th>
                                                    <th>Address</th>
                                                    <th>TIN No.</th>
                                                    <th>Is Available?</th>
                                                    <th>Action</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr v-for="supplier in filteredsuppliers" :key="supplier.id">
                                                    <td>{{ supplier.name }}</td>
                                                    <td>{{ supplier.contact }}</td>
                                                    <td>{{ supplier.email }}</td>
                                                    <td>{{ supplier.address }}</td>
                                                    <td>{{ supplier.tinno }}</td>
                                                    <td v-if="supplier.isAvailable">Yes</td>
                                                    <td v-else>No</td>
                                                    <td>
                                                        <button type="button" class="btn btn-primary btn-sm"
                                                            @click="editSupplier(supplier.id)"><i
                                                                class="fas fa-edit"></i></button>&nbsp;
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>

                                    </div>
                                </div>
                            </div>
                        </div>
                        <div id="purchases" class="tab-pane">
                            <div id="purchases" class="tab-pane">
                                <div class="row">
                                    <div class="col-md-5">
                                        <form>
                                            <div class="mb-3">
                                                <h4>Supplier </h4>
                                                <hr />
                                                <v-select :options="suppliers" label="name" v-model="purchase.supplier"
                                                    required>
                                                </v-select>
                                            </div>

                                            <h4>Product Details</h4>
                                            <hr />
                                            <div class="form-group row" v-for="(item, index) in purchase.items"
                                                :key="index">

                                                <div class="col-3">
                                                    <label class="col-form-label">Stock:</label>
                                                    <select class="form-control" v-model="item.stock">
                                                        <option value="">-- Select Stock --</option>
                                                        <option v-for="stock in stocks" :value="stock">{{ stock.name }}
                                                        </option>
                                                    </select>
                                                </div>
                                                <div class="col-3">
                                                    <label class="col-form-label">Price:</label>
                                                    <input type="number" min="0" class="form-control"
                                                        v-model="item.pricePerItem">
                                                </div>
                                                <div class="col-2">
                                                    <label class="col-form-label">Qty:</label>
                                                    <input type="number" min="0" class="form-control"
                                                        v-model="item.quantity">
                                                </div>
                                                <div class="col-3">
                                                    <label class="col-form-label">Total:</label>
                                                    <input type="number" class="form-control" :value="calculatePrice(item)"
                                                        readonly>
                                                </div>
                                                <div class="col-1">
                                                    <label class="col-form-label text-white">.</label>
                                                    <button v-if="index > 0" type="button"
                                                        class="form-control btn btn-danger" @click="removeItem(index, 0)"
                                                        style="width: fit-content;">
                                                        &times;
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="form-group row">
                                                <div class="col-12 d-flex justify-content-end mt-3">

                                                    <a href="#" @click="addItem(0)">+ Add More</a>
                                                </div>
                                            </div>

                                            <button type="button" @click.prevent="addPurchases()"
                                                class="btn btn-primary">Add to Purchases</button>

                                        </form>



                                    </div>
                                    <div class="col-md-7">
                                        <table class="table">
                                            <thead>
                                                <tr>
                                                    <th>Purchase #</th>
                                                    <th>Supplier</th>
                                                    <th>Total Purchased Price</th>
                                                    <th>Purchased Date</th>
                                                    <th>Action</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <template v-for="item in purchases" :key="item.id">
                                                    <tr>
                                                        <td>{{ item.id }}</td>
                                                        <td>{{ item.supplier_name }}</td>
                                                        <td>{{ item.totalPrice }}</td>
                                                        <td>{{ new Date(item.date_created).toLocaleDateString('en-GB') }}</td>
                                                        <td>
                                                            <button type="button" @click="toggleTable(item.id)"
                                                                class="btn btn-primary btn-sm">
                                                                <span v-if="!showTable[item.id]">+</span>
                                                                <span v-else>-</span>
                                                            </button>
                                                        </td>
                                                    </tr>

                                                    <tr v-if="showTable[item.id]">
                                                        <td colspan="6">
                                                            <h5 class="bg-primary text-white">Items</h5>
                                                            <table class="table"
                                                                style="table-layout: fixed;word-wrap: break-word;">
                                                                <thead>
                                                                    <tr>
                                                                        <th>SKU</th>
                                                                        <th>Name</th>
                                                                        <th>Price</th>
                                                                        <th>Qty</th>
                                                                        <th>Total</th>
                                                                        <th>Date</th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>
                                                                    <template v-for="(item, index) in item.items"
                                                                        :key="index">
                                                                        <tr>
                                                                            <td>{{ item.stock_sku }}</td>
                                                                            <td>{{ item.stock_name }}</td>
                                                                            <td>{{ item.priceRate }}</td>
                                                                            <td>{{ item.purchaseQty }}</td>
                                                                            <td>{{ item.totalCost }}</td>
                                                                            <td>{{ new Date(item.date_created).toLocaleDateString('en-GB') }}</td>
                                                                        </tr>
                                                                    </template>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </template>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div id="sales" class="tab-pane">
                            <div id="sales" class="tab-pane">
                                <div class="row">
                                    <div class="col-md-5">
                                        <form>
                                            <div class="mb-3">
                                                <h4>Customer </h4>
                                                <hr />
                                                <input type="text" class="form-control" v-model="sale.customer.name">
                                            </div>

                                            <h4>Product Details</h4>
                                            <hr />
                                            <div class="form-group row" v-for="(item, index) in sale.items" :key="index">

                                                <div class="col-3">
                                                    <label class="col-form-label">Stock:</label>
                                                    <select class="form-control" v-model="item.stock">
                                                        <option value="">-- Select Stock --</option>
                                                        <option v-for="stock in stocks" :value="stock">{{ stock.name }}
                                                        </option>
                                                    </select>
                                                </div>
                                                <div class="col-3">
                                                    <label class="col-form-label">Price:</label>
                                                    <input type="number" min="0" class="form-control"
                                                        v-model="item.pricePerItem">
                                                </div>
                                                <div class="col-2">
                                                    <label class="col-form-label">Qty:</label>
                                                    <input type="number" min="0" class="form-control"
                                                        v-model="item.quantity">
                                                </div>
                                                <div class="col-3">
                                                    <label class="col-form-label">Total:</label>
                                                    <input type="number" class="form-control" :value="calculatePrice(item)"
                                                        readonly>
                                                </div>
                                                <div class="col-1">
                                                    <label class="col-form-label text-white">.</label>
                                                    <button v-if="index > 0" type="button"
                                                        class="form-control btn btn-danger" @click="removeItem(index, 1)"
                                                        style="width: fit-content;">
                                                        &times;
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="form-group row">
                                                <div class="col-12 d-flex justify-content-end mt-3">

                                                    <a href="#" @click="addItem(1)">+ Add More</a>
                                                </div>
                                            </div>

                                            <button type="button" @click.prevent="addSales()" class="btn btn-primary">Add to
                                                Sales</button>

                                        </form>
                                    </div>
                                    <div class="col-md-7">
                                        <table class="table">
                                            <thead>
                                                <tr>
                                                    <th>Invoice #</th>
                                                    <th>Customer</th>
                                                    <th>Total</th>
                                                    <th>Transaction Date</th>
                                                    <th>Action</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <template v-for="item in sales" :key="item.id">
                                                    <tr>
                                                        <td>{{ item.id }}</td>
                                                        <td>{{ item.customer_name }}</td>
                                                        <td>{{ item.totalPrice }}</td>
                                                        <td>{{ new Date(item.date_created).toLocaleDateString('en-GB') }}</td>
                                                        <td>
                                                            <button type="button" @click="toggleTable2(item.id)"
                                                                class="btn btn-primary btn-sm">
                                                                <span v-if="!showTable2[item.id]">+</span>
                                                                <span v-else>-</span>
                                                            </button>
                                                        </td>
                                                    </tr>

                                                    <tr v-if="showTable2[item.id]">
                                                        <td colspan="6">
                                                            <h5 class="bg-primary text-white">Items</h5>
                                                            <table class="table"
                                                                style="table-layout: fixed;word-wrap: break-word;">
                                                                <thead>
                                                                    <tr>
                                                                        <th>SKU</th>
                                                                        <th>Name</th>
                                                                        <th>Price</th>
                                                                        <th>Qty</th>
                                                                        <th>Total</th>
                                                                        <th>Date</th>
                                                                    </tr>
                                                                </thead>
                                                                <tbody>
                                                                    <template v-for="(item, index) in item.items"
                                                                        :key="index">
                                                                        <tr>
                                                                            <td>{{ item.stock_sku }}</td>
                                                                            <td>{{ item.stock_name }}</td>
                                                                            <td>{{ item.priceRate }}</td>
                                                                            <td>{{ item.purchaseQty }}</td>
                                                                            <td>{{ item.totalCost }}</td>
                                                                            <td>{{ new Date(item.date_created).toLocaleDateString('en-GB') }}</td>
                                                                        </tr>
                                                                    </template>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </template>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>



    </div>
</template>
  
<script>
import { useAuthStore } from "@/stores/authStore";
import axios from 'axios';

export default {
    data() {
        return {
            showTable: {},
            showTable2: {},
            showTable3:{},
            stocks: [],
            suppliers: [],
            purchases: [],
            sales: [],
            sale: {
                customer: {
                    name: '',
                },
                items: [
                    { stock: '', pricePerItem: 0, quantity: 0 },
                ],
            },
            purchase: {
                supplier: {
                    name: '',
                },
                items: [
                    { stock: '', pricePerItem: 0, quantity: 0 },
                ],
            },
            stock: {
                name: "",
                description: "",
                sku: "",
                category: "",
                quantity: 0,
                isAvailable: ""
            },
            supplier: {
                id: null,
                name: "",
                contact: "",
                email: "",
                address: "",
                tinno: "",
                isAvailable: ""
            },
            isUpdatingInventory: false,
            isUpdatingSupplier: false,
            searchInventory: '',
            searchSupplier: '',
        };
    },
    created() {
        this.getInventory();
        this.getSuppliers();
        this.getPurchases();
        this.getSales();
    },
    computed: {
        userdata() {
            const authStore = useAuthStore();
            const user = authStore.user;
            return user;
        },
        totalPurchasePrice() {

        },
        filteredstocks() {
            return this.stocks.map(o => {
                const searchCode = Object.values(o).join("~");
                return {
                    ...o,
                    searchCode
                };
            }).filter(item => item.searchCode.toString().toLowerCase().includes(this.searchInventory.toLowerCase()));
        },
        filteredsuppliers() {
            return this.suppliers.map(o => {
                const searchCode = Object.values(o).join("~");
                return {
                    ...o,
                    searchCode
                };
            }).filter(item => item.searchCode.toString().toLowerCase().includes(this.searchSupplier.toLowerCase()));
        },
    },
    methods: {
        async toggleTable(id) {
            this.showTable[id] = !this.showTable[id];
            if (this.showTable[id]) {
                try {
                    const response = await axios.post(`${this.API_URL}inventory/item/filter/`, [
                        { "columnName": "purchase_id", "columnKey": id },
                    ])
                    const o = response.data;
                    this.purchases = this.purchases.map(t => {

                        if (t.id === id) {
                            t.items = o;
                        }

                        return t;
                    });

                } catch (error) {

                }

            }
        },
        async toggleTable2(id) {
            this.showTable2[id] = !this.showTable2[id];
            if (this.showTable2[id]) {
                try {
                    const response = await axios.post(`${this.API_URL}inventory/item/filter/`, [
                        { "columnName": "sales_id", "columnKey": id },
                    ])
                    const o = response.data;
                    this.sales = this.sales.map(t => {

                        if (t.id === id) {
                            t.items = o;
                        }

                        return t;
                    });

                } catch (error) {

                }

            }
        },
        async toggleTable3(id) {
            this.showTable3[id] = !this.showTable3[id];
            if (this.showTable3[id]) {
                try {
                    const response = await axios.post(`${this.API_URL}inventory/item/filter/`, [
                        { "columnName": "stock_id", "columnKey": id },
                    ])
                    const o = response.data;
                    this.stocks = this.stocks.map(t => {

                        if (t.id === id) {
                            t.items = o;
                        }

                        return t;
                    });

                } catch (error) {

                }

            }
        },
        addItem(o) {
            const arr = (o === 0) ? this.purchase : this.sale;
            arr.items.push({ stock: '', pricePerItem: null, quantity: null });
        },
        removeItem(index, o) {
            const arr = (o === 0) ? this.purchase : this.sale;
            arr.items.splice(index, 1);
        },
        calculatePrice(item) {
            return item.pricePerItem * item.quantity;
        },
        async logout() {
            const authStore = useAuthStore();
            const user = {
                username: authStore.user.username,
                FirstName: authStore.user.fName,
                LastName: authStore.user.lName,
                role: authStore.user.role
            }
            const response = await axios.put(`${this.API_URL}users/${authStore.user.id}/`, { ...user, isActive: false })
            if (response.data !== undefined) {
                authStore.logout();
                this.$router.push('/');
            } else {
                this.$swal({
                    icon: "error",
                    title: "Logout error. Please contact your admin for assistance!"
                });
            }
        },
        addSales() {
            if (this.sale.customer.name === "") {
                this.$swal({
                    icon: "error",
                    title: "Supply customer name!"
                });
                return;
            }
            for (const item of this.sale.items) {
                if (item.stock.name === undefined || item.pricePerItem === null || item.quantity < 1) {
                    this.$swal({
                        icon: "error",
                        title: "Invalid product details!"
                    });
                    return;
                }
            }

            const data = {
                customer_name: this.sale.customer.name,
                totalPrice: this.sale.items.reduce((acc, item) => {
                    return acc + item.pricePerItem * item.quantity;
                }, 0)
            }
            axios
                .post(`${this.API_URL}sales/`, data)
                .then(response => {
                    this.sale.items.forEach(async (item, index) => {
                        const api = `${this.API_URL}inventory/item/`;
                        const itemsdata = {
                            customer_name: data.customer_name,
                            sales_id: response.data.id,
                            stock_id: item.stock.id,
                            stock_sku: item.stock.sku,
                            stock_name: item.stock.name,
                            priceRate: item.pricePerItem,
                            purchaseQty: item.quantity,
                            stock_type: "stock-out",
                            totalCost: this.calculatePrice(item)
                        }
                        try {
                            await axios.post(api, itemsdata);
                            const response = await axios.get(`${this.API_URL}stockitem/${itemsdata.stock_id}/`);
                            await axios.put(`${this.API_URL}stockitem/${itemsdata.stock_id}/`,{
                                ...response.data,
                                quantity : parseFloat(response.data.quantity) - itemsdata.purchaseQty
                            });
                            this.getInventory();
                        } catch (error) {

                        }
                    });
                    this.$swal({
                        icon: "success",
                        title: "Transaction added successfully"
                    });
                    this.sale = {
                        customer: {
                            name: '',
                        },
                        items: [
                            { stock: '', pricePerItem: 0, quantity: 0 },
                        ],
                    }
                    this.getSales();
                })
                .catch(error => {
                    console.log(error);
                });
        },
        addPurchases() {
            if (this.purchase.supplier.name === "") {
                this.$swal({
                    icon: "error",
                    title: "Supply supplier name!"
                });
                return;
            }
            for (const item of this.purchase.items) {
                if (item.stock.name === undefined || item.pricePerItem === null || item.quantity < 1) {
                    this.$swal({
                        icon: "error",
                        title: "Invalid product details!"
                    });
                    return;
                }
            }

            const data = {
                supplier_id: this.purchase.supplier.id,
                supplier_name: this.purchase.supplier.name,
                totalPrice: this.purchase.items.reduce((acc, item) => {
                    return acc + item.pricePerItem * item.quantity;
                }, 0)
            }
            axios
                .post(`${this.API_URL}purchases/`, data)
                .then(response => {
                    this.purchase.items.forEach(async (item, index) => {
                        const api = `${this.API_URL}inventory/item/`;
                        const itemsdata = {
                            supplier_id: data.supplier_id,
                            supplier_name: data.supplier_name,
                            purchase_id: response.data.id,
                            stock_id: item.stock.id,
                            stock_sku: item.stock.sku,
                            stock_name: item.stock.name,
                            priceRate: item.pricePerItem,
                            purchaseQty: item.quantity,
                            stock_type: "stock-in",
                            totalCost: this.calculatePrice(item)
                        }
                        try {
                            await axios.post(api, itemsdata);
                            const response = await axios.get(`${this.API_URL}stockitem/${itemsdata.stock_id}/`);
                            await axios.put(`${this.API_URL}stockitem/${itemsdata.stock_id}/`,{
                                ...response.data,
                                quantity : parseFloat(response.data.quantity) + itemsdata.purchaseQty
                            });
                            this.getInventory();
                        } catch (error) {

                        }
                    });
                    this.$swal({
                        icon: "success",
                        title: "Purchase added successfully"
                    });
                    this.purchase = {
                        supplier: {
                            name: '',
                        },
                        items: [
                            { stock: '', pricePerItem: 0, quantity: 0 },
                        ],
                    }
                    this.getPurchases();
                })
                .catch(error => {
                    console.log(error);
                });
        },
        getInventory() {
            axios
                .get(`${this.API_URL}stockitem/`)
                .then(response => {
                    this.stocks = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        getSuppliers() {
            axios
                .get(`${this.API_URL}supplier/`)
                .then(response => {
                    this.suppliers = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        getPurchases() {
            axios
                .get(`${this.API_URL}purchases/`)
                .then(response => {
                    this.purchases = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        getSales() {
            axios
                .get(`${this.API_URL}sales/`)
                .then(response => {
                    this.sales = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        saveInventory() {
            if (this.isUpdatingInventory) {
                axios
                    .put(`${this.API_URL}stockitem/${this.stock.id}/`, this.stock)
                    .then(response => {
                        this.$swal({
                            icon: "success",
                            title: "Item updated successfully"
                        });
                        this.getInventory();
                        this.stock = {
                            id: null,
                            name: "",
                            description: "",
                            sku: "",
                            category: "",
                            quantity: 0,
                            isAvailable: ""
                        };
                        this.isUpdatingInventory = false;
                    })
                    .catch(error => {
                        console.log(error);
                    });
            } else {
                axios
                    .post(`${this.API_URL}stockitem/filter/`, { columnName: 'name', columnKey: this.stock.name })
                    .then(response => {
                        if (response.data.length > 0) {
                            this.$swal({
                                icon: "error",
                                title: "Item already exists"
                            });
                        } else {
                            axios
                                .post(`${this.API_URL}stockitem/`, this.stock)
                                .then(response => {
                                    this.$swal({
                                        icon: "success",
                                        title: "Item saved successfully"
                                    });
                                    this.getInventory();
                                    this.stock = {
                                        id: null,
                                        name: "",
                                        description: "",
                                        sku: "",
                                        category: "",
                                        quantity: 0,
                                        isAvailable: ""
                                    };
                                })
                                .catch(error => {
                                    console.log(error);
                                });
                        }
                    })
                    .catch(error => {
                        console.log(error);
                    });
            }
        },
        saveSupplier() {
            if (this.isUpdatingSupplier) {
                axios
                    .put(`${this.API_URL}supplier/${this.supplier.id}/`, this.supplier)
                    .then(response => {
                        this.$swal({
                            icon: "success",
                            title: "Supplier updated successfully"
                        });
                        this.getSuppliers();
                        this.supplier = {
                            id: null,
                            name: "",
                            contact: "",
                            email: "",
                            address: "",
                            tinno: "",
                            isAvailable: ""
                        };
                        this.isUpdatingSupplier = false;
                    })
                    .catch(error => {
                        console.log(error);
                    });
            } else {
                axios
                    .post(`${this.API_URL}supplier/filter/`, { columnName: 'name', columnKey: this.supplier.name })
                    .then(response => {
                        if (response.data.length > 0) {
                            this.$swal({
                                icon: "error",
                                title: "Supplier already exists"
                            });
                        } else {
                            axios
                                .post(`${this.API_URL}supplier/`, this.supplier)
                                .then(response => {
                                    this.$swal({
                                        icon: "success",
                                        title: "Supplier saved successfully"
                                    });
                                    this.getSuppliers();
                                    this.supplier = {
                                        id: null,
                                        name: "",
                                        contact: "",
                                        email: "",
                                        address: "",
                                        tinno: "",
                                        isAvailable: ""
                                    };
                                })
                                .catch(error => {
                                    console.log(error);
                                });
                        }
                    })
                    .catch(error => {
                        console.log(error);
                    });
            }
        },

        async logoutUser(item) {
            const user = {
                username: item.username,
                FirstName: item.FirstName,
                LastName: item.LastName,
                role: item.role,
            };

            // Show a confirmation dialog

            const result = await this.$swal.fire({
                title: 'Confirmation',
                text: 'Do you really want to log out this user?',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes, do it!',
                cancelButtonText: 'Cancel'
            });

            if (result.isConfirmed) {
                // User clicked "OK", so proceed with the logout
                await axios.put(`${this.API_URL}users/${item.id}/`, {
                    ...user,
                    isActive: false,
                });
                this.getUsers();
            }
        },
        editInventory(id) {
            axios
                .get(`${this.API_URL}stockitem/${id}/`)
                .then(response => {
                    this.stock = response.data;
                    this.isUpdatingInventory = true;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        editSupplier(id) {
            axios
                .get(`${this.API_URL}supplier/${id}/`)
                .then(response => {
                    this.supplier = response.data;
                    this.isUpdatingSupplier = true;
                })
                .catch(error => {
                    console.log(error);
                });
        },
    },
};
</script>

<style>
@import "vue-select/dist/vue-select.css";
</style>