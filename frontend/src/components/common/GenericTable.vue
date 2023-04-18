<template>
    <div>

        <div v-if="!mainItems.length" class="d-flex justify-content-center align-items-center mt-3">
            <div class="spinner-border" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>
        <div v-else>
            <div class="d-flex justify-content-between align-items-center mt-3">
                <p class="mb-0">
                    <label>Show <select v-model="rowsPerPage" aria-controls="example" class="form-input">
                            <option value="10">10</option>
                            <option value="25">25</option>
                            <option value="50">50</option>
                            <option value="100">100</option>
                        </select> entries</label>
                </p>
                <p class="mb-0">Search: <input type="text" class="form-input mt-2" v-model="searchText"></p>
            </div>

            <table class="table">
                <thead>
                    <tr>
                        <template v-for="(header, index) in mainHeaders" :key="index">
                            <th v-if="header.field === 'toggle'">
                                <button class="btn btn-sm btn-primary" @click="toggleAll()">
                                    <span v-if="showAll === false">+</span>
                                    <span v-else>-</span>
                                </button>
                            </th>
                            <th v-else @click="sort(header.field)" :class="{ 'sortable': header.sortable }">
                                {{ header.label }}
                                <span v-if="header.sortable" class="sort-icon">
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
                        <tr>
                            <td v-for="(header, index) in mainHeaders" :key="index">
                                <template v-if="header.field === 'isAvailable'">
                                    <span v-if="mainItem[header.field]">Yes</span>
                                    <span v-else>No</span>
                                </template>
                                <template v-else-if="header.field === 'toggle'">
                                    <button type="button" @click="toggleTable(mainItem.id)"
                                        class="btn btn-primary btn-sm toggle">
                                        <span v-if="!showTable[mainItem.id]">+</span>
                                        <span v-else>-</span>
                                    </button>
                                </template>
                                <template v-else-if="header.field === 'action' && this.editable">
                                    <button type="button" class="btn btn-primary btn-sm"
                                        @click="$emit('edit-action', mainItem.id)">
                                        <i class="fas fa-edit"></i>
                                    </button>
                                </template>
                                <template v-else>
                                    {{ mainItem[header.field] }}
                                </template>
                            </td>
                        </tr>
                        <tr v-if="showTable[mainItem.id]">
                            <td :colspan="mainHeaders.length + 1">
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
                                                    <td>{{ subItem[subHeader.field] }}</td>
                                                </template>
                                            </tr>
                                        </template>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </template>
                </tbody>
            </table>
            <div>

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
                    const searchCode = Object.values(o).join("~");
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
    },
};
</script>

  