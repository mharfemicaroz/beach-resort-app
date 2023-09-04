<template>
  <TopNavBarComponent />
  <div class="container-fluid main">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12">
          <ul class="nav nav-tabs justify-content-left no-print">
            <li class="nav-item">
              <a
                class="nav-link active text-center"
                data-bs-toggle="tab"
                href="#inventory"
              >
                <i class="fas fa-warehouse fa-2x"></i>
                <br />
                Inventory
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link text-center"
                data-bs-toggle="tab"
                href="#supplier"
              >
                <i class="fas fa-truck fa-2x"></i>
                <br />
                Supplier
              </a>
            </li>

            <li class="nav-item">
              <a
                class="nav-link text-center"
                data-bs-toggle="tab"
                href="#purchases"
              >
                <i class="fas fa-cart-arrow-down fa-2x"></i>
                <br />
                Purchases
              </a>
            </li>

            <li class="nav-item">
              <a
                class="nav-link text-center"
                data-bs-toggle="tab"
                href="#sales"
              >
                <i class="fas fa-dollar-sign fa-2x"></i>
                <br />
                Sales
              </a>
            </li>
          </ul>
          <div class="tab-content">
            <div id="inventory" class="tab-pane active">
              <div id="inventory" class="tab-pane active">
                <div class="row">
                  <div class="col-md-3">
                    <form @submit.prevent="saveInventory" class="no-print">
                      <div class="mb-3">
                        <label for="name" class="form-label">Name</label>
                        <input
                          type="text"
                          class="form-control"
                          id="name"
                          v-model="stock.name"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="description" class="form-label"
                          >Description</label
                        >
                        <input
                          type="text"
                          class="form-control"
                          id="description"
                          v-model="stock.description"
                        />
                      </div>
                      <div class="mb-3">
                        <label for="sku" class="form-label">SKU</label>
                        <input
                          type="text"
                          class="form-control"
                          id="SKU"
                          v-model="stock.sku"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="is-available" class="form-label"
                          >Category</label
                        >
                        <select
                          class="form-select"
                          id="is-available"
                          v-model="stock.category"
                          required
                        >
                          <option value="">-- Select --</option>
                          <option value="raw-materials">Raw materials</option>
                          <option value="finished-goods">Finished goods</option>
                          <option value="supplies">Supplies</option>
                          <option value="equipment">Equipment</option>
                          <option value="parts-and-components">
                            Parts and components
                          </option>
                        </select>
                      </div>

                      <div class="mb-3">
                        <label for="is-available" class="form-label"
                          >Availability</label
                        >
                        <select
                          class="form-select"
                          id="is-available"
                          v-model="stock.isAvailable"
                          required
                        >
                          <option value="">-- Select --</option>
                          <option value="true">Yes</option>
                          <option value="false">No</option>
                        </select>
                      </div>
                      <button type="submit" class="btn btn-primary">
                        {{ isUpdatingInventory ? "Update" : "Save" }}
                      </button>
                    </form>
                  </div>
                  <div class="col-md-9">
                    <div class="form-check">
                      <input
                        class="form-check-input"
                        type="checkbox"
                        v-model="showItems"
                      />
                      <label
                        class="form-check-label"
                        for="unavailableItemsCheckbox"
                      >
                        Show available items only?
                      </label>
                    </div>

                    <div>
                      <table-component
                        :mainHeaders="stocksOptions"
                        :mainItems="switchStocks"
                        :subHeaders="stockssubOptions"
                        @edit-action="editInventory"
                        :editable="true"
                        :toggleable="true"
                        @custombtn-action="viewStock"
                        :custombtn="true"
                      >
                        <template #default="{ data }">
                          <span v-if="data.isAvailable">Yes</span>
                          <span v-else>No</span>
                        </template>
                      </table-component>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="card" style="height: 60px !important"></div>
                </div>
              </div>
            </div>
            <div id="supplier" class="tab-pane">
              <div id="supplier" class="tab-pane">
                <div class="row">
                  <div class="col-md-3">
                    <form @submit.prevent="saveSupplier" class="no-print">
                      <div class="mb-3">
                        <label for="name" class="form-label">Name</label>
                        <input
                          type="text"
                          class="form-control"
                          id="name"
                          v-model="supplier.name"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="contact" class="form-label">Contact</label>
                        <input
                          type="text"
                          class="form-control"
                          id="contact"
                          v-model="supplier.contact"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input
                          type="email"
                          class="form-control"
                          id="email"
                          v-model="supplier.email"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="address" class="form-label">Address</label>
                        <input
                          type="text"
                          class="form-control"
                          id="address"
                          v-model="supplier.address"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="tinno" class="form-label">TIN No.</label>
                        <input
                          type="text"
                          class="form-control"
                          id="tinno"
                          v-model="supplier.tinno"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="is-available" class="form-label"
                          >Availability</label
                        >
                        <select
                          class="form-select"
                          id="is-available"
                          v-model="supplier.isAvailable"
                          required
                        >
                          <option value="">-- Select --</option>
                          <option value="true">Yes</option>
                          <option value="false">No</option>
                        </select>
                      </div>
                      <button type="submit" class="btn btn-primary">
                        {{ isUpdatingSupplier ? "Update" : "Save" }}
                      </button>
                    </form>
                  </div>
                  <div
                    class="col-md-9"
                    style="
                      height: 600px;
                      max-height: 600px;
                      overflow-y: auto;
                      overflow-x: hidden;
                      padding-right: 1px;
                    "
                  >
                    <div class="form-check">
                      <input
                        class="form-check-input"
                        type="checkbox"
                        v-model="showSuppliers"
                      />
                      <label
                        class="form-check-label"
                        for="unavailableItemsCheckbox"
                      >
                        Show available items only?
                      </label>
                    </div>

                    <div>
                      <table-component
                        :mainHeaders="suppliersOptions"
                        :mainItems="switchSuppliers"
                        :editable="true"
                        @edit-action="editSupplier"
                        :toggleable="false"
                      >
                        <template #default="{ data }">
                          <span v-if="data.isAvailable">Yes</span>
                          <span v-else>No</span>
                        </template>
                      </table-component>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="card" style="height: 60px !important"></div>
                </div>
              </div>
            </div>
            <div id="purchases" class="tab-pane">
              <div id="purchases" class="tab-pane">
                <div class="row">
                  <div class="col-md-5">
                    <form class="no-print">
                      <div class="mb-3">
                        <h4>Supplier</h4>
                        <hr />
                        <v-select
                          :options="filteredsupplier"
                          label="name"
                          v-model="purchase.supplier"
                          required
                        >
                        </v-select>
                      </div>

                      <h4>Product Details</h4>
                      <hr />
                      <div
                        class="form-group row"
                        v-for="(item, index) in purchase.items"
                        :key="index"
                      >
                        <div class="col-3">
                          <label class="col-form-label">Stock:</label>
                          <select class="form-control" v-model="item.stock">
                            <option value="">-- Select Stock --</option>
                            <option
                              v-for="stock in filteredstocks"
                              :value="stock"
                            >
                              {{ stock.name }}
                            </option>
                          </select>
                        </div>
                        <div class="col-3">
                          <label class="col-form-label">Price:</label>
                          <input
                            type="number"
                            min="0"
                            class="form-control"
                            v-model="item.pricePerItem"
                          />
                        </div>
                        <div class="col-2">
                          <label class="col-form-label">Qty:</label>
                          <input
                            type="number"
                            min="0"
                            class="form-control"
                            v-model="item.quantity"
                          />
                        </div>
                        <div class="col-3">
                          <label class="col-form-label">Total:</label>
                          <input
                            type="number"
                            class="form-control"
                            :value="calculatePrice(item)"
                            readonly
                          />
                        </div>
                        <div class="col-1">
                          <label class="col-form-label text-white">.</label>
                          <button
                            v-if="index > 0"
                            type="button"
                            class="form-control btn btn-danger"
                            @click="removeItem(index, 0)"
                            style="width: fit-content"
                          >
                            &times;
                          </button>
                        </div>
                      </div>
                      <div class="form-group row">
                        <div class="col-12 d-flex justify-content-end mt-3">
                          <a href="#" @click="addItem(0)">+ Add More</a>
                        </div>
                      </div>

                      <button
                        type="button"
                        @click.prevent="addPurchases()"
                        class="btn btn-primary"
                      >
                        Add to Purchases
                      </button>
                    </form>
                  </div>
                  <div class="col-md-7">
                    <div>
                      <table-component
                        :mainHeaders="purchasesOptions"
                        :mainItems="purchases"
                        :subHeaders="purchasessubOptions"
                        :editable="false"
                        :toggleable="true"
                      />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="card" style="height: 60px !important"></div>
                </div>
              </div>
            </div>
            <div id="sales" class="tab-pane">
              <div id="sales" class="tab-pane">
                <div class="row">
                  <div class="col-md-5">
                    <form class="no-print">
                      <div class="mb-3">
                        <h4>Customer</h4>
                        <hr />
                        <input
                          type="text"
                          class="form-control"
                          v-model="sale.customer.name"
                        />
                      </div>

                      <h4>Product Details</h4>
                      <hr />
                      <div
                        class="form-group row"
                        v-for="(item, index) in sale.items"
                        :key="index"
                      >
                        <div class="col-3">
                          <label class="col-form-label">Stock:</label>
                          <select class="form-control" v-model="item.stock">
                            <option value="">-- Select Stock --</option>
                            <option
                              v-for="stock in filteredstocks"
                              :value="stock"
                            >
                              {{ stock.name }}
                            </option>
                          </select>
                        </div>
                        <div class="col-3">
                          <label class="col-form-label">Price:</label>
                          <input
                            type="number"
                            min="0"
                            class="form-control"
                            v-model="item.pricePerItem"
                          />
                        </div>
                        <div class="col-2">
                          <label class="col-form-label">Qty:</label>
                          <input
                            type="number"
                            min="0"
                            class="form-control"
                            v-model="item.quantity"
                          />
                        </div>
                        <div class="col-3">
                          <label class="col-form-label">Total:</label>
                          <input
                            type="number"
                            class="form-control"
                            :value="calculatePrice(item)"
                            readonly
                          />
                        </div>
                        <div class="col-1">
                          <label class="col-form-label text-white">.</label>
                          <button
                            v-if="index > 0"
                            type="button"
                            class="form-control btn btn-danger"
                            @click="removeItem(index, 1)"
                            style="width: fit-content"
                          >
                            &times;
                          </button>
                        </div>
                      </div>
                      <div class="form-group row">
                        <div class="col-12 d-flex justify-content-end mt-3">
                          <a href="#" @click="addItem(1)">+ Add More</a>
                        </div>
                      </div>

                      <button
                        type="button"
                        @click.prevent="addSales()"
                        class="btn btn-primary"
                      >
                        Add to Sales
                      </button>
                    </form>
                  </div>
                  <div class="col-md-7">
                    <div>
                      <table-component
                        :mainHeaders="salesOptions"
                        :mainItems="sales"
                        :subHeaders="salessubOptions"
                        @edit-action="editInventory"
                        :editable="true"
                        :toggleable="true"
                      />
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="card" style="height: 60px !important"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <FooterComponent />
  <div
    class="modal fade show"
    id="stockModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="stockModalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h4 class="modal-title" id="stockModalLabel">View Stock</h4>
          <button
            type="button"
            class="close"
            data-bs-dismiss="modal"
            aria-label="Close"
            @click="closeModal"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-6">
              <div v-if="stock">
                <h5>{{ stock.name }}</h5>
                <p>Description: {{ stock.description }}</p>
              </div>
              <div v-else>
                <p>No stock information available.</p>
              </div>
            </div>
            <div class="col-md-6">
              <div v-if="stock">
                <p>Category: {{ stock.category }}</p>
                <div class="btn-group mr-2" role="group" aria-label="...">
                  <button
                    type="button"
                    class="m-btn btn-light btn btn-default"
                    style="font-size: small; width: 20px"
                    @click="this.stock.quantity--"
                  >
                    <i class="fa fa-minus"></i>
                  </button>
                  <button
                    type="button"
                    class="m-btn btn-light btn btn-default"
                    style="font-size: medium; width: 20px"
                    disabled
                  >
                    {{ stock.quantity }}
                  </button>
                  <button
                    type="button"
                    class="m-btn btn-light btn btn-default"
                    style="font-size: small; width: 20px"
                    @click="this.stock.quantity++"
                  >
                    <i class="fa fa-plus"></i>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-primary"
            @click="updateQtyOnInventory(stock.id)"
          >
            Save
          </button>
          &nbsp;
          <button type="button" class="btn btn-danger" data-bs-dismiss="modal">
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from "@/stores/authStore";
import TopNavBarComponent from "@/components/common/TopNavBar.vue";
import FooterComponent from "../common/FooterComponent.vue";
import TableComponent from "@/components/common/GenericTable.vue";
import axios from "axios";
import async from "arima/async";

