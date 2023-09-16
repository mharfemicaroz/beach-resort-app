<template>
  <div class="row">
    <div class="col-md-3">
      <ul class="nav bg radius nav-pills nav-fill mb-3 bg mt-3" role="tablist">
        <li class="nav-item">
          <a
            class="nav-link active show"
            data-bs-toggle="tab"
            @click=""
            role="tab"
            href="#reportstab"
          >
            <i class="fa fa-tags"></i>Reports</a
          >
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            data-bs-toggle="tab"
            role="tab"
            @click=""
            href="#workflowstab"
          >
            <i class="fa fa-tags"></i>Work Flows</a
          >
        </li>
      </ul>
    </div>
  </div>
  <div class="tab-content" id="myTabContent">
    <div class="tab-pane fade show active" id="reportstab" role="tabpanel">
      <div class="container-fluid">
        <div class="row justify-content-center">
          <div class="col-md-12 m-2">
            <div
              class="card-body bg-success text-white h3"
              style="
                display: flex;
                justify-content: center;
                align-items: center;
              "
            >
              Daily Reports
            </div>
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="col-md-12 m-2">
            <label for="customRange3" class="form-label"
              >Showing
              {{
                10 - backtrack === 0
                  ? " today..."
                  : `${10 - backtrack} day${
                      10 - backtrack === 1 ? "" : "s"
                    } ago...`
              }}
              ({{ this.chosenDate }})</label
            >
            <input
              type="range"
              :disabled="!loaded[0]"
              class="form-range"
              @change="scrollRecord"
              min="0"
              max="10"
              step="1"
              v-model="backtrack"
              id="customRange3"
            />
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="col-md-2 m-2">
            <div class="card x bg-primary text-white">
              <div class="card-body row">
                <div class="col-md-8">
                  <h5 class="card-title">Bookings</h5>
                  <p class="card-text">
                    {{ numReservations }} / {{ availableRooms }}
                  </p>
                </div>
                <div
                  class="col-md-4 d-flex justify-content-center align-items-center"
                >
                  <i class="fas fa-book-open fa-2x"></i>
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
                <div
                  class="col-md-4 d-flex justify-content-center align-items-center"
                >
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
                <div
                  class="col-md-4 d-flex justify-content-center align-items-center"
                >
                  <i class="fas fa-money-bill-alt fa-2x"></i>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-2 m-2">
            <div class="card x bg-secondary text-white">
              <div class="card-body row">
                <div class="col-md-8">
                  <h5 class="card-title">Pending</h5>
                  <p class="card-text">{{ pending }}</p>
                </div>
                <div
                  class="col-md-4 d-flex justify-content-center align-items-center"
                >
                  <i class="fas fa-hourglass-start fa-2x"></i>
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
                <div
                  class="col-md-4 d-flex justify-content-center align-items-center"
                >
                  <i class="fas fa-times-circle fa-2x"></i>
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
                  <strong>Reservation Summary</strong>
                </div>
                <div
                  class="card-body chart"
                  style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                  "
                >
                  <pie-chart
                    :key="componentKey"
                    v-if="loaded[0]"
                    :chartData="pie1Data"
                  />
                  <div v-else class="spinner-border" role="status">
                    <span class="sr-only">Loading...</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="card x">
                <div class="card-header text-primary text-center">
                  <strong>Current Occupancy</strong>
                </div>
                <div
                  class="card-body chart"
                  style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                  "
                >
                  <bar-chart
                    :key="componentKey"
                    v-if="loaded[1]"
                    :chartData="bar1Data"
                  />
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
                <div
                  class="card-body chart"
                  style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                  "
                >
                  <bar-chart
                    :key="componentKey"
                    v-if="loaded[3]"
                    :chartData="bar3Data"
                  />
                  <div v-else class="spinner-border" role="status">
                    <span class="sr-only">Loading...</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="card x">
                <div class="card-header text-primary text-center">
                  <strong>Transaction Type</strong>
                </div>
                <div
                  class="card-body chart"
                  style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                  "
                >
                  <pie-chart
                    :key="componentKey"
                    v-if="loaded[2]"
                    :chartData="pie2Data"
                  />
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
                  <strong>Approved/Disapproved Agent's Payment Report</strong>
                </div>
                <div
                  class="card-body chart"
                  style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                  "
                >
                  <pie-chart
                    :key="componentKey"
                    v-if="loaded[3]"
                    :chartData="pie3Data"
                  />
                  <div v-else class="spinner-border" role="status">
                    <span class="sr-only">Loading...</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="card x">
                <div class="card-header text-primary text-center">
                  <strong>Agent Type Transaction Summary</strong>
                </div>
                <div
                  class="card-body chart"
                  style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                  "
                >
                  <bar-chart
                    :key="componentKey"
                    v-if="loaded[3]"
                    :chartData="bar4Data"
                  />
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
            <div
              class="card-body bg-success text-white h3"
              style="
                display: flex;
                justify-content: center;
                align-items: center;
              "
            >
              Overall Reports
            </div>
          </div>
        </div>
        <div class="row row justify-content-center">
          <div class="row">
            <div class="col-md-12">
              <div class="card x">
                <div class="card-header text-primary text-center">
                  <strong>Total Revenue</strong>
                </div>
                <div
                  class="card-body chart"
                  style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                  "
                >
                  <bar-chart
                    :key="componentKey"
                    v-if="loaded[7]"
                    :chartData="bar2Data"
                  />
                  <div v-else class="spinner-border" role="status">
                    <span class="sr-only">Loading...</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-12">
              <div class="card x">
                <div class="card-header text-primary text-center">
                  <strong
                    >Reservation Historical Data & 30-point period
                    Forecast</strong
                  >
                </div>
                <div
                  class="card-body chart"
                  style="
                    display: flex;
                    justify-content: center;
                    align-items: center;
                  "
                >
                  <line-chart
                    :key="componentKey"
                    v-if="
                      loaded[6] && (line1Data.datasets[0].data || []).length > 0
                    "
                    :chartData="line1Data"
                  />
                  <div v-else class="spinner-border" role="status">
                    <span class="sr-only">Loading...</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12">
                <div class="card x">
                  <div class="card-header text-primary text-center">
                    <strong
                      >Sales Historical Data & 30-point period Forecast</strong
                    >
                  </div>
                  <div
                    class="card-body chart"
                    style="
                      display: flex;
                      justify-content: center;
                      align-items: center;
                    "
                  >
                    <line-chart
                      :key="componentKey"
                      v-if="
                        loaded[8] &&
                        (line2Data.datasets[0].data || []).length > 0
                      "
                      :chartData="line2Data"
                    />
                    <div v-else class="spinner-border" role="status">
                      <span class="sr-only">Loading...</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12">
                <div class="card x">
                  <div class="card-header text-primary text-center">
                    <strong
                      >Guests Historical Data & 30-point period Forecast</strong
                    >
                  </div>
                  <div
                    class="card-body chart"
                    style="
                      display: flex;
                      justify-content: center;
                      align-items: center;
                    "
                  >
                    <line-chart
                      :key="componentKey"
                      v-if="
                        loaded[9] &&
                        (line3Data.datasets[0].data || []).length > 0
                      "
                      :chartData="line3Data"
                    />
                    <div v-else class="spinner-border" role="status">
                      <span class="sr-only">Loading...</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row row justify-content-center">
          <div class="col-md-4">
            <div class="card x">----------------</div>
          </div>
        </div>
      </div>
    </div>
    <div class="tab-pane fade" id="workflowstab" role="tabpanel">
      <div class="container-fluid">
        <div class="row row justify-content-center">
          <div class="col-md-2">
            <div>
              <div class="form-group">
                <label for="date-filter">Date Filter:</label>
                <select
                  class="form-control"
                  id="date-filter"
                  v-model="dateFilter"
                >
                  <option value="">Any</option>
                  <option value="range">Date Range</option>
                </select>
                <div v-if="dateFilter === 'range'">
                  <div class="form-group">
                    <input
                      type="date"
                      class="form-control"
                      v-model="fromDate"
                    />
                  </div>
                  <div class="form-group">
                    <input type="date" class="form-control" v-model="toDate" />
                  </div>
                </div>
              </div>
              <div class="form-group">
                <label for="payment-method-filter">Payment Method:</label>
                <select
                  class="form-control"
                  id="payment-method-filter"
                  v-model="paymentMethodFilter"
                >
                  <option value="">Any</option>
                  <option value="agentcredit">Agent w/ Credit</option>
                  <option value="agentnocredit">Agent w/ no Credit</option>
                </select>
              </div>
              <div class="form-group">
                <label for="agent-filter">Agent:</label>
                <select
                  class="form-control"
                  id="agent-filter"
                  v-model="agentFilter"
                >
                  <option value="">Any</option>
                  <option v-for="agent in agents" :value="agent">
                    {{ agent }}
                  </option>
                </select>
              </div>
              <div class="form-group">
                <label for="actor-filter">Processed by:</label>
                <select
                  class="form-control"
                  id="actor-filter"
                  v-model="actorFilter"
                >
                  <option value="">Any</option>
                  <option v-for="actor in actors" :value="actor">
                    {{ actor }}
                  </option>
                </select>
              </div>
              <div class="form-group">
                <label for="status-filter">Status:</label>
                <select
                  class="form-control"
                  id="status-filter"
                  v-model="statusFilter"
                >
                  <option value="">Any</option>
                  <option value="0">Pending</option>
                  <option value="1">Approved</option>
                </select>
              </div>
            </div>
          </div>
          <div class="col-md-10">
            <table-component
              :mainHeaders="transrecordOptions"
              :mainItems="filteredtransrecord"
              :editable="false"
              :toggleable="false"
              @custombtn-action="viewRecord"
              :selectable="true"
              :batchAction="true"
              @batch-action="batchAction"
            >
              <template #content="data">
                <span
                  class="badge badge-success rounded-pill d-inline text-white"
                  :class="
                    data.data.dt.agent_payStatus ? 'bg-success' : 'bg-warning'
                  "
                  >{{
                    data.data.dt.agent_payStatus ? "approved" : "pending"
                  }}</span
                >
              </template>
              <template #custombtn="data">
                <button
                  type="button"
                  class="btn btn-lg badge rounded-pill d-inline"
                  :class="
                    data.data.dt.agent_payStatus ? 'btn-danger' : 'btn-primary'
                  "
                  v-html="
                    data.data.dt.agent_payStatus
                      ? `<i class='fa fa-times'></i>`
                      : `<i class='fa fa-check'></i>`
                  "
                  @click="approveAction(data.data.dt.status, data.data.dt.id)"
                ></button>
              </template>
            </table-component>
          </div>
        </div>
        <div class="row row justify-content-center">
          <div class="col-md-12">
            <div class="card x" style="height: 50px">----------------</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import TableComponent from "@/components/common/GenericTable.vue";
