<template>
  <div class="card">
    <div class="card-header">
      <div class="d-flex justify-content-between align-items-center mt-3">
        <p class="mb-0 no-print">
          <label
            >Show
            <select
              v-model="rowsPerPage"
              aria-controls="example"
              class="form-input"
            >
              <option value="10">10</option>
              <option value="25">25</option>
              <option value="50">50</option>
              <option value="100">100</option>
              <option value="999999">Show All</option>
            </select>
            entries</label
          >
          &NonBreakingSpace;
          <button class="btn btn-sm btn-primary" @click="printSection">
            <i class="fas fa-print"></i>
          </button>
          &nbsp;
          <button class="btn btn-sm btn-primary" @click="exportXLSX">
            <i class="fas fa-file-excel"></i>
          </button>
          &nbsp;
          <button class="btn btn-sm btn-primary" @click="saveAsPDF">
            <i class="fas fa-file-pdf"></i>
          </button>
        </p>
        <div class="form-outline col-md-3 mb-0 no-print">
          <input
            type="search"
            class="form-control"
            placeholder="Type query"
            v-model="searchText"
            aria-label="Search"
            autocomplete="off"
            aria-autocomplete="off"
          />
        </div>
      </div>
    </div>
    <div class="card-body">
      <div
        v-if="!mainItems.length"
        class="d-flex justify-content-center align-items-center mt-3"
      >
        <div class="spinner-border" role="status">
          <span class="sr-only">Loading...</span>
        </div>
      </div>
      <div v-else>
        <table
          class="table"
          v-bind:id="uniqueID"
          style="table-layout: fixed; width: 100%"
        >
          <thead>
            <tr v-if="howmanyCheckbox > 0 && batchAction">
              <th :colspan="mainHeaders.length" style="border: 0px">
                <button
                  type="button"
                  class="btn btn-sm btn-round bg-primary text-white"
                  @click="
                    $emit(
                      'batch-action',
                      paginatedMainItems
                        .filter(function (item) {
                          return getItemsfromCheckedBoxes.includes(item.id);
                        })
                        .map(function (item) {
                          return item.id;
                        })
                    )
                  "
                >
                  Change Status
                </button>
              </th>
            </tr>
            <tr>
              <template v-for="(header, index) in mainHeaders" :key="index">
                <th v-if="header.field === 'toggle' && toggleable">
                  <button
                    class="btn btn-sm btn-primary no-print"
                    @click="toggleAll()"
                  >
                    <span v-if="showAll === false">+</span>
                    <span v-else>-</span>
                  </button>
                </th>
                <th v-else-if="header.field === 'checkbox' && selectable">
                  <input
                    type="checkbox"
                    class="form-check-input no-print"
                    @change="toggleCheckboxes"
                    :value="mainCheckbox"
                  />
                </th>
                <th
                  v-else
                  @click="sort(header.field)"
                  :class="{ sortable: header.sortable }"
                >
                  {{ header.label }}
                  <span v-if="header.sortable" class="sort-icon no-print">
                    <i
                      :class="[
                        'fas',
                        sortColumn === header.field && sortDirection === 1
                          ? 'fa-sort-alpha-up'
                          : 'fa-sort-alpha-down',
                      ]"
                    ></i>
                  </span>
                </th>
              </template>
            </tr>
          </thead>
          <tbody>
            <template
              v-for="(mainItem, mainIndex) in paginatedMainItems"
              :key="mainItem.id"
            >
              <tr :class="{ 'table-active': showTable[mainItem.id] }">
                <td
                  v-for="(header, index) in mainHeaders"
                  :key="index"
                  style="
                    word-wrap: break-word;
                    white-space: normal;
                    overflow: hidden;
                    max-width: 1px;
                  "
                >
                  <template v-if="header.field === 'checkbox' && selectable">
                    <input
                      type="checkbox"
                      class="mtCheckbox form-check-input no-print"
                      :data-id="mainItem.id"
                      @change="toggleCheckbox"
                    />
                  </template>
                  <template v-else-if="header.field === 'toggle' && toggleable">
                    <button
                      type="button"
                      @click="toggleTable(mainItem.id)"
                      class="btn btn-primary btn-sm toggle no-print"
                    >
                      <span v-if="!showTable[mainItem.id]">+</span>
                      <span v-else>-</span>
                    </button>
                  </template>
                  <template v-else-if="header.field === 'action'">
                    <button
                      v-if="this.editable"
                      type="button"
                      class="btn btn-primary btn-sm no-print"
                      @click="$emit('edit-action', mainItem.id)"
                      style="margin-right: 10px"
                    >
                      <i class="fas fa-edit"></i>
                    </button>
                    <button
                      v-if="this.custombtn"
                      type="button"
                      class="btn btn-primary btn-sm no-print"
                      @click="$emit('custombtn-action', mainItem.id)"
                    >
                      <i class="fa fa-eye"></i>
                    </button>
                    <button
                      v-if="this.deletable"
                      type="button"
                      class="btn btn-danger btn-sm no-print"
                      @click="$emit('delete-action', mainItem.id)"
                    >
                      <i class="fas fa-trash"></i>
                    </button>
                    <template v-if="header.slot" class="no-print">
                      <slot
                        name="custombtn"
                        :data="{ h: header.field, dt: mainItem }"
                      ></slot>
                    </template>
                  </template>
                  <template v-else-if="header.field.includes('date')">
                    {{ formatDate(new Date(mainItem[header.field])) }}
                  </template>
                  <template v-else>
                    <template v-if="header.slot">
                      <slot
                        name="content"
                        :data="{ h: header.field, dt: mainItem }"
                      ></slot>
                    </template>
                    <template v-else>
                      {{ mainItem[header.field] }}
                    </template>
                  </template>
                </td>
              </tr>
              <tr v-if="showTable[mainItem.id] && toggleable">
                <td :colspan="mainHeaders.length">
                  <div v-if="slotsub" style="padding-left: 60px">
                    <slot name="subcontent" :data="mainItem.items"></slot>
                  </div>
                  <div v-else style="padding-left: 60px">
                    <div v-if="mainItem.items.length > 0">
                      <table
                        class="table"
                        style="table-layout: fixed; word-wrap: break-word"
                      >
                        <thead>
                          <tr>
                            <template
                              v-for="(subHeader, index) in subHeaders"
                              :key="index"
                            >
                              <th>{{ subHeader.label }}</th>
                            </template>
                          </tr>
                        </thead>
                        <tbody>
                          <template
                            v-for="(subItem, subIndex) in mainItem.items"
                            :key="subIndex"
                          >
                            <tr>
                              <template
                                v-for="(subHeader, index) in subHeaders"
                                :key="index"
                              >
                                <template
                                  v-if="subHeader.field.includes('date')"
                                >
                                  <td>
                                    {{
                                      formatDate(
                                        new Date(subItem[subHeader.field])
                                      )
                                    }}
                                  </td>
                                </template>
                                <template v-else>
                                  <td>{{ subItem[subHeader.field] }}</td>
                                </template>
                              </template>
                            </tr>
                          </template>
                        </tbody>
                      </table>
                    </div>
                    <div v-if="mainItem.items2 && mainItem.items2.length > 0">
                      <table
                        class="table"
                        style="table-layout: fixed; word-wrap: break-word"
                      >
                        <thead>
                          <tr>
                            <template
                              v-for="(subHeader, index) in subHeaders2"
                              :key="index"
                            >
                              <th>{{ subHeader.label }}</th>
                            </template>
                          </tr>
                        </thead>
                        <tbody>
                          <template
                            v-for="(subItem, subIndex) in mainItem.items2"
                            :key="subIndex"
                          >
                            <tr>
                              <template
                                v-for="(subHeader, index) in subHeaders2"
                                :key="index"
                              >
                                <template
                                  v-if="subHeader.field.includes('date')"
                                >
                                  <td>
                                    {{
                                      formatDate(
                                        new Date(subItem[subHeader.field])
                                      )
                                    }}
                                  </td>
                                </template>
                                <template v-else>
                                  <td>{{ subItem[subHeader.field] }}</td>
                                </template>
                              </template>
                            </tr>
                          </template>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </td>
              </tr>
            </template>
            <tr>
              <td v-for="(header, index) in mainHeaders" :key="index">
                <span
                  class="text-primary"
                  v-if="header.reducible"
                  style="font-weight: bold"
                  >{{ sumColumn(header.field).toFixed(2) }}</span
                >
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="card-footer">
      <div class="no-print">
        <nav aria-label="Table pagination">
          <div class="d-flex justify-content-between align-items-center mt-3">
            <p class="mb-0">
              Showing
              {{
                Math.min(
                  (currentPage - 1) * rowsPerPage + 1,
                  paginatedMainItems.length
                )
              }}
              to
              {{
                Math.min(currentPage * rowsPerPage, paginatedMainItems.length)
              }}
              of {{ paginatedMainItems.length }} entries{{
                searchText
                  ? " (filtered from " + mainItems.length + " total entries)"
                  : ""
              }}
            </p>

            <ul class="pagination mb-0">
              <li class="page-item" :class="{ disabled: currentPage === 1 }">
                <button
                  class="page-link"
                  @click="currentPage = 1"
                  aria-label="First page"
                >
                  <span aria-hidden="true">First</span>
                </button>
              </li>
              <li class="page-item" :class="{ disabled: currentPage === 1 }">
                <button
                  class="page-link"
                  @click="currentPage -= 1"
                  aria-label="Previous"
                >
                  <span aria-hidden="true">Previous</span>
                </button>
              </li>
              <li
                v-for="pageNumber in visiblePages"
                :key="pageNumber"
                class="page-item"
                :class="{ active: currentPage === pageNumber }"
              >
                <button class="page-link" @click="currentPage = pageNumber">
                  {{ pageNumber }}
                </button>
              </li>
              <li
                v-if="visiblePages[visiblePages.length - 1] < pageCount - 1"
                class="page-item disabled"
              >
                <span class="page-link">...</span>
              </li>
              <li
                class="page-item"
                :class="{ disabled: currentPage === pageCount }"
              >
                <button
                  class="page-link"
                  @click="currentPage += 1"
                  aria-label="Next"
                >
                  <span aria-hidden="true">Next</span>
                </button>
              </li>
              <li
                class="page-item"
                :class="{ disabled: currentPage === pageCount }"
              >
                <button
                  class="page-link"
                  @click="currentPage = pageCount"
                  aria-label="Last page"
                >
                  <span aria-hidden="true">Last</span>
                </button>
              </li>
            </ul>
          </div>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
