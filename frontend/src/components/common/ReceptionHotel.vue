<template>
  <div class="row">
    <div class="cv-header mb-0 p-1" style="background-color: #f0f0f0">
      <div class="cv-header-nav">
        <button
          @click="prevYear"
          class="previousYear"
          aria-label="Previous Year"
        >
          &lt;&lt;
        </button>
        <button
          @click="prevPeriod"
          class="previousPeriod"
          aria-label="Previous Period"
        >
          &lt;
        </button>
        <button class="currentPeriod" aria-label="Current Period">
          {{
            currentDate.toLocaleDateString("en-US", {
              month: "long",
              year: "numeric",
            })
          }}
        </button>
        <button @click="nextPeriod" class="nextPeriod" aria-label="Next Period">
          &gt;
        </button>
        <button @click="nextYear" class="nextYear" aria-label="Next Year">
          &gt;&gt;
        </button>
      </div>
      <div class="periodLabel">
        {{
          nextDate.toLocaleDateString("en-US", {
            month: "long",
            year: "numeric",
          })
        }}
      </div>
      <div class="roomTypeSelect">
        <select
          class="form-select"
          v-model="currentRoomType"
          aria-label="Select Room Type"
        >
          <option selected disabled value="Select Room Type">
            Select Room Type
          </option>
          <option
            v-for="(category, index) in roomcategoriesdata.filter((o) =>
              o.name.toLowerCase().includes('room')
            )"
            :key="category.id"
            :value="category.name"
          >
            {{ category.name }}
          </option>
        </select>
      </div>
    </div>

    <table class="table table-bordered" ref="table">
      <thead>
        <tr>
          <th style="width: 80px">Room</th>
          <th style="width: 60px">Status</th>
          <th
            style="width: 60px; font-size: smaller"
            class="text-center"
            v-for="day in days"
            :key="day"
            :class="{ 'bg-def': isCurrentDate(day) }"
          >
            <span>{{ day.toLocaleDateString() }}</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(room, roomIndex) in filteredRooms" :key="roomIndex">
          <td>{{ room.name }}</td>
          <td>
            <span
              style="height: 40px; max-height: 40px"
              class="d-flex justify-content-center align-items-center btn-item text-white"
              :class="room.status === 'clean' ? 'bg-success' : 'bg-danger'"
              @click="$emit('clickRoom-action', room)"
              >{{ room.status }}</span
            >
          </td>

          <template
            v-for="(day, dayIndex) in daysWithColspan[roomIndex]"
            :key="dayIndex"
          >
            <td v-if="day.bookings.length > 0" :colspan="day.colspan">
              <div class="d-flex justify-content-between align-items-center">
                <span
                  style="height: 40px; max-height: 40px"
                  v-for="(booking, bookingIndex) in day.bookings"
                  :key="bookingIndex"
                  class="d-flex justify-content-center align-items-center pen-border"
                  :class="[
                    'btn-item',
                    'draggable',
                    getBookingStatusClass(booking),
                  ]"
                  draggable="true"
                  @dragstart="
                    this.dayDragging = false;
                    $emit('dragstart-action', $event, room, booking);
                  "
                  @dragend="$emit('dragend-action', $event)"
                  :style="{ width: day.colspan * 75 + 'px' }"
                  @click="$emit('clickItem-action', booking, room)"
                >
                  <i
                    v-if="booking.colspan < booking.bookingDurationDays"
                    style="font-size: xx-small"
                    class="fas fa-arrow-right text-light"
                  ></i>
                  {{ booking.name }}
                </span>
              </div>
            </td>
            <td
              v-else
              draggable="true"
              @dragstart="
                this.dayDragging = true;
                dragstart($event);
                $emit('dragstartday-action', $event, day.day, room);
              "
              @dragend="dragend($event)"
              @dragenter="dragenter($event)"
              @dragover.prevent="$emit('dragover-action', $event)"
              @drop="$emit('dragdrop-action', $event, day.day, room)"
              @click="$emit('clickDay-action', day.day, room)"
            ></td>
          </template>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
function parseDate(dateString) {
  const [day, month, year] = dateString.split("/");
  return new Date(`${year}-${month}-${day}`).setHours(0, 0, 0, 0);
}

