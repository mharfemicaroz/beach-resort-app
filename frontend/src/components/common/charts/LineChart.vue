<template>
    <Line :data="data" :options="options" />
</template>
  
<script lang="ts">
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
)

export default {
    props: {
        chartData: {
            type: Object,
            required: true
        },
    },
    components: {
        Line
    },
    data() {
        return {
            data: {
                labels: [],
                datasets: [
                    {
                        data: [],
                        borderColor: '#FF6384', 
                    },
                    {
                        data: [],
                        borderColor: '#36A2EB',   
                    }, 
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    x: {
                        ticks: {
                            // Include a dollar sign in the ticks
                            callback: function () {
                                return '';
                            }
                        }
                    }
                }
            }
        }
    },
    mounted() {
        this.data = this.chartData;
    }
}
</script>
  