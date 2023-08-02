<template>
    <div class="row justify-content-center">
        <div class="col-md-12 m-2">
            <div class="card-body bg-success text-white h3"
                style="display: flex; justify-content: center; align-items: center;">
                Daily Reports
            </div>
        </div>
    </div>
    <div class="row justify-content-center">
        <div class="col-md-12 m-2">
            <label for="customRange3" class="form-label">Showing {{ (10 - backtrack === 0) ? ' today...' : `${10 - backtrack}
                            day${(10 - backtrack === 1) ? '' : 's'} ago...` }} ({{ this.chosenDate }})</label>
            <input type="range" class="form-range" @change="scrollRecord" min="0" max="10" step="1" v-model="backtrack"
                id="customRange3">
        </div>
    </div>
    <div class="row justify-content-center">

        <div class="col-md-2 m-2">
            <div class="card x bg-success text-white">
                <div class="card-body row">
                    <div class="col-md-8">
                        <h5 class="card-title mb-0">Orders</h5>
                        <p class="mt-0" style="font-size: xx-small;">in progress / closed order</p>
                        <p class="card-text">{{ orderProgress }} / {{ orderclosed }} </p>
                    </div>
                    <div class="col-md-4 d-flex justify-content-center align-items-center">
                        <i class="fa fa-list fa-2x"></i>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-2 m-2">
            <div class="card x bg-danger text-white">
                <div class="card-body row">
                    <div class="col-md-8">
                        <h5 class="card-title mb-0">Gross</h5>
                        <p class="mt-0" style="font-size: xx-small;">w/ tax & discount</p>
                        <p class="card-text">{{ grossIncome.toFixed(2) }}</p>
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
                        <h5 class="card-title mb-0">Collectibles</h5>
                        <p class="mt-0" style="font-size: xx-small;">No tax, no discount.</p>
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
                        <strong>Order Type Summary</strong>
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
                        <strong>Order Status Summary</strong>
                    </div>
                    <div class="card-body chart" style="display: flex; justify-content: center; align-items: center;">
                        <pie-chart :key="componentKey" v-if="loaded[1]" :chartData="pie2Data" />
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
                        <pie-chart :key="componentKey" v-if="loaded[3]" :chartData="pie3Data" />
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
            <div class="col-md-12">
                <div class="card x">
                    <div class="card-header text-primary text-center">
                        <strong>Collection Summary Report</strong>
                    </div>
                    <div class="card-body chart" style="display: flex; justify-content: center; align-items: center;">
                        <bar-chart :key="componentKey" v-if="loaded[4]" :chartData="bar1Data" />
                        <div v-else class="spinner-border" role="status">
                            <span class="sr-only">Loading...</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
    <div class="row justify-content-center">
        <div class="col-md-12 m-2">
            <div class="card-body bg-success text-white h3"
                style="display: flex; justify-content: center; align-items: center;">
                Overall Reports
            </div>
        </div>
    </div>
    <div class="row row justify-content-center">
        <div class="row">
            <div class="col-md-12">
                <div class="card" style="height: 500px;">
                    <div class="card-header text-primary text-center">
                        <strong>Sales Trend</strong>
                    </div>
                    <div class="card-body chart" style="display: flex; justify-content: center; align-items: center;">
                        <line-chart :key="componentKey" v-if="loaded[5]" :chartData="line1Data" />
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
            chosenDate: null,
            backtrack: 10,
            orderProgress: 0,
            orderclosed: 0,
            grossIncome: 0,
            collectibles: 0,
            loaded: {},
            pie1Data: {
                labels: ['paid', 'credit'],
                datasets: [
                    {
                        data: [],
                    }
                ]
            },
            pie2Data: {
                labels: ['progress', 'closed', 'void'],
                datasets: [
                    {
                        data: [],
                    }
                ]
            },
            pie3Data: {
                labels: ['cash', 'noncash'],
                datasets: [
                    {
                        data: [],
                    }
                ]
            },
            bar1Data: {
                labels: [],
                datasets: [
                    {
                        data: [],
                    },
                    {
                        data: [],
                    }
                ]
            },
            line1Data: {
                labels: [],
                datasets: [
                    {
                        label:"Dataset1",
                        data: [],
                    },
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
            const takeout = data.filter(item => item.order_type === 'take-out').length;
            const onhold = data.filter(item => item.order_type === 'on-hold').length;
            this.pie1Data.datasets[0].data = [takeout, onhold]
        },
        pie2Datasets(data) {
            const progress = data.filter(item => item.status === 'progress').length;
            const closed = data.filter(item => item.status === 'closed').length;
            const voided = data.filter(item => item.status === 'void').length;
            this.pie2Data.datasets[0].data = [progress, closed, voided]
        },
        pie3Datasets(data) {
            const cash = data.filter(item => item.payMethod === 'cash').reduce((accumulator, currentValue) => {
                return accumulator + parseFloat(currentValue.totalPay);
            }, 0);
            const noncash = data.filter(item => item.payMethod === 'noncash').reduce((accumulator, currentValue) => {
                return accumulator + parseFloat(currentValue.totalPay);
            }, 0);
            this.pie3Data.datasets[0].data = [cash, noncash]
        },
        bar1Datasets(data){
            const processedByList = data.map(record => record.processedBy);
            const uniqueProcessedByList = [...new Set(processedByList)].filter(name => name !== '');
            let collection = [];
            let collection2 = [];
            for(const name of uniqueProcessedByList){
                const total = data.filter(item => item.processedBy === name).reduce((accumulator, currentValue) => {
                    return accumulator + parseFloat(currentValue.totalPay);
                }, 0);
                collection.push(total);
                collection2.push(-total);
            }

            this.bar1Data.labels = uniqueProcessedByList;
            this.bar1Data.datasets[0].data = collection;
        },
        async line1Datasets(data) {
            const summary = data.reduce((acc, curr) => {
                const index = acc.dates.indexOf(this.parseDate3(curr.date_created));

                if (index === -1) {
                    acc.dates.push(this.parseDate3(curr.date_created));
                    acc.totals.push(parseFloat(curr.totalPay));
                } else {
                    acc.totals[index] += parseFloat(curr.totalPay);
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

            this.line1Data.labels = result.dates;
            this.line1Data.datasets[0].data = result.totalCashAmountPay;

        },
        scrollRecord() {
            this.loaded.fill(false, 0, 3);
            this.loadData();
        },
        async loadData() {
            try {
                this.loaded = Array(6).fill(false);

                const daycount = 10 - this.backtrack;
                const today = new Date();
                const curday = new Date(today);
                curday.setDate(today.getDate() - daycount);
                this.chosenDate = curday.toDateString();

                const restoordersData = await axios.get(this.API_URL + "restoorders/");
                this.orderProgress = restoordersData.data.filter(o => o.status === 'progress' && new Date(o.date_created).toLocaleDateString('en-GB') === curday.toLocaleDateString('en-GB')).length;
                this.orderclosed = restoordersData.data.filter(o => o.status === 'closed' && new Date(o.date_created).toLocaleDateString('en-GB') === curday.toLocaleDateString('en-GB')).length;

                const restotransData = await axios.get(this.API_URL + "restotransaction/");

                this.grossIncome = restotransData.data
                    .filter((item) => {
                        const transactionDate = new Date(item.date_created);
                        return (
                            transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
                            transactionDate < new Date(new Date(new Date(curday.getTime() + 86400000)).setHours(0, 0, 0, 0))
                        );
                    })
                    .reduce((accumulator, currentValue) => {
                        return accumulator + parseFloat(currentValue.totalPay);
                    }, 0);

                const summaryOrder = restoordersData.data
                    .filter((item) => {
                        const transactionDate = new Date(item.date_created);
                        return (
                            transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
                            transactionDate < new Date(new Date(new Date(curday.getTime() + 86400000)).setHours(0, 0, 0, 0))
                        );
                    })

                let grandTotal = 0;
                for (const item of summaryOrder){
                    let sumTotal = 0;
                    const arr = JSON.parse(item.items);
                    for (const o of arr){
                        sumTotal += parseFloat(o.totalPrice);
                    }
                    if(item.status !== "closed"){
                        grandTotal += sumTotal;
                    }
                    
                }
                
                this.collectibles = grandTotal;

                this.pie1Datasets(restoordersData.data.filter(item => new Date(item.date_created).toLocaleDateString('en-GB') === curday.toLocaleDateString('en-GB')));
                this.pie2Datasets(restoordersData.data.filter(item => new Date(item.date_created).toLocaleDateString('en-GB') === curday.toLocaleDateString('en-GB')));
                this.bar1Datasets(restotransData.data.filter(item => new Date(item.date_created).toLocaleDateString('en-GB') === curday.toLocaleDateString('en-GB')));
                this.line1Datasets(restotransData.data);
                this.pie3Datasets(restotransData.data.filter(item => new Date(item.date_created).toLocaleDateString('en-GB') === curday.toLocaleDateString('en-GB')))
                this.loaded = Array(6).fill(true);
            } catch (error) {
                alert(error)
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
}</style>