<template :key="componentKey">
  <div class="container-fluid mt-3">
    <div class="row">
      <div class="col-md-12">
        <div class="calendar-parent c-p mt-1">
          <calendar-view
            :items="calendarItems"
            :show-date="showDate"
            :time-format-options="{ hour: 'numeric', minute: '2-digit' }"
            :enable-drag-drop="true"
            :disable-past="disablePast"
            :disable-future="disableFuture"
            :show-times="showTimes"
            :date-classes="myDateClasses"
            :display-period-uom="displayPeriodUom"
            :display-period-count="displayPeriodCount"
            :starting-day-of-week="startingDayOfWeek"
            :class="themeClasses"
            :period-changed-callback="periodChanged"
            :current-period-label="useTodayIcons ? 'icons' : ''"
            :displayWeekNumbers="displayWeekNumbers"
            :enable-date-selection="true"
            :selection-start="selectionStart"
            :selection-end="selectionEnd"
            @date-selection-start="setSelection"
            @date-selection="setSelection"
            @date-selection-finish="finishSelection"
            @drop-on-date="onDrop"
            @click-date="onClickDay"
            @click-item="onClickItem"
          >
            <template #header="{ headerProps }">
              <calendar-view-header
                slot="header"
                :header-props="headerProps"
                @input="setShowDate"
              />
            </template>
          </calendar-view>
        </div>
      </div>
    </div>
  </div>
  <!-- modals -->
  <div
    class="modal fade"
    id="loadBookingModal"
    tabindex="-1"
    aria-labelledby="loadBookingModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content p-3">
        <div class="modal-header p-0">
          <div class="d-flex justify-content-between w-100">
            <div class="d-flex align-items-center">
              <span class="h3 text-primary">Reservation Info</span>
            </div>
            <div>
              <button
                type="button"
                class="btn btn-circle bg-light text-dark btn-dropdown"
                role="button"
                data-bs-toggle="dropdown"
                style="font-size: small"
              >
                <i class="fa fa-ellipsis-h" aria-hidden="true"></i>
              </button>
              <ul
                class="dropdown-menu dropdown-menu-end"
                aria-labelledby="btnDropdown"
                style="z-index: 60000"
              >
                <li>
                  <a class="dropdown-item" href="#" @click="tempCode">
                    <i class="fas fa-ban"></i> Cancel Reservation
                  </a>
                </li>
                <li>
                  <a class="dropdown-item" href="#" @click="">
                    <i class="fas fa-check"></i> Checkin Guest
                  </a>
                </li>
                <li>
                  <a class="dropdown-item" href="#" @click="">
                    <i class="fas fa-times"></i> Checkout Guest
                  </a>
                </li>
                <li>
                  <a class="dropdown-item" href="#" @click="">
                    <i class="fas fa-money-bill"></i> Show Payments
                  </a>
                </li>
                <li>
                  <a class="dropdown-item" href="#" @click="">
                    <i class="fas fa-right-left"></i> Transfer Room
                  </a>
                </li>
                <li>
                  <a class="dropdown-item" href="#" @click="">
                    <i class="fas fa-print"></i> Print Report
                  </a>
                </li>
                <li>
                  <a class="dropdown-item" href="#" @click="">
                    <i class="fas fa-trash"></i> Delete Reservation
                  </a>
                </li>
              </ul>
              &nbsp;
              <!-- Second button -->
              <button
                type="button"
                class="btn btn-circle bg-light text-dark"
                style="font-size: small"
                data-bs-dismiss="modal"
              >
                <i class="fa fa-times" aria-hidden="true"></i>
              </button>
              &nbsp;
            </div>
          </div>
        </div>

        <div class="modal-body">
          <div class="row">
            <div class="col-md-6">
              <div class="form-group row">
                <div class="col-sm-12">
                  <input
                    type="text"
                    v-model="booking.name"
                    placeholder="Add Customer Name"
                    class="form-control"
                    style="font-size: x-large; border: 0"
                    required
                    autocomplete="off"
                    @change=""
                  />
                </div>
              </div>
              <div class="form-group row mt-2">
                <div class="col-sm-12">
                  <input
                    type="text"
                    v-model="booking.clientmail"
                    placeholder="Customer email"
                    class="form-control"
                    style="font-size: medium; border: 0; color: darkgray"
                    maxlength="64"
                    required
                    autocomplete="off"
                    @change=""
                  />
                </div>
              </div>
              <div class="form-group row mt-2">
                <div class="col-sm-12">
                  <input
                    type="text"
                    v-model="booking.contactNumber"
                    placeholder="Customer contact no."
                    class="form-control"
                    style="font-size: medium; border: 0; color: darkgray"
                    maxlength="64"
                    required
                    autocomplete="off"
                    @change=""
                  />
                </div>
              </div>
              <div class="form-group row mt-2">
                <div class="col-sm-12">
                  <input
                    type="text"
                    v-model="booking.clientaddress"
                    placeholder="Customer address"
                    class="form-control"
                    style="font-size: medium; border: 0; color: darkgray"
                    maxlength="64"
                    required
                    autocomplete="off"
                    @change=""
                  />
                </div>
              </div>
              <div class="form-group row mt-2">
                <div class="col-sm-12">
                  <select
                    class="form-control"
                    v-model="booking.clientnationality"
                    style="font-size: medium; border: 0; color: darkgray"
                    maxlength="64"
                    required
                    @change=""
                  >
                    <option value="">--Please select a nationality--</option>
                    <option value="Filipino">Filipino</option>
                    <option value="Foreign">Foreign</option>
                  </select>
                </div>
              </div>
              <div class="form-group row mt-2">
                <div class="col-sm-12">
                  <select
                    class="form-control"
                    v-model="booking.clientType"
                    style="font-size: medium; border: 0; color: darkgray"
                    maxlength="64"
                    required
                    @change=""
                  >
                    <option value="">--Please select customer type--</option>
                    <option value="in-house">In house</option>
                  </select>
                </div>
              </div>
              <div class="form-group mt-2">
                <textarea
                  class="form-control"
                  maxlength="256"
                  placeholder="Add remarks"
                  rows="3"
                ></textarea>
              </div>
              <div class="form-group mt-2 d-flex justify-content-end">
                <button class="btn btn-circle" @click="">
                  <i class="fas fa-arrow-right"></i>
                </button>
              </div>
              <div class="form-group mt-2">
                <div class="row">
                  <div class="col-md-12" style="height: 10px; overflow-y: auto">
                    <div class="row" v-for="item in []" :key="index">
                      <div class="col-md-1 d-flex align-items-center">
                        <span style="font-size: 28px">
                          <i class="fas fa-comment text-primary"></i>
                        </span>
                      </div>
                      <div class="col-md-11">
                        <div class="row"></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6 bg-light p-0">
              <div id="accordion">
                <div class="card">
                  <div class="card-header" id="headingOne">
                    <h5 class="mb-0 d-flex justify-content-between">
                      <span style="font-size: large">
                        <i class="fa fa-calendar"></i>
                        <span class="p-2">Reservation Date</span>
                      </span>
                    </h5>
                  </div>
                  <div
                    id="collapseOne"
                    class="collapse show"
                    aria-labelledby="headingOne"
                    data-parent="#accordion"
                  >
                    <div class="card-body">
                      <div class="form-group row">
                        <label for="startdate" class="col-sm-4 col-form-label"
                          >Select Date:</label
                        >
                        <div class="col-sm-8">
                          <input
                            ref="daterange"
                            type="text"
                            class="form-control"
                            name="daterange"
                            value=""
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="card">
                  <div class="card-header" id="headingOne">
                    <h5 class="mb-0 d-flex justify-content-between">
                      <span style="font-size: large">
                        <i class="fas fa-building"></i>
                        <span class="p-2">Property</span>
                      </span>
                    </h5>
                  </div>
                  <div
                    id="collapseOne"
                    class="collapse show"
                    aria-labelledby="headingOne"
                    data-parent="#accordion"
                  >
                    <div class="card-body">
                      <div class="form-group row">
                        <label for="startdate" class="col-sm-4 col-form-label"
                          >Room/Cottage:</label
                        >
                        <div class="col-sm-8">
                          <v-select
                            :multiple="true"
                            :options="updatedRooms"
                            label="name"
                            v-model="booking.room_name"
                            required
                          >
                            <template #option="{ name, type, price }">
                              <h6 style="margin: 0">{{ name }}</h6>
                              <em
                                ><small>{{ type }}</small></em
                              >
                              <em
                                ><small> ({{ price }} units)</small></em
                              >
                            </template>
                          </v-select>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="card" style="z-index: 50000 !important">
                  <div class="card-body">
                    <ul class="list-group list-group-flush">
                      <li class="list-group-item p-0">
                        <div class="row">
                          <div class="col-md-1">
                            <i class="fa fa-briefcase" aria-hidden="true"></i>
                          </div>
                          <div class="col-md-9">
                            <span style="font-weight: bold">Status</span>
                            <br />
                            {{ booking.status }}
                          </div>
                        </div>
                      </li>

                      <li class="list-group-item p-0">
                        <div class="row">
                          <div class="col-md-1">
                            <i class="fas fa-plus-circle"></i>
                          </div>
                          <div class="col-md-11">
                            <span style="font-weight: bold">Created</span>
                            <br />
                            {{ booking.created }}
                          </div>
                        </div>
                      </li>
                      <li class="list-group-item p-0">
                        <div class="row">
                          <div class="col-md-1">
                            <i class="fas fa-pen"></i>
                          </div>
                          <div class="col-md-11">
                            <span style="font-weight: bold">Updated</span>
                            <br />
                            {{ booking.modified }}
                          </div>
                        </div>
                      </li>
                      <li class="list-group-item p-0">
                        <div class="row">
                          <div class="col-md-1">
                            <i class="fas fa-link"></i>
                          </div>
                          <div class="col-md-11">
                            <span style="font-weight: bold">Task ID</span><br />
                            {{ booking.itemID.substring(0, 24) }}
                          </div>
                        </div>
                      </li>
                      <li class="list-group-item p-0">
                        <div class="row">
                          <div class="col-md-1">
                            <i class="fas fa-link"></i>
                          </div>
                          <div class="col-md-11">
                            <span style="font-weight: bold">Group ID</span
                            ><br />
                            {{
                              booking.groupkey === null
                                ? "None"
                                : booking.groupkey.substring(0, 24)
                            }}
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="addBookingModal"
    tabindex="-1"
    aria-labelledby="addBookingLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="addBookingModalLabel">
            Add New Reservation
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="loadNewBooking">
            <div class="form-group row">
              <div class="col-sm-12">
                <input
                  type="text"
                  class="form-control"
                  v-model="this.booking.name"
                  maxlength="64"
                  placeholder="Name of the customer"
                  required
                  autocomplete="off"
                />
              </div>
            </div>
            <div class="form-group row mt-2">
              <div class="col-sm-6">
                <select
                  class="form-control"
                  v-model="this.booking.status"
                  required
                >
                  <option value="">-- Select Reservation Status --</option>
                  <option value="reserved">Pre-booked</option>
                  <option value="checkedin">Walk-in Guest</option>
                </select>
              </div>
              <div class="col-sm-6">
                <v-select
                  :multiple="true"
                  :options="updatedRooms"
                  label="name"
                  v-model="booking.room_name"
                  required
                >
                  <template #option="{ name, type, price }">
                    <h6 style="margin: 0">{{ name }}</h6>
                    <em
                      ><small>{{ type }}</small></em
                    >
                    <em
                      ><small> ({{ price }} units)</small></em
                    >
                  </template>
                </v-select>
              </div>
            </div>
            <div class="form-group row mt-2">
              <label for="startdate" class="col-sm-3 col-form-label"
                >Select Date:</label
              >
              <div class="col-sm-9">
                <input
                  ref="daterange"
                  type="text"
                  class="form-control"
                  name="daterange"
                  value=""
                  required
                />
              </div>
            </div>
            <div class="form-group row mt-2">
              <div class="col-sm-12 d-flex flex-row-reverse">
                <button type="submit" class="btn btn-primary">
                  Create Booking
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
import axios from "axios";
import { useAuthStore } from "@/stores/authStore";
import "/node_modules/vue-simple-calendar/dist/style.css";
import "/node_modules/vue-simple-calendar/dist/css/default.css";
import "/node_modules/vue-simple-calendar/dist/css/holidays-us.css";
import "/node_modules/vue-final-modal/dist/style.css";

