<template>
    <div class="container-fluid main">
    <h2>{{ currentMonth }} {{ currentYear }}</h2>
    <table class="table table-bordered">
        <thead>
            <tr>
                <th style="width: 100px;">Room Number</th>
                <th style="width: 45px" class="text-center" v-for="day in days" :key="day">{{ day }}</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(room, roomIndex) in rooms" :key="roomIndex">
                <td>{{ room.name }}</td>
                <td v-for="(day, dayIndex) in daysWithColspan[roomIndex]" :key="dayIndex" :colspan="day.colspan">
                    <template v-if="day.bookings.length > 0">
                        <button v-for="(booking, bookingIndex) in day.bookings" :key="bookingIndex" :class="booking.class"
                            class="btn btn-success btn-sm" :style="{ width: `${100 / day.bookings.length}%` }">
                            <i class="fas fa-check"></i>
                        </button>
                    </template>
                </td>
            </tr>
        </tbody>
    </table>
</div>
</template>
<script>
import axios from 'axios';
function parseDate(dateString) {
    const [day, month, year] = dateString.split('/');
    return new Date(`${year}-${month}-${day}`);
}
export default {
    data() {
        return {
            bookings: [
                // {
                //         room_name: "BR1 Room",
                //         checkinDate: "01/07/2023",
                //         checkoutDate: "02/07/2023",
                //         status: "reserved",
                //     },
                //     {
                //         room_name: "BR1 Room",
                //         checkinDate: "20/07/2023",
                //         checkoutDate: "25/07/2023",
                //         status: "reserved",
                //     },
            ],
            days: [],
            rooms: [],
            booking: [],
        };
    },
    created() {
        this.loadData();
    },
    methods: {
        async loadData() {
            const rooms = await axios.get(this.API_URL + "rooms/");
            this.rooms = rooms.data.filter(item => item.isAvailable === true && item.type === "BEACH ROOM");
            const bookings = await axios.get(this.API_URL + "bookings/");
            let filteredBookings = bookings.data.filter(
                booking => booking.status !== "cancelled" && new Date(parseDate(booking.checkinDate).toLocaleString()).getMonth() === new Date().getMonth()
            );
            // Now, filteredBookings contains unique bookings per checkinDate.
            filteredBookings.sort((a, b) => {
                const dateA = new Date(parseDate(a.checkinDate));
                const dateB = new Date(parseDate(b.checkinDate));
                return dateA - dateB;
            });
            this.bookings = filteredBookings;
            // alert(
            //     JSON.stringify(
            //         this.bookings[0]
            //     )
            // )
        },
    },
    computed: {
        currentMonth() {
            const currentDate = new Date();
            const monthNames = [
                "January", "February", "March", "April", "May", "June", "July",
                "August", "September", "October", "November", "December"
            ];
            return monthNames[currentDate.getMonth()];
        },
        currentYear() {
            const currentDate = new Date();
            return currentDate.getFullYear();
        },
        daysWithColspan() {
            return this.rooms.map((room) => {
                let daysWithColspan = [];
                const bookingsForRoom = this.bookings.filter(booking => booking.room_name === room.name);
                let dayIndex = 1;
                while (dayIndex <= this.days.length) {
                    const bookingsForDay = bookingsForRoom.filter(booking => {
                        const checkinDay = new Date(parseDate(booking.checkinDate).toLocaleString()).getDate();
                        const checkoutDay = new Date(parseDate(booking.checkoutDate).toLocaleString()).getDate();
                        return dayIndex >= checkinDay && dayIndex <= checkoutDay;
                    });
                    if (bookingsForDay.length > 0) {
                        const daysSpan = bookingsForDay.reduce((span, booking) => {
                            const checkinDay = new Date(parseDate(booking.checkinDate).toLocaleString()).getDate();
                            const checkoutDay = new Date(parseDate(booking.checkoutDate).toLocaleString()).getDate();
                            return Math.max(span, checkoutDay - checkinDay + 1);
                        }, 0);
                        // Store the bookings in the cell for the day
                        daysWithColspan.push({
                            bookings: bookingsForDay.map(booking => ({ class: "bg-success", colspan: 1 })),
                            colspan: daysSpan
                        });
                        dayIndex += daysSpan;
                    } else {
                        // Add non-booked days
                        daysWithColspan.push({ bookings: [], colspan: 1 });
                        dayIndex++;
                    }
                }
                return daysWithColspan;
            });
        },
    },
    mounted() {
        // Dynamically generate the days of the current month
        const currentDate = new Date();
        const daysInMonth = new Date(
            currentDate.getFullYear(),
            currentDate.getMonth() + 1,
            0
        ).getDate();
        this.days = Array.from({ length: daysInMonth }, (_, i) => i + 1);
    },
};
</script>
<style scoped>
/* Add any additional CSS styles here */
table {
    table-layout: fixed;
    word-wrap: break-word;
}
</style>

rooms has types do display category before each room and it is collapsible and expandable rows

this.rooms = [{name:"", type:""}]