export default {
  components: {
    TopNavBarComponent,
    FooterComponent,
    TableComponent,
  },
  data() {
    return {
      stocksOptions: [
        {
          label: "",
          field: "toggle",
          sortable: false,
        },
        {
          label: "Name",
          field: "name",
          sortable: true,
        },
        {
          label: "Description",
          field: "description",
          sortable: true,
        },
        {
          label: "SKU",
          field: "sku",
          sortable: true,
        },
        {
          label: "Category",
          field: "category",
          sortable: true,
        },
        {
          label: "Qty",
          field: "quantity",
          sortable: true,
        },
        {
          label: "Is Available?",
          field: "isAvailable",
          sortable: true,
          slot: true,
        },
        {
          label: "",
          field: "action",
          sortable: false,
        },
      ],
      stockssubOptions: [
        {
          label: "Status",
          field: "stock_type",
        },
        {
          label: "Price",
          field: "priceRate",
        },
        {
          label: "Qty",
          field: "purchaseQty",
        },
        {
          label: "Total",
          field: "totalCost",
        },
        {
          label: "Date",
          field: "date_created",
        },
      ],
      purchasesOptions: [
        {
          label: "",
          field: "toggle",
          sortable: false,
        },
        {
          label: "Purchase #",
          field: "id",
          sortable: true,
        },
        {
          label: "Supplier Name",
          field: "supplier_name",
          sortable: true,
        },
        {
          label: "Total Purchased Price",
          field: "totalPrice",
          sortable: true,
        },
        {
          label: "Purchased Date",
          field: "date_created",
          sortable: true,
        },
      ],
      purchasessubOptions: [
        {
          label: "SKU",
          field: "stock_sku",
        },
        {
          label: "Name",
          field: "stock_name",
        },
        {
          label: "Price",
          field: "priceRate",
        },
        {
          label: "Qty",
          field: "purchaseQty",
        },
        {
          label: "Total",
          field: "totalCost",
        },
      ],
      salesOptions: [
        {
          label: "",
          field: "toggle",
          sortable: false,
        },
        {
          label: "Invoice #",
          field: "id",
          sortable: true,
        },
        {
          label: "Customer Name",
          field: "customer_name",
          sortable: true,
        },
        {
          label: "Total",
          field: "totalPrice",
          sortable: true,
        },
        {
          label: "Transaction Date",
          field: "date_created",
          sortable: true,
        },
      ],
      salessubOptions: [
        {
          label: "SKU",
          field: "stock_sku",
        },
        {
          label: "Name",
          field: "stock_name",
        },
        {
          label: "Price",
          field: "priceRate",
        },
        {
          label: "Qty",
          field: "purchaseQty",
        },
        {
          label: "Total",
          field: "totalCost",
        },
      ],
      suppliersOptions: [
        {
          label: "Name",
          field: "name",
          sortable: true,
        },
        {
          label: "Contact",
          field: "contact",
          sortable: true,
        },
        {
          label: "Email",
          field: "email",
          sortable: true,
        },
        {
          label: "Address",
          field: "address",
          sortable: true,
        },
        {
          label: "Address",
          field: "address",
          sortable: true,
        },
        {
          label: "TIN No.",
          field: "tinno",
          sortable: true,
        },
        {
          label: "Is Available?",
          field: "isAvailable",
          sortable: true,
          slot: true,
        },
        {
          label: "",
          field: "action",
          sortable: false,
        },
      ],
      showItems: true,
      showSuppliers: true,
      stocks: [],
      suppliers: [],
      purchases: [],
      sales: [],
      sale: {
        customer: {
          name: "",
        },
        items: [{ stock: "", pricePerItem: 0, quantity: 0 }],
      },
      purchase: {
        supplier: {
          name: "",
        },
        items: [{ stock: "", pricePerItem: 0, quantity: 0 }],
      },
      stock: {
        name: "",
        description: "",
        sku: "",
        category: "",
        quantity: 0,
        isAvailable: "",
      },
      supplier: {
        id: null,
        name: "",
        contact: "",
        email: "",
        address: "",
        tinno: "",
        isAvailable: "",
      },
      isUpdatingInventory: false,
      isUpdatingSupplier: false,
      searchInventory: "",
      searchSupplier: "",
      searchPurchases: "",
      searchSales: "",
    };
  },
  async created() {
    if (this.EVALUATION_STAGE) {
      const countdownMessage = `This app is for evaluation and not the full version. Please wait for <span id="countdowntimer">${this.EVALUATION_TIME}</span> seconds to load.`;
      let countdownResult;
      let timeoutExpired = false; // New variable for tracking timeout

      countdownResult = await this.$swal.fire({
        title: "Please wait",
        html: countdownMessage,
        icon: "info",
        showCancelButton: false,
        showConfirmButton: false,
        allowOutsideClick: false,
        didOpen: () => {
          const countdownEl = document.querySelector("#countdowntimer");
          let count = this.EVALUATION_TIME - 1;
          const timerId = setInterval(() => {
            countdownEl.textContent = count;
            count--;
            if (count < 0) {
              clearInterval(timerId);
              timeoutExpired = true; // Update timeoutExpired to true
              this.$swal.close();
            }
          }, 1000);
        },
      });

      if (!countdownResult.isConfirmed && timeoutExpired) {
        countdownResult.isConfirmed = true; // Set isConfirmed to true if timeout expired
      }

      if (!countdownResult.isConfirmed) {
        return;
      }
    }

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
    switchStocks() {
      if (this.showItems) {
        return this.stocks.filter((item) => item.isAvailable);
      } else {
        return this.stocks;
      }
    },
    switchSuppliers() {
      if (this.showSuppliers) {
        return this.suppliers.filter((item) => item.isAvailable);
      } else {
        return this.suppliers;
      }
    },
    filteredstocks() {
      //remove stocks with zero quantity
      return this.stocks.filter((item) => item.isAvailable);
    },
    filteredsupplier() {
      //remove suupplier not available
      return this.suppliers.filter((item) => item.isAvailable);
    },
  },
  methods: {
    viewStock(id) {
      const stock = this.stocks.find((item) => item.id === id);
      this.stock = stock;
      $("#stockModal").modal("toggle");
    },
    async updateQtyOnInventory(id) {
      await axios
        .get(`${this.API_URL}stockitem/${id}/`)
        .then(async (response) => {
          const prevQty = response.data.quantity;
          await axios
            .put(`${this.API_URL}stockitem/${id}/`, this.stock)
            .then(async (response) => {
              this.$swal({
                icon: "success",
                title: "Item updated successfully",
              });

              const api = `${this.API_URL}inventory/item/`;
              const itemsdata = {
                supplier_id: data.supplier_id,
                supplier_name: data.supplier_name,
                purchase_id: response.data.id,
                stock_id: response.data.id,
                stock_sku: response.data.sku,
                stock_name: response.data.name,
                priceRate: 0,
                purchaseQty: item.quantity,
                stock_type: "stock-in",
                totalCost: this.calculatePrice(item),
              };
              try {
                await axios.post(api, itemsdata);
              } catch (error) {}

              this.stock = {
                id: null,
                name: "",
                description: "",
                sku: "",
                category: "",
                quantity: 0,
                isAvailable: "",
              };
              $("#stockModal").modal("toggle");
            })
            .catch((error) => {
              console.log(error);
            });
        });
    },
    addItem(o) {
      const arr = o === 0 ? this.purchase : this.sale;
      arr.items.push({ stock: "", pricePerItem: null, quantity: null });
    },
    removeItem(index, o) {
      const arr = o === 0 ? this.purchase : this.sale;
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
        role: authStore.user.role,
      };
      const response = await axios.put(
        `${this.API_URL}users/${authStore.user.id}/`,
        { ...user, isActive: false }
      );
      if (response.data !== undefined) {
        authStore.logout();
        this.$router.push("/");
      } else {
        this.$swal({
          icon: "error",
          title: "Logout error. Please contact your admin for assistance!",
        });
      }
    },
    addSales() {
      if (this.sale.customer.name === "") {
        this.$swal({
          icon: "error",
          title: "Please provide customer name!",
        });
        return;
      }

      for (const item of this.sale.items) {
        if (
          item.stock.name === undefined ||
          item.pricePerItem === null ||
          item.quantity < 1
        ) {
          this.$swal({
            icon: "error",
            title: "Please provide valid product details!",
          });
          return;
        }
      }

      for (const item of this.sale.items) {
        if (item.stock.quantity < item.quantity) {
          this.$swal({
            icon: "error",
            title:
              "I'm sorry, but your request for " +
              item.quantity +
              " units of " +
              item.stock.name +
              " cannot be fulfilled as there are only " +
              item.stock.quantity +
              " units left in stock.",
          });
          return;
        }
      }

      const data = {
        customer_name: this.sale.customer.name,
        totalPrice: this.sale.items.reduce((acc, item) => {
          return acc + item.pricePerItem * item.quantity;
        }, 0),
      };

      this.$swal({
        icon: "warning",
        title: "Are you sure you want to add this transaction?",
        showCancelButton: true,
        confirmButtonText: "Yes",
        cancelButtonText: "No",
      }).then((result) => {
        if (result.isConfirmed) {
          axios
            .post(`${this.API_URL}sales/`, data)
            .then((response) => {
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
                  totalCost: this.calculatePrice(item),
                };
                try {
                  await axios.post(api, itemsdata);
                  const response = await axios.get(
                    `${this.API_URL}stockitem/${itemsdata.stock_id}/`
                  );
                  await axios.put(
                    `${this.API_URL}stockitem/${itemsdata.stock_id}/`,
                    {
                      ...response.data,
                      quantity:
                        parseFloat(response.data.quantity) -
                        itemsdata.purchaseQty,
                    }
                  );
                  this.getInventory();
                } catch (error) {
                  console.log(error);
                }
              });
              this.$swal({
                icon: "success",
                title: "Transaction added successfully",
              });
              this.sale = {
                customer: {
                  name: "",
                },
                items: [{ stock: "", pricePerItem: 0, quantity: 0 }],
              };
              this.getSales();
            })
            .catch((error) => {
              console.log(error);
            });
        }
      });
    },

    addPurchases() {
      if (this.purchase.supplier.name === "") {
        this.$swal({
          icon: "error",
          title: "Please provide supplier name!",
        });
        return;
      }

      for (const item of this.purchase.items) {
        if (
          item.stock.name === undefined ||
          item.pricePerItem === null ||
          item.quantity < 1
        ) {
          this.$swal({
            icon: "error",
            title: "Please provide valid product details!",
          });
          return;
        }
      }

      const data = {
        supplier_id: this.purchase.supplier.id,
        supplier_name: this.purchase.supplier.name,
        totalPrice: this.purchase.items.reduce((acc, item) => {
          return acc + item.pricePerItem * item.quantity;
        }, 0),
      };

      this.$swal({
        icon: "warning",
        title: "Are you sure you want to add this purchase?",
        showCancelButton: true,
        confirmButtonText: "Yes",
        cancelButtonText: "No",
      }).then((result) => {
        if (result.isConfirmed) {
          axios
            .post(`${this.API_URL}purchases/`, data)
            .then((response) => {
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
                  totalCost: this.calculatePrice(item),
                };
                try {
                  await axios.post(api, itemsdata);
                  const response = await axios.get(
                    `${this.API_URL}stockitem/${itemsdata.stock_id}/`
                  );
                  await axios.put(
                    `${this.API_URL}stockitem/${itemsdata.stock_id}/`,
                    {
                      ...response.data,
                      quantity:
                        parseFloat(response.data.quantity) +
                        itemsdata.purchaseQty,
                    }
                  );
                  this.getInventory();
                } catch (error) {
                  console.log(error);
                }
              });
              this.$swal({
                icon: "success",
                title: "Purchase added successfully",
              });
              this.purchase = {
                supplier: {
                  name: "",
                },
                items: [{ stock: "", pricePerItem: 0, quantity: 0 }],
              };
              this.getPurchases();
            })
            .catch((error) => {
              console.log(error);
            });
        }
      });
    },

    getInventory() {
      axios
        .get(`${this.API_URL}stockitem/`)
        .then((response) => {
          this.stocks = response.data;
          this.stocks.forEach(async (item, index) => {
            try {
              const res = await axios.post(
                `${this.API_URL}inventory/item/filter/`,
                [{ columnName: "stock_id", columnKey: item.id }]
              );
              const o = res.data;
              this.stocks[index].items = o;
            } catch (error) {}
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getSuppliers() {
      axios
        .get(`${this.API_URL}supplier/`)
        .then((response) => {
          this.suppliers = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getPurchases() {
      axios
        .get(`${this.API_URL}purchases/`)
        .then((response) => {
          this.purchases = response.data;
          this.purchases.forEach(async (item, index) => {
            try {
              const res = await axios.post(
                `${this.API_URL}inventory/item/filter/`,
                [{ columnName: "purchase_id", columnKey: item.id }]
              );
              const o = res.data;
              this.purchases[index].items = o;
            } catch (error) {}
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getSales() {
      axios
        .get(`${this.API_URL}sales/`)
        .then((response) => {
          this.sales = response.data;
          this.sales.forEach(async (item, index) => {
            try {
              const res = await axios.post(
                `${this.API_URL}inventory/item/filter/`,
                [{ columnName: "sales_id", columnKey: item.id }]
              );
              const o = res.data;
              this.sales[index].items = o;
            } catch (error) {}
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    saveInventory() {
      if (this.isUpdatingInventory) {
        axios
          .put(`${this.API_URL}stockitem/${this.stock.id}/`, this.stock)
          .then((response) => {
            this.$swal({
              icon: "success",
              title: "Item updated successfully",
            });
            this.getInventory();
            this.stock = {
              id: null,
              name: "",
              description: "",
              sku: "",
              category: "",
              quantity: 0,
              isAvailable: "",
            };
            this.isUpdatingInventory = false;
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        axios
          .post(`${this.API_URL}stockitem/filter/`, {
            columnName: "name",
            columnKey: this.stock.name,
          })
          .then((response) => {
            if (response.data.length > 0) {
              this.$swal({
                icon: "error",
                title: "Item already exists",
              });
            } else {
              axios
                .post(`${this.API_URL}stockitem/`, this.stock)
                .then((response) => {
                  this.$swal({
                    icon: "success",
                    title: "Item saved successfully",
                  });
                  this.getInventory();
                  this.stock = {
                    id: null,
                    name: "",
                    description: "",
                    sku: "",
                    category: "",
                    quantity: 0,
                    isAvailable: "",
                  };
                })
                .catch((error) => {
                  console.log(error);
                });
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    saveSupplier() {
      if (this.isUpdatingSupplier) {
        axios
          .put(`${this.API_URL}supplier/${this.supplier.id}/`, this.supplier)
          .then((response) => {
            this.$swal({
              icon: "success",
              title: "Supplier updated successfully",
            });
            this.getSuppliers();
            this.supplier = {
              id: null,
              name: "",
              contact: "",
              email: "",
              address: "",
              tinno: "",
              isAvailable: "",
            };
            this.isUpdatingSupplier = false;
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        axios
          .post(`${this.API_URL}supplier/filter/`, {
            columnName: "name",
            columnKey: this.supplier.name,
          })
          .then((response) => {
            if (response.data.length > 0) {
              this.$swal({
                icon: "error",
                title: "Supplier already exists",
              });
            } else {
              axios
                .post(`${this.API_URL}supplier/`, this.supplier)
                .then((response) => {
                  this.$swal({
                    icon: "success",
                    title: "Supplier saved successfully",
                  });
                  this.getSuppliers();
                  this.supplier = {
                    id: null,
                    name: "",
                    contact: "",
                    email: "",
                    address: "",
                    tinno: "",
                    isAvailable: "",
                  };
                })
                .catch((error) => {
                  console.log(error);
                });
            }
          })
          .catch((error) => {
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
        title: "Confirmation",
        text: "Do you really want to log out this user?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, do it!",
        cancelButtonText: "Cancel",
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
        .then((response) => {
          this.stock = response.data;
          this.isUpdatingInventory = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editSupplier(id) {
      axios
        .get(`${this.API_URL}supplier/${id}/`)
        .then((response) => {
          this.supplier = response.data;
          this.isUpdatingSupplier = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
@import "vue-select/dist/vue-select.css";
</style>