export default {
  props: {
    bookingsdata: {
      type: Array,
      required: true,
    },
    roomcategoriesdata: {
      type: Array,
      required: true,
    },
    roomsdata: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      dayDragging: false,
      activeCells: [],
      booking: [],
      startDay: new Date().getDate(),
      monthIndex: new Date().getMonth(),
      currentYear: new Date().getFullYear(),
      currentDay: new Date(),
      draggedBooking: null,
      dropTarget: null,
      currentRoomType: "",
      draggedBookingIndex: null,
      draggedRoomIndex: null,
    };
  },
  methods: {
    dragstart(event) {
      //event.target.style.opacity = 0;
      event.target.style.backgroundColor = "#fff3cd";
      this.activeCells.push(event.target);
      const img = new Image();
      event.dataTransfer.setDragImage(img, 0, 0);
    },
    dragend(event) {
      //event.target.style.opacity = 1;
      this.activeCells.forEach((cell) => (cell.style.backgroundColor = ""));
      this.activeCells = [];
      this.dayDragging = false;
    },
    dragenter(event) {
      if (this.dayDragging) {
        // Change background color of the cell
        event.target.style.backgroundColor = "#fff3cd";
        // Add the cell to the active cells
        this.activeCells.push(event.target);
      }
    },
    getBookingStatusClass(booking) {
      if (booking.status === "reserved") {
        return booking.isPaid === "partial"
          ? "cv-item hotel-reserved"
          : "cv-item hotel-reserved-unpaid";
      } else if (booking.status === "checkedin") {
        return booking.isPaid === "yes"
          ? "cv-item hotel-checkedin-paid"
          : booking.isPaid === "partial"
          ? "cv-item hotel-checkedin-partial"
          : "cv-item hotel-checkedin-unpaid";
      } else if (booking.status === "checkedout") {
        return "cv-item hotel-checkedout";
      } else if (booking.status === "cancelled") {
        return "cv-item hotel-cancelled";
      } else {
        return ""; // Return an empty string for default/unknown cases
      }
    },
    isCurrentDate(day) {
      const currentDate = new Date();
      return (
        day.getFullYear() === currentDate.getFullYear() &&
        day.getMonth() === currentDate.getMonth() &&
        day.getDate() === currentDate.getDate()
      );
    },
    prevYear() {
      this.startDay -= 16; // Decrease the current year by 1
      this.adjustMonth(); // Adjust the month based on the new year
    },

    nextYear() {
      this.startDay += 16; // Increase the current year by 1
      this.adjustMonth(); // Adjust the month based on the new year
    },
    prevPeriod() {
      this.startDay -= 1;
      this.adjustMonth();
    },
    nextPeriod() {
      this.startDay += 1;
      this.adjustMonth();
    },
    adjustMonth() {
      while (this.startDay < 1) {
        this.monthIndex--;
        if (this.monthIndex < 0) {
          this.monthIndex = 11;
          this.currentYear--; // Also adjust the year if necessary
        }
        this.startDay += this.daysInMonth;
      }

      while (this.startDay > this.daysInMonth) {
        this.startDay -= this.daysInMonth;
        this.monthIndex++;
        if (this.monthIndex > 11) {
          this.monthIndex = 0;
          this.currentYear++; // Also adjust the year if necessary
        }
      }
    },
    getDayOfWeek(day) {
      const currentDate = new Date(this.currentYear, this.monthIndex, day);
      const dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
      return dayNames[currentDate.getDay()];
    },
  },
  computed: {
    filteredRooms() {
      return this.roomsdata.filter(
        (item) =>
          item.type === this.currentRoomType && item.isAvailable === true
      );
    },
    bookings() {
      let filteredBookings = this.bookingsdata.filter(
        (booking) =>
          booking.status !== "cancelled" && booking.status !== "checkedout"
      );
      // Now, filteredBookings contains unique bookings per checkinDate.
      filteredBookings.sort((a, b) => {
        const dateA = new Date(parseDate(a.checkinDate));
        const dateB = new Date(parseDate(b.checkinDate));
        return dateA - dateB;
      });
      return filteredBookings;
    },
    daysInMonth() {
      return new Date(this.currentYear, this.monthIndex + 1, 0).getDate();
    },
    currentDate() {
      return new Date(this.currentYear, this.monthIndex, this.startDay);
    },
    nextDate() {
      return new Date(
        this.currentYear,
        this.monthIndex,
        Math.min(this.startDay + 15, this.daysInMonth)
      );
    },
    days() {
      return Array.from(
        { length: 16 },
        (_, i) => new Date(this.currentYear, this.monthIndex, this.startDay + i)
      );
    },
    monthIndex() {
      const currentDate = new Date();
      return currentDate.getMonth();
    },
    currentMonth() {
      const currentDate = new Date();
      const monthNames = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ];
      return monthNames[currentDate.getMonth()];
    },
    currentYear() {
      const currentDate = new Date();
      return currentDate.getFullYear();
    },
    daysWithColspan() {
      return this.filteredRooms.map((room) => {
        let daysWithColspan = [];
        const bookingsForRoom = this.bookings;

        // Initialize a pointer to track the current day index
        let dayIndex = 0;

        while (dayIndex < this.days.length) {
          const day = this.days[dayIndex];

          const bookingsForDay = bookingsForRoom.filter((booking) => {
            const isRoom = booking.room_name === room.name;
            const checkinDay = new Date(parseDate(booking.checkinDate));
            const checkoutDay = new Date(parseDate(booking.checkoutDate));
            return day >= checkinDay && day <= checkoutDay && isRoom;
          });

          if (bookingsForDay.length > 0) {
            // Compute the duration of the booking
            const booking = bookingsForDay[0];
            const checkinDay = new Date(parseDate(booking.checkinDate));
            const checkoutDay = new Date(parseDate(booking.checkoutDate));
            const bookingDurationDays =
              Math.ceil((checkoutDay - checkinDay) / (1000 * 60 * 60 * 24)) + 1;

            // Check if the booking duration exceeds the remaining days in the period
            const remainingDays = this.days.length - dayIndex;
            const daysFromCheckin = Math.ceil(
              (day - checkinDay) / (1000 * 60 * 60 * 24)
            ); // Add this line
            const effectiveBookingDays = Math.min(
              bookingDurationDays - daysFromCheckin,
              remainingDays
            ); // Change this line

            // Store the bookings in the cell for the day
            daysWithColspan.push({
              bookings: bookingsForDay.map((booking) => ({
                ...booking,
                class: "bg-success",
                colspan: effectiveBookingDays,
                bookingDurationDays: bookingDurationDays,
              })),
              colspan: effectiveBookingDays,
            });

            // Update the day index to skip the booked days
            dayIndex += effectiveBookingDays;
          } else {
            // Add non-booked day
            daysWithColspan.push({ bookings: [], colspan: 1, day: day });

            // Move to the next day
            dayIndex++;
          }
        }

        return daysWithColspan;
      });
    },
  },
  mounted() {},
};
</script>
<style scoped>
/* Add any additional CSS styles here */
table {
  table-layout: fixed;
  word-wrap: break-word;
}

