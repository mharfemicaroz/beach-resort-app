<template>
    <div class="row justify-content-center">
        <div class="col-md-2 m-2">
            <div class="card x bg-primary text-white">
                <div class="card-body row">
                    <div class="col-md-8">
                        <h5 class="card-title">Bookings</h5>
                        <p class="card-text">{{ numReservations }}</p>
                    </div>
                    <div class="col-md-4 d-flex justify-content-center align-items-center">
                        <i class="fas fa-book-open fa-2x"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-2 m-2">
            <div class="card x bg-secondary text-white">
                <div class="card-body row">
                    <div class="col-md-8">
                        <h5 class="card-title">Lodgings</h5>
                        <p class="card-text">{{ availableRooms }} available</p>
                    </div>
                    <div class="col-md-4 d-flex justify-content-center align-items-center">
                        <i class="fas fa-door-open fa-2x"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-2 m-2">
            <div class="card x bg-success text-white">
                <div class="card-body row">
                    <div class="col-md-8">
                        <h5 class="card-title">Guests</h5>
                        <p class="card-text">{{ numGuests }}</p>
                    </div>
                    <div class="col-md-4 d-flex justify-content-center align-items-center">
                        <i class="fas fa-users fa-2x"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-2 m-2">
            <div class="card x bg-danger text-white">
                <div class="card-body row">
                    <div class="col-md-8">
                        <h5 class="card-title">Gross</h5>
                        <p class="card-text">{{ grossIncome }}</p>
                    </div>
                    <div class="col-md-4 d-flex justify-content-center align-items-center">
                        <i class="fas fa-money-bill-alt fa-2x"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-2 m-2">
            <div class="card x bg-warning text-white">
                <div class="card-body row">
                    <div class="col-md-8">
                        <h5 class="card-title">Collectibles</h5>
                        <p class="card-text">{{ collectibles }}</p>
                    </div>
                    <div class="col-md-4 d-flex justify-content-center align-items-center">
                        <i class="fas fa-times-circle fa-2x"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row row justify-content-center">
        <div class="row">
            <div class="col-md-4">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Reservation Summary</strong>
                    </div>
                    <div class="card-body chart">
                        <pie-chart v-if="loaded[0]" :chartData="pie1Data" />
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Current Occupancy</strong>
                    </div>
                    <div class="card-body chart">
                        <bar-chart v-if="loaded[1]" :chartData="bar1Data" />
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Reservation Trend</strong>
                    </div>
                    <div class="card-body chart">
                        <line-chart v-if="loaded[2]" :chartData="line1Data" />
                    </div>
                </div>
            </div>
        </div>

    </div>
    <!-- <div class="row row justify-content-center">
        <div class="row">
            <div class="col-md-4">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Occupancy Rate</strong>
                    </div>
                    <div class="card-body chart">

                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Average Daily Rate (ADR)</strong>
                    </div>
                    <div class="card-body chart">

                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Revenue Per Available Room (RevPAR)</strong>
                    </div>
                    <div class="card-body chart">

                    </div>
                </div>
            </div>
        </div>

    </div> -->
