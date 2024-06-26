<template>
  <nav
    class="navbar navbar-fixed-top navbar-expand-lg navbar-light bg-primary shadow-sm no-print"
    :style="{
      'background-image': currentBackground,
      'background-repeat': 'no-repeat',
      'background-position': 'center',
      'background-size': 'cover',
      'background-attachment': 'fixed',
      position: 'fixed',
      width: '100vw',
      left: 0,
      top: 0,
      display: 'flex',
      'z-index': 200,
    }"
  >
    <div
      class="container-fluid"
      style="padding-left: 25px; padding-right: 25px"
    >
      <!-- Logo and Search Bar -->
      <a class="navbar-brand text-white align-middlev vv vv v vv v" href="#">
        <div style="display: flex; align-items: center">
          <img
            :src="`/src/assets/${this.APP_LOGO_NAME}`"
            width="45"
            height="45"
            class="d-inline-block align-top"
            alt="Logo"
            style="margin-right: 10px"
          />
          <span style="flex: 1">{{ this.APP_NAME }}</span>
        </div>
      </a>

      <!-- Navigation Links -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <span class="navbar-text ms-auto me-3 text-white">
          <small>Current Date and Time: {{ formattedTime }}</small>
        </span>
        <ul class="navbar-nav">
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle text-white"
              href="#"
              id="navbarDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              <i class="fas fa-user-circle me-1"></i> {{ userdata.fName }}
              {{ userdata.lName }}
            </a>
            <ul
              class="dropdown-menu dropdown-menu-end"
              aria-labelledby="navbarDropdown"
            >
              <div v-if="userdata.role === 'superuser'">
                <li>
                  <router-link to="/main" tag="a" class="dropdown-item"
                    >Main</router-link
                  >
                </li>
                <li>
                  <router-link to="/booking" tag="a" class="dropdown-item"
                    >Booking</router-link
                  >
                </li>
                <li>
                  <router-link to="/inventory" tag="a" class="dropdown-item"
                    >Inventory</router-link
                  >
                </li>
                <li>
                  <router-link to="/restaurant" tag="a" class="dropdown-item"
                    >Restaurant</router-link
                  >
                </li>
                <li>
                  <router-link
                    to="/gokart"
                    tag="a"
                    target="_blank"
                    class="dropdown-item"
                    >GoKart</router-link
                  >
                </li>
                <li>
                  <router-link
                    to="/taskmgr"
                    tag="a"
                    target="_blank"
                    class="dropdown-item"
                    >Task Manager</router-link
                  >
                </li>
                <hr class="dropdown-divider" />
              </div>
              <!--<li>
                <a
                  class="dropdown-item"
                  href="#"
                  @click="toggleShowTransModal()"
                  ><i class="fas fa-eye me-1"></i>Show Transactions</a
                >
              </li>-->
              <li>
                <a
                  class="dropdown-item"
                  href="#"
                  @click="toggleChangePassModal()"
                  ><i class="fas fa-gear me-1"></i>Change Password</a
                >
              </li>
              <li>
                <a class="dropdown-item" href="#" @click="logout()"
                  ><i class="fas fa-sign-out-alt me-1"></i> Logout</a
                >
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- <div
    class="modal fade show"
    id="showTransModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="showTransModalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="showTransModalLabel">
            Show all Today's Transaction
          </h4>
          <button
            type="button"
            class="close"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div
          class="modal-body"
          style="height: 600px; overflow-y: auto; overflow-x: hidden"
        >
          <div>
            <table-component
              :mainHeaders="transactionhistory"
              :mainItems="transactionrecord"
              :editable="false"
              :toggleable="false"
              :currentNoPage="999999"
            />
          </div>
        </div>
      </div>
    </div>
  </div> -->

  <div
    class="modal fade show"
    id="changePassModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="changePassModalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="changePassModalLabel">Update Password</h4>
          <button
            type="button"
            class="close"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="changePassword">
            <!-- Client Information -->
            <div class="form-group row">
              <label for="name" class="col-sm-4 col-form-label"
                >Old Password:*</label
              >
              <div class="col-sm-8">
                <input
                  type="password"
                  class="form-control"
                  id="oldpass"
                  v-model="oldpass"
                  required
                  autocomplete="off"
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="name" class="col-sm-4 col-form-label"
                >New Password:*</label
              >
              <div class="col-sm-8">
                <input
                  type="password"
                  class="form-control"
                  id="newpass"
                  v-model="newpass"
                  required
                  autocomplete="off"
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="name" class="col-sm-4 col-form-label"
                >Confirm Password:*</label
              >
              <div class="col-sm-8">
                <input
                  type="password"
                  class="form-control"
                  id="conpass"
                  v-model="conpass"
                  required
                  autocomplete="off"
                />
              </div>
            </div>

            <div class="form-group row">
              <div class="mt-3 mb-3 d-flex flex-row-reverse">
                <button type="submit" class="btn btn-primary">Update</button
                >&nbsp;
                <button
                  type="button"
                  class="btn btn-danger"
                  data-bs-dismiss="modal"
                >
                  Close
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from "@/stores/authStore";
import TableComponent from "@/components/common/GenericTable.vue";
import axios from "axios";
export default {
  components: {
    TableComponent,
  },
  data() {
    return {
      currentTime: new Date(),
      backgroundIndex: 0,
      backgrounds: this.LOGIN_BG,
      newpass: "",
      conpass: "",
      oldpass: "",
      transactionrecord: [],
      user: {
        username: "",
        password: "",
        FirstName: "",
        LastName: "",
        role: "",
      },
      transactionhistory: [
        {
          label: "Trans ID",
          field: "transaction",
        },
        {
          label: "Method",
          field: "paymentMethod",
        },
        {
          label: "Ref. No.",
          field: "nonCashReference",
        },
        {
          label: "Total",
          field: "totalAmountToPay",
        },
        {
          label: "Amount Paid",
          field: "cashAmountPay",
        },
        {
          label: "Balance",
          field: "balance",
        },
        {
          label: "Discount Mode",
          field: "discountMode",
        },
        {
          label: "Discount Value",
          field: "discountValue",
        },
        {
          label: "Processed by",
          field: "processedBy",
        },
        {
          label: "Status",
          field: "payStatus",
        },
        {
          label: "Date",
          field: "transaction_date",
        },
      ],
    };
  },
  created() {
    this.startBackgroundSlideshow();
    //this.enterFullscreen();
    this.loadData();
    setInterval(() => {
      this.currentTime = new Date();
    }, 1000);
  },
  computed: {
    formattedTime() {
      return `Current Date and Time: ${this.currentTime.toLocaleString()}`;
    },
    userdata() {
      const authStore = useAuthStore();
      const user = authStore.user;
      return user;
    },
    currentBackground() {
      return `url(src/assets/${this.backgrounds[this.backgroundIndex]})`;
    },
  },
  methods: {
    async loadData() {
      if (this.userdata.role === "cashier") {
        const response = await axios.post(
          this.API_URL + `restotransaction/filter/`,
          {
            columnName: "processedBy",
            columnKey: this.userdata.fName + " " + this.userdata.lName,
          }
        );
        this.transactionhistory = [
          {
            label: "Trans ID",
            field: "id",
          },
          {
            label: "Method",
            field: "payMethod",
          },
          {
            label: "Ref. No.",
            field: "nonCashref",
          },
          {
            label: "Total",
            field: "totalPay",
          },
          {
            label: "Amount Paid",
            field: "totalCharge",
          },
          {
            label: "Discount Mode",
            field: "discountType",
          },
          {
            label: "Discount Value",
            field: "discountValue",
          },
          {
            label: "Processed by",
            field: "processedBy",
          },
          {
            label: "Date",
            field: "date_created",
          },
        ];
        this.transactionrecord = response.data
          .filter((item) => {
            const transactionDate = new Date(item.date_created);
            return (
              transactionDate >= new Date(new Date().setHours(0, 0, 0, 0)) &&
              transactionDate <
                new Date(
                  new Date(new Date(new Date().getTime() + 86400000)).setHours(
                    0,
                    0,
                    0,
                    0
                  )
                )
            );
          })
          .map((o) => {
            const items = JSON.parse(o.items);
            return {
              ...o,
              items,
            };
          });
      } else {
        const response = await axios.post(
          this.API_URL + `transaction/record/filter/`,
          {
            columnName: "processedBy",
            columnKey: this.userdata.fName + " " + this.userdata.lName,
          }
        );

        this.transactionrecord = response.data.filter((item) => {
          const transactionDate = new Date(item.transaction_date);
          return (
            transactionDate >= new Date(new Date().setHours(0, 0, 0, 0)) &&
            transactionDate <
              new Date(
                new Date(new Date(new Date().getTime() + 86400000)).setHours(
                  0,
                  0,
                  0,
                  0
                )
              )
          );
        });
      }
    },
    async changePassword() {
      if (this.newpass !== this.conpass) {
        this.toggleChangePassModal();
        this.$swal({
          icon: "error",
          title: "Password does not match!",
        });
        return;
      }
      const response = await axios.get(
        this.API_URL + `users/${this.userdata.id}`
      );
      const userdetails = response.data;
      // alert(JSON.stringify(userdetails));
      // return;
      axios
        .post(this.API_URL + "login/", {
          username: userdetails.username,
          password: this.oldpass,
        })
        .then(async (result) => {
          const user = {
            username: userdetails.username,
            FirstName: userdetails.FirstName,
            LastName: userdetails.LastName,
            role: userdetails.role,
            route: userdetails.route,
          };
          await axios.put(`${this.API_URL}users/${userdetails.id}/`, {
            ...user,
            password: this.newpass,
          });
          $("#changePassModal").modal("toggle");
          this.$swal
            .fire({
              title: "Success!",
              text: "Password is updated successfully!",
              icon: "success",
            })
            .then((result) => {
              this.logout();
            });
        })
        .catch((error) => {
          this.toggleChangePassModal();
          this.$swal({
            icon: "error",
            title: "There is an error. Please try again!",
          });
        });
    },
    toggleShowTransModal() {
      $("#showTransModal").modal("toggle");
    },
    toggleChangePassModal() {
      this.oldpass = "";
      this.newpass = "";
      this.conpass = "";
      $("#changePassModal").modal("toggle");
    },
    async logout() {
      const authStore = useAuthStore();
      const user = {
        username: authStore.user.username,
        FirstName: authStore.user.fName,
        LastName: authStore.user.lName,
        role: authStore.user.role,
        route: authStore.user.route,
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
    startBackgroundSlideshow() {
      setInterval(() => {
        this.backgroundIndex =
          (this.backgroundIndex + 1) % this.backgrounds.length;
      }, 5000);
    },

    enterFullscreen() {
      const element = document.documentElement; // Select the root element of your component
      if (element.requestFullscreen) {
        element.requestFullscreen();
      } else if (element.mozRequestFullScreen) {
        element.mozRequestFullScreen();
      } else if (element.webkitRequestFullscreen) {
        element.webkitRequestFullscreen();
      } else if (element.msRequestFullscreen) {
        element.msRequestFullscreen();
      }
    },
  },
  mounted() {
    //this.enterFullscreen();
  },
};
</script>

<style scoped>
.navbar {
  position: relative;
  background-image: url("@/assets/headerbg1.png");
  /* Replace with your background image */
  z-index: 1;
  transition: background-image 1s ease-out;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  background-attachment: fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}

.navbar::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  /* Adjust the opacity and color as desired */
  z-index: -1;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  background-attachment: fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}

/* Custom font style for the top navbar */
.navbar {
  font-family: "Arial", sans-serif;
  font-weight: bold;
}

.navbar-brand {
  font-size: 18px;
}

.navbar-text small {
  font-size: 12px;
}

.dropdown-item {
  font-size: 14px;
}
</style>