.draggable {
  cursor: grab;
}

.bg-def {
  background-color: #fff3cd;
}

.cv-item.hotel-reserved {
  background-color: #5c6bc0;
  /* adjust the color as needed */
}

.cv-item.hotel-reserved-unpaid {
  background-color: #ef5350;
  /* adjust the color as needed */
}

.cv-item.hotel-checkedin-unpaid {
  background-color: #66bb6a;
  /* adjust the color as needed */
}

.cv-item.hotel-checkedin-partial {
  background-color: #42a5f5;
  /* adjust the color as needed */
}

.cv-item.hotel-checkedin-paid {
  background-color: #ffee58;
  /* adjust the color as needed */
}

.cv-item.hotel-cancelled {
  background-color: #bdbdbd;
  /* adjust the color as needed */
}

.cv-item.hotel-checkedout {
  background-color: #ff7043;
  /* adjust the color as needed */
}

.dropzone {
  display: block;
  height: 100%;
  text-align: center;
  padding: 10px;

  cursor: pointer;
}
.btn-item {
  position: relative;
  white-space: nowrap;
  overflow: hidden;
  border-width: 1px;
  direction: initial;
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
  border: 1px solid #f7fcff;
  border-radius: 1rem;
  transition: all 0.2s ease-in-out;
  text-align: center;
}
.btn-item:hover {
  cursor: pointer;
  transform: translateY(-5px);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
}
/* .pen-border {
    position: relative;
    padding-right: 20px; 
}

.pen-border:after {
    content: "";
    position: absolute;
    top: 0;
    bottom: 0;
    right: -15px;
    width: 50px;
    background: #f7fcff;
    transform: skewX(-45deg);
} */
</style>