import arima from "arima/async";
import PieChart from "./charts/PieChart.vue";
import BarChart from "./charts/BarChart.vue";
import LineChart from "./charts/LineChart.vue";
import axios from "axios";
import async from "arima/async";

function formatdate(currentDate) {
  const year = currentDate.getFullYear();
  const month = String(currentDate.getMonth() + 1).padStart(2, "0");
  const day = String(currentDate.getDate()).padStart(2, "0");
  const formattedDate = `${year}-${month}-${day}`;
  return formattedDate;
}

function padTo2Digits(num) {
  return num.toString().padStart(2, "0");
}

function parseDate(date = new Date()) {
  return [
    date.getFullYear(),
    padTo2Digits(date.getMonth() + 1),
    padTo2Digits(date.getDate()),
  ].join("-");
}

function formatDate2(dateString) {
  const index = dateString.indexOf("T");
  const result = dateString.substring(0, index);
  const [year, month, day] = result.split("-");
  return `${year}-${month}-${day}`;
}

function xparseDate(dateString) {
  const [day, month, year] = dateString.split("/");
  return new Date(`${year}-${month}-${day}`).setHours(0, 0, 0, 0);
}
function xparseDate2(dateString) {
  const index = dateString.indexOf("T");
  const result = dateString.substring(0, index);
  const [year, month, day] = result.split("-");
  return new Date(`${year}-${month}-${day}`).setHours(0, 0, 0, 0);
}