import xlsx from "json-as-xlsx";
import jsPDF from "jspdf";

export default {
  props: {
    uniqueID: {
      type: String,
      default: () => {
        const affix = "table";
        return `${affix}-${Math.random().toString(36).substring(7)}`;
      },
    },
    currentNoPage: {
      type: Number,
      default: 10,
    },
    mainHeaders: {
      type: Array,
      required: true,
    },
    mainItems: {
      type: Array,
      required: true,
    },
    subHeaders: {
      type: Array,
      required: false,
    },
    subHeaders2: {
      type: Array,
      required: false,
    },
    editable: {
      type: Boolean,
      required: false,
    },
    custombtn: {
      type: Boolean,
      required: false,
    },
    deletable: {
      type: Boolean,
      required: false,
    },
    toggleable: {
      type: Boolean,
      required: false,
    },
    selectable: {
      type: Boolean,
      required: false,
    },
    slotsub: {
      type: Boolean,
      required: false,
    },
    batchAction: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  data() {
    return {
      isLoading: true,
      currentPage: 1,
      rowsPerPage: 10,
      showAll: false,
      showTable: {},
      searchText: "",
      sortColumn: null,
      sortDirection: 1,
      mainCheckbox: false,
      howmanyCheckbox: 0,
      getItemsfromCheckedBoxes: [],
    };
  },
  computed: {
    paginatedMainItems() {
      const startIndex = (this.currentPage - 1) * this.rowsPerPage;
      const endIndex = parseFloat(startIndex) + parseFloat(this.rowsPerPage);
      return this.filteredItems.slice(startIndex, endIndex);
    },
    filteredItems() {
      const sortedItems = [...this.mainItems];

      sortedItems.sort((a, b) => {
        const aValue = a[this.sortColumn];
        const bValue = b[this.sortColumn];

        if (aValue === undefined || bValue === undefined) return 0;

        const isAscending = this.sortDirection === 1;

        const aDate = Date.parse(aValue);
        const bDate = Date.parse(bValue);

        // Sort dates
        if (!isNaN(aDate) && !isNaN(bDate)) {
          return isAscending ? aDate - bDate : bDate - aDate;
        }

        const aString = aValue.toString().toLowerCase();
        const bString = bValue.toString().toLowerCase();

        if (parseFloat(aString) == aString && parseFloat(bString) == bString) {
          if (parseFloat(aString) < parseFloat(bString)) {
            return isAscending ? -1 : 1;
          } else if (parseFloat(aString) > parseFloat(bString)) {
            return isAscending ? 1 : -1;
          } else {
            return 0;
          }
        } else {
          if (aString < bString) {
            return isAscending ? -1 : 1;
          } else if (aString > bString) {
            return isAscending ? 1 : -1;
          } else {
            return 0;
          }
        }
      });

      return sortedItems
        .map((o) => {
          if (o) {
            // Add check for undefined
            const searchCode =
              Object.keys(o)
                .map((key) => `${key}:${o[key]}`)
                .join("~") +
              (o.items
                ? o.items
                    .map((item) => Object.values(item).join(" "))
                    .join(", ")
                : []);
            return {
              ...o,
              searchCode,
            };
          }
        })
        .filter((item) =>
          item.searchCode
            .toString()
            .toLowerCase()
            .includes(this.searchText.toLowerCase())
        );
    },
    pageCount() {
      return Math.ceil(this.mainItems.length / this.rowsPerPage);
    },
    visiblePages() {
      let startPage = 1;
      let endPage = this.pageCount;
      if (this.pageCount > this.rowsPerPage) {
        const halfVisiblePages = Math.floor(this.rowsPerPage / 2);
        startPage = Math.max(this.currentPage - halfVisiblePages, 1);
        endPage = startPage + this.rowsPerPage - 1;
        if (endPage > this.pageCount) {
          endPage = this.pageCount;
          startPage = endPage - this.rowsPerPage + 1;
        } else if (startPage > 1) {
          startPage += 1;
        }
      }
      const pages = [];
      for (let i = startPage; i <= endPage; i++) {
        pages.push(i);
      }
      return pages;
    },
  },
  methods: {
    toggleCheckboxes() {
      this.mainCheckbox = !this.mainCheckbox;
      $(".mtCheckbox").prop("checked", this.mainCheckbox);
      this.howmanyCheckbox = $(".mtCheckbox").filter(":checked").length;
      let dataIds = [];
      this.getItemsfromCheckedBoxes = [];
      $(".mtCheckbox")
        .filter(":checked")
        .each(function () {
          var dataId = $(this).data("id");
          dataIds.push(dataId);
        });
      this.getItemsfromCheckedBoxes = dataIds;
    },
    toggleCheckbox() {
      this.howmanyCheckbox = $(".mtCheckbox").filter(":checked").length;
      let dataIds = [];
      this.getItemsfromCheckedBoxes = [];
      $(".mtCheckbox")
        .filter(":checked")
        .each(function () {
          var dataId = $(this).data("id");
          dataIds.push(dataId);
        });
      this.getItemsfromCheckedBoxes = dataIds;
    },
    sort(field) {
      if (this.sortColumn === field) {
        this.sortDirection = -this.sortDirection;
      } else {
        this.sortColumn = field;
        this.sortDirection = 1;
      }
    },

    toggleAll() {
      const propKey = `showTable`;
      const toggleKey = `showAll`;
      this[toggleKey] = !this[toggleKey];
      this.filteredItems.forEach((item) => {
        this[propKey] = Object.assign({}, this[propKey], {
          [item.id]: this[toggleKey],
        });
      });
    },

    toggleTable(id) {
      this.showTable[id] = !this.showTable[id];
    },
    formatDate(date) {
      const options = {
        month: "2-digit",
        day: "2-digit",
        year: "numeric",
        hour: "numeric",
        minute: "numeric",
        second: "numeric",
      };
      return new Intl.DateTimeFormat("en-US", options).format(date);
    },

    sumColumn(col) {
      const total = this.paginatedMainItems.reduce(
        (accumulator, currentValue) =>
          accumulator + parseFloat(currentValue[col]),
        0
      );
      return total;
    },

    getObjectProperties(object) {
      return Object.keys(object).map((key) => {
        return {
          label: key,
          value: key,
        };
      });
    },

    transformData(jsonData) {
      const transformedData = [];

      jsonData.forEach((item) => {
        const mainRow = { ...item };

        // Remove items and items2 from the main row
        delete mainRow.items;
        delete mainRow.items2;

        // Add each item in 'items' as a new row under the main row
        item.items.forEach((itemRow) => {
          transformedData.push({ ...mainRow, ...itemRow });
        });

        // Add each item in 'items2' as a new row under the main row
        item.items2.forEach((itemRow) => {
          transformedData.push({ ...mainRow, ...itemRow });
        });
      });

      return transformedData;
    },

    exportXLSX() {
      let data = [
        {
          sheet: "data",
          columns: this.getObjectProperties(this.filteredItems[0]),
          content: this.filteredItems,
        },
      ];

      let settings = {
        fileName: "jsondata", // Name of the resulting spreadsheet
        extraLength: 3, // A bigger number means that columns will be wider
        writeMode: "writeFile", // The available parameters are 'WriteFile' and 'write'. This setting is optional. Useful in such cases https://docs.sheetjs.com/docs/solutions/output#example-remote-file
        writeOptions: {}, // Style options from https://docs.sheetjs.com/docs/api/write-options
        RTL: false, // Display the columns from right-to-left (the default value is false)
      };

      xlsx(data, settings); // Will download the excel file
    },

    saveAsPDF() {
      const doc = new jsPDF("l", "pt", [612, 936]);
      const content =
        "<div style='width:675pt'>" +
        document.getElementById(this.uniqueID).outerHTML +
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
          const dataTable = document.getElementById(this.uniqueID);
          const printElement = document.createElement("div");
          printElement.appendChild(dataTable.cloneNode(true));

          // Open a new window and write the printElement to it
          const printWindow = window.open("", "Print Window");
          printWindow.document.write("<html><head>");
          printWindow.document.write(
            '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
          );
          printWindow.document.write(
            "<style>html,body{display:none;}.no-print{display: none;} @media print{@page {size: legal landscape; margin:auto} html,body{display: block;} tr{page-break-inside: auto;} .no-print{display: none;}}</style>"
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
  mounted() {
    this.rowsPerPage = this.currentNoPage;
  },
};
</script>

<style scoped>
.badge-danger {
  background-color: #dc3545;
  color: #fff;
}
</style>