//helper functions
function formatDate(date) {
  const yyyy = date.getFullYear();
  let mm = date.getMonth() + 1; // Months are 0-based, so +1
  let dd = date.getDate();

  // Convert month and date to 2 digits
  mm = (mm < 10 ? "0" : "") + mm;
  dd = (dd < 10 ? "0" : "") + dd;

  return yyyy + "-" + mm + "-" + dd;
}

function defaultFormatDate(date) {
  let dd = date.getDate();
  let mm = date.getMonth() + 1; // January is 0!
  let yyyy = date.getFullYear();

  if (dd < 10) {
    dd = "0" + dd;
  }

  if (mm < 10) {
    mm = "0" + mm;
  }

  return dd + "/" + mm + "/" + yyyy;
}

function parseDate(dateString) {
  const [day, month, year] = dateString.split("/");
  return new Date(`${year}-${month}-${day}`).setHours(0, 0, 0, 0);
}

function generateUniqueString() {
  let randomString = "";
  while (randomString.length < 8) {
    randomString += Math.random().toString(36).substr(2, 36);
  }
  randomString = randomString.substr(0, 8);
  return randomString;
}

import {
  CalendarView,
  CalendarViewHeader,
  CalendarMath,
} from "vue-simple-calendar";
export default {
  components: {
    CalendarView,
    CalendarViewHeader,
  },
  data() {
    return {
      //generic config for vue-simple-calendar
      showDate: this.thisMonth(1),
      message: "",
      startingDayOfWeek: 1,
      disablePast: false,
      disableFuture: false,
      displayPeriodUom: "week",
      displayPeriodCount: 1,
      displayWeekNumbers: false,
      showTimes: true,
      selectionStart: null,
      selectionEnd: null,
      newItemTitle: "",
      newItemStartDate: "",
      newItemEndDate: "",
      useDefaultTheme: true,
      useHolidayTheme: true,
      useTodayIcons: false,
      calendarItems: [
        // {
        //   id: "asasasasas",
        //   startDate: new Date(),
        //   endDate: new Date(),
        //   title: "asasasas",
        //   classes: "purple",
        //   tooltip: "This spans multiple days hehe",
        // },
      ],
      booking: {
        name: "",
        clientmail: "",
        clientaddress: "",
        clientnationality: "",
        clientType: "",
        checkinDate: formatDate(new Date()),
        checkoutDate: formatDate(new Date()),
        room_name: "",
        room_type: "",
        room_price: "",
        remarks: "",
        contactNumber: "",
        status: "",
        itemID: "",
        actualCheckoutDate: "",
        cancellationDate: "",
        isPaid: "",
        created_at: "",
        totalPrice: "",
        partialPayment: "",
        processedBy: "",
        groupkey: "",
        created: "",
        modified: "",
        states: [],
      },
      reservationDaterange: "",
      currentItemID: "",
      itemIndex: -1,
      bookings: [],
      transactions: [],
      rooms: [],
      leisures: [],
    };
  },
  computed: {
    userdata() {
      const authStore = useAuthStore();
      const user = authStore.user;
      return user;
    },
    userLocale() {
      return CalendarMath.getDefaultBrowserLocale;
    },
    dayNames() {
      return CalendarMath.getFormattedWeekdayNames(this.userLocale, "long", 0);
    },
    themeClasses() {
      return {
        "theme-default": this.useDefaultTheme,
        "holiday-us-traditional": this.useHolidayTheme,
        "holiday-us-official": this.useHolidayTheme,
      };
    },
    myDateClasses() {
      // This was added to demonstrate the dateClasses prop. Note in particular that the
      // keys of the object are `yyyy-mm-dd` ISO date strings (not dates), and the values
      // for those keys are strings or string arrays. Keep in mind that your CSS to style these
      // may need to be fairly specific to make it override your theme's styles. See the
      // CSS at the bottom of this component to see how these are styled.
      const o = {};
      const theFirst = this.thisMonth(1);
      const ides = [2, 4, 6, 9].includes(theFirst.getMonth()) ? 15 : 13;
      const idesDate = this.thisMonth(ides);
      o[CalendarMath.isoYearMonthDay(idesDate)] = "ides";
      o[CalendarMath.isoYearMonthDay(this.thisMonth(21))] = [
        "do-you-remember",
        "the-21st",
      ];
      return o;
    },
    currentDate() {
      const options = {
        month: "2-digit",
        day: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: true,
      };
      return new Date().toLocaleString("en-US", options);
    },
    updatedRooms() {
      return this.rooms.filter((room) => {
        // Check if there are any bookings for this room that overlap with the specified date range
        const overlappingBookings = this.bookings.filter((booking) => {
          // Check if the booking is not cancelled and not checked out
          if (
            booking.status === "cancelled" ||
            booking.status === "checkedout"
          ) {
            return false;
          }

          // Check if the booking's room_name matches the current room and the date range overlaps with the reservation
          const checkInDate = parseDate(booking.checkinDate);
          const checkOutDate = parseDate(booking.checkoutDate);
          const startDate = parseDate(this.booking.checkinDate);
          const endDate = parseDate(this.booking.checkoutDate);
          const isOverlap =
            booking.room_name === room.name &&
            startDate <= checkOutDate &&
            endDate >= checkInDate;

          return isOverlap;
        });

        // Check if there exists a booking with the same room_name in yesterday that has not been checked out
        const yesterday = new Date();
        yesterday.setDate(yesterday.getDate() - 1);
        const yesterdayBooking = this.bookings.find((prevBooking) => {
          const prevCheckOutDate = parseDate(prevBooking.checkoutDate);
          return (
            prevBooking.room_name === room.name &&
            new Date(prevCheckOutDate).toDateString() ===
              new Date(yesterday).toDateString() &&
            prevBooking.status === "checkedin"
          );
        });

        // Return true if there are no overlapping bookings and no booking in yesterday that has not been checked out
        return overlappingBookings.length === 0 && !yesterdayBooking;
      });
    },
    formattedDateRange() {
      const daterange = this.$refs.daterange.value;
      const [checkinDate, checkoutDate] = daterange
        .split(" - ")
        .map((date) => formatDate(new Date(date)));
      return { checkinDate: checkinDate, checkoutDate: checkinDate };
    },
  },
  created() {
    this.loadData();
  },
  methods: {
    toggleModal(id) {
      $(`#${id}`).modal("toggle");
    },
    convertToDate(dateString) {
      let [day, month, year] = dateString.split("/");
      return `${month}/${day}/${year}`;
    },
    reverseFormatDateRange(checkin, checkout) {
      return `${this.convertToDate(checkin)} - ${this.convertToDate(checkout)}`;
    },
    async loadData() {
      this.loadRooms();
      this.loadBookings();
      this.loadTransactions();
      this.loadLeisures();
    },
    async loadRooms() {
      const response = await axios.get(this.API_URL + "rooms/");
      this.rooms = response.data;
    },
    async loadBookings() {
      const response = await axios.get(this.API_URL + "bookings/");
      this.bookings = response.data;
      this.populateCalendarItems();
    },
    async loadTransactions() {
      const response = await axios.get(
        this.API_URL + "transactions_itemizer/0/"
      );
      this.transactions = response.data;
    },
    async loadLeisures() {
      const response = await axios.get(this.API_URL + "leisures/");
      this.leisures = response.data;
    },
    async saveBookings() {
      let data = {
        name: this.booking.name,
        clientmail: this.booking.clientmail,
        clientaddress: this.booking.clientaddress,
        clientnationality: this.booking.clientnationality,
        clientType: this.booking.clientType,
        checkinDate: this.booking.checkinDate,
        checkoutDate: this.booking.checkoutDate,
        room_name: this.booking.room_name,
        room_type: this.booking.room_type,
        room_price: this.booking.room_price,
        remarks: this.booking.remarks,
        contactNumber: this.booking.contactNumber,
        status: this.booking.status,
        itemID: this.booking.itemID,
        actualCheckoutDate: this.booking.actualCheckoutDate,
        cancellationDate: this.booking.cancellationDate,
        isPaid: this.booking.isPaid,
        created_at: this.booking.created_at,
        totalPrice: this.booking.totalPrice,
        partialPayment: this.booking.partialPayment,
        processedBy: this.booking.processedBy,
        groupkey: this.booking.groupkey,
        states: JSON.stringify(this.booking.states),
      };
      const isDataExists =
        this.bookings.findIndex((o) => o.itemID === data.itemID) !== -1;
      if (!isDataExists) {
        this.bookings.push(data);
      } else {
        this.generateArrayID(this.bookings, this.currentItemID);
        let item = this.bookings[this.itemIndex];
        item.name = data.name;
        item.clientmail = data.clientmail;
        item.clientaddress = data.clientaddress;
        item.clientnationality = data.clientnationality;
        item.clientType = data.clientType;
        item.checkinDate = data.checkinDate;
        item.checkoutDate = data.checkoutDate;
        item.room_name = data.room_name;
        item.room_type = data.room_type;
        item.room_price = data.room_price;
        item.remarks = data.remarks;
        item.contactNumber = data.contactNumber;
        item.status = data.status;
        item.itemID = data.itemID;
        item.actualCheckoutDate = data.actualCheckoutDate;
        item.cancellationDate = data.cancellationDate;
        item.isPaid = data.isPaid;
        item.created_at = data.created_at;
        item.totalPrice = data.totalPrice;
        item.partialPayment = data.partialPayment;
        item.processedBy = data.processedBy;
        item.groupkey = data.groupkey;
        item.states = data.states;
      }
      this.populateCalendarItems();
      // try {
      //   await axios.put(`${this.API_URL}bookings/${booking.id}/`, data);
      // } catch (e) {
      //   console.error(e);
      // }
    },
    generateArrayID(arr, ref) {
      this.itemIndex = arr.findIndex((o) => o.itemID === ref);
    },
    setInitialData(e) {
      this.currentItemID = e.id;
      this.generateArrayID(this.bookings, this.currentItemID);
      const data = this.bookings[this.itemIndex];
      this.booking = {
        name: data.name,
        clientmail: data.clientmail,
        clientaddress: data.clientaddress,
        clientnationality: data.clientnationality,
        clientType: data.clientType,
        checkinDate: data.checkinDate,
        checkoutDate: data.checkoutDate,
        room_name: data.room_name,
        room_type: data.room_type,
        room_price: data.room_price,
        remarks: data.remarks,
        contactNumber: data.contactNumber,
        status: data.status,
        itemID: data.itemID,
        actualCheckoutDate: data.actualCheckoutDate,
        cancellationDate: data.cancellationDate,
        isPaid: data.isPaid,
        created_at: data.created_at,
        totalPrice: data.totalPrice,
        partialPayment: data.partialPayment,
        processedBy: data.processedBy,
        groupkey: data.groupkey,
        created: new Date(data.created).toLocaleString(),
        modified: new Date(data.modified).toLocaleString(),
        states: JSON.parse(data.states),
      };
      $('input[name="daterange"]').daterangepicker({
        autoApply: true,
        startDate: this.convertToDate(this.booking.checkinDate),
        endDate: this.convertToDate(this.booking.checkoutDate),
      });
    },
    initializeData() {
      this.booking = {
        name: "",
        clientmail: "",
        clientaddress: "",
        clientnationality: "",
        clientType: "",
        checkinDate: defaultFormatDate(this.dayreserve),
        checkoutDate: defaultFormatDate(this.dayreserve),
        room_name: "",
        room_type: "",
        room_price: "",
        remarks: "",
        contactNumber: "",
        status: "reserved",
        itemID: "e" + new Date().getTime().toString() + generateUniqueString(),
        actualCheckoutDate: "",
        cancellationDate: "",
        isPaid: "no",
        created_at: new Date().toLocaleString(),
        totalPrice: 0,
        partialPayment: 0,
        processedBy: this.userdata.fName + " " + this.userdata.lName,
        groupkey: null,
        created: new Date().toLocaleString(),
        modified: new Date().toLocaleString(),
        states: [
          {
            created_at: new Date(),
            actor: this.userdata.role,
            comment: "created the task on " + new Date().toLocaleString(),
          },
        ],
      };
      $('input[name="daterange"]').daterangepicker({
        autoApply: true,
        startDate: this.dayreserve.toLocaleDateString(),
        endDate: this.dayreserve.toLocaleDateString(),
      });
    },
    //generic calendar functions
    onClickItem(e) {
      this.setInitialData(e);
      this.toggleModal("loadBookingModal");
    },
    thisMonth(d, h, m) {
      const t = new Date();
      return new Date(t.getFullYear(), t.getMonth(), d, h || 0, m || 0);
    },
    periodChanged() {
      // range, eventSource) {
      // Demo does nothing with this information, just including the method to demonstrate how
      // you can listen for changes to the displayed range and react to them (by loading items, etc.)
      //console.log(eventSource)
      //console.log(range)
    },
    setShowDate(d) {
      this.showDate = d;
    },
    addNewBooking() {
      this.initializeData();
      this.toggleModal("addBookingModal");
    },
    loadNewBooking() {
      this.toggleModal("addBookingModal");
      this.toggleModal("loadBookingModal");

      for (let prop of this.booking.room_name) {
        this.booking.itemID =
          "e" + new Date().getTime().toString() + generateUniqueString();
        this.booking.room_name = prop.name;
        this.booking.room_price = prop.price;
        this.booking.room_type = prop.type;
        console.log(this.booking);
        this.saveBookings();
      }
    },
    onClickDay(d) {
      this.dayreserve = d;
      this.addNewBooking();
    },
    setSelection(dateRange) {},
    finishSelection(dateRange) {},
    onDrop(item, date) {},
    populateCalendarItems() {
      this.calendarItems = this.bookings.map((booking) => {
        const startDate =
          booking.checkinDate.split("/")[2] +
          "-" +
          booking.checkinDate.split("/")[1] +
          "-" +
          booking.checkinDate.split("/")[0];
        const endDate =
          booking.checkoutDate.split("/")[2] +
          "-" +
          booking.checkoutDate.split("/")[1] +
          "-" +
          booking.checkoutDate.split("/")[0];
        const title = `${booking.room_name}-${
          booking.groupkey === null
            ? ""
            : '<span class="text-white">group</span>-'
        }${booking.name}<span style="display:none">~${booking.itemID}~</span>`;
        const id = booking.itemID;
        const tooltip = `${booking.room_name}-${booking.name}\n*${
          booking.status
        }-${
          booking.isPaid === "yes"
            ? "fully paid"
            : booking.isPaid === "no"
            ? "not paid"
            : "partial"
        }`;
        let classes = "";
        if (booking.status === "reserved") {
          if (booking.isPaid === "partial" || booking.isPaid === "yes") {
            classes = ["hotel-reserved"];
          } else {
            classes = ["hotel-reserved-unpaid"];
          }
        } else if (booking.status === "checkedin") {
          if (booking.isPaid === "no" || booking.isPaid === "") {
            classes = ["hotel-checkedin-unpaid"];
          } else if (booking.isPaid === "partial") {
            classes = ["hotel-checkedin-partial"];
          } else {
            classes = ["hotel-checkedin-paid"];
          }
        } else if (booking.status === "cancelled") {
          classes = ["hotel-cancelled"];
        } else if (booking.status === "checkedout") {
          classes = ["hotel-checkedout"];
        }
        return { startDate, endDate, title, id, classes, tooltip };
      });
    },
  },
  mounted() {
    var vm = this;
    $(document).on("click", function (e) {
      // Check if the clicked element or its parents don't have the 'btn-dropdown' class
      if (
        !$(e.target).hasClass("btn-dropdown") &&
        $(e.target).closest(".btn-dropdown").length === 0
      ) {
        e.stopPropagation();
        vm.isDropdownVisible = false;
      }
    });
    $(".currentPeriod").click();
    this.newItemStartDate = CalendarMath.isoYearMonthDay(CalendarMath.today());
    this.newItemEndDate = CalendarMath.isoYearMonthDay(CalendarMath.today());
  },
};
</script>
<style scoped>
.btn-circle {
  border-radius: 50%;
  /* Makes the button circular */
  padding: 5px 10px;
  /* Adjust as per your need */
  background-color: #007bff;
  /* Default bootstrap primary color */
  color: #fff;
  /* White color for the icon */
}

.dropdown-menu .dropdown-item {
  display: flex;
  align-items: center;
}

.dropdown-item i.fas {
  width: 20px; /* Adjust as per your requirements */
  margin-right: 8px; /* Space between icon and text */
}

.app-header {
  background-color: #3d474d;
  color: white;
  box-shadow: 0 0.125rem 0.5rem rgba(0, 0, 0, 0.2);
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 0px;
}
</style>
