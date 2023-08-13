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
</template>

<script>
import axios from "axios";
import "/node_modules/vue-simple-calendar/dist/style.css";
import "/node_modules/vue-simple-calendar/dist/css/default.css";
import "/node_modules/vue-simple-calendar/dist/css/holidays-us.css";
import "/node_modules/vue-final-modal/dist/style.css";
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
        //     // id: 'asasasasas',
        //     // startDate: new Date(),
        //     // endDate: new Date(),
        //     // title: 'asasasas',
        //     // classes: "purple",
        //     // tooltip: "This spans multiple days hehe",
        // },
      ],
      bookings: [],
      transactions: [],
      rooms: [],
      leisures: [],
    };
  },
  computed: {
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
  },
  created() {
    this.loadData();
  },
  methods: {
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
    //generic calendar functions
    onClickItem(e) {},
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
    onClickDay(d) {
      this.dayreserve = d;
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
    $(".currentPeriod").click();
    this.newItemStartDate = CalendarMath.isoYearMonthDay(CalendarMath.today());
    this.newItemEndDate = CalendarMath.isoYearMonthDay(CalendarMath.today());
  },
};
</script>
<style scoped></style>
