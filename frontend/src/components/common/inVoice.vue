<template>
  <div id="invoicedoc">
    <div class="row d-flex align-items-baseline">
      <div class="col-xl-10">
        <p class="text-primary" style="font-size: 20px">
          Invoice >> <strong>ID: {{ invoiceId }}</strong>
        </p>
      </div>
      <div class="col-xl-2 float-end no-print">
        <a
          class="btn btn-light text-capitalize border-0"
          data-mdb-ripple-color="dark"
          @click="printSection"
          ><i class="fas fa-print text-primary"></i> Print</a
        >
        <!-- <a
          class="btn btn-light text-capitalize"
          data-mdb-ripple-color="dark"
          @click="saveAsPDF"
          ><i class="far fa-file-pdf text-danger"></i> Export</a
        > -->
      </div>
      <hr />
    </div>

    <div class="container">
      <div class="col-md-12">
        <div class="text-center">
          <img
            :src="`/src/assets/${this.APP_LOGO_NAME}`"
            width="45"
            height="45"
            class="d-inline-block align-top"
            alt="Logo"
            style="margin-right: 10px"
          />
          <p class="pt-0">Dumaluan Gokart</p>
        </div>
      </div>

      <div class="row">
        <div class="col-xl-7">
          <ul class="list-unstyled">
            <li class="text-muted">
              To: <span class="text-primary">{{ actor }}</span>
            </li>
            <li class="text-muted">{{ desc }}</li>
          </ul>
        </div>
        <div class="col-xl-5">
          <p class="text-muted">Invoice</p>
          <ul class="list-unstyled">
            <li class="text-muted">
              <i class="fas fa-circle text-primary"></i>
              <span class="fw-bold">ID:</span>{{ invoiceId }}
            </li>
            <li class="text-muted">
              <i class="fas fa-circle text-primary"></i>
              <span class="fw-bold">Creation Date: </span
              >{{ new Date().toDateString() }}
            </li>
            <li class="text-muted">
              <i class="fas fa-circle text-primary"></i>
              <span class="me-1 fw-bold">Status:</span
              ><span
                class="badge text-black fw-bold"
                :class="isPaid ? 'bg-success' : 'bg-warning'"
              >
                {{ isPaid ? "Paid" : "Unpaid" }}</span
              >
            </li>
          </ul>
        </div>
      </div>

      <div class="row my-2 mx-1 justify-content-center">
        <table class="table table-striped table-borderless">
          <thead class="bg-primary text-white">
            <tr>
              <th scope="col">#</th>
              <th scope="col">Description</th>
              <th scope="col">Qty</th>
              <th scope="col">Unit Price</th>
              <th scope="col">Amount</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in invdata" :key="index">
              <th scope="row">{{ index + 1 }}</th>
              <td>{{ item.item }}</td>
              <td>{{ item.qty }}</td>
              <td>{{ item.price }}</td>
              <td>{{ item.total }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="row">
        <div class="col-xl-8">
          <p class="ms-3">We accept online payment via bank and e-wallet.</p>
        </div>
        <div class="col-xl-4">
          <ul class="list-unstyled">
            <li class="text-muted ms-3">
              <span class="text-black me-4">SubTotal</span>₱{{ totalCost }}
            </li>
            <!-- <li class="text-muted ms-3 mt-2">
            <span class="text-black me-4">Tax(15%)</span>₱111
          </li> -->
          </ul>
          <p class="text-black float-start">
            <span class="text-black me-3"> Total Amount</span
            ><span style="font-size: 25px">₱{{ totalCost }}</span>
          </p>
        </div>
      </div>
      <hr />
      <div class="row">
        <div class="col-xl-10">
          <p>Thank you for your patronage</p>
        </div>
        <div class="col-xl-2 no-print" v-if="!isPaid">
          <button
            @click="$emit('pay-action', totalCost)"
            type="button"
            class="btn btn-primary text-capitalize"
          >
            Checkout
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import jsPDF from "jspdf";
export default {
  props: {
    invoiceId: {
      type: Number,
      required: true,
    },
    actor: {
      type: String,
      required: true,
    },
    desc: {
      type: String,
      required: true,
    },
    isPaid: {
      type: Boolean,
      required: true,
    },
    invdata: {
      type: Array,
      default: [{ item: "", qty: 1, price: 0, total: 0 }],
      required: true,
    },
  },
  computed: {
    totalCost() {
      return this.invdata.reduce((accumulator, item) => {
        return accumulator + parseFloat(item.price) * parseFloat(item.qty);
      }, 0);
    },
  },
  methods: {
    saveAsPDF() {
      const doc = new jsPDF("l", "pt", [612, 936]);
      const content =
        "<div style='width:675pt'>" +
        document.getElementById("invoicedoc").outerHTML +
        "</div>";
      doc.html(content, {
        callback: function (doc) {
          doc.save("download.pdf");
        },
      });
    },
    printSection() {
      // Add Bootstrap stylesheet to the head
      const bootstrapLink = document.createElement("link");
      bootstrapLink.rel = "stylesheet";
      bootstrapLink.href =
        "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css";
      document.head.appendChild(bootstrapLink);

      // Create a progress bar element
      const progressBar = document.createElement("div");
      progressBar.className = "progress fixed-top";
      progressBar.innerHTML =
        '<div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>';

      // Add the progress bar to the body
      document.body.appendChild(progressBar);
      progressBar.style.zIndex = 1057;
      // Create the overlay element
      const overlay = document.createElement("div");
      overlay.style.position = "fixed";
      overlay.style.top = 0;
      overlay.style.left = 0;
      overlay.style.width = "100%";
      overlay.style.height = "100%";
      overlay.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
      overlay.style.zIndex = 1056;
      overlay.classList.add("overlay");
      document.body.appendChild(overlay);

      // Track the loading progress of the stylesheet
      let progress = 0;
      const interval = setInterval(() => {
        progress += 10;
        if (progress >= 100) {
          clearInterval(interval);
          // Remove the progress bar
          document.body.removeChild(progressBar);
          // Get the dataTable section and create the print window
          const dataTable = document.getElementById("invoicedoc");
          const printElement = document.createElement("div");
          printElement.appendChild(dataTable.cloneNode(true));

          // Open a new window and write the printElement to it
          const printWindow = window.open("", "Print Window");
          printWindow.document.write("<html><head>");
          printWindow.document.write(
            '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
          );
          printWindow.document.write(
            "<style>html,body{display:none;}.no-print{display: none;} @media print{@page {size: legal; margin:auto} html,body{display: block;} tr{page-break-inside: auto;} .no-print{display: none;}}</style>"
          );
          printWindow.document.write("</head><body>");
          printWindow.document.write(printElement.innerHTML);
          printWindow.document.write("</body></html>");
          printWindow.document.close();

          // Print the window and close it after printing
          printWindow.onload = function () {
            printWindow.focus();
            printWindow.print();
            printWindow.close();

            // Remove the Bootstrap stylesheet from the head
            document.head.removeChild(bootstrapLink);
            document.body.removeChild(overlay);
          };
        } else {
          // Update the progress bar
          const progressBarChild = progressBar.querySelector(".progress-bar");
          progressBarChild.style.width = `${progress}%`;
          progressBarChild.setAttribute("aria-valuenow", progress);
        }
      }, 200);
    },
  },
};
</script>
<style scoped></style>
