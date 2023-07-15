<template>
    <div class="row justify-content-center">
        <div class="col-md-12 m-2">
            <label for="customRange3" class="form-label">Showing {{ (10 - backtrack === 0)? ' today...':`${10 - backtrack} day${(10 - backtrack === 1)?'':'s'} ago...` }}</label>
                <input type="range" class="form-range" @change="scrollRecord" min="0" max="10" step="1" v-model="backtrack" id="customRange3">
        </div>
    </div>
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
                        <p class="card-text">{{ numGuests }} / {{ counter }}</p>
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
                    <div class="card-body chart" style="display: flex; justify-content: center; align-items: center;">
                        <pie-chart :key="componentKey" v-if="loaded[0]" :chartData="pie1Data" />
                        <div v-else class="spinner-border" role="status">
                            <span class="sr-only">Loading...</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Current Occupancy</strong>
                    </div>
                    <div class="card-body chart" style="display: flex; justify-content: center; align-items: center;">
                        <bar-chart :key="componentKey" v-if="loaded[1]" :chartData="bar1Data" />
                        <div v-else class="spinner-border" role="status">
                            <span class="sr-only">Loading...</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Transaction Type</strong>
                    </div>
                    <div class="card-body chart" style="display: flex; justify-content: center; align-items: center;">
                        <pie-chart :key="componentKey" v-if="loaded[3]" :chartData="pie2Data" />
                        <div v-else class="spinner-border" role="status">
                            <span class="sr-only">Loading...</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
    <div class="row row justify-content-center">
        <div class="row">
            <div class="col-md-6">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Collection Summary Report</strong>
                    </div>
                    <div class="card-body chart" style="display: flex; justify-content: center; align-items: center;">
                        <bar-chart :key="componentKey" v-if="loaded[6]" :chartData="bar3Data" />
                        <div v-else class="spinner-border" role="status">
                            <span class="sr-only">Loading...</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Guest Counter Report</strong>
                    </div>
                    <div class="card-body chart">
                        
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
                        <strong>Reservation Trend</strong>
                    </div>
                    <div class="card-body chart" style="display: flex; justify-content: center; align-items: center;">
                        <line-chart :key="componentKey" v-if="loaded[2]" :chartData="line1Data" />
                        <div v-else class="spinner-border" role="status">
                            <span class="sr-only">Loading...</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Total Revenue</strong>
                    </div>
                    <div class="card-body chart" style="display: flex; justify-content: center; align-items: center;">
                        <bar-chart :key="componentKey" v-if="loaded[5]" :chartData="bar2Data" />
                        <div v-else class="spinner-border" role="status">
                            <span class="sr-only">Loading...</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Sales Trend</strong>
                    </div>
                    <div class="card-body chart" style="display: flex; justify-content: center; align-items: center;">
                        <line-chart :key="componentKey" v-if="loaded[4]" :chartData="line2Data" />
                        <div v-else class="spinner-border" role="status">
                            <span class="sr-only">Loading...</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
    <div class="row row justify-content-center">
        <div class="col-md-4">
                <div class="card x">
                        ----------------
                </div>
            </div>
    </div>
</template>
<script>
import arima from 'arima/async';
import PieChart from "./charts/PieChart.vue";
import BarChart from "./charts/BarChart.vue";
import LineChart from "./charts/LineChart.vue";
import axios from "axios";

function formatdate(currentDate) {
    const year = currentDate.getFullYear();
    const month = String(currentDate.getMonth() + 1).padStart(2, '0');
    const day = String(currentDate.getDate()).padStart(2, '0');
    const formattedDate = `${year}-${month}-${day}`;
    return formattedDate;
}

function padTo2Digits(num) {
    return num.toString().padStart(2, '0');
}

function parseDate(date = new Date()) {
    return [
        date.getFullYear(),
        padTo2Digits(date.getMonth() + 1),
        padTo2Digits(date.getDate()),
    ].join('-');
}

function formatDate2(dateString) {
    const index = dateString.indexOf('T');
    const result = dateString.substring(0, index);
    const [year, month, day] = result.split('-');
    return `${year}-${month}-${day}`;
}

