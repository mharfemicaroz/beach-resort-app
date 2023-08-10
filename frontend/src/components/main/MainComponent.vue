<template>
  <TopNavBarComponent />
  <div class="container-fluid main">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12">
          <ul class="nav nav-tabs justify-content-left">
            <li class="nav-item">
              <a class="nav-link active" data-bs-toggle="tab" href="#users">
                <i class="fas fa-users fa-2x"></i>
                <br />
                Users
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-bs-toggle="tab" href="#rooms">
                <i class="fas fa-door-open fa-2x"></i>
                <br />
                Rooms
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-bs-toggle="tab" href="#leisures">
                <i class="fas fa-swimming-pool fa-2x"></i>
                <br />
                Leisures
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link text-center"
                data-bs-toggle="tab"
                href="#restotables"
              >
                <i class="fa fa-table fa-2x"></i>
                <br />
                Resto Tables
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" data-bs-toggle="tab" href="#logs">
                <i class="fas fa-list fa-2x"></i>
                <br />
                Logs
              </a>
            </li>
          </ul>
          <div class="tab-content">
            <div id="users" class="tab-pane active">
              <div id="users" class="tab-pane active">
                <div class="row">
                  <div class="col-md-3">
                    <form @submit.prevent="saveUser">
                      <div class="mb-3">
                        <label for="username" class="form-label"
                          >Username</label
                        >
                        <input
                          type="text"
                          class="form-control"
                          id="username"
                          v-model="user.username"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="password" class="form-label"
                          >Password</label
                        >
                        <input
                          type="text"
                          class="form-control"
                          id="password"
                          v-model="user.password"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="firstName" class="form-label"
                          >First Name</label
                        >
                        <input
                          type="text"
                          class="form-control"
                          id="firstName"
                          v-model="user.FirstName"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="lastName" class="form-label"
                          >Last Name</label
                        >
                        <input
                          type="text"
                          class="form-control"
                          id="lastName"
                          v-model="user.LastName"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="role" class="form-label">Role</label>
                        <select
                          class="form-select"
                          id="role"
                          v-model="user.role"
                          required
                        >
                          <option value="">-- Select Role --</option>
                          <option value="reservationist">Reservationist</option>
                          <option value="frontdesk">Front Desk</option>
                          <option value="inventorymanager">
                            Inventory Manager
                          </option>
                          <option value="cashier">Cashier</option>
                          <option value="waiter">Server/Waiter</option>
                          <option value="foodserver">Food Server</option>
                          <option value="restoinventory">
                            Restaurant Inventory Manager
                          </option>
                          <option value="supervisor">Supervisor</option>
                          <option value="supervisor-aide">
                            Supervisor Aide
                          </option>
                          <option value="guard">Guest Counter</option>
                          <option value="errand">Errand</option>
                        </select>
                      </div>
                      <button type="submit" class="btn btn-primary">
                        {{ isUpdatingUser ? "Update" : "Save" }}
                      </button>
                    </form>
                  </div>
                  <div
                    class="col-md-9"
                    style="
                      height: 550px;
                      max-height: 550px;
                      overflow-y: auto;
                      overflow-x: hidden;
                      padding-right: 1px;
                    "
                  >
                    <table class="table">
                      <thead>
                        <tr>
                          <th>Username</th>
                          <th>First Name</th>
                          <th>Last Name</th>
                          <th>Role</th>
                          <th>Is Active now?</th>
                          <th>Action</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="user in users" :key="user.id">
                          <td>{{ user.username }}</td>
                          <td>{{ user.FirstName }}</td>
                          <td>{{ user.LastName }}</td>
                          <td>{{ user.role }}</td>
                          <td v-if="user.isActive">
                            <span class="bg-success text-white">online</span>
                          </td>
                          <td v-else>
                            <span class="bg-danger text-white">inactive</span>
                          </td>
                          <td>
                            <button
                              type="button"
                              class="btn btn-primary btn-sm"
                              @click="editUser(user.id)"
                            >
                              <i class="fas fa-edit"></i></button
                            >&nbsp;
                            <button
                              v-if="user.isActive"
                              type="button"
                              class="btn btn-danger btn-sm"
                              @click="logoutUser(user)"
                            >
                              <i class="fas fa-sign-out-alt"></i>
                            </button>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
            <div id="rooms" class="tab-pane">
              <div id="rooms" class="tab-pane">
                <div class="row">
                  <div class="col-md-3">
                    <form @submit.prevent="saveRoom">
                      <div class="mb-3">
                        <label for="name" class="form-label">Name</label>
                        <input
                          type="text"
                          class="form-control"
                          id="name"
                          v-model="room.name"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="price" class="form-label">Price</label>
                        <input
                          type="number"
                          step="0.01"
                          class="form-control"
                          id="price"
                          v-model="room.price"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="type" class="form-label">Type</label>
                        <select
                          class="form-select"
                          id="type"
                          v-model="room.type"
                          required
                        >
                          <option value="">-- Select Type --</option>
                          <option value="BEACH ROOM">BEACH ROOM</option>
                          <option value="POOL ROOM">POOL ROOM</option>
                          <option value="POOL COTTAGE">POOL COTTAGE</option>
                          <option value="GAZEBO COTTAGE">
                            NATIVE GAZEBO COTTAGE
                          </option>
                          <option value="BEACH COTTAGE">
                            BEACH COTTAGE (day)
                          </option>
                          <option value="N-BEACH COTTAGE">
                            BEACH COTTAGE (night)
                          </option>
                          <option value="HALL">HALL</option>
                        </select>
                      </div>
                      <div class="mb-3">
                        <label for="type" class="form-label"
                          >Availability</label
                        >
                        <select
                          class="form-select"
                          id="type"
                          v-model="room.isAvailable"
                          required
                        >
                          <option value="">-- Select --</option>
                          <option value="true">Yes</option>
                          <option value="false">No</option>
                        </select>
                      </div>
                      <button type="submit" class="btn btn-primary">
                        {{ isUpdatingRoom ? "Update" : "Save" }}
                      </button>
                    </form>
                  </div>
                  <div
                    class="col-md-9"
                    style="
                      height: 550px;
                      max-height: 550px;
                      overflow-y: auto;
                      overflow-x: hidden;
                      padding-right: 1px;
                    "
                  >
                    <table class="table">
                      <thead>
                        <tr>
                          <th>Name</th>
                          <th>Price</th>
                          <th>Type</th>
                          <th>Is Available?</th>
                          <th>Action</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="room in rooms" :key="room.id">
                          <td>{{ room.name }}</td>
                          <td>{{ room.price }}</td>
                          <td>{{ room.type }}</td>
                          <td v-if="room.isAvailable">Yes</td>
                          <td v-else>No</td>
                          <td>
                            <button
                              type="button"
                              class="btn btn-primary btn-sm"
                              @click="editRoom(room.id)"
                            >
                              <i class="fas fa-edit"></i></button
                            >&nbsp;
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
            <div id="leisures" class="tab-pane">
              <div id="leisures" class="tab-pane">
                <div class="row">
                  <div class="col-md-3">
                    <form @submit.prevent="saveLeisure">
                      <div class="mb-3">
                        <label for="item-name" class="form-label"
                          >Item Name</label
                        >
                        <input
                          type="text"
                          class="form-control"
                          id="item-name"
                          v-model="leisure.item"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="type" class="form-label">Type</label>
                        <select
                          class="form-select"
                          id="type"
                          v-model="leisure.type"
                          required
                        >
                          <option value="">-- Select Type --</option>
                          <option value="ENTRANCE">Entrance</option>
                          <option value="SPORTS">Sports</option>
                          <option value="LEISURES">Leisures</option>
                          <option value="ITEMS">Items</option>
                          <option value="CORKAGE">Corkage</option>
                          <option value="MISC">Misc</option>
                        </select>
                      </div>
                      <div class="mb-3">
                        <label for="price-rate" class="form-label"
                          >Price Rate</label
                        >
                        <input
                          type="number"
                          step="0.01"
                          class="form-control"
                          id="price-rate"
                          v-model="leisure.priceRate"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="counter" class="form-label">Counter</label>
                        <select
                          class="form-select"
                          id="counter"
                          v-model="leisure.counter"
                          required
                        >
                          <option value="">-- Select Counter --</option>
                          <option value="head">Head</option>
                          <option value="hour">Hour</option>
                          <option value="usage">Usage</option>
                          <option value="unit">Unit</option>
                        </select>
                      </div>
                      <div class="mb-3">
                        <label for="is-available" class="form-label"
                          >Availability</label
                        >
                        <select
                          class="form-select"
                          id="is-available"
                          v-model="leisure.isAvailable"
                          required
                        >
                          <option value="">-- Select --</option>
                          <option value="true">Yes</option>
                          <option value="false">No</option>
                        </select>
                      </div>
                      <button type="submit" class="btn btn-primary">
                        {{ isUpdatingLeisure ? "Update" : "Save" }}
                      </button>
                    </form>
                  </div>
                  <div
                    class="col-md-9"
                    style="
                      height: 550px;
                      max-height: 550px;
                      overflow-y: auto;
                      overflow-x: hidden;
                      padding-right: 1px;
                    "
                  >
                    <table class="table">
                      <thead>
                        <tr>
                          <th>Item Name</th>
                          <th>Type</th>
                          <th>Price Rate</th>
                          <th>Counter</th>
                          <th>Is Available?</th>
                          <th>Action</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="leisure in leisures" :key="leisure.id">
                          <td>{{ leisure.item }}</td>
                          <td>{{ leisure.type }}</td>
                          <td>{{ leisure.priceRate }}</td>
                          <td>{{ leisure.counter }}</td>
                          <td v-if="leisure.isAvailable">Yes</td>
                          <td v-else>No</td>
                          <td>
                            <button
                              type="button"
                              class="btn btn-primary btn-sm"
                              @click="editLeisure(leisure.id)"
                            >
                              <i class="fas fa-edit"></i>
                            </button>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
            <div id="restotables" class="tab-pane">
              <div id="restotables" class="tab-pane">
                <div class="row">
                  <div class="col-md-3">
                    <form @submit.prevent="saveRestotables">
                      <div class="mb-3">
                        <label for="table-name" class="form-label"
                          >Table Name</label
                        >
                        <input
                          type="text"
                          class="form-control"
                          id="table-name"
                          v-model="restaurantTable.name"
                          required
                        />
                      </div>
                      <div class="mb-3">
                        <label for="seating-capacity" class="form-label"
                          >Seating Capacity</label
                        >
                        <input
                          type="number"
                          class="form-control"
                          id="seating-capacity"
                          v-model="restaurantTable.capacity"
                          min="0"
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
                          v-model="restaurantTable.isAvailable"
                          required
                        >
                          <option value="">-- Select --</option>
                          <option value="true">Yes</option>
                          <option value="false">No</option>
                        </select>
                      </div>
                      <button type="submit" class="btn btn-primary">
                        {{ isUpdatingTable ? "Update" : "Save" }}
                      </button>
                    </form>
                  </div>
                  <div
                    class="col-md-9"
                    style="
                      height: 550px;
                      max-height: 550px;
                      overflow-y: auto;
                      overflow-x: hidden;
                      padding-right: 1px;
                    "
                  >
                    <table class="table">
                      <thead>
                        <tr>
                          <th>Table Name</th>
                          <th>Seating Capacity</th>
                          <th>Availability</th>
                          <th>Action</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="table in restaurantTables" :key="table.id">
                          <td>{{ table.name }}</td>
                          <td>{{ table.capacity }}</td>
                          <td v-if="table.isAvailable">Yes</td>
                          <td v-else>No</td>
                          <td>
                            <button
                              type="button"
                              class="btn btn-primary btn-sm"
                              @click="editTable(table.id)"
                            >
                              <i class="fas fa-edit"></i>
                            </button>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
            <div id="logs" class="tab-pane">
              <div id="logs" class="tab-pane">
                <div class="row">
                  <div class="col-md-12">
                    <table-component
                      :mainHeaders="logsOptions"
                      :mainItems="logs"
                      :editable="false"
                      :toggleable="false"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <FooterComponent />
