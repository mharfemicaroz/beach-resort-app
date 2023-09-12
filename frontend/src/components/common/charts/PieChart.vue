<template>
  <Doughnut :data="data" :options="options" />
</template>

<script lang="ts">
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Doughnut } from "vue-chartjs";

ChartJS.register(ArcElement, Tooltip, Legend);

export default {
  props: {
    chartData: {
      type: Object,
      required: true,
    },
  },
  components: {
    Doughnut,
  },
  data() {
    return {
      data: {
        labels: [],
        datasets: [
          {
            data: [],
            backgroundColor: [
              "#FF6384",
              "#36A2EB",
              "#FFCE56",
              "#42b983",
              "#3f51b5",
              "#e91e63",
              "#00bcd4",
              "#8bc34a",
              "#ff9800",
              "#9c27b0",
              "#4caf50",
              "#2196f3",
              "#ffc107",
            ].sort(() => Math.random() - 0.5),
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          datalabels: {
            anchor: "middle",
            align: "middle",
            color: "black",
            formatter: Math.round,
            font: {
              weight: "bold",
              size: 16,
            },
          },
        },
      },
    };
  },
  mounted() {
    this.data = this.chartData;
  },
};
</script>
