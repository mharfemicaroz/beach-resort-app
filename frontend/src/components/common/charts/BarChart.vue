<template>
    <Bar :data="data" :options="options" />
</template>
  
<script lang="ts" scope>
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale
} from 'chart.js'
import ChartDataLabels from 'chartjs-plugin-datalabels';
import { Bar } from 'vue-chartjs'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend, ChartDataLabels)

export default {
    props: {
        chartData: {
            type: Object,
            required: true
        },
    },
    components: {
        Bar
    },
    data() {
        return {
            data: {
                labels: [],
                datasets: [
                    {
                        data: [],
                        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#42b983', '#3f51b5', '#e91e63', '#00bcd4', '#8bc34a', '#ff9800', '#9c27b0', '#4caf50', '#2196f3', '#ffc107'].sort(() => Math.random() - 0.5),
                    }
                ]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    datalabels: {
                        anchor: 'end',
                        align: 'top',
                        color: 'red',
                        formatter: Math.round,
                        font: {
                            weight: 'bold',
                            size: 16,
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
  