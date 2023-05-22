<template>
  <div class="container-fluid">
    <TopNavBarComponent />
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="tables-tab" data-bs-toggle="tab" data-bs-target="#tables" type="button"
          role="tab" aria-controls="tables" aria-selected="true" @click="resetCounter">Tables</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="pos-tab" data-bs-toggle="tab" data-bs-target="#pos" type="button" role="tab"
          aria-controls="pos" aria-selected="true">POS</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="inventory-tab" data-bs-toggle="tab" data-bs-target="#inventory" type="button"
          role="tab" aria-controls="inventory" aria-selected="true" @click="resetCounter">Inventory</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="reports-tab" data-bs-toggle="tab" data-bs-target="#reports" type="button" role="tab"
          aria-controls="reports" aria-selected="false" @click="resetCounter">Reports</button>
      </li>
    </ul>

    <div class="tab-content mt-3" id="myTabContent">
      <div class="tab-pane fade show active" id="tables" role="tabpanel" aria-labelledby="tables-tab">
        <div class="row mt-2">
          <div class="col-md-3">
            <ul class="nav bg radius nav-pills nav-fill mb-3 bg mt-3" role="tablist">
              <li class="nav-item">
                <a class="nav-link active show" data-bs-toggle="tab" role="tab" href="#dineintab">
                  <i class="fa fa-tags"></i>Dine-in</a>
              </li>
              <!-- <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#takeouttab">
                  <i class="fa fa-tags"></i>Take Out</a>
              </li> -->
            </ul>
          </div>

          <div class="tab-content" id="myTabContent" style="height: 550px; overflow-y: auto;">
            <div class="tab-pane fade show active" id="dineintab" role="tabpanel" aria-labelledby="dinein-tab">
              <div class="container-fluid">
                <div class="row">
                  <div class="col-md-12">
                    <div class="row row-cols-1 row-cols-md-6">
                      <div class="col mb-6" v-for="(item, index) in filteredresto_tables" :key="item.id">
                        <div class="card" style="transition: transform 0.2s ease-in-out;" @click="dineInAction(item)">
                          <div class="card-header d-flex justify-content-between align-items-center"
                            :style="{ 'background-color': ('order_id' in item) ? '#66bb6a' : '' }">
                            <h5 class="card-title"><i class="fas fa-table"></i> {{ item.name }}</h5>
                          </div>
                          <div class="card-body">
                            <h6 class="text-dark">
                              <i class="fas fa-info-circle"></i> {{ ('order_id' in item) ? 'occupied' : 'vacant' }}
                            </h6>
                          </div>

                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- <div class="tab-pane fade" id="takeouttab" role="tabpanel" aria-labelledby="takeout-tab">
              <div class="container-fluid">
                <div class="row">
                  <div class="col-md-12">
                    
                  </div>
                </div>
              </div>
            </div> -->
          </div>

        </div>
      </div>
      <div class="tab-pane fade" id="pos" role="tabpanel" aria-labelledby="pos-tab">
        <div class="row mt-2">
          <div class="col-md-8">
            <div class="row">
              <div class="col-lg-6 col-sm-6">
                <h4>Point of Sales
                  <span v-if="customer.reference_id !== null">
                    >>>&NonBreakingSpace; <span class="blink_me text-danger" style="font-style: italic;">Now serving: {{
                      customer.identifier }} for {{ customer.type }}</span>
                  </span>
                </h4>
              </div>
              <div class="col-lg-6 col-sm-6">
                <form action="#" class="search-wrap">
                  <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search" v-model="searchText">
                    <div class="input-group-append">
                      <button class="btn btn-primary" type="submit">
                        <i class="fa fa-search"></i>
                      </button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
            <ul class="nav bg radius nav-pills nav-fill mb-3 bg mt-3" role="tablist">
              <li class="nav-item">
                <a class="nav-link active show" data-bs-toggle="tab" data-bs-target="#alltab" role="tab" href="#alltab"
                  @click="setActiveTab('alltab')">
                  <i class="fa fa-tags"></i> All</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category1"
                  @click="setActiveTab('nav-tab-category1')">
                  <i class="fa fa-tags "></i>Main Courses</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category2"
                  @click="setActiveTab('nav-tab-category2')">
                  <i class="fa fa-tags "></i>Appetizers</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category3"
                  @click="setActiveTab('nav-tab-category3')">
                  <i class="fa fa-tags "></i>Desserts</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category4"
                  @click="setActiveTab('nav-tab-category4')">
                  <i class="fa fa-tags "></i>Beverages</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category5"
                  @click="setActiveTab('nav-tab-category5')">
                  <i class="fa fa-tags "></i>Specials</a>
              </li>
            </ul>

            <div class="tab-content" id="myTabContent" style="height: 550px; overflow-y: auto;">
              <div class="tab-pane fade show active" id="alltab" role="tabpanel" aria-labelledby="all-tab">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray" @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category1" role="tabpanel" aria-labelledby="nav-tab-category1">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Main Courses')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category2" role="tabpanel" aria-labelledby="nav-tab-category2">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Appetizers')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category3" role="tabpanel" aria-labelledby="nav-tab-category3">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Desserts')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category4" role="tabpanel" aria-labelledby="nav-tab-category4">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Beverages')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category5" role="tabpanel" aria-labelledby="nav-tab-category5">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Specials')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-4">

            <div class="card" style="height: 215px; overflow-y: auto;">

              <div class="row">
                <div class="col-md-12">
                  <table class="table">
                    <thead>
                      <tr>
                        <th scope="col" style="width: 180px;">Item <span v-if="cartItems.length > 0"
                            class="badge-pill badge-danger">{{ cartItems.length }}</span></th>
                        <th scope="col">Qty</th>
                        <th scope="col">Price</th>
                        <th scope="col">
                          <button v-if="cartItems.length > 0" type="button" @click="clearAll"
                            class="btn btn-sm  btn-danger">
                            <i class="fas fa-trash-alt"></i>
                          </button>
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item, index) in cartItems" :key="index">
                        <td>
                          <div class="row d-flex flex-row">
                            <div class="col-sm-6 text-left">
                              <img :src="item.image" class="img-thumbnail img-xs">
                            </div>
                            <div class="col-sm-6 text-left m-0 p-0 ">
                              <h6 class="text-left title text-truncate" style="font-weight: bold;">{{ item.name }}</h6>
                            </div>
                          </div>
                        </td>
                        <td>
                          <div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
                            <button type="button" class="m-btn btn-light btn btn-default" @click="decreaseQty(item)">
                              <i class="fa fa-minus"></i>
                            </button>
                            <button type="button" class="m-btn btn-light btn btn-default" disabled>
                              {{ item.qty }}
                            </button>
                            <button type="button" class="m-btn btn-light btn btn-default" @click="increaseQty(item)">
                              <i class="fa fa-plus"></i>
                            </button>
                          </div>
                        </td>
                        <td class="text-right">
                          <strong>₱{{ item.totalPrice.toFixed(2) }}</strong>
                        </td>
                        <td>
                          <button class="btn btn-outline-danger btn-sm" type="button" @click="removeFromCart(item)">
                            <i class="fas fa-times"></i>
                          </button>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            <div class="box p-2">
              <div class="row p-0 m-0">
                <div class="col-md-6">
                  <dt>Tax: </dt>
                </div>
                <div class="col-md-6 d-flex flex-row-reverse">
                  <dd class="text-right">{{ taxValue }}%</dd>
                </div>
              </div>
              <div class="row p-0 m-0">
                <div class="col-md-6">
                  <dt>Discount:</dt>
                </div>
                <div class="col-md-6 d-flex flex-row-reverse">
                  <dd class="text-right"><a href="#">{{ discountValue }}%</a></dd>
                </div>
              </div>
              <div class="row p-0 m-0">
                <div class="col-md-6">
                  <dt>Sub Total:</dt>
                </div>
                <div class="col-md-6 d-flex flex-row-reverse">
                  <dd class="text-right">₱{{ subTotal }}</dd>
                </div>
              </div>
              <div class="row p-0 m-0">
                <div class="col-md-6">
                  <dt>Total: </dt>
                </div>
                <div class="col-md-6 d-flex flex-row-reverse">
                  <dd class="text-right h4 b"> ₱{{ totalCost }} </dd>
                </div>
              </div>
            </div> <!-- box.// -->
            <div class="box mt-2">
              <div class="row bg-primary text-white d-flex flex-row-reverse align-items-center">
                <div class="col-md-6">
                  <div class="input-group">
                    <span class="input-group-text bg-primary text-white "
                      style="vertical-align: middle;font-weight: bold;border: none; font-size: x-large;">₱</span>
                    <input :disabled="(cartItems.length < 1)" type="text"
                      class="form-control bg-primary text-white rounded-lg px-2 outline-none"
                      style="text-align:right; font-weight: bold; font-size: x-large; border: none;" v-model="totalCash">
                  </div>
                </div>
                <div class="col-md-6">
                  <dd class="text-right h3 b" style="margin-right: 10px;"> Cash</dd>
                </div>
              </div>
              <div class="row mt-2">
                <div class="col-md-12">
                  <div class="row row-cols-1 row-cols-md-4">
                    <div class="col mb-1" v-for="item in cashDenominations" :key="item.id">
                      <button :disabled="(cartItems.length < 1)"
                        class="btn bg-white rounded-lg shadow hover:shadow-xs focus:outline-none inline-block px-2 py-0 text-sm"
                        @click="addToCash(item.value)"><span>{{
                          item.label }}</span></button>
                    </div>
                  </div>
                </div>
              </div>
              <div
                :class="(totalChange < 0 ? 'row mt-2 mb-2 bg-danger text-white' : 'row mt-2 mb-2 bg-success text-white')">
                <div class="col-md-6">
                  <dt v-if="totalChange >= 0">Change: </dt>
                </div>
                <div class="col-md-6 d-flex flex-row-reverse">
                  <dd class="text-right h4 b"> ₱{{ totalChange }} </dd>
                </div>
              </div>
              <div class="row">
                <div class="col-md-4">
                  <button :disabled="(cartItems.length < 1)" class="btn btn-light btn-default btn-sm btn-block"
                    @click="printBill" style="width: 125px;">
                    <i class="fa fa-print"></i> Print Bill [F1]
                  </button>
                </div>
                <div class="col-md-4">
                  <button :disabled="(cartItems.length < 1)" class="btn btn-danger btn-default btn-sm btn-block"
                    style="width: 125px;" @click="placeOrder">
                    <i class="fa fa-bookmark"></i> Place Order [F2]
                  </button>
                </div>
                <div class="col-md-4 d-flex flex-row-reverse">
                  <button :disabled="(cartItems.length < 1)" class="btn btn-primary btn-sm btn-block" @click="payOrder"
                    style="width: 125px;">
                    <i class="fa fa-shopping-bag"></i> Charge [F3]
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="tab-pane fade" id="inventory" role="tabpanel" aria-labelledby="inventory-tab">
        <div class="row">
          <div class="col-md-3">
            <form @submit.prevent="saveInventory" class="no-print">
              <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" v-model="stock.name" required>
              </div>
              <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <input type="text" class="form-control" id="description" v-model="stock.description">
              </div>
              <div class="mb-3">
                <label for="sku" class="form-label">SKU</label>
                <input type="text" class="form-control" id="SKU" v-model="stock.sku" required>
              </div>
              <div class="mb-3">
                <label for="imgurl" class="form-label">Image URL</label>
                <input type="text" class="form-control" id="imgurl" v-model="stock.imageUrl" required>
              </div>
              <div class="mb-3">
                <label for="is-available" class="form-label">Category</label>
                <select class="form-select" id="is-available" v-model="stock.category" required>
                  <option value="">-- Select --</option>
                  <option value="Main Courses">Main Courses</option>
                  <option value="Appetizers">Appetizers</option>
                  <option value="Desserts">Desserts</option>
                  <option value="Beverages">Beverages</option>
                  <option value="Specials">Specials</option>
                </select>
              </div>

              <div class="mb-3">
                <label for="qty" class="form-label">Qty</label>
                <input type="number" min="0" class="form-control" id="qty" v-model="stock.stocks" required>
              </div>


              <div class="mb-3">
                <label for="price" class="form-label">Price</label>
                <input type="number" min="0" class="form-control" id="price" v-model="stock.price" required>
              </div>

              <div class="mb-3">
                <label for="is-available" class="form-label">Availability</label>
                <select class="form-select" id="is-available" v-model="stock.isAvailable" required>
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
          <div class="col-md-9">
            <div>
              <table-component :mainHeaders=stocksOptions :mainItems="filtereditemarray" :subHeaders="inventorysubitem"
                @edit-action="editInventory" :editable="true" :toggleable="true" :slotsub="true">
                <template #subcontent="{ data }">
                  <table-component :mainHeaders="inventorysubitem" :mainItems="data" />
                </template>
                <template #content="{ data }">
                  <template v-if="data.h === 'isAvailable'">
                    <span v-if="data.dt.isAvailable">Yes</span>
                    <span v-else>No</span>
                  </template>
                  <template v-else="data.h==='imageUrl'">
                    <img :src="data.dt.imageUrl" class="img-thumbnail" style="height: 80px;width: 80px;" />
                  </template>
                </template>
              </table-component>
            </div>
          </div>
        </div>
      </div>
      <div class="tab-pane fade" id="reports" role="tabpanel" aria-labelledby="reports-tab">
        <div class="row">
          <div class="col-sm-1">
            <ul class="nav nav-tabs flex-column">
              <li class="nav-item">
                <a class="nav-link rotated-text active" data-bs-toggle="tab" href="#bytransaction">By Transactions</a>
              </li>
              <li class="nav-item">
                <a class="nav-link rotated-text" data-bs-toggle="tab" href="#byitems">By Items</a>
              </li>
            </ul>
          </div>
          <div class="col-sm-11">
            <div class="tab-content">
              <div id="bytransaction" class="tab-pane active">
                <div class="row">
                  <div class="col-sm-2">
                    <div class="form-group">
                      <label for="date-filter">Date Filter:</label>
                      <select class="form-control" id="date-filter" v-model="resdateFilter">
                        <option value="any">Any</option>
                        <option value="range">Date Range</option>
                      </select>
                      <div v-if="resdateFilter === 'range'">
                        <div class="form-group">
                          <input type="date" class="form-control" v-model="resfromDate">
                        </div>
                        <div class="form-group">
                          <input type="date" class="form-control" v-model="restoDate">
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-10">
                    <table-component :mainHeaders=transactionsOptions :mainItems="superfilteredTransactions"
                      :subHeaders="transactionitem" :toggleable="true" />
                  </div>
                </div>
              </div>
              <div id="byitems" class="tab-pane">
                <div class="row">
                  <div class="col-sm-2">
                    <div class="form-group">
                      <label for="date-filter">Date Filter:</label>
                      <select class="form-control" id="date-filter" v-model="resitemdateFilter">
                        <option value="any">Any</option>
                        <option value="range">Date Range</option>
                      </select>
                      <div v-if="resitemdateFilter === 'range'">
                        <div class="form-group">
                          <input type="date" class="form-control" v-model="resitemfromDate">
                        </div>
                        <div class="form-group">
                          <input type="date" class="form-control" v-model="resitemtoDate">
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-10">
                    <table-component :mainHeaders=transactionitem :mainItems="itemfilteredTransactions" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>


  </div>

  <div style="display:none;">
    <div class="container" id="billing-statement">
      <div class="row">
        <div class="col-md-3 offset-md-3">
          <div class="card">
            <div class="card-header text-center">
              <h4 class="m-0 p-0" style="font-weight: bold;">Waterworld Pantukan</h4>
              <h6 class="m-0 p-0">Magnaga, Pantukan, Davao de Oro</h6>
              <h6 class="m-0 p-0" style="font-weight: bold;">Billing Statement Receipt</h6>
              <p class="m-0 p-0">{{ transactionDate }}</p>
            </div>
            <div class="card-body">
              <h5 class="text-center">{{ customerName }}</h5>
              <table class="table" style="border-style: none; border-width: 0px;">
                <thead>
                  <tr>
                    <th>Item</th>
                    <th>Quantity</th>
                    <th>Price</th>
                    <th>Total</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, index) in cartItems" :key="index">
                    <td>{{ item.name }}</td>
                    <td>{{ item.qty }}</td>
                    <td>{{ item.price }}</td>
                    <td>{{ item.totalPrice }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="card-footer text-center">
              <p class="m-0 p-0 d-flex justify-content-end">Subtotal: {{ subTotal }}</p>
              <p class="m-0 p-0 d-flex justify-content-end">Discount: {{ discountValue }}</p>
              <p class="m-0 p-0 d-flex justify-content-end">Tax: {{ taxValue }}</p>
              <p class="m-0 p-0 d-flex justify-content-end">Total: {{ totalCost }}</p>
              <p class="text-center m-0 p-0">
                ===================================
              </p>
              <p>Thank you for your purchase!</p>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { useAuthStore } from "@/stores/authStore";
import TopNavBarComponent from "@/components/common/TopNavBar.vue";
import TableComponent from "@/components/common/GenericTable.vue";
import CardItems from "../common/CardItems.vue";
import axios from 'axios';

//helper functions
function parseDate(dateString) {
  const [day, month, year] = dateString.split('/');
  return new Date(`${year}-${month}-${day}`).setHours(0, 0, 0, 0);
}

function parseDate2(dateString) {
  const index = dateString.indexOf('T');
  const result = dateString.substring(0, index);
  const [year, month, day] = result.split('-');
  return new Date(`${year}-${month}-${day}`).setHours(0, 0, 0, 0);
}

function formatDate(date) {
  const options = {
    month: '2-digit',
    day: '2-digit',
    year: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
    second: 'numeric'
  };
  return new Intl.DateTimeFormat('en-US', options).format(date);
}

export default {
  components: {
    TopNavBarComponent,
    TableComponent,
    CardItems,
  },
  data() {
    return {
      restypeFilter: "0",
      resdateFilter: "any",
      resfromDate: null,
      restoDate: null,
      customer: {
        reference_id: null,
        type: '',
        identifier: '',
        order_type: '',
        items: [],
      },
      orderStaus: false,
      searchText: "",
      isUpdatingInventory: false,
      stock: {
        name: "",
        imageUrl: "",
        description: "",
        sku: "",
        category: "",
        stocks: 0,
        price: 0,
        inventory: "",
        isAvailable: "",
      },
      transactionitem: [{
        'label': 'Name',
        'field': 'name',
      }, {
        'label': 'Category',
        'field': 'category',
      }, {
        'label': 'Qty',
        'field': 'qty',
      }, {
        'label': 'Price',
        'field': 'price',
      }, {
        'label': 'Total',
        'field': 'totalPrice',
      }],
      transactionsOptions: [{
        'label': '',
        'field': 'toggle',
        'sortable': false,
      }, {
        'label': 'Transaction ID',
        'field': 'id',
        'sortable': true,
      }, {
        'label': 'Sub-Total',
        'field': 'subTotal',
        'sortable': true,
        'reducible': true
      }, {
        'label': 'Tax Value',
        'field': 'taxValue',
        'sortable': true,
      }, {
        'label': 'Discount Value',
        'field': 'discountValue',
        'sortable': true,
      }, {
        'label': 'Total',
        'field': 'totalCharge',
        'sortable': true,
        'reducible': true
      }, {
        'label': 'Date',
        'field': 'date_created',
        'sortable': true,
      }, {
        'label': 'Processed By',
        'field': 'processedBy',
        'sortable': true,
      }],
      stocksOptions: [{
        'label': '',
        'field': 'toggle',
        'sortable': false,
      }, {
        'label': 'Image',
        'field': 'imageUrl',
        'slot': true,
      }, {
        'label': 'Name',
        'field': 'name',
        'sortable': true
      }, {
        'label': 'Description',
        'field': 'description',
        'sortable': true
      }, {
        'label': 'SKU',
        'field': 'sku',
        'sortable': true
      }, {
        'label': 'Category',
        'field': 'category',
        'sortable': true
      }, {
        'label': 'Qty',
        'field': 'stocks',
        'sortable': true
      }, {
        'label': 'Price',
        'field': 'price',
        'sortable': true
      }, {
        'label': 'Is Available?',
        'field': 'isAvailable',
        'sortable': true,
        'slot': true,
      }, {
        'label': '',
        'field': 'action',
        'sortable': false
      }],
      inventorysubitem: [{
        'label': 'Type',
        'field': 'type',
      }, {
        'label': 'Qty',
        'field': 'qty',
      }, {
        'label': 'Stocks',
        'field': 'stocks',
      }, {
        'label': 'processedBy',
        'field': 'processedBy',
      }, {
        'label': 'Date',
        'field': 'date_created',
      },],
      activeTab: 'alltab',
      taxValue: 12,
      discountValue: 0,
      totalCash: 0,
      resto_order: [

      ],
      resto_tables: [

      ],
      itemarray: [

      ],
      cartItems: [

      ],
      transactions: [

      ],
      cashDenominations: [{
        'label': '+1.00',
        'value': 1,
      }, {
        'label': '+5.00',
        'value': 5,
      }, {
        'label': '+10.00',
        'value': 10,
      }, {
        'label': '+20.00',
        'value': 20,
      }, {
        'label': '+50.00',
        'value': 50,
      }, {
        'label': '+100.00',
        'value': 100,
      }, {
        'label': '+500.00',
        'value': 500,
      }, {
        'label': '+1000.00',
        'value': 1000,
      },],
    }
  },
  created() {
    this.getInventory();
    this.getTransaction();
    this.getRestoTables();
    this.getCurrentOrders();
  },
  computed: {
    userdata() {
      const authStore = useAuthStore();
      const user = authStore.user;
      return user;
    },
    subTotal() {
      return this.cartItems.reduce((acc, item) => acc + parseFloat(item.totalPrice), 0).toFixed(2);
    },
    totalCost() {
      return (this.subTotal * (1 + this.taxValue / 100) * (1 - this.discountValue / 100)).toFixed(2);
    },
    totalChange() {
      return (this.totalCash - this.totalCost).toFixed(2);
    },
    filteredresto_tables() {
      return this.resto_tables.map(item => {
        const order = this.resto_order.filter(o => o.table_id === item.id);
        if (order.length > 0) {
          const order_data = order[0];
          const order_id = order_data.id;
          const order_type = order_data.order_type;
          const order_cname = order_data.customer_name;
          const order_status = order_data.status;
          const order_items = JSON.parse(order_data.items);
          return {
            ...item,
            order_id,
            order_type,
            order_cname,
            order_status,
            order_items,
          };
        } else {
          return {
            ...item,
          };
        }
      })
    },
    filtereditemarray() {
      return this.itemarray.map(item => {
        const searchCode = item.name + "~" + item.description;
        const items = JSON.parse(item.inventory);
        return {
          ...item,
          items,
          searchCode
        };
      }).filter(item => item.searchCode.toString().toLowerCase().includes(this.searchText.toLowerCase()));
    },
    superfilteredTransactions() {

      let filtered = this.filteredTransactions;
      if (this.resdateFilter === 'range' && this.resfromDate && this.restoDate) {
        filtered = filtered.filter(transaction => {
          return parseDate2(transaction.date_created) >= parseDate(this.resfromDate) && parseDate2(transaction.date_created) <= parseDate(this.restoDate);
        });
      }

      return filtered;
    },
    itemfilteredTransactions(){
      let itemsArray = [];
      let filtered = this.transactions.map(item => {
        const items = JSON.parse(item.items);
        return {
          ...item,
          items
        };
      })
      for (let obj of filtered) {
        for (let key in obj) {
          if (key === "items") {
            itemsArray.push(...obj[key]);
          }
        }
      }
      return itemsArray
    },
    filteredTransactions() {
      return this.transactions.map(item => {
        const items = JSON.parse(item.items);
        return {
          ...item,
          items
        };
      })
    },
  },
  methods: {
    setActiveTab(tab) {
      this.activeTab = tab
    },
    dineInAction(item) {
      this.customer = {
        reference_id: item.id,
        type: "dine-in",
        identifier: item.name,
      }
      if ('order_id' in item) {
        this.cartItems = item.order_items;
        this.customer.order_id = item.order_id;
        this.customer.order_type = item.order_type;
      }
      this.customer.items = (item.order_items || []);
      $("#pos-tab").tab('show');
    },
    async placeOrder() {

      if (this.customer.reference_id === null) {
        $("#tables-tab").tab('show');
        return;
      }

      const confirmMessage = 'Are you sure you want to place this order?';
      const result = await this.$swal.fire({
        title: 'Confirmation',
        text: confirmMessage,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, place it!',
        cancelButtonText: 'Cancel'
      });

      if (result.isConfirmed) {
        const countdownMessage = 'Order will be saved in <span id="countdown">5</span> seconds. Do you want to cancel?';
        let countdownResult;
        countdownResult = await this.$swal.fire({
          title: 'Please wait',
          html: countdownMessage,
          icon: 'info',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Confirm now',
          cancelButtonText: 'Cancel',
          didOpen: () => {
            const countdownEl = document.querySelector('#countdown');
            let count = 5;
            const timerId = setInterval(() => {
              countdownEl.textContent = count;
              count--;
              if (count < 0) {
                clearInterval(timerId);
                this.$swal.close();
              }
            }, 1000);
          }
        });

        if (!countdownResult.isConfirmed) {
          return;
        }

        const customer = this.customer;
        const customer_id = customer.reference_id;
        const customer_type = customer.type;
        const customer_name = customer.identifier;
        const customer_orderId = customer.order_id || -1;
        if (customer_id !== null) {
          if (customer_type === "dine-in") {

            const res = await axios.post(`${this.API_URL}restoorders/filter/`, { columnName: 'id', columnKey: customer_orderId });
            const existingOrder = res.data;
            if (existingOrder.length > 0) {

              for (const item of (this.cartItems || this.cartItems.filter(item => !this.customer.items.includes(item)))) {
                const items = item.inventory;
                const curstock = parseFloat(item.stocks) - parseFloat(item.qty);
                const prevstock = parseFloat(items[items.length - 1].stocks);
                if (prevstock - curstock > 0) {
                  items.push({ "type": "stockout", "qty": prevstock - curstock, "stocks": curstock, "date_created": formatDate(new Date()), "processedBy": (this.userdata.fName + " " + this.userdata.lName).toString() });
                }
                const inventory = JSON.stringify(items);
                axios
                  .put(`${this.API_URL}restoitem/${item.id}/`, {
                    sku: item.sku,
                    name: item.name,
                    description: item.description,
                    imageUrl: item.image,
                    category: item.category,
                    price: item.price,
                    inventory: inventory,
                    isAvailable: item.isAvailable,
                    stocks: parseFloat(item.stocks) - parseFloat(item.qty),
                  });
              }

              axios
                .put(`${this.API_URL}restoorders/${existingOrder[0].id}/`, {
                  order_type: customer_type,
                  table_id: customer_id,
                  customer_name: customer_name,
                  status: 'progress',
                  items: JSON.stringify(this.cartItems),
                  processedBy: this.userdata.fName + " " + this.userdata.lName,
                })

              this.$swal({
                title: 'Success',
                icon: "success",
                title: "Order updated successfully!"
              }).then((result) => {
                document.location.reload();
              });

            } else {

              for (const item of this.cartItems) {
                const items = item.inventory;
                const curstock = parseFloat(item.stocks) - parseFloat(item.qty);
                const prevstock = parseFloat(items[items.length - 1].stocks);
                if (prevstock - curstock > 0) {
                  items.push({ "type": "stockout", "qty": prevstock - curstock, "stocks": curstock, "date_created": formatDate(new Date()), "processedBy": (this.userdata.fName + " " + this.userdata.lName).toString() });
                }
                const inventory = JSON.stringify(items);
                axios
                  .put(`${this.API_URL}restoitem/${item.id}/`, {
                    sku: item.sku,
                    name: item.name,
                    description: item.description,
                    imageUrl: item.image,
                    category: item.category,
                    price: item.price,
                    inventory: inventory,
                    isAvailable: item.isAvailable,
                    stocks: parseFloat(item.stocks) - parseFloat(item.qty),
                  });
              }

              axios
                .post(`${this.API_URL}restoorders/`, {
                  order_type: customer_type,
                  table_id: customer_id,
                  customer_name: customer_name,
                  status: 'progress',
                  items: JSON.stringify(this.cartItems),
                  processedBy: this.userdata.fName + " " + this.userdata.lName,
                })

              this.$swal({
                title: 'Success',
                icon: "success",
                title: "Order placed successfully!"
              }).then((result) => {
                document.location.reload();
              });

            }

            // this.clearAll();
            // this.getCurrentOrders();
            // this.getRestoTables();
            // this.getInventory();
            // $("#tables-tab").tab('show');

            //document.location.reload();

          } else {
            //take-out
          }
        }

      }

    },
    addToCash(d) {
      this.totalCash = isNaN(parseFloat(this.totalCash)) ? 0 : parseFloat(this.totalCash) + d;
    },
    clearAll() {
      this.customer = {
        reference_id: null,
        type: '',
        identifier: '',
        order_type: '',
        items: [],
      },
        this.cartItems = [];
      this.totalCash = 0;
    },
    resetCounter() {
      this.clearAll();
      this.customer = {
        reference_id: null,

      }
    },
    async payOrder() {
      if (this.totalCash < this.totalCost) {
        this.$swal({
          title: 'Warning',
          text: 'The tendered amount is less than the total cost.',
          icon: 'warning',
        });
        return;
      }

      const confirmMessage = 'Are you sure you want to save this transaction?';
      const result = await this.$swal.fire({
        title: 'Confirmation',
        text: confirmMessage,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, save it!',
        cancelButtonText: 'Cancel'
      });
      if (result.isConfirmed) {
        const countdownMessage = 'Transaction will be saved in <span id="countdown">5</span> seconds. Do you want to cancel?';
        let countdownResult;
        countdownResult = await this.$swal.fire({
          title: 'Please wait',
          html: countdownMessage,
          icon: 'info',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Confirm now',
          cancelButtonText: 'Cancel',
          didOpen: () => {
            const countdownEl = document.querySelector('#countdown');
            let count = 5;
            const timerId = setInterval(() => {
              countdownEl.textContent = count;
              count--;
              if (count < 0) {
                clearInterval(timerId);
                this.$swal.close();
              }
            }, 1000);
          }
        });

        if (!countdownResult.isConfirmed) {
          return;
        }

        for (const item of (this.cartItems || this.cartItems.filter(item => !this.customer.items.includes(item)))) {
          const items = item.inventory;
          const curstock = parseFloat(item.stocks) - parseFloat(item.qty);
          const prevstock = parseFloat(items[items.length - 1].stocks);
          if (prevstock - curstock > 0) {
            items.push({ "type": "stockout", "qty": prevstock - curstock, "stocks": curstock, "date_created": formatDate(new Date()), "processedBy": (this.userdata.fName + " " + this.userdata.lName).toString() });
          }
          const inventory = JSON.stringify(items);
          axios
            .put(`${this.API_URL}restoitem/${item.id}/`, {
              sku: item.sku,
              name: item.name,
              description: item.description,
              imageUrl: item.image,
              category: item.category,
              price: item.price,
              inventory: inventory,
              isAvailable: item.isAvailable,
              stocks: parseFloat(item.stocks) - parseFloat(item.qty),
            });

        }

        if (this.customer.reference_id !== null) {
          axios
            .put(`${this.API_URL}restoorders/${this.customer.order_id}/`, {
              order_type: this.customer.order_type,
              table_id: this.customer.reference_id,
              customer_name: this.customer.order_cname,
              items: JSON.stringify(this.customer.order_items),
              processedBy: this.userdata.fName + " " + this.userdata.lName,
              status: 'closed',
            })
        }

        axios
          .post(`${this.API_URL}restotransaction/`, {
            taxValue: this.taxValue,
            discountValue: this.discountValue,
            subTotal: this.subTotal,
            totalCharge: this.totalCost,
            totalPay: this.totalCost,
            items: JSON.stringify(this.cartItems),
            processedBy: this.userdata.fName + " " + this.userdata.lName,
          })
          .then(response => {
            this.$swal({
              title: 'Success',
              icon: "success",
              title: "Transaction saved successfully!"
            }).then((result) => {
              document.location.reload();
            });
            // this.clearAll();
            // this.getRestoTables();
            // this.getCurrentOrders();
            // this.getInventory();
            // $("#tables-tab").tab('show');
          })
          .catch(error => {
            console.log(error);
          });
      }
    },
    printBill() {
      this.printSection();
    },
    getInventory() {
      axios
        .get(`${this.API_URL}restoitem/`)
        .then(response => {
          this.itemarray = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getRestoTables() {
      axios
        .get(`${this.API_URL}restotables/`)
        .then(response => {
          this.resto_tables = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getTransaction() {
      axios
        .get(`${this.API_URL}restotransaction/`)
        .then(response => {
          this.transactions = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getCurrentOrders() {
      axios
        .post(`${this.API_URL}restoorders/filter/`, { columnName: 'status', columnKey: 'progress' })
        .then(response => {
          this.resto_order = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    saveInventory() {
      if (this.isUpdatingInventory) {
        axios.get(`${this.API_URL}restoitem/${this.stock.id}/`)
          .then(response => {
            const items = JSON.parse(response.data.inventory);
            const curstock = this.stock.stocks;
            const prevstock = items[items.length - 1].stocks;
            if (curstock < prevstock) {
              items.push({ "type": "stockout", "qty": prevstock - curstock, "stocks": curstock, "date_created": formatDate(new Date()), "processedBy": (this.userdata.fName + " " + this.userdata.lName).toString() });
            } else {
              items.push({ "type": "stockin", "qty": curstock - prevstock, "stocks": curstock, "date_created": formatDate(new Date()), "processedBy": (this.userdata.fName + " " + this.userdata.lName).toString() });
            }
            this.stock.inventory = JSON.stringify(items);
            axios
              .put(`${this.API_URL}restoitem/${this.stock.id}/`, this.stock)
              .then(response => {
                this.$swal({
                  icon: "success",
                  title: "Item updated successfully"
                }).then((result) => {
                  document.location.reload();
                });
                // this.getInventory();
                // this.stock = {
                //   id: null,
                //   name: "",
                //   imageUrl: "",
                //   description: "",
                //   sku: "",
                //   category: "",
                //   stocks: 0,
                //   price: 0,
                //   isAvailable: "",
                // };
                // this.isUpdatingInventory = false;

              })
              .catch(error => {
                console.log(error);
              });
          })
      } else {
        axios
          .post(`${this.API_URL}restoitem/filter/`, { columnName: 'name', columnKey: this.stock.name })
          .then(response => {
            if (response.data.length > 0) {
              this.$swal({
                icon: "error",
                title: "Item already exists"
              });
            } else {
              this.stock.inventory = `[{"type":"stockin","qty":${this.stock.stocks},"stocks":${this.stock.stocks},"date_created":"${formatDate(new Date())}", "processedBy": "${this.userdata.fName + " " + this.userdata.lName}"}]`;
              axios
                .post(`${this.API_URL}restoitem/`, this.stock)
                .then(response => {
                  this.$swal({
                    icon: "success",
                    title: "Item saved successfully"
                  }).then((result) => {
                    document.location.reload();
                  });
                  // this.getInventory();
                  // this.stock = {
                  //   id: null,
                  //   name: "",
                  //   imageUrl: "",
                  //   description: "",
                  //   sku: "",
                  //   category: "",
                  //   stocks: 0,
                  //   price: 0,
                  //   isAvailable: "",
                  // };

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
    editInventory(id) {
      axios
        .get(`${this.API_URL}restoitem/${id}/`)
        .then(response => {
          this.stock = response.data;
          this.isUpdatingInventory = true;
        })
        .catch(error => {
          console.log(error);
        });
    },
    addItemToCart(item) {
      const isItemExist = (this.cartItems.filter(o => o.id === item.id).length > 0);
      const cart = {
        id: item.id,
        sku: item.sku,
        name: item.name,
        description: item.description,
        category: item.category,
        isAvailable: item.isAvailable,
        image: item.imageUrl,
        qty: 1,
        inventory: JSON.parse(item.inventory),
        price: parseFloat(item.price),
        totalPrice: parseFloat(item.price),
        stocks: parseFloat(item.stocks),
      }

      if (item.stocks > 0) {
        if (!isItemExist) {
          this.cartItems.push(cart);
        } else {
          const obj = this.cartItems.find(item => item.id === cart.id);
          obj.qty += (obj.qty < obj.stocks) ? 1 : 0;
          obj.totalPrice = obj.price * obj.qty;
        }
      } else {
        this.$swal({
          title: "Out of Stock",
          text: "The item you are trying to add is currently out of stock.",
          icon: "warning",
          buttons: {
            confirm: "OK",
          },
        });
      }
    },
    increaseQty(item) {
      if (item.qty < item.stocks) {
        item.qty++
        this.updatePrice(item)
      }
    },
    decreaseQty(item) {
      if (item.qty > 1) {
        item.qty--
        this.updatePrice(item)
      }
    },
    removeFromCart(item) {
      const index = this.cartItems.indexOf(item)
      this.cartItems.splice(index, 1)
    },
    updatePrice(item) {
      item.totalPrice = item.qty * item.price
    },
    printSection() {

      // Add Bootstrap stylesheet to the head
      const bootstrapLink = document.createElement('link');
      bootstrapLink.rel = 'stylesheet';
      bootstrapLink.href = 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css';
      document.head.appendChild(bootstrapLink);

      // Create a progress bar element
      const progressBar = document.createElement('div');
      progressBar.className = 'progress fixed-top';
      progressBar.innerHTML = '<div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>';

      // Add the progress bar to the body
      document.body.appendChild(progressBar);
      progressBar.style.zIndex = 1057;
      // Create the overlay element
      const overlay = document.createElement('div');
      overlay.style.position = 'fixed';
      overlay.style.top = 0;
      overlay.style.left = 0;
      overlay.style.width = '100%';
      overlay.style.height = '100%';
      overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
      overlay.style.zIndex = 1056;
      overlay.classList.add('overlay');
      document.body.appendChild(overlay);

      // Track the loading progress of the stylesheet
      let progress = 0;
      const interval = setInterval(() => {
        progress += 10;
        if (progress >= 100) {
          clearInterval(interval);
          // Remove the progress bar
          document.body.removeChild(progressBar);
          // Get the dataTable section and create the print window
          const dataTable = document.getElementById('billing-statement');
          const printElement = document.createElement('div');
          printElement.appendChild(dataTable.cloneNode(true));

          // Open a new window and write the printElement to it
          const printWindow = window.open('', 'Print Window');
          printWindow.document.write('<html><head>');
          printWindow.document.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">');
          printWindow.document.write('<style>html,body{display:none;}.no-print{display: none;} @media print{@page {size: letter; margin: 0; padding: 0;} html,body{display: block;margin: 0; padding: 0;} tr{page-break-inside: auto;} .no-print{display: none;}}</style>');
          printWindow.document.write('</head><body>');
          printWindow.document.write(printElement.innerHTML);
          printWindow.document.write('</body></html>');
          printWindow.document.close();

          // Print the window and close it after printing
          printWindow.onload = function () {
            printWindow.focus();
            printWindow.print();
            printWindow.close();

            // Remove the Bootstrap stylesheet from the head
            document.head.removeChild(bootstrapLink);
            document.body.removeChild(overlay);
          };
        } else {
          // Update the progress bar
          const progressBarChild = progressBar.querySelector('.progress-bar');
          progressBarChild.style.width = `${progress}%`;
          progressBarChild.setAttribute('aria-valuenow', progress);
        }
      }, 200);
    },
    handleKeyPress(event) {
      switch (event.key) {
        case 'F1':
          this.printBill();
          break;
        case 'F2':
          this.placeOrder();
          break;
        case 'F3':
          this.payOrder();
          break;
        default:
          break;
      }
    },
  },
  mounted() {
    document.addEventListener('keydown', this.handleKeyPress);
  },
}
</script>
<style>
.title {
  margin: 0;
  font-size: 1rem;
  line-height: 1.2;
}

.text-truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.media-body {
  margin-left: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

dt,
dd {
  font-size: medium;
}

.badge-pill {
  display: inline-block;
  padding: 0.25em 0.6em;
  font-size: 75%;
  font-weight: 700;
  vertical-align: top;
  line-height: 1;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: 10rem;
  position: relative;
  top: -0.75em;
  left: -0.25em;
}

.blink_me {
  animation: blinker 1s linear infinite;
}

@keyframes blinker {
  50% {
    opacity: 0;
  }
}

.badge-danger { 
  background-color: #dc3545;
  color: #fff;
}

.btn-error {
  color: #ef5f5f;
}
</style>