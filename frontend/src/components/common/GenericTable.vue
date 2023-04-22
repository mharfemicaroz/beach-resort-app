<template>
    <div>

        <div v-if="!mainItems.length" class="d-flex justify-content-center align-items-center mt-3">
            <div class="spinner-border" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>
        <div v-else>
            <div class="d-flex justify-content-between align-items-center mt-3">
                <p class="mb-0 no-print">
                    <label>Show <select v-model="rowsPerPage" aria-controls="example" class="form-input">
                            <option value="10">10</option>
                            <option value="25">25</option>
                            <option value="50">50</option>
                            <option value="100">100</option>
                        </select> entries</label> &NonBreakingSpace;
                    <button class="btn btn-sm btn-primary" @click="printSection">
                        <i class="fas fa-print"></i>
                    </button>

                </p>
                <p class="mb-0 no-print">Search: <input type="text" class="form-input mt-2" v-model="searchText"></p>
            </div>

            <table class="table" v-bind:id="uniqueID">
                <thead>
                    <tr>
                        <template v-for="(header, index) in mainHeaders" :key="index">
                            <th v-if="header.field === 'toggle' && toggleable">
                                <button class="btn btn-sm btn-primary no-print" @click="toggleAll()">
                                    <span v-if="showAll === false">+</span>
                                    <span v-else>-</span>
                                </button>
                            </th>
                            <th v-else @click="sort(header.field)" :class="{ 'sortable': header.sortable }">
                                {{ header.label }}
                                <span v-if="header.sortable" class="sort-icon no-print">
                                    <i :class="[
                                        'fas',
                                        sortColumn === header.field && sortDirection === 1
                                            ? 'fa-sort-alpha-up'
                                            : 'fa-sort-alpha-down',
                                    ]"></i>
                                </span>
                            </th>
                        </template>
                    </tr>
                </thead>
                <tbody>
                    <template v-for="(mainItem, mainIndex) in filteredItems" :key="mainItem.id">
                        <tr :class="{ 'table-active': showTable[mainItem.id] }">
                            <td v-for="(header, index) in mainHeaders" :key="index">
                                <template v-if="header.field === 'isAvailable'">
                                    <span v-if="mainItem[header.field]">Yes</span>
                                    <span v-else>No</span>
                                </template>
                                <template v-else-if="header.field === 'toggle' && toggleable">
                                    <button type="button" @click="toggleTable(mainItem.id)"
                                        class="btn btn-primary btn-sm toggle no-print">
                                        <span v-if="!showTable[mainItem.id]">+</span>
                                        <span v-else>-</span>
                                    </button>
                                </template>
                                <template v-else-if="header.field === 'action' && this.editable">
                                    <button type="button" class="btn btn-primary btn-sm no-print"
                                        @click="$emit('edit-action', mainItem.id)">
                                        <i class="fas fa-edit"></i>
                                    </button>
                                </template>
                                <template v-else-if="header.field.includes('date')">
                                    {{ formatDate(new Date(mainItem[header.field])) }}
                                </template>
                                <template v-else>
                                    {{ mainItem[header.field] }}
                                </template>
                            </td>
                        </tr>
                        <tr v-if="showTable[mainItem.id] && toggleable">
                            <td :colspan="mainHeaders.length + 1">
                                <div style="padding-left: 60px;">
                                    <div v-if="mainItem.items.length > 0">
                                        <h5 class="bg-primary text-white">Records</h5>
                                        <table class="table" style="table-layout: fixed;word-wrap: break-word;">
                                            <thead>
                                                <tr>
                                                    <template v-for="(subHeader, index) in subHeaders" :key="index">
                                                        <th>{{ subHeader.label }}</th>
                                                    </template>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <template v-for="(subItem, subIndex) in mainItem.items" :key="subIndex">
                                                    <tr>
                                                        <template v-for="(subHeader, index) in subHeaders" :key="index">
                                                            <template v-if="subHeader.field.includes('date')">
                                                                {{ formatDate(new Date(subItem[subHeader.field])) }}
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
                </tbody>
            </table>
            <div class="no-print">

                <nav aria-label="Table pagination">
                    <div class="d-flex justify-content-between align-items-center mt-3">
                        <p class="mb-0">
                            Showing {{ Math.min((currentPage - 1) * rowsPerPage + 1, filteredItems.length) }} to {{
                                Math.min(currentPage * rowsPerPage, filteredItems.length) }} of {{ filteredItems.length }}
                            entries{{ searchText ? ' (filtered from ' + mainItems.length + ' total entries)' : '' }}
                        </p>

                        <ul class="pagination mb-0">
                            <li class="page-item" :class="{ disabled: currentPage === 1 }">
                                <button class="page-link" @click="currentPage = 1" aria-label="First page">
                                    <span aria-hidden="true">First</span>
                                </button>
                            </li>
                            <li class="page-item" :class="{ disabled: currentPage === 1 }">
                                <button class="page-link" @click="currentPage -= 1" aria-label="Previous">
                                    <span aria-hidden="true">Previous</span>
                                </button>
                            </li>
                            <li v-for="pageNumber in visiblePages" :key="pageNumber" class="page-item"
                                :class="{ active: currentPage === pageNumber }">
                                <button class="page-link" @click="currentPage = pageNumber">{{ pageNumber }}</button>
                            </li>
                            <li v-if="visiblePages[visiblePages.length - 1] < pageCount - 1" class="page-item disabled">
                                <span class="page-link">...</span>
                            </li>
                            <li class="page-item" :class="{ disabled: currentPage === pageCount }">
                                <button class="page-link" @click="currentPage += 1" aria-label="Next">
                                    <span aria-hidden="true">Next</span>
                                </button>
                            </li>
                            <li class="page-item" :class="{ disabled: currentPage === pageCount }">
                                <button class="page-link" @click="currentPage = pageCount" aria-label="Last page">
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
export default {
    props: {
        uniqueID: {
            type: String,
            default: () => {
                const affix = 'table';
                return `${affix}-${Math.random().toString(36).substring(7)}`;
            },
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
            required: true,
        },
        editable: {
            type: Boolean,
            required: true,
        },
        toggleable: {
            type: Boolean,
            required: true,
        }
    },
    data() {
        return {
            isLoading: true,
            currentPage: 1,
            maxVisiblePages: 10,
            rowsPerPage: 10,
            showAll: false,
            showTable: {},
            searchText: '',
            sortColumn: null,
            sortDirection: 'asc',
        };
    },
    computed: {
        paginatedMainItems() {
            const startIndex = (this.currentPage - 1) * this.rowsPerPage;
            const endIndex = startIndex + this.rowsPerPage;
            return this.mainItems.slice(startIndex, endIndex);
        },
        filteredItems() {
            const sortedItems = [...this.paginatedMainItems];

            sortedItems.sort((a, b) => {
                const aValue = a[this.sortColumn];
                const bValue = b[this.sortColumn];
                let bool = this.sortDirection === 1 ? true : false;
                if (!isNaN(aValue) && !isNaN(bValue)) {
                    // Sort numbers numerically
                    return bool ? parseFloat(aValue) - parseFloat(bValue) : parseFloat(bValue) - parseFloat(aValue);
                } else {
                    // Sort strings alphabetically
                    const aString = (aValue || '').toString().toLowerCase(); // Add check for undefined
                    const bString = (bValue || '').toString().toLowerCase(); // Add check for undefined
                    if (aString < bString) {
                        return bool ? -1 : 1;
                    } else if (aString > bString) {
                        return bool ? 1 : -1;
                    } else {
                        return 0;
                    }
                }
            });

            return sortedItems.map(o => {
                if (o) { // Add check for undefined
                    const searchCode = Object.values(o).join("~") + (o.items ? o.items.map(item => Object.values(item).join(" ")).join(", ") : []);
                    return {
                        ...o,
                        searchCode
                    };
                }
            }).filter(item => item.searchCode.toString().toLowerCase().includes(this.searchText.toLowerCase()));
        },
        pageCount() {
            return Math.ceil(this.mainItems.length / this.rowsPerPage);
        },
        visiblePages() {
            let startPage = 1;
            let endPage = this.pageCount;
            if (this.pageCount > this.maxVisiblePages) {
                const halfVisiblePages = Math.floor(this.maxVisiblePages / 2);
                startPage = Math.max(this.currentPage - halfVisiblePages, 1);
                endPage = startPage + this.maxVisiblePages - 1;
                if (endPage > this.pageCount) {
                    endPage = this.pageCount;
                    startPage = endPage - this.maxVisiblePages + 1;
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
        sort(field) {
            if (this.sortColumn === field) {
                this.sortDirection = -this.sortDirection;
            } else {
                this.sortColumn = field;
                this.sortDirection = 1
            }
        },

        toggleAll() {
            const propKey = `showTable`;
            const toggleKey = `showAll`;
            this[toggleKey] = !this[toggleKey];
            this.filteredItems.forEach((item) => {
                this[propKey] = Object.assign({}, this[propKey], { [item.id]: this[toggleKey] });
            });
        },

        toggleTable(id) {
            this.showTable[id] = !this.showTable[id];
        },
        formatDate(date) {
            const options = {
                month: '2-digit',
                day: '2-digit',
                year: 'numeric',
                hour: 'numeric',
                minute: 'numeric',
                second: 'numeric'
            };
            return new Intl.DateTimeFormat('en-US', options).format(date);
        },
        printSection() {
            // Add Bootstrap stylesheet to the head
            const bootstrapLink = document.createElement('link');
            bootstrapLink.rel = 'stylesheet';
            bootstrapLink.href = 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css';
            document.head.appendChild(bootstrapLink);

            // Set the media query for landscape printing
            const mediaQuery = '@media print{@page {size: legal landscape; margin:auto} .no-print{display: none;}}';
            const style = document.createElement('style');
            style.appendChild(document.createTextNode(mediaQuery));
            document.head.appendChild(style);

            // Get the dataTable section and create a new element to hold it
            const dataTable = document.getElementById(this.uniqueID);
            const printElement = document.createElement('div');
            printElement.appendChild(dataTable.cloneNode(true));

            // Hide everything else on the page except the printElement
            const bodyChildren = document.body.children;
            for (let i = 0; i < bodyChildren.length; i++) {
                if (bodyChildren[i] !== printElement) {
                    bodyChildren[i].classList.add('no-print');
                }
            }

            // Add the printElement to the body and call the print function
            document.body.appendChild(printElement);
            window.print();

            // Restore the original page state
            for (let i = 0; i < bodyChildren.length; i++) {
                bodyChildren[i].classList.remove('no-print');
            }
            document.head.removeChild(style);
            document.head.removeChild(bootstrapLink);
            document.body.removeChild(printElement);
        }

    },
};
</script>

  