</template>

<script>
import { useAuthStore } from "@/stores/authStore";
import TopNavBarComponent from "@/components/common/TopNavBar.vue";
import FooterComponent from "../common/FooterComponent.vue";
import TableComponent from "@/components/common/GenericTable.vue";
import axios from "axios";

export default {
  components: {
    TopNavBarComponent,
    FooterComponent,
    TableComponent,
  },
  data() {
    return {
      logsOptions: [
        {
          label: "Actor",
          field: "actor",
          sortable: true,
        },
        {
          label: "Task",
          field: "task",
          sortable: true,
        },
        {
          label: "Date Created",
          field: "date_created",
          sortable: true,
        },
      ],
      users: [],
      rooms: [],
      leisures: [],
      restaurantTables: [],
      logs: [],
      user: {
        username: "",
        password: "",
        FirstName: "",
        LastName: "",
        role: "",
        route: "",
      },
      room: {
        // object representing the current room being edited or added
        id: null,
        name: "",
        price: "",
        type: "",
        isAvailable: "",
      },
      leisure: {
        id: null,
        item: "",
        type: "",
        priceRate: null,
        counter: "",
        isAvailable: "",
      },
      restaurantTable: {
        id: null,
        name: "",
        capacity: "",
        isAvailable: "",
      },
      isUpdatingUser: false,
      isUpdatingRoom: false,
      isUpdatingLeisure: false,
      isUpdatingTable: false,
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

    this.getUsers();
    this.getRooms();
    this.getLeisures();
    this.getRestaurantTables();
    this.getLogs();
  },
  computed: {
    userdata() {
      const authStore = useAuthStore();
      const user = authStore.user;
      return user;
    },
  },
  methods: {
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
    getLogs() {
      axios
        .get(`${this.API_URL}task/record/`)
        .then((response) => {
          this.logs = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getUsers() {
      axios
        .get(`${this.API_URL}users/`)
        .then((response) => {
          this.users = response.data.filter(
            (item) => item.role !== "superuser"
          );
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getRooms() {
      axios
        .get(`${this.API_URL}rooms/`)
        .then((response) => {
          this.rooms = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getLeisures() {
      axios
        .get(`${this.API_URL}leisures/`)
        .then((response) => {
          this.leisures = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getRestaurantTables() {
      axios
        .get(`${this.API_URL}restotables/`)
        .then((response) => {
          this.restaurantTables = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    saveUser() {
      // Add the route property to the user object based on their role
      if (
        this.user.role === "reservationist" ||
        this.user.role === "frontdesk"
      ) {
        this.user.route = "booking";
      } else if (this.user.role === "inventorymanager") {
        this.user.route = "inventory";
      } else if (
        this.user.role === "cashier" ||
        this.user.role === "waiter" ||
        this.user.role === "foodserver" ||
        this.user.role === "restoinventory"
      ) {
        this.user.route = "pos";
      } else if (this.user.role === "guard") {
        this.user.route = "counter";
      } else if (this.user.role === "supervisor") {
        this.user.route = "taskmgr";
      } else if (this.user.role === "supervisor-aide") {
        this.user.route = "taskmgr";
      } else {
        this.user.route = "errand";
      }

      if (this.isUpdatingUser) {
        axios
          .put(`${this.API_URL}users/${this.user.id}/`, this.user)
          .then((response) => {
            this.$swal({
              icon: "success",
              title: "User updated successfully",
            });
            this.getUsers();
            this.user = {
              id: null,
              username: "",
              password: "",
              firstName: "",
              lastName: "",
              role: "",
              route: "", // Add the route property to the empty user object
            };
            this.isUpdatingUser = false;
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        axios
          .post(`${this.API_URL}users/filter/`, {
            columnName: "username",
            columnKey: this.user.username,
          })
          .then((response) => {
            if (response.data.length > 0) {
              this.$swal({
                icon: "error",
                title: "Username already exists",
              });
            } else {
              axios
                .post(`${this.API_URL}users/`, this.user)
                .then((response) => {
                  this.$swal({
                    icon: "success",
                    title: "User saved successfully",
                  });
                  this.getUsers();
                  this.user = {
                    username: "",
                    password: "",
                    FirstName: "",
                    LastName: "",
                    role: "",
                    route: "", // Add the route property to the empty user object
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
    saveRestotables() {
      if (this.isUpdatingTable) {
        axios
          .put(
            `${this.API_URL}restotables/${this.restaurantTable.id}/`,
            this.restaurantTable
          )
          .then((response) => {
            this.$swal({
              icon: "success",
              title: "Restaurant table updated successfully",
            });
            this.getRestaurantTables();
            this.restaurantTable = {
              id: null,
              name: "",
              capacity: "",
              isAvailable: "",
            };
            this.isUpdatingTable = false;
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        axios
          .post(`${this.API_URL}restotables/filter/`, {
            columnName: "name",
            columnKey: this.restaurantTable.name,
          })
          .then((response) => {
            if (response.data.length > 0) {
              this.$swal({
                icon: "error",
                title: "Restaurant table name already exists",
              });
            } else {
              axios
                .post(`${this.API_URL}restotables/`, this.restaurantTable)
                .then((response) => {
                  this.$swal({
                    icon: "success",
                    title: "Restaurant table saved successfully",
                  });
                  this.getRestaurantTables();
                  this.restaurantTable = {
                    id: null,
                    name: "",
                    capacity: "",
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
    saveRoom() {
      if (this.isUpdatingRoom) {
        axios
          .put(`${this.API_URL}rooms/${this.room.id}/`, this.room)
          .then((response) => {
            this.$swal({
              icon: "success",
              title: "Room updated successfully",
            });
            this.getRooms();
            this.room = {
              id: null,
              name: "",
              price: "",
              type: "",
              isAvailable: "",
            };
            this.isUpdatingRoom = false;
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        axios
          .post(`${this.API_URL}rooms/filter/`, {
            columnName: "name",
            columnKey: this.room.name,
          })
          .then((response) => {
            if (response.data.length > 0) {
              this.$swal({
                icon: "error",
                title: "Room name already exists",
              });
            } else {
              axios
                .post(`${this.API_URL}rooms/`, this.room)
                .then((response) => {
                  this.$swal({
                    icon: "success",
                    title: "Room saved successfully",
                  });
                  this.getRooms();
                  this.room = {
                    id: null,
                    name: "",
                    price: "",
                    type: "",
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
    saveLeisure() {
      if (this.isUpdatingLeisure) {
        axios
          // .put(`${this.API_URL}leisures/${this.leisure.id}/`, (this.leisure.item.toLowerCase() !== 'general entrance') ? {
          //     id: this.leisure.id,
          //     item: this.leisure.item,
          //     type: this.leisure.type,
          //     priceRate: this.leisure.priceRate,
          //     counter: this.leisure.counter,
          //     isAvailable: this.leisure.isAvailable
          // } : this.leisure)
          .put(`${this.API_URL}leisures/${this.leisure.id}/`, this.leisure)
          .then((response) => {
            this.$swal({
              icon: "success",
              title: "Item updated successfully",
            });
            this.getLeisures();
            this.leisure = {
              id: null,
              item: "",
              type: "",
              priceRate: null,
              counter: "",
              isAvailable: null,
            };
            this.isUpdatingLeisure = false;
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        axios
          .post(`${this.API_URL}leisures/filter/`, {
            columnName: "item",
            columnKey: this.leisure.item,
          })
          .then((response) => {
            if (response.data.length > 0) {
              this.$swal({
                icon: "error",
                title: "Item already exists",
              });
            } else {
              axios
                .post(`${this.API_URL}leisures/`, this.leisure)
                .then((response) => {
                  this.$swal({
                    icon: "success",
                    title: "Item saved successfully",
                  });
                  this.getLeisures();
                  this.room = {
                    id: null,
                    item: "",
                    type: "",
                    priceRate: null,
                    counter: "",
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
        route: item.route,
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
    editUser(id) {
      axios
        .get(`${this.API_URL}users/${id}/`)
        .then((response) => {
          this.user = response.data;
          this.isUpdatingUser = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editRoom(id) {
      axios
        .get(`${this.API_URL}rooms/${id}/`)
        .then((response) => {
          this.room = response.data;
          this.isUpdatingRoom = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editTable(id) {
      axios
        .get(`${this.API_URL}restotables/${id}/`)
        .then((response) => {
          this.restaurantTable = response.data;
          this.isUpdatingTable = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editLeisure(id) {
      axios
        .get(`${this.API_URL}leisures/${id}/`)
        .then((response) => {
          this.leisure = response.data;
          this.isUpdatingLeisure = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