export default {
    components: {
        PieChart,
        BarChart,
        LineChart
    },
    props: {
        active: {
            type: Boolean,
            required: true,
        }
    },
    data() {
        return {
            backtrack: 10,
            counter: 0,
            forecastedData: null,
            componentKey: 0,
            prevBookings: [],
            prevTransactions: [],
            prevransItems: [],
            predictions: [],
            numReservations: 0,
            numGuests: 0,
            availableRooms: 0,
            grossIncome: 0,
            collectibles: 0,
            loaded: {},
            pie1Data: {
                labels: ['cancelled', 'reserved', 'checkedin', 'checkedout'],
                datasets: [
                    {
                        data: [],
                    }
                ]
            },
            pie2Data: {
                labels: ['cash', 'non-cash'],
                datasets: [
                    {
                        data: [],
                    }
                ]
            },
            bar1Data: {
                labels: ['Beach Rooms', 'Pool Rooms', 'Beach Cottages (day)', 'Beach Cottages (night)', 'Pool Cottages', 'Gazebo Cottages'],
                datasets: [
                    {
                        data: [],
                    }
                ]
            },
            bar2Data: {
                labels: ['Beach Room', 'Pool Room', 'Beach Cottage', 'Pool Cottage', 'Gazebo Cottage'],
                datasets: [
                    {
                        data: [],
                    }
                ]
            },
            bar3Data: {
                labels: [],
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
            line2Data: {
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
        parseDate3(dateString) {
            const dateObj = new Date(dateString);
            const month = dateObj.getMonth() + 1;
            const day = dateObj.getDate();
            const year = dateObj.getFullYear();
            const newDateString = `${month}/${day}/${year}`;
            return newDateString;
        },
        pie1Datasets(data) {
            const numCancelled = data.filter(item => item.status === 'cancelled').length;
            const numReserved = data.filter(item => item.status === 'reserved').length;
            const numIn = data.filter(item => item.status === 'checkedin').length;
            const numOut = data.filter(item => item.status === 'checkedout').length;
            this.pie1Data.datasets[0].data = [numCancelled, numReserved, numIn, numOut]
        },
        pie2Datasets(data) {
            const totcash = data.filter(item => item.paymentMethod === 'cash').reduce((accumulator, currentValue) => {
                return accumulator + parseFloat(currentValue.actualIncomeOfThisDay);
            }, 0);
            const totnoncash = data.filter(item => item.paymentMethod === 'non-cash').reduce((accumulator, currentValue) => {
                return accumulator + parseFloat(currentValue.actualIncomeOfThisDay);
            }, 0);
            this.pie2Data.datasets[0].data = [totcash, totnoncash]
        },
        bar1Datasets(data) {
            const br = data.filter(item => item.room_type === 'BEACH ROOM').length;
            const pl = data.filter(item => item.room_type === 'POOL ROOM').length;
            const bc = data.filter(item => item.room_type === 'BEACH COTTAGE').length;
            const bcn = data.filter(item => item.room_type === 'N-BEACH COTTAGE').length;
            const pc = data.filter(item => item.room_type === 'POOL COTTAGE').length;
            const gc = data.filter(item => item.room_type === 'GAZEBO COTTAGE').length;
            this.bar1Data.datasets[0].data = [br, pl, bc, bcn, pc, gc]
        },
        bar2Datasets(data) {
            const all = data.reduce((accumulator, currentValue) => {
                return accumulator + parseFloat(currentValue.totalCost);
            }, 0);
            const br = data.filter(item => item.itemType === 'BEACH ROOM').reduce((accumulator, currentValue) => {
                return accumulator + parseFloat(currentValue.totalCost);
            }, 0);
            const pl = data.filter(item => item.itemType === 'POOL ROOM').reduce((accumulator, currentValue) => {
                return accumulator + parseFloat(currentValue.totalCost);
            }, 0);
            const bc = data.filter(item => item.itemType === 'BEACH COTTAGE').reduce((accumulator, currentValue) => {
                return accumulator + parseFloat(currentValue.totalCost);
            }, 0);
            const pc = data.filter(item => item.itemType === 'POOL COTTAGE').reduce((accumulator, currentValue) => {
                return accumulator + parseFloat(currentValue.totalCost);
            }, 0);
            const gc = data.filter(item => item.itemType === 'GAZEBO COTTAGE').reduce((accumulator, currentValue) => {
                return accumulator + parseFloat(currentValue.totalCost);
            }, 0);
            this.bar2Data.datasets[0].data = [br, pl, bc, pc, gc]
        },
        bar3Datasets(data){
            const processedByList = data.map(record => record.processedBy);
            const uniqueProcessedByList = [...new Set(processedByList)].filter(name => name !== '');
            let collection = [];
            for(const name of uniqueProcessedByList){
                const total = data.filter(item => item.processedBy === name).reduce((accumulator, currentValue) => {
                    return accumulator + parseFloat(currentValue.cashAmountPay);
                }, 0);
                collection.push(total);
            }

            this.bar3Data.labels = uniqueProcessedByList;
            this.bar3Data.datasets[0].data = collection;
        },
        line1Datasets(data) {
            const arr = data.reduce((acc, curr) => {
                const date = this.parseDate(curr.checkinDate);
                acc[date] = (acc[date] || 0) + 1;
                return acc;
            }, {});

            const dates = Object.keys(arr).sort();
            const frequency = dates.map(date => arr[date]);
            dates.unshift('');
            frequency.unshift(0);
            this.line1Data.labels = dates;
            this.line1Data.datasets[0].data = frequency;
        },
        async line2Datasets(data) {
            const summary = data.reduce((acc, curr) => {
                const index = acc.dates.indexOf(this.parseDate3(curr.transaction_date));

                if (index === -1) {
                    acc.dates.push(this.parseDate3(curr.transaction_date));
                    acc.totals.push(parseFloat(curr.cashAmountPay));
                } else {
                    acc.totals[index] += parseFloat(curr.cashAmountPay);
                }

                return acc;
            }, { dates: [], totals: [] });

            const result = {
                dates: summary.dates,
                totalCashAmountPay: summary.totals
            };

            const o = result.dates.map((date, index) => ({ date, totalCashAmountPay: result.totalCashAmountPay[index] }));
            o.sort((a, b) => new Date(a.date) - new Date(b.date));
            result.totalCashAmountPay = o.map(item => item.totalCashAmountPay);
            result.dates.sort((a, b) => new Date(a) - new Date(b));
            result.dates.unshift('');
            result.totalCashAmountPay.unshift(0);

            this.line2Data.labels = result.dates;
            this.line2Data.datasets[0].data = result.totalCashAmountPay;



        },
        forecast(data) {
            let vm = this;
            arima.then(ARIMA => {
                const arima = new ARIMA({ p: 2, d: 1, q: 2, P: 0, D: 0, Q: 0, S: 0, verbose: false }).train(data)
                const [pred, errors] = arima.predict(data.length)
                vm.forecastedData = pred
            })
        },
        scrollRecord(){
            this.loaded = Array(6).fill(false);
            this.loadData();
        },
        async loadData() {
            try {
                const daycount = 10 - this.backtrack;
                const today = new Date();
                const curday = new Date(today);
                curday.setDate(today.getDate() - daycount);

                const guestcounterdata = await axios.get(this.API_URL + "guestcounter/");

                const foundItem = guestcounterdata.data.find((item) => formatDate2(item.date_created) === parseDate(new Date()));
                if (foundItem) {
                    this.counter = parseFloat(foundItem.counter);
                } else {
                    this.counter = 0;
                }

                const bookingData = await axios.get(this.API_URL + "bookings/");
                const transactionData = await axios.get(this.API_URL + "transaction/");
                const transactionItemsData = await axios.get(this.API_URL + "transaction/item/");
                const transactionRecordsData = await axios.get(this.API_URL + "transaction/record/");
                
                if (JSON.stringify(bookingData.data) !== JSON.stringify(this.prevBookings)) {
                    this.componentKey += 1;
                    this.prevBookings = bookingData.data;
                    this.prevTransactions = transactionData.data;
                    this.prevransItems = transactionItemsData.data;
                    this.loaded = Array(7).fill(false);
                }

                const roomsData = await axios.get(this.API_URL + "rooms/");

                this.numReservations = bookingData.data.filter(item => item.checkinDate === curday.toLocaleDateString('en-GB')).length;
                this.numGuests = transactionItemsData.data.filter(item => item.itemType === 'ENTRANCE' && new Date(item.dateCreated).setHours(0, 0, 0, 0).toLocaleString('en-US') === curday.setHours(0, 0, 0, 0).toLocaleString('en-US')).length
                this.availableRooms = roomsData.data.filter(room => {
                    // Check if there are any bookings for this room that overlap with the specified date range
                    const overlappingBookings = bookingData.data.filter(booking => {
                        return booking.room_name === room.name &&
                            booking.status === 'checkedin' && booking.checkinDate === curday.toLocaleDateString('en-GB');
                    });

                    // Return true if there are no overlapping bookings
                    return overlappingBookings.length === 0;
                }).length;

                this.pie1Datasets(bookingData.data.filter(item => item.checkinDate === curday.toLocaleDateString('en-GB')));
                this.bar1Datasets(bookingData.data.filter(item => item.checkinDate === curday.toLocaleDateString('en-GB')));
                this.bar2Datasets(transactionItemsData.data);
                this.line1Datasets(bookingData.data);
                this.line2Datasets(transactionData.data);
                
                const trans_itemizer_data =  await axios.get(this.API_URL + `transactions_itemizer/${daycount}/`);

                this.grossIncome = trans_itemizer_data.data
                    .filter((item) => {
                        const transactionDate = new Date(item.transaction_date);
                        return (
                            transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
                            transactionDate < new Date(new Date(new Date(curday.getTime() + 86400000)).setHours(0,0,0,0))
                        );
                    })
                    .reduce((accumulator, currentValue) => {
                        return accumulator + parseFloat(currentValue.actualIncomeOfThisDay);
                    }, 0);
                this.collectibles = transactionData.data
                    .filter((item) => {
                        const transactionDate = new Date(item.transaction_date);
                        return (
                            transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
                            transactionDate < new Date(new Date(new Date(curday.getTime() + 86400000)).setHours(0,0,0,0))
                        );
                    })
                    .reduce((accumulator, currentValue) => {
                        return accumulator + parseFloat(currentValue.balance);
                    }, 0);

                
                this.pie2Datasets(trans_itemizer_data.data.filter((item) => {
                    const transactionDate = new Date(item.transaction_date);
                        return (
                            transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
                            transactionDate < new Date(new Date(new Date(curday.getTime() + 86400000)).setHours(0,0,0,0))
                        );
                } ));

                this.bar3Datasets(transactionRecordsData.data.filter((item) => {
                    const transactionDate = new Date(item.transaction_date);
                    return (
                        transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
                        transactionDate < new Date(new Date(new Date(curday.getTime() + 86400000)).setHours(0, 0, 0, 0))
                    );
                }));

                this.loaded = Array(7).fill(true);
            } catch (error) {

            }
        }
    },
    async mounted() {

        // initialize loaded array
        this.loaded = Array(6).fill(false);

        // load data
        await this.loadData();

        // set interval to refresh data every 3 seconds if component is in focus
        // const intervalId = setInterval(async () => {
        if (this.active && !document.hidden && document.hasFocus()) {
            await this.loadData();
        }
        // }, 3000);

        // add event listener to clear interval when component is not in focus
        document.addEventListener('visibilitychange', () => {
            if (!this.active || document.hidden || !document.hasFocus()) {
                // clearInterval(intervalId);
            } else {
                // intervalId = setInterval(async () => {
                // await this.loadData();
                this.loadData();
                // }, 3000);
            }
        });

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