export default {
  components: {
    TableComponent,
    PieChart,
    BarChart,
    LineChart,
  },
  props: {
    active: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      transrecordOptions: [
        {
          label: "",
          field: "checkbox",
          sortable: false,
        },
        {
          label: "ID",
          field: "id",
          sortable: true,
        },
        {
          label: "Date",
          field: "transaction_date",
          sortable: true,
        },
        {
          label: "Method",
          field: "paymentMethod",
          sortable: true,
        },
        {
          label: "Reference",
          field: "nonCashReference",
          sortable: true,
        },
        {
          label: "Bill amount",
          field: "totalAmountToPay",
          sortable: true,
          reducible: true,
        },
        {
          label: "Cash Payment",
          field: "cashAmountPay",
          sortable: true,
          reducible: true,
        },
        {
          label: "Agent Payment",
          field: "agentPayment",
          sortable: true,
          reducible: true,
        },
        {
          label: "Discount",
          field: "discount",
          sortable: true,
        },
        {
          label: "Processed by",
          field: "processedBy",
          sortable: true,
        },
        {
          label: "Status",
          field: "status",
          sortable: true,
          slot: true,
        },
        {
          label: "Action",
          field: "action",
          sortable: false,
          slot: true,
        },
      ],
      dateFilter: "",
      paymentMethodFilter: "",
      agentFilter: "",
      actorFilter: "",
      statusFilter: "",
      fromDate: null,
      toDate: null,
      pending: 0,
      chosenDate: null,
      backtrack: 10,
      counter: 0,
      forecastedData: null,
      forecastedData2: null,
      componentKey: 0,
      prevBookings: [],
      prevTransactions: [],
      prevransItems: [],
      predictions: [],
      roomcategories: [],
      transrecords: [],
      actors: [],
      agents: ["agoda"],
      numReservations: 0,
      numGuests: 0,
      availableRooms: 0,
      grossIncome: 0,
      collectibles: 0,
      loaded: {},
      pie1Data: {
        labels: ["cancelled", "reserved", "checkedin", "checkedout"],
        datasets: [
          {
            data: [],
          },
        ],
      },
      pie2Data: {
        labels: ["cash", "non-cash", "agent"],
        datasets: [
          {
            data: [],
          },
        ],
      },
      pie3Data: {
        labels: ["approved", "pending"],
        datasets: [
          {
            data: [],
          },
        ],
      },
      bar1Data: {
        labels: [],
        datasets: [
          {
            data: [],
          },
        ],
      },
      bar2Data: {
        labels: [],
        datasets: [
          {
            data: [],
          },
        ],
      },
      bar3Data: {
        labels: [],
        datasets: [
          {
            data: [],
          },
        ],
      },
      bar4Data: {
        labels: [],
        datasets: [
          {
            data: [],
          },
        ],
      },
      line1Data: {
        labels: [],
        datasets: [
          {
            data: [],
            borderDash: [10, 5],
            borderColor: "#36A2EB",
          },
          {
            data: [],
            borderColor: "#36A2EB",
          },
        ],
      },
      line2Data: {
        labels: [],
        datasets: [
          {
            data: [],
            borderDash: [10, 5],
            borderColor: "#FF6384",
          },
          {
            data: [],
            borderColor: "#FF6384",
          },
        ],
      },
      line3Data: {
        labels: [],
        datasets: [
          {
            data: [],
            borderDash: [10, 5],
            borderColor: "#FFCE56",
          },
          {
            data: [],
            borderColor: "#FFCE56",
          },
        ],
      },
    };
  },
  computed: {
    filteredtransrecord() {
      let filtered = this.transrecords
        .filter(
          (o) =>
            o.paymentMethod.includes("agent") &&
            o.paymentMethod.includes("credit")
        )
        .map((o) => {
          const p = { ...o };
          const discount =
            parseFloat(o.discountValue) === 0
              ? "none"
              : p.discountMode + "-" + p.discountValue;
          const status = p.agent_isApproved == 0 ? "pending" : "approved";
          p.agent_payStatus = o.agent_isApproved;
          p.agent_dateConfirmed = o.agent_approvalDate;
          delete p.agent_isApproved;
          delete p.agent_approvalDate;
          return {
            status,
            discount,
            ...p,
          };
        });
      if (this.dateFilter === "range" && this.fromDate && this.toDate) {
        filtered = filtered.filter((transaction) => {
          return (
            xparseDate2(transaction.transaction_date) >=
              xparseDate(this.fromDate) &&
            xparseDate2(transaction.transaction_date) <= xparseDate(this.toDate)
          );
        });
      }
      if (this.paymentMethodFilter) {
        filtered = filtered.filter((transaction) => {
          return transaction.paymentMethod === this.paymentMethodFilter;
        });
      }
      if (this.statusFilter) {
        filtered = filtered.filter((transaction) => {
          return transaction.agent_payStatus == this.statusFilter;
        });
      }
      if (this.agentFilter) {
        filtered = filtered.filter((transaction) => {
          return transaction.nonCashReference
            .toLowerCase()
            .includes(this.agentFilter);
        });
      }
      if (this.actorFilter) {
        filtered = filtered.filter((transaction) => {
          return transaction.processedBy
            .toLowerCase()
            .includes(this.actorFilter.toLowerCase());
        });
      }
      return filtered;
    },
  },
  methods: {
    async batchAction(arr) {
      for (const id of arr) {
        await axios
          .get(`${this.API_URL}transaction/record/${id}/`)
          .then(async (response) => {
            const record = response.data;
            await axios
              .put(`${this.API_URL}transaction/record/${id}/`, {
                transaction: record.transaction,
                paymentMethod: record.paymentMethod,
                nonCashReference: record.nonCashReference,
                totalAmountToPay: record.totalAmountToPay,
                cashAmountPay: record.cashAmountPay,
                balance: record.balance,
                discountMode: record.discountMode,
                discountValue: record.discountValue,
                processedBy: record.processedBy,
                payStatus: record.payStatus,
                agentPayment: record.agentPayment,
                agent_approvalDate: new Date(),
                agent_isApproved: record.agent_isApproved == 0 ? 1 : 0,
              })
              .then((result) => {
                const index = this.transrecords.findIndex((o) => o.id === id);
                this.transrecords[index] = result.data;
              });
          });
      }
      this.loadData();
    },
    async approveAction(status, id) {
      await axios
        .get(`${this.API_URL}transaction/record/${id}/`)
        .then(async (response) => {
          const record = response.data;
          await axios
            .put(`${this.API_URL}transaction/record/${id}/`, {
              transaction: record.transaction,
              paymentMethod: record.paymentMethod,
              nonCashReference: record.nonCashReference,
              totalAmountToPay: record.totalAmountToPay,
              cashAmountPay: record.cashAmountPay,
              balance: record.balance,
              discountMode: record.discountMode,
              discountValue: record.discountValue,
              processedBy: record.processedBy,
              payStatus: record.payStatus,
              agentPayment: record.agentPayment,
              agent_approvalDate: new Date(),
              agent_isApproved: status === "pending" ? 1 : 0,
            })
            .then((result) => {
              const index = this.transrecords.findIndex((o) => o.id === id);
              this.transrecords[index] = result.data;
              this.loadData();
            });
        });
    },
    parseDate(dateString) {
      const [day, month, year] = dateString.split("/");
      const options = {
        month: "2-digit",
        day: "2-digit",
        year: "numeric",
      };
      return new Intl.DateTimeFormat("en-US", options).format(
        new Date(`${year}-${month}-${day}`)
      );
    },
    parseDate2(dateString) {
      const [day, month, year] = dateString.split("/");
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
      const numCancelled = data.filter(
        (item) => item.status === "cancelled"
      ).length;
      const numReserved = data.filter(
        (item) => item.status === "reserved"
      ).length;
      const numIn = data.filter((item) => item.status === "checkedin").length;
      const numOut = data.filter((item) => item.status === "checkedout").length;
      this.pie1Data.datasets[0].data = [
        numCancelled,
        numReserved,
        numIn,
        numOut,
      ];
    },
    pie2Datasets(data) {
      const totcash = data
        .filter((item) => item.paymentMethod === "cash")
        .reduce((accumulator, currentValue) => {
          return accumulator + parseFloat(currentValue.actualIncomeOfThisDay);
        }, 0);
      const totnoncash = data
        .filter((item) => item.paymentMethod === "non-cash")
        .reduce((accumulator, currentValue) => {
          return accumulator + parseFloat(currentValue.actualIncomeOfThisDay);
        }, 0);
      const totagent = data
        .filter((item) => item.paymentMethod.includes("agent"))
        .reduce((accumulator, currentValue) => {
          return accumulator + parseFloat(currentValue.actualIncomeOfThisDay);
        }, 0);
      this.pie2Data.datasets[0].data = [totcash, totnoncash, totagent];
    },
    pie3Datasets(data) {
      const approved = data
        .filter((item) => item.agent_isApproved == 1)
        .reduce((accumulator, currentValue) => {
          return accumulator + parseFloat(currentValue.agentPayment);
        }, 0);
      const pending = data
        .filter(
          (item) => item.agent_isApproved == 0 || item.agent_isApproved == null
        )
        .reduce((accumulator, currentValue) => {
          return accumulator + parseFloat(currentValue.agentPayment);
        }, 0);
      this.pie3Data.datasets[0].data = [approved, pending];
    },
    bar1Datasets(data) {
      this.bar1Data.datasets[0].data = this.roomcategories.map((o) => {
        const counter = data.filter((item) => item.room_type === o).length;
        return counter;
      });
    },
    bar2Datasets(data) {
      this.bar2Data.datasets[0].data = this.roomcategories.map((o) => {
        const counter = data
          .filter((item) => item.itemType === o)
          .reduce((accumulator, currentValue) => {
            return accumulator + parseFloat(currentValue.totalCost);
          }, 0);
        return counter;
      });
    },
    bar3Datasets(data) {
      const processedByList = data.map((record) => record.processedBy);
      const uniqueProcessedByList = [...new Set(processedByList)].filter(
        (name) => name !== ""
      );
      let collection = [];
      for (const name of uniqueProcessedByList) {
        const total = data
          .filter(
            (item) =>
              item.processedBy === name && !item.paymentMethod.includes("agent")
          )
          .reduce((accumulator, currentValue) => {
            return accumulator + parseFloat(currentValue.cashAmountPay);
          }, 0);
        collection.push(total);
      }

      this.bar3Data.labels = uniqueProcessedByList;
      this.bar3Data.datasets[0].data = collection;
      console.log(data);
    },
    bar4Datasets(data) {
      let collection = [];
      for (const agent of this.agents) {
        const total = data
          .filter((item) => item.nonCashReference.toLowerCase().includes(agent))
          .reduce((accumulator, currentValue) => {
            return accumulator + parseFloat(currentValue.agentPayment);
          }, 0);
        collection.push(total);
      }

      this.bar4Data.labels = this.agents;
      this.bar4Data.datasets[0].data = collection;
    },
    line1Datasets(data) {
      const arr = data.reduce((acc, curr) => {
        const date = this.parseDate(curr.checkinDate);
        acc[date] = (acc[date] || 0) + 1;
        return acc;
      }, {});

      const dates = Object.keys(arr).sort();
      const frequency = dates.map((date) => arr[date]);
      dates.unshift("");
      frequency.unshift(0);
      const actualdata = frequency;
      const actualdates = dates;

      arima.then((ARIMA) => {
        const arima = new ARIMA({
          p: 2,
          d: 1,
          q: 1,
          P: 0,
          D: 1,
          Q: 1,
          s: 4,
          verbose: false,
        }).train(actualdata);
        const [pred, errors] = arima.predict(30);
        if (pred.length > 0) {
          let dummydates = [...actualdates];
          let forecastdata = [...actualdata];
          for (const item of pred) {
            dummydates.push("");
            forecastdata.push(item);
          }
          this.line1Data.labels = dummydates;
          this.line1Data.datasets[0].data = forecastdata;
        }
      });
      this.line1Data.labels = actualdates;
      this.line1Data.datasets[1].data = actualdata;
    },
    line2Datasets(data) {
      const summary = data.reduce(
        (acc, curr) => {
          const index = acc.dates.indexOf(
            this.parseDate3(curr.transaction_date)
          );

          if (index === -1) {
            acc.dates.push(this.parseDate3(curr.transaction_date));
            acc.totals.push(parseFloat(curr.cashAmountPay));
          } else {
            acc.totals[index] += parseFloat(curr.cashAmountPay);
          }

          return acc;
        },
        { dates: [], totals: [] }
      );

      const result = {
        dates: summary.dates,
        totalCashAmountPay: summary.totals,
      };

      const o = result.dates.map((date, index) => ({
        date,
        totalCashAmountPay: result.totalCashAmountPay[index],
      }));
      o.sort((a, b) => new Date(a.date) - new Date(b.date));
      result.totalCashAmountPay = o.map((item) => item.totalCashAmountPay);
      result.dates.sort((a, b) => new Date(a) - new Date(b));
      result.dates.unshift("");
      result.totalCashAmountPay.unshift(0);
      const actualdata = result.totalCashAmountPay;
      const actualdates = result.dates;
      arima.then((ARIMA) => {
        const arima = new ARIMA({
          p: 2,
          d: 1,
          q: 1,
          P: 0,
          D: 1,
          Q: 1,
          s: 4,
          verbose: false,
        }).train(actualdata);
        const [pred, errors] = arima.predict(30);
        if (pred.length > 0) {
          let dummydates = [...actualdates];
          let forecastdata = [...actualdata];
          for (const item of pred) {
            dummydates.push("");
            forecastdata.push(item);
          }
          this.line2Data.labels = dummydates;
          this.line2Data.datasets[0].data = forecastdata;
        }
      });
      this.line2Data.labels = actualdates;
      this.line2Data.datasets[1].data = actualdata;
    },
    line3Datasets(data) {
      const summary = data.reduce(
        (acc, curr) => {
          const index = acc.dates.indexOf(this.parseDate3(curr.dateCreated));

          if (index === -1) {
            acc.dates.push(this.parseDate3(curr.dateCreated));
            acc.totals.push(parseFloat(curr.purchaseQty));
          } else {
            acc.totals[index] += parseFloat(curr.purchaseQty);
          }

          return acc;
        },
        { dates: [], totals: [] }
      );

      const result = {
        dates: summary.dates,
        frequency: summary.totals,
      };

      const o = result.dates.map((date, index) => ({
        date,
        frequency: result.frequency[index],
      }));
      o.sort((a, b) => new Date(a.date) - new Date(b.date));
      result.frequency = o.map((item) => item.frequency);
      result.dates.sort((a, b) => new Date(a) - new Date(b));
      result.dates.unshift("");
      result.frequency.unshift(0);
      const actualdata = result.frequency;
      const actualdates = result.dates;
      arima.then((ARIMA) => {
        const arima = new ARIMA({
          p: 2,
          d: 1,
          q: 1,
          P: 0,
          D: 1,
          Q: 1,
          s: 4,
          verbose: false,
        }).train(actualdata);
        const [pred, errors] = arima.predict(30);
        if (pred.length > 0) {
          let dummydates = [...actualdates];
          let forecastdata = [...actualdata];
          for (const item of pred) {
            dummydates.push("");
            forecastdata.push(item);
          }
          this.line3Data.labels = dummydates;
          this.line3Data.datasets[0].data = forecastdata;
        }
      });
      this.line3Data.labels = actualdates;
      this.line3Data.datasets[1].data = actualdata;
    },
    scrollRecord() {
      this.loaded.fill(false, 0, 4);
      this.loadData();
    },
    async loadData() {
      try {
        const daycount = 10 - this.backtrack;
        const today = new Date();
        const curday = new Date(today);
        curday.setDate(today.getDate() - daycount);
        this.chosenDate = curday.toDateString();

        const guestcounterdata = await axios.get(
          this.API_URL + "guestcounter/"
        );

        const foundItem = guestcounterdata.data.find(
          (item) => formatDate2(item.date_created) === parseDate(new Date())
        );
        if (foundItem) {
          this.counter = parseFloat(foundItem.counter);
        } else {
          this.counter = 0;
        }

        const bookingData = await axios.get(this.API_URL + "bookings/");
        const transactionData = await axios.get(this.API_URL + "transaction/");
        const transactionItemsData = await axios.get(
          this.API_URL + "transaction/item/"
        );
        const transactionRecordsData = await axios.get(
          this.API_URL + "transaction/record/"
        );

        this.transrecords = transactionRecordsData.data;

        const processedByList = this.transrecords
          .filter(
            (o) =>
              o.paymentMethod.includes("agent") &&
              o.paymentMethod.includes("credit")
          )
          .map((record) => record.processedBy);
        const uniqueProcessedByList = [...new Set(processedByList)].filter(
          (name) => name !== ""
        );
        this.actors = uniqueProcessedByList;

        const roomscatResponse = await axios.get(
          this.API_URL + "rooms/category/"
        );

        const agentsResponse = await axios.get(this.API_URL + "agents/");
        this.agents = [];
        for (const agent of agentsResponse.data) {
          this.agents.push(agent.name.toLowerCase());
        }

        this.roomcategories = roomscatResponse.data
          .filter((item) => item.isAvailable === true)
          .map((o) => {
            return o.name;
          });

        this.bar1Data.labels = this.roomcategories;
        this.bar2Data.labels = this.roomcategories;

        if (
          JSON.stringify(bookingData.data) !== JSON.stringify(this.prevBookings)
        ) {
          this.componentKey += 1;
          this.prevBookings = bookingData.data;
          this.prevTransactions = transactionData.data;
          this.prevransItems = transactionItemsData.data;
          this.loaded = Array(10).fill(false);
        }

        const roomsData = await axios.get(this.API_URL + "rooms/");

        this.numReservations = bookingData.data.filter(
          (item) => item.checkinDate === curday.toLocaleDateString("en-GB")
        ).length;

        this.numGuests = transactionItemsData.data
          .filter(
            (item) =>
              item.itemType === "ENTRANCE" &&
              new Date(item.dateCreated)
                .setHours(0, 0, 0, 0)
                .toLocaleString("en-US") ===
                curday.setHours(0, 0, 0, 0).toLocaleString("en-US")
          )
          .reduce((accumulator, currentValue) => {
            return accumulator + parseFloat(currentValue.purchaseQty);
          }, 0);

        this.availableRooms = roomsData.data.filter((room) => {
          // Check if there are any bookings for this room that overlap with the specified date range
          const overlappingBookings = bookingData.data.filter((booking) => {
            return (
              booking.room_name === room.name &&
              booking.status === "checkedin" &&
              booking.checkinDate === curday.toLocaleDateString("en-GB")
            );
          });

          // Return true if there are no overlapping bookings
          return overlappingBookings.length === 0;
        }).length;

        this.pie1Datasets(
          bookingData.data.filter(
            (item) => item.checkinDate === curday.toLocaleDateString("en-GB")
          )
        );
        this.bar1Datasets(
          bookingData.data.filter(
            (item) => item.checkinDate === curday.toLocaleDateString("en-GB")
          )
        );
        this.bar2Datasets(transactionItemsData.data);
        this.line1Datasets(
          bookingData.data.filter((o) => o.status === "checkedout")
        );
        this.line2Datasets(transactionData.data);
        this.line3Datasets(
          transactionItemsData.data.filter((o) => o.itemType === "ENTRANCE")
        );
        const trans_itemizer_data = await axios.get(
          this.API_URL + `transactions_itemizer/${daycount}/`
        );

        // const nonAgentIncome = trans_itemizer_data.data
        //   .filter((item) => {
        //     const transactionDate = new Date(item.transaction_date);
        //     const isAgentRecord =
        //       item.items2.filter((o) => o.paymentMethod.includes("agent"))
        //         .length > 0;
        //     return (
        //       !isAgentRecord &&
        //       transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
        //       transactionDate <
        //         new Date(
        //           new Date(new Date(curday.getTime() + 86400000)).setHours(
        //             0,
        //             0,
        //             0,
        //             0
        //           )
        //         )
        //     );
        //   })
        //   .reduce((accumulator, currentValue) => {
        //     return accumulator + parseFloat(currentValue.actualIncomeOfThisDay);
        //   }, 0);

        const nonAgentIncome = transactionRecordsData.data
          .filter((item) => {
            const transactionDate = new Date(item.transaction_date);
            const isAgentRecord = item.paymentMethod.includes("agent");
            return (
              !isAgentRecord &&
              transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
              transactionDate <
                new Date(
                  new Date(new Date(curday.getTime() + 86400000)).setHours(
                    0,
                    0,
                    0,
                    0
                  )
                )
            );
          })
          .reduce((accumulator, currentValue) => {
            return accumulator + parseFloat(currentValue.cashAmountPay);
          }, 0);

        const approvedAgentPayment = transactionRecordsData.data
          .filter((item) => {
            const transactionDate = new Date(item.transaction_date);
            const isAgentType = item.paymentMethod.includes("agent");
            const isApproved = item.agent_isApproved;
            return (
              isAgentType &&
              isApproved &&
              transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
              transactionDate <
                new Date(
                  new Date(new Date(curday.getTime() + 86400000)).setHours(
                    0,
                    0,
                    0,
                    0
                  )
                )
            );
          })
          .reduce((accumulator, currentValue) => {
            return accumulator + parseFloat(currentValue.agentPayment);
          }, 0);

        this.grossIncome = nonAgentIncome + approvedAgentPayment;

        const nonAgentBalance = trans_itemizer_data.data
          .filter((item) => {
            const transactionDate = new Date(item.transaction_date);
            const isAgentRecord =
              item.items2.filter((o) => o.paymentMethod.includes("agent"))
                .length > 0;
            return (
              !isAgentRecord &&
              transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
              transactionDate <
                new Date(
                  new Date(new Date(curday.getTime() + 86400000)).setHours(
                    0,
                    0,
                    0,
                    0
                  )
                )
            );
          })
          .reduce((accumulator, currentValue) => {
            return accumulator + parseFloat(currentValue.balance);
          }, 0);

        const notApprovedAgentPayment = transactionRecordsData.data
          .filter((item) => {
            const transactionDate = new Date(item.transaction_date);
            const isAgentType = item.paymentMethod.includes("agentnocredit");
            const isApproved = item.agent_isApproved;
            return (
              isAgentType &&
              !isApproved &&
              transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
              transactionDate <
                new Date(
                  new Date(new Date(curday.getTime() + 86400000)).setHours(
                    0,
                    0,
                    0,
                    0
                  )
                )
            );
          })
          .reduce((accumulator, currentValue) => {
            return accumulator + parseFloat(currentValue.agentPayment);
          }, 0);

        this.collectibles = nonAgentBalance + notApprovedAgentPayment;

        const notApprovedAllAgentPayment = transactionRecordsData.data
          .filter((item) => {
            const transactionDate = new Date(item.transaction_date);
            const isAgentType = item.paymentMethod.includes("agent");
            const isApproved = item.agent_isApproved;
            return (
              isAgentType &&
              !isApproved &&
              transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
              transactionDate <
                new Date(
                  new Date(new Date(curday.getTime() + 86400000)).setHours(
                    0,
                    0,
                    0,
                    0
                  )
                )
            );
          })
          .reduce((accumulator, currentValue) => {
            return accumulator + parseFloat(currentValue.agentPayment);
          }, 0);

        this.pending = notApprovedAllAgentPayment;

        this.pie2Datasets(
          trans_itemizer_data.data.filter((item) => {
            const transactionDate = new Date(item.transaction_date);
            return (
              transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
              transactionDate <
                new Date(
                  new Date(new Date(curday.getTime() + 86400000)).setHours(
                    0,
                    0,
                    0,
                    0
                  )
                )
            );
          })
        );

        this.pie3Datasets(
          transactionRecordsData.data.filter((item) => {
            const transactionDate = new Date(item.transaction_date);
            const isAgentType = item.paymentMethod.includes("agent");
            return (
              isAgentType &&
              transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
              transactionDate <
                new Date(
                  new Date(new Date(curday.getTime() + 86400000)).setHours(
                    0,
                    0,
                    0,
                    0
                  )
                )
            );
          })
        );

        this.bar3Datasets(
          transactionRecordsData.data.filter((item) => {
            const transactionDate = new Date(item.transaction_date);
            return (
              transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
              transactionDate <
                new Date(
                  new Date(new Date(curday.getTime() + 86400000)).setHours(
                    0,
                    0,
                    0,
                    0
                  )
                )
            );
          })
        );

        this.bar4Datasets(
          transactionRecordsData.data.filter((item) => {
            const transactionDate = new Date(item.transaction_date);
            const isAgentType = item.paymentMethod.includes("agent");
            return (
              isAgentType &&
              transactionDate >= new Date(curday.setHours(0, 0, 0, 0)) &&
              transactionDate <
                new Date(
                  new Date(new Date(curday.getTime() + 86400000)).setHours(
                    0,
                    0,
                    0,
                    0
                  )
                )
            );
          })
        );

        this.loaded = Array(10).fill(true);
      } catch (error) {}
    },
  },
  async mounted() {
    // initialize loaded array
    this.loaded = Array(10).fill(false);

    // load data
    await this.loadData();

    // set interval to refresh data every 3 seconds if component is in focus
    // const intervalId = setInterval(async () => {
    if (this.active && !document.hidden && document.hasFocus()) {
      await this.loadData();
    }
    // }, 3000);

    // add event listener to clear interval when component is not in focus
    document.addEventListener("visibilitychange", () => {
      if (!this.active || document.hidden || !document.hasFocus()) {
        // clearInterval(intervalId);
      } else {
        // intervalId = setInterval(async () => {
        // await this.loadData();
        this.loadData();
        // }, 3000);
      }
    });
  },
};
</script>
<style>
.card.x,
.card-header.x {
  border: none;
  background-color: transparent;
}

.card-body.chart {
  height: 400px !important;
}
</style>