</template>
<script>
import arima from 'arima/async';
import PieChart from "./charts/PieChart.vue";
import BarChart from "./charts/BarChart.vue";
import LineChart from "./charts/LineChart.vue";
import axios from "axios";
export default {
    components: {
        PieChart,
        BarChart,
        LineChart
    },
    data() {
        return {
            predictions: [],
            numReservations: 0,
            numGuests: 0,
            availableRooms: 0,
            grossIncome: 0,
            collectibles:0,
            loaded: {},
            pie1Data: {
                labels: ['cancelled', 'reserved', 'checkedin', 'checkedout'],
                datasets: [
                    {
                        data: [],
                    }
                ]
            },
            bar1Data: {
                labels: ['Beach Room', 'Pool Room', 'Beach Cottage', 'Pool Cottage', 'Gazebo Cottage'],
                datasets: [
                    {
                        data: [],
                    }
                ]
            },
            line1Data: {
                labels: [],
                datasets: [
                    {
                        data: [],
                    }
                ]
            },
        }
    },
    methods: {
        parseDate(dateString) {
            const [day, month, year] = dateString.split('/');
            const options = {
                month: '2-digit',
                day: '2-digit',
                year: 'numeric'
            };
            return new Intl.DateTimeFormat('en-US', options).format(new Date(`${year}-${month}-${day}`));
        },
        parseDate2(dateString) {
            const [day, month, year] = dateString.split('/');
            return new Date(`${year}-${month}-${day}`);
        },
        parseDate3(){
            const date = new Date(dateString);
            const options = {
                month: 'short',
                day: 'numeric',
                year: 'numeric',
                hour: 'numeric',
                minute: 'numeric',
                second: 'numeric',
                timeZoneName: 'short',
                timeZone: 'Asia/Shanghai'
            };
            return date.toLocaleString('en-US', options);            
        },
        pie1Datasets(data) {
            const numCancelled = data.filter(item => item.status === 'cancelled').length;
            const numReserved = data.filter(item => item.status === 'reserved').length;
            const numIn = data.filter(item => item.status === 'checkedin').length;
            const numOut = data.filter(item => item.status === 'checkedout').length;
            this.pie1Data.datasets[0].data = [numCancelled, numReserved, numIn, numOut]
        },
        bar1Datasets(data) {
            const br = data.filter(item => item.room_type === 'BEACH ROOM').length;
            const pl = data.filter(item => item.room_type === 'POOL ROOM').length;
            const bc = data.filter(item => item.room_type === 'BEACH COTTAGE').length;
            const pc = data.filter(item => item.room_type === 'POOL COTTAGE').length;
            const gc = data.filter(item => item.room_type === 'GAZEBO COTTAGE').length;
            this.bar1Data.datasets[0].data = [br, pl, bc, pc, gc]
        },
        line1Datasets(data) {
            const bookingsByDate = data.reduce((acc, curr) => {
                const date = this.parseDate(curr.checkinDate);
                acc[date] = (acc[date] || 0) + 1;
                return acc;
            }, {});

            const dates = Object.keys(bookingsByDate).sort();
            const frequency = dates.map(date => bookingsByDate[date]);
            dates.unshift('');
            frequency.unshift(0);
            this.line1Data.labels = dates;
            this.line1Data.datasets[0].data = frequency;
        },
        forecast(data) {
            return arima.then(ARIMA => {
                const arima = new ARIMA({ p: 2, d: 1, q: 2, P: 0, D: 0, Q: 0, S: 0, verbose: false }).train(data)
                const [pred, errors] = arima.predict(data.length)
                return pred
            })
        },
    },
    async mounted() {
        console.log(new Date())
        this.loaded[0] = false;
        this.loaded[1] = false;
        this.loaded[2] = false;
        try {
            const bookingData = await axios.get(this.API_URL + "bookings/");
            const transactionData = await axios.get(this.API_URL + "transaction/");

            const transactionItemsData = await axios.get(this.API_URL + "transaction/item/");
            const roomsData = await axios.get(this.API_URL + "rooms/");

            this.numReservations = bookingData.data.filter(item=>item.checkinDate === new Date().toLocaleDateString('en-GB')).length;
            this.numGuests = transactionItemsData.data.filter(item => item.itemType === 'ENTRANCE' && new Date(item.dateCreated).setHours(0, 0, 0, 0).toLocaleString('en-US') === new Date().setHours(0, 0, 0, 0).toLocaleString('en-US')).length
            this.availableRooms = roomsData.data.filter(room => {
                // Check if there are any bookings for this room that overlap with the specified date range
                const overlappingBookings = bookingData.data.filter(booking => {
                    return booking.room_name === room.name &&
                        booking.status === 'checkedin' && booking.checkinDate === new Date().toLocaleDateString('en-GB');
                });

                // Return true if there are no overlapping bookings
                return overlappingBookings.length === 0;
            }).length;
            this.grossIncome = transactionData.data.filter(item=>new Date(item.transaction_date).setHours(0, 0, 0, 0).toLocaleString('en-US') === new Date().setHours(0, 0, 0, 0).toLocaleString('en-US')).reduce((accumulator, currentValue) => {
                return accumulator + parseFloat(currentValue.cashAmountPay);
            }, 0);
            this.collectibles = transactionData.data.filter(item=>new Date(item.transaction_date).setHours(0, 0, 0, 0).toLocaleString('en-US') === new Date().setHours(0, 0, 0, 0).toLocaleString('en-US')).reduce((accumulator, currentValue) => {
                return accumulator + parseFloat(currentValue.balance);
            }, 0);


            this.pie1Datasets(bookingData.data.filter(item=>item.checkinDate === new Date().toLocaleDateString('en-GB')));
            this.bar1Datasets(bookingData.data.filter(item=>item.checkinDate === new Date().toLocaleDateString('en-GB')));
            this.line1Datasets(bookingData.data);

            this.loaded[0] = true;
            this.loaded[1] = true;
            this.loaded[2] = true;
        } catch (error) {

        }
    }

} 
</script>
<style>
.card.x,
.card-header.x {
    border: none;
    background-color: transparent;
}

.card-body.chart {
    height: 300px;
}
</style>