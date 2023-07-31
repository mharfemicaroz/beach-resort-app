<template :key="componentKey">
  <TopNavBarComponent />
  <div class="container-fluid main">
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li v-if="userdata.role === 'superuser'" class="nav-item" role="presentation">
        <button class="nav-link" id="dashboard-tab" data-bs-toggle="tab" data-bs-target="#dashboard" type="button"
          role="tab" aria-controls="dashboard" aria-selected="true" @click="resetSummary(0)">Dashboard</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="booking-tab" data-bs-toggle="tab" data-bs-target="#booking" type="button"
          role="tab" aria-controls="booking" aria-selected="true" @click="resetSummary(1)">Calendar</button>
      </li>
      <li v-if="userdata.role !== 'reservationist'" class="nav-item" role="presentation">
        <button class="nav-link" id="monitor-tab" data-bs-toggle="tab" data-bs-target="#monitor" type="button" role="tab"
          aria-controls="monitor" aria-selected="false" @click="resetSummary(4)">Room Reservations</button>
      </li>
      <li v-if="userdata.role !== 'reservationist'" class="nav-item" role="presentation">
        <button class="nav-link" id="reception-tab" data-bs-toggle="tab" data-bs-target="#reception" type="button"
          role="tab" aria-controls="reception" aria-selected="false" @click="resetSummary(5)">Reception</button>
      </li>
      <li v-if="userdata.role !== 'reservationist'" class="nav-item" role="presentation">
        <button class="nav-link" id="others-tab" data-bs-toggle="tab" data-bs-target="#others" type="button" role="tab"
          aria-controls="others" aria-selected="false" @click="resetSummary(2)">Account</button>
      </li>
      <li v-if="userdata.role === 'superuser'" class="nav-item" role="presentation">
        <button class="nav-link" id="reports-tab" data-bs-toggle="tab" data-bs-target="#reports" type="button" role="tab"
          aria-controls="reports" aria-selected="false" @click="resetSummary(3)">Reports</button>
      </li>
    </ul>
    <div class="tab-content mt-3" id="myTabContent">
      <div v-if="userdata.role === 'superuser'" class="tab-pane fade" id="dashboard" role="tabpanel"
        aria-labelledby="dashboard-tab">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-12">
              <BookingDashboard :active="dashboardStatus" :key="componentKey" />
            </div>
          </div>
        </div>
      </div>
      <div class="tab-pane fade show active" id="booking" role="tabpanel" aria-labelledby="booking-tab">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-12">
              <div class="d-flex justify-content-between">
                <h2>Calendar <a href="#" class="btn btn-link text-decoration-none" @click="toggleSettingsModal()"><i
                      class="fa fa-bars" style="font-size: 1.25em;"></i></a></h2>
                <div class="form-outline col-md-3">
                  <input type="search" id="form1" class="form-control" placeholder="Type query" v-model="booksearchtext"
                    @input="populateCalendarItems" @click="showAutosuggestions = false" @blur="hideAutosuggestions"
                    aria-label="Search" ref="searchQuery" autocomplete="off" aria-autocomplete="off" />
                  <ul id="suglist" class="autosuggestions" v-if="!showAutosuggestions">
                    <li v-for="suggestion in autosuggestions" @click="selectSuggestion(suggestion)">{{ suggestion }}</li>
                  </ul>
                </div>
              </div>
              <div class="calendar-parent">
                <calendar-view :items="calendarItems" :show-date="showDate"
                  :time-format-options="{ hour: 'numeric', minute: '2-digit' }" :enable-drag-drop="true"
                  :disable-past="disablePast" :disable-future="disableFuture" :show-times="showTimes"
                  :date-classes="myDateClasses" :display-period-uom="displayPeriodUom"
                  :display-period-count="displayPeriodCount" :starting-day-of-week="startingDayOfWeek"
                  :class="themeClasses" :period-changed-callback="periodChanged"
                  :current-period-label="useTodayIcons ? 'icons' : ''" :displayWeekNumbers="displayWeekNumbers"
                  :enable-date-selection="true" :selection-start="selectionStart" :selection-end="selectionEnd"
                  @date-selection-start="setSelection" @date-selection="setSelection"
                  @date-selection-finish="finishSelection" @drop-on-date="onDrop" @click-date="onClickDay"
                  @click-item="onClickItem">
                  <template #header="{ headerProps }">
                    <calendar-view-header slot="header" :header-props="headerProps" @input="setShowDate" />
                  </template>
                </calendar-view>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="card" style="height: 60px!important;">
            </div>
          </div>
        </div>
      </div>
      <div class="tab-pane fade" id="monitor" role="tabpanel" aria-labelledby="monitor-tab">
        <div class="container-fluid">
          <div class="row">
            <div class="col-sm-2">
              <ul class="nav nav-tabs flex-column" id="propertyTab" role="tablist">
                <li class="nav-item">
                  <a class="nav-link active " data-bs-toggle="tab" @click="activeMainTab = 'BEACH ROOM'"
                    href="#beachroom">Beach Rooms</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link " data-bs-toggle="tab" @click="activeMainTab = 'POOL ROOM'" href="#poolrooms">Pool
                    Rooms</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link " data-bs-toggle="tab" @click="activeMainTab = 'POOL COTTAGE'"
                    href="#poolcottages">Pool Cottages</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-bs-toggle="tab" @click="activeMainTab = 'GAZEBO COTTAGE'"
                    href="#gazebocottages">Native Gazebo Cottages</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link " data-bs-toggle="tab" @click="activeMainTab = 'BEACH COTTAGE'"
                    href="#beachcottages">Beach Cottages (Day)</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link " data-bs-toggle="tab" @click="activeMainTab = 'N-BEACH COTTAGE'"
                    href="#nbeachcottages">Beach Cottages (Night)</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link " data-bs-toggle="tab" @click="activeMainTab = 'HALL'" href="#halls">Halls</a>
                </li>
              </ul>
            </div>
            <div class="col-sm-10">
              <div class="tab-content mt-3" id="propertyTabContent">
                <div class="tab-pane fade show active" id="beachroom" role="tabpanel" aria-labelledby="beachroom-tab">
                  <div class="container-fluid">
                    <div class="row">
                      <div class="col-md-12">
                        <CardBookingsVue :roomData="roomsjoinbookings" v-on:click-action="cardAction" />
                      </div>
                    </div>
                  </div>
                </div>
                <div class="tab-pane fade" id="poolrooms" role="tabpanel" aria-labelledby="poolroom-tab">
                  <div class="container-fluid">
                    <div class="row">
                      <div class="col-md-12">
                        <CardBookingsVue :roomData="roomsjoinbookings" v-on:click-action="cardAction" />
                      </div>
                    </div>
                  </div>
                </div>
                <div class="tab-pane fade" id="poolcottages" role="tabpanel" aria-labelledby="poolcottage-tab">
                  <div class="container-fluid">
                    <div class="row">
                      <div class="col-md-12">
                        <CardBookingsVue :roomData="roomsjoinbookings" v-on:click-action="cardAction" />
                      </div>
                    </div>
                  </div>
                </div>
                <div class="tab-pane fade" id="gazebocottages" role="tabpanel" aria-labelledby="gazebocottage-tab">
                  <div class="container-fluid">
                    <div class="row">
                      <div class="col-md-12">
                        <CardBookingsVue :roomData="roomsjoinbookings" v-on:click-action="cardAction" />
                      </div>
                    </div>
                  </div>
                </div>
                <div class="tab-pane fade" id="beachcottages" role="tabpanel" aria-labelledby="beachcottage-tab">
                  <div class="container-fluid bg-beachday">
                    <div class="row">
                      <div class="col-md-12">
                        <CardBookingsVue :roomData="roomsjoinbookings" v-on:click-action="cardAction" />
                      </div>
                    </div>
                  </div>
                </div>
                <div class="tab-pane fade" id="nbeachcottages" role="tabpanel" aria-labelledby="nbeachcottage-tab">
                  <div class="container-fluid">
                    <div class="row">
                      <div class="col-md-12">
                        <CardBookingsVue :roomData="roomsjoinbookings" v-on:click-action="cardAction" />
                      </div>
                    </div>
                  </div>
                </div>
                <div class="tab-pane fade" id="halls" role="tabpanel" aria-labelledby="halls-tab">
                  <div class="container-fluid">
                    <div class="row">
                      <div class="col-md-12">
                        <CardBookingsVue :roomData="roomsjoinbookings" v-on:click-action="cardAction" />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="tab-pane fade" id="reception" role="tabpanel" aria-labelledby="others-tab">
        <div class="container-fluid">
          <div class="row">
            <ReceptionHotel :bookingsdata="bookings" :roomsdata="rooms" @clickItem-action="handleReceptionItemAction"
              @clickDay-action="handleReceptionDayAction" @clickRoom-action="handleReceptionRoomAction" />
          </div>
        </div>
      </div>
      <div class="tab-pane fade" id="others" role="tabpanel" aria-labelledby="others-tab">
        <div class="container-fluid">
          <div class="row">
            <!-- <div class="col-md-3">
              <h2>Add-ons</h2>
              <input type="text" class="form-control mb-3" placeholder="Search item" v-model="searchText3">
              <div class="wrapper-content" :style="`height:${calcMeasure.height1}`">
                <table class="table" style="table-layout: fixed;word-wrap: break-word;">
                  <thead>
                    <tr>
                      <th style="white-space: nowrap;">Item</th>
                      <th>Qty</th>
                      <th>Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, index) in filteredItems" :key="index">
                      <td>{{ item.item }} ({{ item.priceRate }}/{{ item.counter }})</td>
                      <td>
                        <input style="width:75px!important" class="form-control input-sm" type="number"
                          v-model.number="howMany[index]">
                      </td>
                      <td>
                        <button class="btn btn-primary" @click="addToCart(item, index)" :disabled="!item.isAvailable">
                          <i class="fa fa-cart-plus"></i>
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div> -->
            <div class="col-md-3">
              <div class="d-flex align-items-center">
                <h2 class="position-relative">
                  Cart
                  <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger"
                    style="font-size: 0.75rem;">
                    {{ numItemCart }}
                    <span class="visually-hidden">items in cart</span>
                  </span>
                </h2>
                <div class="ms-auto d-flex align-items-center"> <!-- Wrap the buttons in a flex container -->
                  <button type="button" class="btn btn-primary me-2" :class="{ 'wiggle-animation': countInclusion === 0 }"
                    @click="showShoppingModal()">
                    <i class="fa fa-shopping-cart"><br>
                      <span style="font-size: 8px;">[F1]</span></i>
                  </button>
                  <button type="button" class="btn btn-primary" :class="{ 'wiggle-animation': countInclusion > 0 }"
                    @click="moveInclusionCartToMain()">
                    <i class="fas fa-thumbs-up" style="position: relative;"><br>
                      <span style="font-size: 8px;">[F2]</span>
                      <span class="position-absolute start-1000 translate-middle badge rounded-pill bg-danger"
                        style="font-size: 0.50rem; top: -25%; left: 120%;">
                        {{ countInclusion }}
                        <span class="visually-hidden">items in cart</span>
                      </span>
                    </i>
                  </button>
                </div>
              </div>
              <div class="card-deck"
                :style="`height:${calcMeasure.height2};overflow-y: auto;overflow-x: hidden;padding-right: 1px;`">
                <div class="card" v-for="(item, index) in cart.sort((a, b) => a.category.localeCompare(b.category))"
                  :key="item.id">
                  <div class="card-header d-flex justify-content-between align-items-center">
                    <h5 class="card-title">{{ item.name }} <span
                        v-html="(item.category === 'main') ? '<i class=\'fas fa-check text-success\'></i>' : '<i class=\'fas fa-hourglass-start text-warning\'></i>'"></span>
                    </h5>
                    <button v-if="item.category === 'inclusion'" type="button" class="btn btn-sm btn-close"
                      aria-label="Close" @click="cancelItem(item)"></button>
                  </div>
                  <div class="card-body">
                    <p class="card-text">Type: {{ item.type }}</p>
                    <p class="card-text">Price Rate: {{ item.priceRate }}</p>
                    <p class="card-text">Purchase Qty.:{{ item.purqty }}</p>
                    <p class="card-text">Total Price: {{ item.totalCartPrice }}</p>
                  </div>
                </div>
              </div>
            </div>
            <!-- <div class="col-md-3">
              <div class="d-flex align-items-center">
                <h2 class="position-relative">
                  Order Summary 
                  <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger"
                    style="font-size: 0.75rem;">
                    {{ numItemCart }}
                    <span class="visually-hidden">items in cart</span>
                  </span>
                </h2>
                <button v-if="this.itemIndex === -1" type="button" class="btn btn-primary ms-auto"
                  @click="toggleAddAccountModal()">
                  <i class="fa fa-plus"></i>
                </button>
              </div>
              <div class="card-deck wrapper-content" :style="`height:${calcMeasure.height3};`">
                <div class="card" v-for="(item, index) in combinedcart" :key="item.id">
                  <div class="card-header d-flex justify-content-between align-items-center">
                    <h5 class="card-title">{{ item.name }}</h5>
                    <button v-if="item.itemOption === 'addons' && userdata.role === 'superuser'" type="button"
                      class="btn btn-sm btn-close" aria-label="Close" @click="cancelItem(item)"></button>
                  </div>
                  <div class="card-body">
                    <p class="card-text">Type: {{ item.type }}</p>
                    <p class="card-text">Price Rate: {{ item.priceRate }}</p>
                    <p class="card-text">{{ (item.itemOption === 'room') ? `No. of Days: ${item.purqty}` : `Purchase Qty.:
                      ${item.purqty}` }}</p>
                    <p class="card-text">Total Price: {{ item.totalCartPrice }}</p>
                  </div>
                </div>
              </div>
            </div> -->
            <div class="col-md-6">
              <div class="d-flex align-items-center">
                <h2 class="position-relative">
                  Billing Statement (preview)
                </h2>
                <div class="ms-auto d-flex align-items-center"> <!-- Wrap the buttons in a flex container -->
                  <button type="button" class="btn btn-primary" v-show="this.isItNew"
                    v-if="!this.walkinStatus && !this.justDiscounted" @click="generateBillingStatement()">
                    <i class="fas fa-print"><br>
                      <span style="font-size: 8px;">[F10]</span></i>
                  </button>
                </div>
              </div>
              <!-- <div class="card">
                  <div class="card-body">
                    <span><strong>Name:</strong> {{ billing.clientName }}</span><br />
                    <span><strong>Email:</strong> {{ billing.clientEmail }}</span><br />
                    <span><strong>Phone:</strong> {{ billing.clientPhone }}</span><br />
                    <span><strong>Address:</strong> {{ billing.clientAddress }}</span>
                  </div>
                </div> -->
              <div id="billing-details-preview" class="bg-light"
                :style="`height:${calcMeasure.height3}!important;overflow-y: auto;overflow-x: hidden;font-size: 100%;padding: 20px;box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);`">
                <div class="container">
                  <div class="row">
                    <div class="col-12">
                      <div class="row justify-content-between">
                        <div class="col-4">
                          <img src="@/assets/pantukan-waterworld-logo.jpg" width="60" height="60" alt="Company Logo"
                            class="logo">
                        </div>
                        <div class="col-4 text-right">
                          <span style="font-size: small;">Billing Statement</span>
                          <p>Transaction No.: {{ this.billing.bookingID }}</p>
                        </div>
                      </div>
                      <hr style="margin-bottom: 0px; margin-top: 0px;">
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-12">
                      <div class="row">
                        <div class="col-6">
                          <span style="font-size: small;">Client Details:</span>
                          <p style="margin-bottom: 0px;">Name: {{ this.billing.clientName }}</p>
                          <p style="margin-bottom: 0px;">Email: {{ this.billing.clientEmail }}</p>
                          <p style="margin-bottom: 0px;">Contact No.: {{ this.billing.clientPhone }}</p>
                          <p style="margin-bottom: 0px;">Address: {{ this.billing.clientAddress }}</p>
                        </div>
                      </div>
                      <hr style="margin-bottom: 0px; margin-top: 0px;">
                      <div class="row">
                        <div class="col-12">
                          <span style="font-size: small;">Order Details:</span>
                          <table class="table">
                            <thead>
                              <tr>
                                <th>Item Name</th>
                                <th>Category</th>
                                <th>Rate</th>
                                <th>Qty</th>
                                <th>Total Cost</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr v-for="item in combinedcart" :key="item.id">
                                <td>{{ item.name }}</td>
                                <td>{{ item.type }}</td>
                                <td>{{ item.priceRate }}</td>
                                <td>{{ item.purqty }}</td>
                                <td v-if="item.itemOption !== 'room'">{{ item.totalCartPrice }}</td>
                                <td v-else>
                                  <span v-if="!isNaN(subroom.discountValue)"
                                    v-html="`${item.totalCartPrice} <sup class='text-danger font-weight-bold'>${(subroom.discountMode === 'percentage') ? (subroom.discountValue) + '%' : (subroom.discountValue / gbookingscount).toFixed(2)} off</sup> <span class='text-success font-weight-bold'>${(subroom.discountMode === 'percentage') ? item.totalCartPrice * (1 - parseFloat(subroom.discountValue / 100)) : item.totalCartPrice - (subroom.discountValue / gbookingscount).toFixed(2)}</span>`"></span>
                                  <span v-else v-html="`${item.totalCartPrice}`"></span>
                                </td>
                              </tr>
                              <tr>
                                <td colspan="4" class="text-right"><strong>Partial Payment:</strong></td>
                                <td class="text-danger"><strong>-Php {{ partialPayment }}</strong></td>
                              </tr>
                              <tr>
                                <td colspan="4" class="text-right"><strong>Total Due:</strong></td>
                                <td><strong>Php {{ total }}</strong></td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                      <hr style="margin-bottom: 0px; margin-top: 0px;">
                      <div class="row">
                        <div class="col-12">
                          <span style="font-size: small;">Account History:</span>
                          <table class="table">
                            <thead>
                              <tr>
                                <th>Date</th>
                                <th>Type</th>
                                <th>Invoice ID</th>
                                <th>Description</th>
                                <th>Amount</th>
                                <th>Balance</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr v-for="(item, index) in cashHistory" :key="item.id">
                                <td>
                                  {{ new Date(item.transaction_date).toLocaleDateString() }}, {{ getTime(new
                                    Date(item.transaction_date)) }}
                                </td>
                                <td>
                                  {{ item.paymentMethod }}
                                </td>
                                <td>
                                  {{ (item.nonCashReference.toString().replace("-", "") ===
                                    "") ? item.transactionrecord_id : item.transactionrecord_id + "-" +
                                    item.nonCashReference }}
                                </td>
                                <td>
                                  {{ (index === 0) ? 'Init/DP' : (parseFloat(item.balance) === 0) ? 'Full' : 'Partial'
                                  }}
                                </td>
                                <td>
                                  {{ item.cashAmountPay }}
                                </td>
                                <td>
                                  {{ item.balance }}
                                </td>
                              </tr>
                            </tbody>
                          </table>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-3" :style="`height:${calcMeasure.height4}!important;overflow-y: auto;overflow-x: hidden;`">
              <div class="d-flex align-items-center" style="padding:10px">
                <h2 class="position-relative">
                  Payment
                </h2>
                <div class="ms-auto d-flex align-items-center"> <!-- Wrap the buttons in a flex container -->
                  <button type="button" class="btn btn-primary" @click="placeOrder"
                    :disabled="total <= 0 || countInclusion > 0"
                    style="display: flex; flex-direction: column; align-items: center;">
                    <i class="fas fa-money-bill"></i>
                    <span style="font-size: 8px;">[Enter]</span>
                  </button>
                </div>
              </div>
              <div class="container">
                <div class="row">
                  <div class="col-12">
                    <form>
                      <!-- <div class="form-group">
                    <label for="paymentMethod">Payment method:</label>
                    <select class="form-control" id="paymentMethod" v-model="paymentMethod">
                      <option value="cash">Cash</option>
                      <option value="non-cash">Non-cash</option>
                    </select>
                  </div> -->
                      <!-- <div v-if="paymentMethod === 'non-cash'" class="form-group">
                    <label for="nonCashReference">Reference No.:</label>
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <select class="form-control selectpicker" data-style="btn-primary" data-width="fit"
                          v-model="nonCashPayPlatform">
                          <option value="">-- Please select --</option>
                          <option>GCash</option>
                          <option>PayMaya</option>
                          <option>Debit Card</option>
                          <option>Credit Card</option>
                          <option>Bank</option>
                        </select>
                      </div>
                      <input type="text" class="form-control" id="nonCashReference" v-model="nonCashReference">
                    </div>
                  </div> -->
                      <!-- <div class="form-group row mt-2">
                    <label for="name" class="col-sm-4 col-form-label">Dicount:</label>
                    <div class="col-sm-4">
                      <div v-if="alreadyDiscounted === false">
                        <select style="width: 100px;" class="form-control" id="discountMode" v-model="discountMode">
                          <option value="percentage">Percentage</option>
                          <option value="fixed">Fixed amount</option>
                        </select>
                      </div>
                    </div>
                    <div class="col-sm-4">
                      <input type="number" class="form-control" id="discountValue" v-model="discountValue">
                    </div>
                  </div> -->
                      <div class="form-group mb-2 mt-0">
                        <div class="input-group">
                          <input type="text" class="form-control" :value="this.billing.clientName" readonly>
                          <button type="button" class="btn btn-primary" @click="toggleAddAccountModal">
                            <i :class="(this.billing.clientName === '') ? 'fa fa-user-plus' : 'fas fa-user-edit'"></i>
                          </button>
                        </div>
                      </div>
                      <div class="form-group mb-2">
                        <div class="form-control p-3">
                          <div class="row mb-2 mb-0">
                            <div class="col-6">
                              <a href="#" @click="setTax">
                                <i class="fas fa-pencil-alt"></i>
                              </a>
                              <strong>Tax:</strong>
                            </div>
                            <div class="col-6 text-right">{{ taxValue }}</div>
                          </div>
                          <div class="row mt-0">
                            <div class="col-6">
                              <a href="#" @click="setDiscount" v-if="!alreadyDiscounted">
                                <i class="fas fa-pencil-alt"></i>
                              </a>
                              <strong>Discount:</strong>
                            </div>
                            <div class="col-6 text-right">{{ discountValue }}{{ (discountMode === 'percentage') ? '%' :
                              ' off'
                            }}</div>
                          </div>

                          <div class="row mb-2">
                            <div class="col-6"><strong>Reservation:</strong></div>
                            <div class="col-6 text-right" v-html="subroom.original + ' ' + subroom.discounted"></div>
                          </div>
                          <div class="row mb-2">
                            <div class="col-6"><strong>Add-ons:</strong></div>
                            <div class="col-6 text-right">{{ subaddons }}</div>
                          </div>

                          <div class="row mb-2" v-if="paymentMethod === 'non-cash'">
                            <div class="col-6"><strong>Reference No.:</strong></div>
                            <div class="col-6 text-right">{{ nonCashPayPlatform }} - {{ nonCashReference }}</div>
                          </div>
                          <div class="row mb-2">
                            <div class="col-6"><strong>Subtotal:</strong></div>
                            <div class="col-6 text-right">{{ subtotal }}</div>
                          </div>
                          <div class="row mb-2">
                            <div class="col-6"><strong>Partial:</strong></div>
                            <div class="col-6 text-right">{{ partialPayment }}</div>
                          </div>
                          <div class="row mb-0">
                            <div class="col-6"><strong class="text-primary">Total:</strong>
                            </div>
                            <div class="col-6 text-right"><strong>{{ total }}</strong></div>
                          </div>
                          <!-- <div class="row">
                        <div class="col-6"><strong style="font-size: 18px;">Change:</strong></div>
                        <div class="col-6 text-right text-danger" style="font-size: 18px;">{{ change }}</div>
                      </div> -->
                        </div>
                      </div>
                      <div class="form-group">
                        <div class="input-group">
                          <select id="payment-method" v-model="paymentMethod" class="form-control"
                            style="font-weight: bolder; " @change="setNonCash">
                            <option value="cash">Cash</option>
                            <option value="non-cash">Non-cash</option>
                          </select>
                          <span class="input-group-text">₱</span>
                          <input type="number" class="form-control" id="cashAmount" v-model.number="cashAmount"
                            step="0.01" @keyup="updateTotalCash" @keydown="updateTotalCash">
                          <span class="input-group-text">{{ (cashAmount - Math.floor(cashAmount)).toFixed(2).substr(1)
                          }}</span>
                        </div>
                      </div>
                      <div class="row mt-2 mb-2">
                        <div class="col-md-12">
                          <div class="row row-cols-1 row-cols-md-4">
                            <div class="col mb-1" v-for="item in cashDenominations" :key="item.id">
                              <button type="button"
                                class="btn bg-white rounded-lg shadow hover:shadow-xs focus:outline-none inline-block px-0 py-0 text-sm"
                                @click="addToCash(item.value)"><span>{{
                                  item.label }}</span></button>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="form-group">
                        <div class="input-group">
                          <span class="input-group-text">Remarks</span>
                          <input type="text" class="form-control" v-model="cashRemarks">
                        </div>
                      </div>
                      <div class="row mt-2 mb-2 bg-light">
                        <div class="col-md-6">
                          <dt v-if="change >= 0">Change: </dt>
                        </div>
                        <div class="col-md-6 d-flex flex-row-reverse">
                          <dd class="text-right h4 b"> ₱{{ change }} </dd>
                        </div>
                      </div>
                      <!-- 
                  <button v-show="this.isItNew" v-if="!this.walkinStatus" type="button" class="btn btn-primary"
                    @click="generateBillingStatement">Generate
                    BS</button>&nbsp; -->
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="tab-pane fade" id="reports" role="tabpanel" aria-labelledby="reports-tab">
        <div class="container-fluid">
          <div class="row">
            <div class="row">
              <div class="col-sm-1">
                <ul class="nav nav-tabs flex-column">
                  <li class="nav-item">
                    <a class="nav-link rotated-text active" data-bs-toggle="tab" href="#reservations">Reservations</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link rotated-text" data-bs-toggle="tab" href="#transactions">Transactions</a>
                  </li>
                </ul>
              </div>
              <div class="col-sm-11">
                <div class="tab-content">
                  <div id="reservations" class="tab-pane active">
                    <div class="row">
                      <div class="col-md-3">
                        <div>
                          <!-- <div class="form-group">
                            <label for="search">Search Reservation:</label>
                            <div class="input-group">
                              <div class="input-group-append">
                                <button class="btn btn-outline-secondary" type="button">
                                  <i class="fa fa-search"></i>
                                </button>
                              </div>
                              <input type="text" class="form-control" placeholder="Search reservation"
                                v-model="searchTerm2">
                            </div>
                          </div> -->
                          <div class="form-group">
                            <label for="date-filter">Date Filter:</label>
                            <select class="form-control" id="date-filter" v-model="resdateFilter">
                              <option value="any">Any</option>
                              <option value="range">Date Range</option>
                            </select>
                            <div v-if="resdateFilter === 'range'">
                              <div class="form-group">
                                <input type="date" class="form-control" v-model="resfromDate">
                              </div>
                              <div class="form-group">
                                <input type="date" class="form-control" v-model="restoDate">
                              </div>
                            </div>
                          </div>
                          <div class="form-group">
                            <label for="payment-method-filter">Payment Status:</label>
                            <select class="form-control" id="payment-method-filter" v-model="respaymentStatusFilter">
                              <option value="">Any</option>
                              <option value="no">No Payment</option>
                              <option value="partial">Partial</option>
                              <option value="yes">Full</option>
                            </select>
                          </div>
                          <div class="form-group">
                            <label for="status-filter">Status:</label>
                            <select class="form-control" id="status-filter" v-model="resstatusFilter">
                              <option value="">Any</option>
                              <option value="cancelled">Cancelled</option>
                              <option value="reserved">Reserved</option>
                              <option value="checkedin">Occupied</option>
                              <option value="checkedout">Checked Out</option>
                            </select>
                          </div>
                          <!-- <div class="form-group mt-2">
                            <button type="button" class="btn btn-primary"
                              @click="printReservationHistory">Print</button>&nbsp;
                          </div> -->
                        </div>
                      </div>
                      <div class="col-md-9">
                        <div id="reservationHistory">
                          <h2>Reservation History</h2>
                          <table-component :mainHeaders=reservationsOptions :mainItems="filteredReservationsHistory"
                            :editable="false" :toggleable="false" />
                        </div>
                      </div>
                    </div>
                  </div>
                  <div id="transactions" class="tab-pane">
                    <div class="row">
                      <div class="col-md-2">
                        <div>
                          <!-- <div class="form-group">
                            <label for="search">Search Transaction:</label>
                            <div class="input-group">
                              <div class="input-group-append">
                                <button class="btn btn-outline-secondary" type="button">
                                  <i class="fa fa-search"></i>
                                </button>
                              </div>
                              <input type="text" class="form-control" placeholder="Search transaction"
                                v-model="searchTerm" id="search">
                            </div>
                          </div> -->
                          <div class="form-group">
                            <label for="date-filter">Date Filter:</label>
                            <select class="form-control" id="date-filter" v-model="dateFilter">
                              <option value="any">Any</option>
                              <option value="range">Date Range</option>
                            </select>
                            <div v-if="dateFilter === 'range'">
                              <div class="form-group">
                                <input type="date" class="form-control" v-model="fromDate">
                              </div>
                              <div class="form-group">
                                <input type="date" class="form-control" v-model="toDate">
                              </div>
                            </div>
                          </div>
                          <div class="form-group">
                            <label for="payment-method-filter">Payment Method:</label>
                            <select class="form-control" id="payment-method-filter" v-model="paymentMethodFilter">
                              <option value="">Any</option>
                              <option value="cash">Cash</option>
                              <option value="non-cash">Non-cash</option>
                            </select>
                          </div>
                          <div class="form-group">
                            <label for="status-filter">Status:</label>
                            <select class="form-control" id="status-filter" v-model="statusFilter">
                              <option value="">Any</option>
                              <option value="full">Full</option>
                              <option value="partial">Partial</option>
                            </select>
                          </div>
                          <!-- <div class="form-group mt-2">
                            <button type="button" class="btn btn-primary"
                              @click="printTransactionHistory">Print</button>&nbsp;
                          </div> -->
                        </div>
                      </div>
                      <div class="col-md-10">
                        <div id="transactionHistory">
                          <h2>Transaction History</h2>
                          <table-component :mainHeaders=transactionsOptions :mainItems="filteredTransactions"
                            :subHeaders2="transactionhistory" :subHeaders="transactionitem"
                            @delete-action="deleteTransaction" :deletable="true" :editable="false" :toggleable="true" />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="card" style="height: 60px!important;">
              </div>
            </div>
          </div>
          <!-- <div class="row">
            <div class="col-md-6">
              <h2>Reservations Chart</h2>
              <div style="height:350px">
                <Line :data="linedata" :options="lineoptions" />
              </div>
            </div>
            <div class="col-md-6">
              <h2>Sales Chart</h2>
              <div style="height:350px">
                <Line :data="linedata" :options="lineoptions" />
              </div>
            </div>
          </div> -->
        </div>
      </div>
    </div>
    <div id="billing-details" class="container-fluid billing" style="font-size: 100%;">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="row justify-content-between" :style="!isThereLeisures ? 'border-right: dotted;' : ''">
              <div class="col-4">
                <img src="@/assets/pantukan-waterworld-logo.jpg" width="60" height="60" alt="Company Logo" class="logo">
              </div>
              <div class="col-4 text-right">
                <span style="font-size: small;">Billing Statement</span>
                <p>Transaction No.: {{ this.billing.bookingID }}</p>
              </div>
            </div>
            <hr>
          </div>
        </div>
        <div class="row">
          <div class="col-12" :style="!isThereLeisures ? 'border-right: dotted;' : ''">
            <div class="row">
              <div class="col-6">
                <span style="font-size: small;">Client Details:</span>
                <p>Name: {{ this.billing.clientName }}</p>
                <p>Email: {{ this.billing.clientEmail }}</p>
                <p>Contact No.: {{ this.billing.clientPhone }}</p>
                <p>Address.: {{ this.billing.clientAddress }}</p>
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-12">
                <span style="font-size: small;">Order Details:</span>
                <table border="1">
                  <thead>
                    <tr>
                      <th>Item Name</th>
                      <th>Category</th>
                      <th>Rate</th>
                      <th>Qty</th>
                      <th>Total Cost</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in combinedcart" :key="item.id">
                      <td>{{ item.name }}</td>
                      <td>{{ item.type }}</td>
                      <td>{{ item.priceRate }}</td>
                      <td>{{ item.purqty }}</td>
                      <td v-if="item.itemOption !== 'room'">{{ item.totalCartPrice }}</td>
                      <td v-else>
                        <span v-if="!isNaN(subroom.discountValue)"
                          v-html="`${item.totalCartPrice} <sup class='text-danger font-weight-bold'>${(subroom.discountMode === 'percentage') ? (subroom.discountValue) + '%' : (subroom.discountValue / gbookingscount).toFixed(2)} off</sup> <span class='text-success font-weight-bold'>${(subroom.discountMode === 'percentage') ? item.totalCartPrice * (1 - parseFloat(subroom.discountValue / 100)) : item.totalCartPrice - (subroom.discountValue / gbookingscount).toFixed(2)}</span>`"></span>
                        <span v-else v-html="`${item.totalCartPrice}`"></span>
                      </td>
                    </tr>
                    <tr>
                      <td colspan="4" class="text-right"><strong>Partial Payment:</strong></td>
                      <td class="text-danger"><strong>-Php {{ partialPayment }}</strong></td>
                    </tr>
                    <tr>
                      <td colspan="4" class="text-right"><strong>Total Due:</strong></td>
                      <td><strong>Php {{ total }}</strong></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-12">
                <span style="font-size: small;">Account History:</span>
                <table border="1">
                  <thead>
                    <tr>
                      <th>Date</th>
                      <th>Type</th>
                      <th>Invoice ID</th>
                      <th>Description</th>
                      <th>Amount</th>
                      <th>Balance</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, index) in cashHistory" :key="item.id">
                      <td>
                        {{ item.transaction_date }}
                      </td>
                      <td>
                        {{ item.paymentMethod }}
                      </td>
                      <td>
                        {{ (item.nonCashReference.toString().replace("-", "") ===
                          "") ? item.transactionrecord_id : item.transactionrecord_id + "-" + item.nonCashReference }}
                      </td>
                      <td>
                        {{ (index === 0) ? 'Init/DP' : (parseFloat(item.balance) === 0) ? 'Full' : 'Partial' }}
                      </td>
                      <td>
                        {{ item.cashAmountPay }}
                      </td>
                      <td>
                        {{ item.balance }}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-12">
                <span style="font-size: small;">Terms &amp; Conditions:</span>
                <p>1. Check-in time is at 2:00 PM. Check-out time is at 12:00 PM.</p>
                <p>2. Late check-out is subject to availability and may be charged an additional fee.</p>
                <p>3. Smoking is strictly prohibited inside the resort premises.</p>
                <p>4. Pets are not allowed inside the resort.</p>
                <p>5. Any damage or loss to the resort property will be charged to the guest.</p>
                <p>6. The resort reserves the right to refuse service to anyone.</p>
                <p>7. All rates are inclusive of taxes and service charge.</p>
                <p>8. Payment must be settled upon check-out.</p>
                <p>9. The resort is not responsible for any loss or damage to personal belongings.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div v-if="isThereLeisures" :class="isThereLeisures ? 'col-12' : 'col-0'">
            <span style="font-size: small;">WAIVER AND AGREEMENT TO LEASE WATER SPORTS</span>
            <p>The undersigned <span style="text-decoration: underline;">{{ this.billing.clientName }}</span> further
              states and affirms that he/she has been fully advised and thoroughly informed of the dangers of using WATER
              SPORTS. By fixing his/her signature hereunder, he/she attests and certifies that he/she is fully aware of
              such basic risks.</p>
            <p>The UNDERSIGND herein agrees and acknowledge that neither WATERWORLD PANTUKAN BEACH RESORT located at
              Mendoza,King-king, Pantukan Davao De oro nor any of its officers, employees and staff or representative may
              not be held responsible or liable in any way what so ever for any incident, mishap or other occurrence in
              connection with the use of the WATER SPORTS which may result in injury, death illness or other physical or
              mental damages to the undersigned or company.</p>
            <p>The UNDERSIGNED finally declares that he/she is of legal age and legally competent to sign this waiver and
              release: he/she has acquired the consent of his/her parents or guardians and that he/she fully completely
              agrees without any qualification or reservation having signed and same voluntary and or his/her own
              freewill.</p>
            <p>In witness thereof; this Waiver and Release is voluntary signed at <span
                style="text-decoration: underline;">WATER WORLD PANTUKAN BEACH RESORT</span> on this day of <span
                style="text-decoration: underline;">{{ currentDate }}</span></p>
            <hr>
            <div class="row">
              <div class="col-12">
                <span style="font-size: small;">Terms &amp; Conditions:</span>
                <p>1. Since water sport needs the skill and know-how of the operator, the lessee warrants that he/she can
                  properly operate the water sport.</p>
                <p>2. In no case shall Water Sport be used by any other person other than the lessee.</p>
                <p>3. The Water Sports shall be operated only 300 meters radius from the resort.</p>
                <p>4. In the event of any wrong use, abuse or negligence on the part of the lessee and the Water Sport
                  suffers any damage, the lessee/s hold himself/herself/themselves personally liable for the cost of
                  damage, repairs spare parts and loss on income.</p>
                <p>5. The lessee/s shall abide by all laws, rules and guidelines in the operation of Water Sports.</p>
                <p>6. Any untoward incident resulting to the Operation of Water Sports</p>
                <p>7. Never start the engine if you are less than 3 feet deep. Otherwise, pebbles and sands could be
                  sucked into the jet intake, causing impelled damage.</p>
                <p>8. Your are advised to slow down if you are still on the shallow area.</p>
                <p>9. Be careful with the swimmers, boat, people, sharp objects, ropes and floating debris.</p>
                <p>10. Observed distance to any WATER SPORTS to prevent any collision.</p>
                <p>11. The lessor has the right to stop the operation of the WATERN SPORT and the amount paid or deposit
                  shall be forfeited if the rules and regulations are not followed accordingly.</p>
                <p>12. No one is allowed to operate the WATER SPORTS if the person is under the influence of liquor/drugs.
                </p>
                <p>13. Upon signing hereof, the lessee/s hereby agree/s to all the above terms and conditions.</p>
              </div>
            </div>
            <div class="row">
              <div class="col-12">
                <span style="font-size: small;">List of Participants with Signature:</span>
                <table border="0" cellpadding="0" cellspcing="0">
                  <tr>
                    <td>
                      <p>1. <span style="text-decoration: underline;">{{ this.billing.clientName }}</span> </p>
                      <p>2._____________________________ </p>
                      <p>3._____________________________ </p>
                      <p>4._____________________________ </p>
                      <p>5._____________________________ </p>
                    </td>
                    <td>
                      <p>6._____________________________ </p>
                      <p>7._____________________________ </p>
                      <p>8._____________________________ </p>
                      <p>9._____________________________ </p>
                      <p>10._____________________________ </p>
                    </td>
                  </tr>
                </table>
              </div>
            </div>
          </div>
        </div>
        <div class="row mt-2">
          <div class="col-12" :style="!isThereLeisures ? 'border-right: dotted;' : ''">
            <hr>
            <div class="row">
              <div class="col-6">
                <span style="font-size: small;">Check-In Staff Signature:</span>
              </div>
              <div class="col-6 text-right">
                <span style="font-size: small;">Customer Signature:</span>
                <p class="mt-2">Date: {{ currentDate }}</p>
              </div>
            </div>
            <hr style="border-bottom: dotted;" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- Modals -->
  <div class="modal fade show" id="showall-modal" tabindex="-1" role="dialog" aria-labelledby="showall-modalLabel"
    style="display: none; padding-right: 17px;" aria-modal="true">
    <div class="modal-dialog modal-xl" style="max-width: 1200px!important;" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="showall-modalLabel">Room Status</h4>
          <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
        </div>
        <div class="modal-body">
          <ul class="nav nav-tabs" id="roomTab" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="cancelled-tab" data-bs-toggle="tab" data-bs-target="#cancelled" type="button"
                role="tab" aria-controls="cancelled" aria-selected="true"
                @click="activeTab = 'cancelled'">Cancelled</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="reserved-tab" data-bs-toggle="tab" data-bs-target="#reserved" type="button"
                role="tab" aria-controls="reserved" aria-selected="true" @click="activeTab = 'reserved'">Reserved</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="occupied-tab" data-bs-toggle="tab" data-bs-target="#occupied" type="button"
                role="tab" aria-controls="occupied" aria-selected="false"
                @click="activeTab = 'occupied'">Occupied</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="checkedout-tab" data-bs-toggle="tab" data-bs-target="#checkedout" type="button"
                role="tab" aria-controls="checkedout" aria-selected="false" @click="activeTab = 'checkedout'">Checked
                Out</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="all-tab" data-bs-toggle="tab" data-bs-target="#all" type="button"
                role="tab" aria-controls="all" aria-selected="false" @click="activeTab = 'all'">All</button>
            </li>
          </ul>
          <div class="tab-content mt-3" id="roomTabContent">
            <div class="tab-pane fade" :class="{ 'show active': activeTab === 'cancelled' }" id="cancelled"
              role="tabpanel" aria-labelledby="cancelled-tab">
              <div class="container-fluid">
                <table-component :mainHeaders=bookingsOptions :mainItems="filteredRoomBookings" :editable="false"
                  :toggleable="false" />
                <!-- <table class="table" style="table-layout: fixed;word-wrap: break-word;">
                  <thead>
                    <tr>
                      <th>Room Name</th>
                      <th>Checkin Date</th>
                      <th>Checkout Date</th>
                      <th>Guest</th>
                      <th>Contact Number</th>
                      <th>Email</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="reservation in filteredRoomBookings" :key="reservation.id">
                      <td>{{ reservation.room_name }}</td>
                      <td>{{ reservation.checkinDate }}</td>
                      <td>{{ reservation.checkoutDate }}</td>
                      <td>{{ reservation.name }}</td>
                      <td>{{ reservation.contactNumber }}</td>
                      <td>{{ reservation.clientemail }}</td>
                    </tr>
                  </tbody>
                </table> -->
              </div>
            </div>
            <div class="tab-pane fade" :class="{ 'show active': activeTab === 'reserved' }" id="reserved" role="tabpanel"
              aria-labelledby="reserved-tab">
              <div class="container-fluid">
                <table-component :mainHeaders=bookingsOptions :mainItems="filteredRoomBookings" :editable="false"
                  :toggleable="false" />
                <!-- <table class="table" style="table-layout: fixed;word-wrap: break-word;">
                  <thead>
                    <tr>
                      <th>Room Name</th>
                      <th>Checkin Date</th>
                      <th>Checkout Date</th>
                      <th>Guest</th>
                      <th>Contact Number</th>
                      <th>Email</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="reservation in filteredRoomBookings" :key="reservation.id">
                      <td>{{ reservation.room_name }}</td>
                      <td>{{ reservation.checkinDate }}</td>
                      <td>{{ reservation.checkoutDate }}</td>
                      <td>{{ reservation.name }}</td>
                      <td>{{ reservation.contactNumber }}</td>
                      <td>{{ reservation.clientemail }}</td>
                    </tr>
                  </tbody>
                </table> -->
              </div>
            </div>
            <div class="tab-pane fade" :class="{ 'show active': activeTab === 'occupied' }" id="occupied" role="tabpanel"
              aria-labelledby="occupied-tab">
              <div class="container-fluid">
                <table-component :mainHeaders=bookingsOptions :mainItems="filteredRoomBookings" :editable="false"
                  :toggleable="false" />
                <!-- <table class="table" style="table-layout: fixed;word-wrap: break-word;">
                  <thead>
                    <tr>
                      <th>Room Name</th>
                      <th>Checkin Date</th>
                      <th>Checkout Date</th>
                      <th>Guest</th>
                      <th>Contact Number</th>
                      <th>Email</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="reservation in filteredRoomBookings" :key="reservation.id">
                      <td>{{ reservation.room_name }}</td>
                      <td>{{ reservation.checkinDate }}</td>
                      <td>{{ reservation.checkoutDate }}</td>
                      <td>{{ reservation.name }}</td>
                      <td>{{ reservation.contactNumber }}</td>
                      <td>{{ reservation.clientemail }}</td>
                    </tr>
                  </tbody>
                </table> -->
              </div>
            </div>
            <div class="tab-pane fade" :class="{ 'show active': activeTab === 'checkedout' }" id="checkedout"
              role="tabpanel" aria-labelledby="checkedout-tab">
              <div class="container-fluid">
                <table-component :mainHeaders=bookingsOptions :mainItems="filteredRoomBookings" :editable="false"
                  :toggleable="false" />
                <!-- <table class="table" style="table-layout: fixed;word-wrap: break-word;">
                  <thead>
                    <tr>
                      <th>Room Name</th>
                      <th>Checkin Date</th>
                      <th>Checkout Date</th>
                      <th>Guest</th>
                      <th>Contact Number</th>
                      <th>Email</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="reservation in filteredRoomBookings" :key="reservation.id">
                      <td>{{ reservation.room_name }}</td>
                      <td>{{ reservation.checkinDate }}</td>
                      <td>{{ reservation.checkoutDate }}</td>
                      <td>{{ reservation.name }}</td>
                      <td>{{ reservation.contactNumber }}</td>
                      <td>{{ reservation.clientemail }}</td>
                    </tr>
                  </tbody>
                </table> -->
              </div>
            </div>
            <div class="tab-pane fade" :class="{ 'show active': activeTab === 'all' }" id="all" role="tabpanel"
              aria-labelledby="all-tab">
              <div class="container-fluid">
                <table-component :mainHeaders=bookingsAllOptions :mainItems="filteredRoomBookings" :editable="false"
                  :toggleable="false">
                  <template #content="data">
                    <!-- {{ data.data.id  }} -->
                  </template>
                </table-component>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade show" id="addAccountModal" tabindex="-1" role="dialog" aria-labelledby="addAccountModalLabel"
    style="display: none; padding-right: 17px;" aria-modal="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="addAccountModalLabel">Add Account</h4>
          <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="addWalkInGuest">
            <!-- Client Information -->
            <div class="form-group row">
              <label for="name" class="col-sm-2 col-form-label">Name:*</label>
              <div class="col-sm-4">
                <input type="text" class="form-control" id="name" v-model="walkinreservation.clientName" required
                  autocomplete="off">
              </div>
              <label for="email" class="col-sm-2 col-form-label">Email:</label>
              <div class="col-sm-4">
                <input type="email" class="form-control" id="email" v-model="walkinreservation.clientEmail"
                  autocomplete="off">
              </div>
            </div>
            <div class="form-group row">
              <label for="address" class="col-sm-2 col-form-label">Address:</label>
              <div class="col-sm-4">
                <input type="text" class="form-control" id="address" v-model="walkinreservation.clientAddress"
                  autocomplete="off">
              </div>
              <label for="phone" class="col-sm-2 col-form-label">Phone:</label>
              <div class="col-sm-4">
                <input type="tel" class="form-control" id="phone" v-model="walkinreservation.clientPhone"
                  autocomplete="off">
              </div>
            </div>
            <div class="form-group row">
              <label for="nationality" class="col-sm-2 col-form-label">Nationality:*</label>
              <div class="col-sm-4">
                <select class="form-control" id="nationality" v-model="walkinreservation.clientNationality" required>
                  <option value="">-- Please select --</option>
                  <option value="Filipino">Filipino</option>
                  <option value="Foreign">Foreign</option>
                </select>
              </div>
              <label for="clientType" class="col-sm-2 col-form-label">Type:*</label>
              <div class="col-sm-4">
                <select class="form-control" id="clientType" v-model="walkinreservation.clientType" required>
                  <option value="">-- Please select --</option>
                  <option value="walkin">Walk-in</option>
                </select>
              </div>
            </div>
            <div class="form-group row">
              <div class="mt-3 mb-3 d-flex flex-row-reverse">
                <button type="submit" class="btn btn-primary">Add</button>&nbsp;
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade show" id="settings-modal" tabindex="-1" role="dialog" aria-labelledby="settings-modalLabel"
    style="display: none; padding-right: 17px;" aria-modal="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="settings-modalLabel">Settings</h4>
          <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label class="form-label">Period UOM</label>
                <div class="input-group">
                  <select class="form-select" v-model="displayPeriodUom">
                    <option>month</option>
                    <option>week</option>
                    <option>year</option>
                  </select>
                </div>
              </div>
              <div class="form-group">
                <label class="form-label">Period Count</label>
                <div class="input-group">
                  <select class="form-select" v-model="displayPeriodCount">
                    <option :value="1">1</option>
                    <option :value="2">2</option>
                    <option :value="3">3</option>
                  </select>
                </div>
              </div>
              <div class="form-group">
                <label class="form-label">Starting day of the week</label>
                <div class="input-group">
                  <select class="form-select" v-model="startingDayOfWeek">
                    <option v-for="(d, index) in dayNames" :key="index" :value="index">
                      {{ d }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="form-group form-check">
                <input class="form-check-input" type="checkbox" v-model="useTodayIcons" />
                <label class="form-check-label">Use icon for today's period</label>
              </div>
              <div class="form-group form-check">
                <input class="form-check-input" type="checkbox" v-model="displayWeekNumbers" />
                <label class="form-check-label">Show week number</label>
              </div>
              <div class="form-group form-check">
                <input class="form-check-input" type="checkbox" v-model="showTimes" />
                <label class="form-check-label">Show times</label>
              </div>
              <div class="form-group">
                <label class="form-label">Themes</label>
              </div>
              <div class="form-group form-check">
                <input class="form-check-input" type="checkbox" v-model="useDefaultTheme" />
                <label class="form-check-label">Default</label>
              </div>
              <div class="form-group form-check">
                <input class="form-check-input" type="checkbox" v-model="useHolidayTheme" />
                <label class="form-check-label">Holidays</label>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <table class="table" style="table-layout: fixed;word-wrap: break-word;">
                  <thead>
                    <tr>
                      <th scope="col">Status</th>
                      <th scope="col">Color</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Cancelled</td>
                      <td style="background-color: #bdbdbd; width: 25px;"></td>
                    </tr>
                    <tr>
                      <td>Reserved</td>
                      <td style="background-color: #ef5350; width: 25px;"></td>
                    </tr>
                    <tr>
                      <td>Reserved (partially paid)</td>
                      <td style="background-color: #5c6bc0; width: 25px;"></td>
                    </tr>
                    <tr>
                      <td>Checked In</td>
                      <td style="background-color: #66bb6a; width: 25px;"></td>
                    </tr>
                    <tr>
                      <td>Checked In (partially paid)</td>
                      <td style="background-color: #42a5f5; width: 25px;"></td>
                    </tr>
                    <tr>
                      <td>Checked In (paid)</td>
                      <td style="background-color: #ffee58; width: 25px;"></td>
                    </tr>
                    <tr>
                      <td>Checked Out (paid)</td>
                      <td style="background-color: #ff7043; width: 25px;"></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade come-from-modal left" id="shopModal" tabindex="-1" aria-labelledby="shopModalLabel"
    aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="shopModalLabel">Add-ons
          </h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-12">

              <input type="text" class="form-control mb-3" placeholder="Search item" v-model="searchText3">
              <div class="wrapper-content">
                <table class="table" style="table-layout: fixed;word-wrap: break-word;">
                  <thead>
                    <tr>
                      <th style="white-space: nowrap;">Item</th>
                      <th>Qty</th>
                      <th>Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, index) in filteredItems" :key="index">
                      <td>{{ item.item }} ({{ item.priceRate }}/{{ item.counter }})</td>
                      <td>
                        <input style="width:75px!important" class="form-control input-sm" type="number"
                          v-model.number="howMany[index]">
                      </td>
                      <td>
                        <button class="btn btn-primary" @click="addToCart(item, index)" :disabled="!item.isAvailable">
                          <i class="fa fa-cart-plus"></i>
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="dayMenuModal" tabindex="-1" aria-labelledby="dayMenuModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-sm modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="dayMenuModalLabel">Room Reservation for {{ dayreserve.toLocaleDateString('en-GB') }}
          </h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-6">
              <a href="#" @click="clickDay" class="d-flex flex-column align-items-center">
                <i class="fa fa-calendar-plus"></i>
                <span>Create</span>
              </a>
            </div>
            <div class="col-md-6">
              <a href="#" @click="viewAllReservation" class="d-flex flex-column align-items-center">
                <i class="fa fa-calendar-check"></i>
                <span>View</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade show" id="BookDayModal" tabindex="-1" role="dialog" aria-labelledby="BookDayModalLabel"
    style="display: none; padding-right: 17px;" aria-modal="true" ref="modal">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 id="BookDayModalLabel" class="text-primary">Reservation Info</h4>
          <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close"><span
              aria-hidden="true">&times;</span></button>
        </div>
        <div class="modal-body">
          <div v-if="!movetocartFlag || !bookNowFlag" class="loading-spinner">
            <div class="spinner-border text-primary" role="status">
              <span class="visually-hidden"></span>
            </div>
            <p class="loading-text h5">Loading...(Do not click anywhere!)</p>
          </div>
          <form v-else>
            <!-- Client Information -->
            <h5>Booking Details<span class="text-muted" style="font-size: 12px;">*Field required</span></h5>
            <div class="form-group row">
              <label for="name" class="col-sm-2 col-form-label">Name:*</label>
              <div class="col-sm-4">
                <input type="text" class="form-control" id="name" v-model="reservation.clientName" required
                  autocomplete="off">
              </div>
              <label for="email" class="col-sm-2 col-form-label">Email:</label>
              <div class="col-sm-4">
                <input type="email" class="form-control" id="email" v-model="reservation.clientEmail" autocomplete="off">
              </div>
            </div>
            <div class="form-group row mt-2">
              <label for="address" class="col-sm-2 col-form-label">Address:</label>
              <div class="col-sm-4">
                <input type="text" class="form-control" id="address" v-model="reservation.clientAddress"
                  autocomplete="off">
              </div>
              <label for="phone" class="col-sm-2 col-form-label">Phone:</label>
              <div class="col-sm-4">
                <input type="tel" class="form-control" id="phone" v-model="reservation.clientPhone" autocomplete="off">
              </div>
            </div>
            <div class="form-group row mt-2">
              <label for="nationality" class="col-sm-2 col-form-label">Nationality:*</label>
              <div class="col-sm-4">
                <select class="form-control" id="nationality" v-model="reservation.clientNationality" required>
                  <option value="">-- Please select --</option>
                  <option value="Filipino">Filipino</option>
                  <option value="Foreign">Foreign</option>
                </select>
              </div>
              <label for="clientType" class="col-sm-2 col-form-label">Type:*</label>
              <div class="col-sm-4">
                <select class="form-control" id="clientType" v-model="reservation.clientType" required>
                  <option value="">-- Please select --</option>
                  <option value="in-house">In-house</option>
                </select>
              </div>
            </div>
            <div class="form-group row mt-2">
              <label for="checkin" class="col-sm-2 col-form-label">Check-in Date:*</label>
              <div class="col-sm-4">
                <input type="text" aria-describedby="inputhelp" class="form-control mb-0" id="checkin"
                  v-model="reservation.checkinDate" required readonly>
              </div>
              <label for="checkout" class="col-sm-2 col-form-label">Check-out Date:*</label>
              <div class="col-sm-4">
                <input v-if="reservation.status == 'vacant'" aria-describedby="inputhelp2" type="date"
                  class="form-control" id="checkout" v-model="reservation.checkoutDate" required>
                <input v-else type="text" class="form-control" id="checkout" v-model="reservation.checkoutDate" readonly>
                <small v-if="reservation.status == 'vacant'" id="inputhelp2" class="form-text text-muted mt-0"
                  style="font-size: 11px;">Please enter the date in the format: DD/MM/YYYY.</small>
              </div>
            </div>
            <div class="form-group row mt-2">
              <label for="room" class="col-sm-2 col-form-label">Room:*</label>
              <div v-if="reservation.status === 'vacant' || toggleselect" class="col-sm-4">
                <v-select :disabled="roomSelect !== 'ok'" aria-describedby="inputhelp3" :multiple="!toggleselect"
                  :options="updatedRooms" label="name" v-model="reservation.roomName" required>
                  <template #option="{ name, type, price }">
                    <h6 style="margin: 0">{{ name }}</h6>
                    <em><small>{{ type }}</small></em>
                    <em><small> ({{ price }} units)</small></em>
                  </template>
                </v-select>
                <small v-if="toggleselect" id="inputhelp3" class="form-text text-muted mt-0">Please select a new
                  room.</small>
              </div>
              <div v-else class="col-sm-4">
                <input type="text" class="form-control" v-model="reservation.roomName" readonly>
              </div>
              <label for="remarks" class="col-sm-2 col-form-label">Remarks:</label>
              <div class="col-sm-4">
                <input type="text" class="form-control" v-model="reservation.remarks" autocomplete="off">
              </div>
            </div>
            <div class="form-group row mt-2">
              <div class="mt-3 mb-3 d-flex justify-content-end">
                <div v-if="reservation.status == 'reserved'">
                  <button v-if="reservation.isPaid === 'no'" v-show="!toggleselect" type="button"
                    class="btn btn-primary btn-sm btn-margin rounded" @click="cancelReservation()">
                    <i class="fas fa-times"></i> Cancel Reservation
                  </button>
                  <span v-if="userdata.role !== 'reservationist'">
                    <button :disabled="disablebutton" v-show="!toggleselect"
                      v-if="reservation.isPaid === '' || reservation.isPaid === 'no'"
                      @click="moveToCart(); disablebutton = true" type="button"
                      class="btn btn-success btn-sm btn-margin rounded">
                      <i class="fas fa-check"></i> Down Payment
                    </button>
                    <button :disabled="disablebutton" v-show="!toggleselect" v-else-if="reservation.isPaid === 'partial'"
                      @click="moveToCart(); disablebutton = true" type="button"
                      class="btn btn-warning btn-sm btn-margin rounded">
                      <i class="fas fa-check"></i> Partial Payment
                    </button>
                    <button :disabled="disablebutton" v-show="!toggleselect" v-else-if="reservation.isPaid === 'yes'"
                      @click="moveToCart(); disablebutton = true" type="button"
                      class="btn btn-primary btn-sm btn-margin rounded">
                      <i class="fas fa-eye"></i> View Summary
                    </button>
                    <button :disabled="disablebutton" v-show="!toggleselect"
                      v-if="new Date().setHours(0, 0, 0, 0) === parseDate2(reservation.checkinDate)" type="button"
                      class="btn btn-success btn-sm btn-margin rounded" @click="checkinGuest(); disablebutton = true">
                      <i class="fas fa-sign-in-alt"></i> Check-in
                    </button>
                  </span>
                </div>
                <div v-else-if="reservation.status == 'checkedin'">
                  <span v-if="userdata.role !== 'reservationist'">
                    <div v-if="reservation.isPaid === '' || reservation.isPaid === 'no'">
                      <button :disabled="disablebutton" v-show="!toggleselect" @click="moveToCart(); disablebutton = true"
                        type="button" class="btn btn-success btn-sm btn-margin rounded">
                        <i class="fas fa-credit-card"></i> Pay Now
                      </button>
                    </div>
                    <div v-else-if="reservation.isPaid === 'partial'">
                      <button :disabled="disablebutton" v-show="!toggleselect" @click="moveToCart(); disablebutton = true"
                        type="button" class="btn btn-success btn-sm btn-margin rounded">
                        <i class="fas fa-credit-card"></i> Pay Now
                      </button>
                      <button :disabled="disablebutton" v-show="!toggleselect" type="button"
                        class="btn btn-primary btn-sm btn-margin rounded" @click="extendBooking(); disablebutton = true">
                        <i class="fas fa-calendar-plus"></i> Extend (1 day)
                      </button>
                    </div>
                    <div v-else>
                      <button :disabled="disablebutton" v-show="!toggleselect" type="button"
                        class="btn btn-primary btn-sm btn-margin rounded" @click="viewSummary(); disablebutton = true">
                        <i class="fas fa-eye"></i> View Summary
                      </button>
                      <button :disabled="disablebutton" v-show="!toggleselect" type="button"
                        class="btn btn-primary btn-sm btn-margin rounded" @click="extendBooking(); disablebutton = true">
                        <i class="fas fa-calendar-plus"></i> Extend (1 day)
                      </button>
                      <button :disabled="disablebutton" v-show="!toggleselect" type="button"
                        class="btn btn-success btn-sm btn-margin rounded" @click="checkOutGuest(); disablebutton = true">
                        <i class="fas fa-sign-out-alt"></i> Check-out
                      </button>
                    </div>
                  </span>
                </div>
                <button :disabled="disablebutton" @click="clickTestAddItem(); disablebutton = true"
                  v-else-if="reservation.status == 'vacant'" type="button"
                  class="btn btn-primary btn-sm btn-margin rounded">
                  <i class="fas fa-book"></i> Book Now
                </button>
                <button
                  v-if="new Date().setHours(0, 0, 0, 0) <= parseDate2(reservation.checkinDate) && userdata.role !== 'reservationist' && (reservation.status !== 'vacant' && reservation.status !== 'checkedout' && reservation.status !== 'cancelled')"
                  @click="transferRoom()" type="button" class="btn btn-success btn-sm btn-margin rounded">
                  <i class="fas fa-exchange-alt"></i> {{ toggleselect ? 'Save' : 'Transfer' }}
                </button>
                <button :disabled="disablebutton"
                  v-if="userdata.role !== 'reservationist' && reservation.status !== 'vacant'" type="button"
                  @click="voidBook(); disablebutton = true" class="btn btn-danger btn-sm btn-margin rounded"
                  v-show="!toggleselect">
                  <i class="fas fa-trash"></i> Void
                </button>
                <button :disabled="disablebutton" @click="disablebutton = true" type="button"
                  class="btn btn-danger btn-sm btn-margin rounded" data-bs-dismiss="modal">
                  <i class="fas fa-times"></i> Close
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <vue-simple-context-menu element-id="myFirstMenu" :options="optionsArray1" ref="vueSimpleContextMenu1"
    @option-clicked="optionClicked1">
  </vue-simple-context-menu>
  <FooterComponent />
</template>
<script>
import { useAuthStore } from "@/stores/authStore";
import TopNavBarComponent from "@/components/common/TopNavBar.vue";
import FooterComponent from "../common/FooterComponent.vue";
import TableComponent from "@/components/common/GenericTable.vue";
import BookingDashboard from "@/components/common/BookingDashboard.vue";
import CardBookingsVue from "../common/CardBookings.vue";
import ReceptionHotel from "../common/ReceptionHotel.vue";
import "/node_modules/vue-simple-calendar/dist/style.css"
import "/node_modules/vue-simple-calendar/dist/css/default.css"
import "/node_modules/vue-simple-calendar/dist/css/holidays-us.css"
import "/node_modules/vue-final-modal/dist/style.css"
import moment from 'moment'
import jsPDF from "jspdf";
import axios from 'axios';
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
import { CalendarView, CalendarViewHeader, CalendarMath } from "vue-simple-calendar" // published version
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)
//helper functions
function parseDate(dateString) {
  const [day, month, year] = dateString.split('/');
  return new Date(`${year}-${month}-${day}`).setHours(0, 0, 0, 0);
}
function parseDate2(dateString) {
  const index = dateString.indexOf('T');
  const result = dateString.substring(0, index);
  const [year, month, day] = result.split('-');
  return new Date(`${year}-${month}-${day}`).setHours(0, 0, 0, 0);
}
function padTo2Digits(num) {
  return num.toString().padStart(2, '0');
}
function formatDate(date = new Date()) {
  return [
    date.getFullYear(),
    padTo2Digits(date.getMonth() + 1),
    padTo2Digits(date.getDate()),
  ].join('-');
}
function formatDate2(date = new Date()) {
  let inputDate = date;
  let dateObj = new Date(inputDate);
  let day = dateObj.getDate().toString().padStart(2, "0");
  let month = (dateObj.getMonth() + 1).toString().padStart(2, "0");
  let year = dateObj.getFullYear().toString();
  let outputDate = `${day}/${month}/${year}`;
  return outputDate;
}
export default {
  components: {
    Line,
    CalendarView,
    CalendarViewHeader,
    TopNavBarComponent,
    FooterComponent,
    TableComponent,
    BookingDashboard,
    CardBookingsVue,
    ReceptionHotel,
  },
  data() {
    return {
      justDiscounted: false,
      gbookingscount: 0,
      activeAccountFlag: false,
      movetocartFlag: true,
      bookNowFlag: true,
      socket: null,
      test: '',
      dashboardStatus: true,
      bookingComponentStatus: true,
      componentKey: 0,
      activeMainTab: 'BEACH ROOM',
      roomSelect: "ok",
      toggleselect: false,
      isItNew: false,
      disablebutton: false,
      bookingsOptions: [{
        'label': 'Room Name',
        'field': 'room_name',
        'sortable': true
      }, {
        'label': 'Checkin Date',
        'field': 'checkinDate',
        'sortable': true
      }, {
        'label': 'Checkout Date',
        'field': 'checkoutDate',
        'sortable': true
      }, {
        'label': 'Guest',
        'field': 'name',
        'sortable': true
      }, {
        'label': 'Contact Number',
        'field': 'contactNumber',
        'sortable': true
      }, {
        'label': 'Email',
        'field': 'clientemail',
        'sortable': true
      },],
      bookingsAllOptions: [{
        'label': 'Room Name',
        'field': 'room_name',
        'sortable': true
      }, {
        'label': 'Checkin Date',
        'field': 'checkinDate',
        'sortable': true
      }, {
        'label': 'Checkout Date',
        'field': 'checkoutDate',
        'sortable': true
      }, {
        'label': 'Guest',
        'field': 'name',
        'sortable': true
      }, {
        'label': 'Contact Number',
        'field': 'contactNumber',
        'sortable': true
      }, {
        'label': 'Email',
        'field': 'clientemail',
        'sortable': true
      }, {
        'label': 'Status',
        'field': 'status',
        'sortable': true
      }, {
        'label': 'Total Price (room+addons)',
        'field': 'totalPrice',
        'sortable': true,
        'reducible': true,
      }, {
        'label': 'Partial Payment',
        'field': 'partialPayment',
        'sortable': true,
        'reducible': true,
      }, {
        'label': 'Balance',
        'field': 'balance',
        'sortable': true,
        'reducible': true,
      }, {
        'label': 'Action',
        'field': '',
        'slot': true,
      }],
      reservationsOptions: [{
        'label': '',
        'field': 'toggle',
        'sortable': false,
      }, {
        'label': 'No.',
        'field': 'id',
        'sortable': true
      }, {
        'label': 'Name',
        'field': 'name',
        'sortable': true
      }, {
        'label': 'Contact',
        'field': 'contactNumber',
        'sortable': true
      }, {
        'label': 'Address',
        'field': 'clientaddress',
        'sortable': true
      }, {
        'label': 'Checkin Date',
        'field': 'checkinDate',
        'sortable': true
      }, {
        'label': 'Checkout Date',
        'field': 'checkoutDate',
        'sortable': true
      }, {
        'label': 'Room',
        'field': 'room_name',
        'sortable': true
      }, {
        'label': 'Cost (Room+addon)',
        'field': 'totalPrice',
        'sortable': true,
        'reducible': true,
      }, {
        'label': 'Status',
        'field': 'status',
        'sortable': true
      }, {
        'label': 'Payment',
        'field': 'isPaid',
        'sortable': true
      },],
      transactionsOptions: [{
        'label': '',
        'field': 'toggle',
        'sortable': false,
      }, {
        'label': '#',
        'field': 'id',
        'sortable': true
      }, {
        'label': 'Name',
        'field': 'clientname',
        'sortable': true
      }, {
        'label': 'Contact',
        'field': 'clientcontact',
        'sortable': true
      }, {
        'label': 'Total Amount',
        'field': 'totalAmountToPay',
        'sortable': true,
        'reducible': true
      }, {
        'label': 'Actual Income',
        'field': 'actualIncomeOfThisDay',
        'sortable': true,
        'reducible': true,
      }, {
        'label': 'Total Cash',
        'field': 'cashAmountPay',
        'sortable': true,
        'reducible': true
      }, {
        'label': 'New Balance',
        'field': 'balance',
        'sortable': true,
        'reducible': true
      }, {
        'label': 'Latest Status',
        'field': 'payStatus',
        'sortable': true
      }, {
        'label': 'Remarks',
        'field': 'cashRemarks',
        'sortable': true
      }, {
        'label': 'Latest Transaction Date',
        'field': 'transaction_date',
        'sortable': true
      }, {
        'label': '',
        'field': 'action',
        'sortable': false
      }],
      transactionhistory: [{
        'label': 'Method',
        'field': 'paymentMethod'
      }, {
        'label': 'Ref. No.',
        'field': 'nonCashReference'
      }, {
        'label': 'Total',
        'field': 'totalAmountToPay'
      }, {
        'label': 'Amount Paid',
        'field': 'cashAmountPay'
      }, {
        'label': 'Balance',
        'field': 'balance'
      }, {
        'label': 'Discount Mode',
        'field': 'discountMode'
      }, {
        'label': 'Discount Value',
        'field': 'discountValue'
      }, {
        'label': 'Processed by',
        'field': 'processedBy'
      }, {
        'label': 'Status',
        'field': 'payStatus'
      }, {
        'label': 'Date',
        'field': 'transaction_date'
      },],
      transactionitem: [{
        'label': 'Name',
        'field': 'itemName'
      }, {
        'label': 'Category',
        'field': 'itemOption'
      }, {
        'label': 'Type',
        'field': 'itemType'
      }, {
        'label': 'Rate',
        'field': 'itemPriceRate'
      }, {
        'label': 'Qty',
        'field': 'purchaseQty'
      }, {
        'label': 'Total',
        'field': 'totalCost'
      }, {
        'label': 'Date',
        'field': 'dateCreated'
      },],
      dayreserve: new Date(),
      showTable: {},
      toggleAll: true,
      resdateFilter: 'any',
      resfromDate: null,
      restoDate: null,
      respaymentStatusFilter: '',
      resstatusFilter: '',
      dateFilter: 'any',
      fromDate: null,
      toDate: null,
      paymentMethodFilter: '',
      statusFilter: '',
      convDate: "",
      optionsArray1: [
        {
          name: 'Show Account',
          slug: 'show',
        },
        {
          type: 'divider',
        },
        {
          name: 'Edit',
          slug: 'edit',
        },
        {
          name: '<em>Delete</em>',
          slug: 'delete',
        },
      ],
      itemIndex: -1,
      walkinreservation: {
        clientName: '',
        clientEmail: '',
        clientPhone: '',
        clientAddress: '',
        clientNationality: 'Filipino',
        clientType: ''
      },
      reservation: {
        clientName: '',
        clientEmail: '',
        clientPhone: '',
        clientAddress: '',
        clientNationality: '',
        clientType: '',
        checkinDate: '',
        checkoutDate: '',
        roomName: '',
        roomPrice: '',
        roomType: '',
        remarks: '',
        status: 'vacant',
        isPaid: 'no',
        numguests: ''
      },
      showDate: this.thisMonth(1),
      message: "",
      startingDayOfWeek: 1,
      disablePast: false,
      disableFuture: false,
      displayPeriodUom: "week",
      displayPeriodCount: 1,
      displayWeekNumbers: false,
      showTimes: true,
      selectionStart: null,
      selectionEnd: null,
      newItemTitle: "",
      newItemStartDate: "",
      newItemEndDate: "",
      useDefaultTheme: true,
      useHolidayTheme: true,
      useTodayIcons: false,
      booksearchtext: "",
      autosuggestions: [],
      showAutosuggestions: false,
      origbookings: [],
      calendarItems: [
        /*{
            id: id,
            startDate: this.thisMonth(day, hr, min),
            endDate: this.thisMonth(day, hr, min),
            title: book.title,
            classes: "purple",
            tooltip: "This spans multiple days hehe",
        },*/
      ],
      linedata: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [
          {
            label: 'Cancelled',
            backgroundColor: 'gray',
            data: [50, 29, 1, 4, 37, 80, 40]
          },
          {
            label: 'Reserved',
            backgroundColor: 'red',
            data: [40, 39, 10, 40, 39, 80, 40]
          },
          {
            label: 'Check-in',
            backgroundColor: 'green',
            data: [40, 39, 10, 40, 39, 80, 40]
          },
          {
            label: 'Check-out',
            backgroundColor: 'yellow',
            data: [40, 39, 10, 40, 39, 80, 40]
          }
        ]
      },
      lineoptions: {
        responsive: true,
        maintainAspectRatio: false
      },
      paymentMethod: 'cash',
      cashAmount: 0,
      nonCashPayPlatform: '',
      nonCashReference: '',
      discountMode: 'percentage',
      discountValue: 0,
      taxValue: 0,
      partialPayment: 0,
      cashHistory: [],
      cashRemarks: '',
      activeTab: 'all',
      clientName: "",
      clientEmail: "",
      clientPhone: "",
      clientAddress: "",
      clientNationality: "",
      clientType: "",
      transactions: [],
      rooms: [],
      howMany: [],
      choice_room: null,
      items: [],
      inclusionCart: [],
      cart: [],
      itemCart: {
        id: 0,
        name: "",
        type: "",
        priceRate: "",
        rate: "",
        counter: "",
        purqty: "",
        totalCartPrice: "",
        category: "",
        itemOption: "",
        groupkey: "",
      },
      billing: {
        clientName: "",
        clientEmail: "",
        clientPhone: "",
        clientAddress: "",
        clientNationality: "Filipino",
        clientType: "walkin",
        bookingID: ""
      },
      reservations: [],
      searchText1: "",
      searchText2: "",
      searchText3: "",
      searchText4: "",
      searchTerm: "",
      searchTerm2: "",
      walkinStatus: false,
      alreadyDiscounted: false,
      cashDenominations: [{
        'label': '+1.00',
        'value': 1,
      }, {
        'label': '+5.00',
        'value': 5,
      }, {
        'label': '+10.00',
        'value': 10,
      }, {
        'label': '+20.00',
        'value': 20,
      }, {
        'label': '+50.00',
        'value': 50,
      }, {
        'label': '+100.00',
        'value': 100,
      }, {
        'label': '+500.00',
        'value': 500,
      }, {
        'label': '+1000.00',
        'value': 1000,
      },],
    };
  },
  async created() {
    if (this.EVALUATION_STAGE) {
      const countdownMessage = `This app is for evaluation and not the full version. Please wait for <span id="countdowntimer">${this.EVALUATION_TIME}</span> seconds to load.`;
      let countdownResult;
      let timeoutExpired = false; // New variable for tracking timeout
      countdownResult = await this.$swal.fire({
        title: 'Please wait',
        html: countdownMessage,
        icon: 'info',
        showCancelButton: false,
        showConfirmButton: false,
        allowOutsideClick: false,
        didOpen: () => {
          const countdownEl = document.querySelector('#countdowntimer');
          let count = this.EVALUATION_TIME - 1;
          const timerId = setInterval(() => {
            countdownEl.textContent = count;
            count--;
            if (count < 0) {
              clearInterval(timerId);
              timeoutExpired = true; // Update timeoutExpired to true
              this.$swal.close();
            }
          }, 1000);
        }
      });
      if (!countdownResult.isConfirmed && timeoutExpired) {
        countdownResult.isConfirmed = true; // Set isConfirmed to true if timeout expired
      }
      if (!countdownResult.isConfirmed) {
        return;
      }
    }
    this.loadAlldata();
  }
  ,
  computed: {
    currentRouteName() {
      return this.$route.name;
    },
    userdata() {
      const authStore = useAuthStore();
      const user = authStore.user;
      return user;
    },
    calcMeasure() {
      return {
        "height1": parseFloat(window.innerHeight) - 300 + "px",
        "height2": parseFloat(window.innerHeight) - 230 + "px",
        "height3": parseFloat(window.innerHeight) - 240 + "px",
        "height4": parseFloat(window.innerHeight) - 150 + "px",
      }
    },
    combinedcart() {
      // let result = [];
      // let combinedItems = {};
      // for (let item of this.cart.filter(item => item.category === 'main')) {
      //   if (!combinedItems[item.name]) {
      //     combinedItems[item.name] = {
      //       purqty: item.purqty,
      //       priceRate: item.priceRate,
      //       type: item.type,
      //       totalCartPrice: item.totalCartPrice,
      //       category: item.category,
      //       itemOption: item.itemOption,
      //       id: item.id,
      //     };
      //   } else {
      //     combinedItems[item.name].purqty += item.purqty;
      //     combinedItems[item.name].totalCartPrice = parseFloat(combinedItems[item.name].totalCartPrice) + parseFloat(item.totalCartPrice);
      //   }
      // }
      // for (let name in combinedItems) {
      //   result.push({
      //     name: name,
      //     purqty: combinedItems[name].purqty,
      //     priceRate: combinedItems[name].priceRate,
      //     type: combinedItems[name].type,
      //     totalCartPrice: combinedItems[name].totalCartPrice,
      //     category: combinedItems[name].category,
      //     itemOption: combinedItems[name].itemOption,
      //     id: combinedItems[name].id,
      //   });
      // }
      return this.cart.filter(item => item.category === 'main');
    },
    filteredInclusionCart() {
      return this.cart.map(o => {
        return {
          ...o
        };
      }).filter(item => item.category === 'inclusion');
    },
    filteredReservationsHistory() {
      let filtered = this.bookings.filter(reservation => {
        // Filter by date range
        if (this.resdateFilter === 'range' && this.resfromDate && this.restoDate) {
          const checkinDate = parseDate(reservation.checkinDate);
          const checkoutDate = parseDate(reservation.checkoutDate);
          const fromDate = parseDate(this.resfromDate);
          const toDate = parseDate(this.restoDate);
          return fromDate <= checkoutDate && toDate >= checkinDate;
        }
        return true;
      }).filter(reservation => {
        // Filter by payment method
        if (this.respaymentStatusFilter) {
          return reservation.isPaid === this.respaymentStatusFilter;
        }
        return true;
      }).filter(reservation => {
        // Filter by status
        if (this.resstatusFilter) {
          return reservation.status === this.resstatusFilter;
        }
        return true;
      });
      return filtered.map(item => {
        const searchCode = Object.values(item).join("~");
        return {
          ...item,
          searchCode
        };
      }).filter(item => item.searchCode.toString().toLowerCase().includes(this.searchTerm2.toLowerCase()));
    },
    filteredTransactionsTotal() {
      return this.filteredTransactions.reduce((acc, item) => acc + parseFloat(item.cashAmountPay), 0);
    },
    filteredTransactionsBalance() {
      return this.filteredTransactions.reduce((acc, item) => acc + parseFloat(item.balance), 0);
    },
    filteredTransactions() {
      let filtered = this.transactions;
      // Filter by date
      if (this.dateFilter === 'range' && this.fromDate && this.toDate) {
        filtered = filtered.filter(transaction => {
          return parseDate2(transaction.transaction_date) >= parseDate(this.fromDate) && parseDate2(transaction.transaction_date) <= parseDate(this.toDate);
        });
      }
      // Filter by payment method
      if (this.paymentMethodFilter) {
        filtered = filtered.filter(transaction => {
          return transaction.paymentMethod === this.paymentMethodFilter;
        });
      }
      // Filter by status
      if (this.statusFilter) {
        filtered = filtered.filter(transaction => {
          return transaction.payStatus === this.statusFilter;
        });
      }
      return filtered.map(item => {
        const searchCode = Object.values(item).join("~") + (item.items ? JSON.stringify(item.items) : []) + (item.props ? JSON.stringify(item.props) : []);
        return {
          ...item,
          searchCode
        };
      }).filter(item => item.searchCode.toString().toLowerCase().includes(this.searchTerm.toLowerCase()));
    },
    roomsjoinbookings() {
      return this.rooms.filter(item => item.type === this.activeMainTab).filter(item => item.type === this.activeMainTab.toString()).map(room => {
        const booking = this.bookings.filter(item => (item.status !== "checkedout")).filter(item => (item.status !== "cancelled") && (parseDate(new Date().toLocaleDateString('en-GB')) >= parseDate(item.checkinDate) && parseDate(item.checkoutDate) >= parseDate(new Date().toLocaleDateString('en-GB')))).find(booking => booking.room_name === room.name);
        if (booking) {
          return {
            ...room,
            clientName: booking.name,
            clientEmail: booking.clientemail,
            clientAddress: booking.clientaddress,
            contactNumber: booking.contactNumber,
            checkinDate: booking.checkinDate,
            checkoutDate: booking.checkoutDate,
            status: booking.status,
            itemID: booking.itemID,
            groupkey: booking.groupkey,
            totalPrice: booking.totalPrice,
            partialPayment: booking.partialPayment,
            status: booking.status,
            isPaid: booking.isPaid,
            selected: false,
          };
        } else {
          return room;
        }
      });
    },
    filteredRoomBookings() {
      const isCancelled = this.activeTab === 'cancelled';
      const isReserved = this.activeTab === 'reserved';
      const isOccupied = this.activeTab === 'occupied';
      const isCheckedout = this.activeTab === 'checkedout';
      const selectedDate = parseDate(this.convDate);
      return this.bookings.filter(booking => {
        const bookingCheckinDate = parseDate(booking.checkinDate);
        const bookingCheckoutDate = parseDate(booking.checkoutDate);
        const dateInRange = (selectedDate >= bookingCheckinDate && selectedDate <= bookingCheckoutDate);
        const isReservedMatch = !isReserved || booking.status === 'reserved';
        const isOccupiedMatch = !isOccupied || booking.status === 'checkedin';
        const isCancelledMatch = !isCancelled || booking.status === 'cancelled';
        const isCheckedoutMatch = !isCheckedout || booking.status === 'checkedout';
        return dateInRange && isCancelledMatch && isReservedMatch && isOccupiedMatch && isCheckedoutMatch;
      }).map(o => {
        const balance = parseFloat(o.totalPrice) - parseFloat(o.partialPayment);
        return {
          ...o,
          balance
        };
      });
    },
    updatedRooms() {
      return this.rooms.filter(room => {
        // Check if there are any bookings for this room that overlap with the specified date range
        const overlappingBookings = this.bookings.filter(booking => {
          // Check if the booking is not cancelled and not checked out
          if (booking.status === 'cancelled' || booking.status === 'checkedout') {
            return false;
          }

          // Check if the booking's room_name matches the current room and the date range overlaps with the reservation
          const checkInDate = parseDate(booking.checkinDate);
          const checkOutDate = parseDate(booking.checkoutDate);
          const startDate = parseDate(this.reservation.checkinDate);
          const endDate = parseDate(this.reservation.checkoutDate);
          const isOverlap = booking.room_name === room.name &&
            startDate <= checkOutDate && endDate >= checkInDate;

          return isOverlap;
        });

        // Check if there exists a booking with the same room_name in yesterday that has not been checked out
        const yesterday = new Date();
        yesterday.setDate(yesterday.getDate() - 1);
        const yesterdayBooking = this.bookings.find(prevBooking => {
          const prevCheckOutDate = parseDate(prevBooking.checkoutDate);
          return prevBooking.room_name === room.name &&
            new Date(prevCheckOutDate).toDateString() === new Date(yesterday).toDateString() &&
            prevBooking.status === 'checkedin';
        });

        // Return true if there are no overlapping bookings and no booking in yesterday that has not been checked out
        return overlappingBookings.length === 0 && !yesterdayBooking;
      });
    },
    userLocale() {
      return CalendarMath.getDefaultBrowserLocale
    },
    dayNames() {
      return CalendarMath.getFormattedWeekdayNames(this.userLocale, "long", 0)
    },
    themeClasses() {
      return {
        "theme-default": this.useDefaultTheme,
        "holiday-us-traditional": this.useHolidayTheme,
        "holiday-us-official": this.useHolidayTheme,
      }
    },
    myDateClasses() {
      // This was added to demonstrate the dateClasses prop. Note in particular that the
      // keys of the object are `yyyy-mm-dd` ISO date strings (not dates), and the values
      // for those keys are strings or string arrays. Keep in mind that your CSS to style these
      // may need to be fairly specific to make it override your theme's styles. See the
      // CSS at the bottom of this component to see how these are styled.
      const o = {}
      const theFirst = this.thisMonth(1)
      const ides = [2, 4, 6, 9].includes(theFirst.getMonth()) ? 15 : 13
      const idesDate = this.thisMonth(ides)
      o[CalendarMath.isoYearMonthDay(idesDate)] = "ides"
      o[CalendarMath.isoYearMonthDay(this.thisMonth(21))] = ["do-you-remember", "the-21st"]
      return o
    },
    currentDate() {
      const options = {
        month: '2-digit',
        day: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
      }
      return new Date().toLocaleString('en-US', options)
    },
    subroom() {
      const mainRoomItems = this.cart.filter(item => item.category === 'main' && item.itemOption === 'room');
      const originalPrice = mainRoomItems.reduce((acc, item) => acc + parseFloat(item.totalCartPrice), 0);
      if (this.discount === 0) {
        return { original: originalPrice, discounted: '' };
      }
      const discountedPrice = originalPrice - this.discount;
      const discountAmount = this.discountMode === 'percentage' ? `${this.discountValue}%` : `₱${this.discountValue}`;
      const formattedOriginalPrice = `<del class="text-danger">${originalPrice}</del>`;
      const formattedDiscountedPrice = `<sup class="text-danger font-weight-bold">${discountAmount} off</sup> <span class="text-success font-weight-bold">${discountedPrice}</span>`;
      return { original: formattedOriginalPrice, discounted: formattedDiscountedPrice, discountMode: this.discountMode, discountValue: this.discountValue };
    },
    subaddons() {
      return this.cart.filter(item => item.category === 'main' && item.itemOption === 'addons').reduce((acc, item) => acc + parseFloat(item.totalCartPrice), 0);
    },
    subtotal() {
      return this.cart.filter(item => item.category === 'main').reduce((acc, item) => acc + parseFloat(item.totalCartPrice), 0) - this.discount;
    },
    sumInclusion() {
      return this.cart.filter(item => item.category === 'inclusion').reduce((acc, item) => acc + parseFloat(item.totalCartPrice), 0);
    },
    discount() {
      if (this.discountMode === 'percentage') {
        return (this.cart.filter(item => item.category === 'main').reduce((acc, item) => acc + parseFloat(item.totalCartPrice), 0) - this.subaddons) * this.discountValue / 100;
      } else {
        return this.discountValue;
      }
    },
    total() {
      return this.subtotal - this.partialPayment;
    },
    change() {
      return (this.cashAmount > this.total) ? this.cashAmount - this.total : 0;
    },
    isThereLeisures() {
      return this.cart.filter(item => item.type === 'LEISURES').length > 0;
    },
    countInclusion() {
      return this.cart.filter(item => item.category === 'inclusion').length;
    },
    numItemCart() {
      return this.cart.filter(item => item.category === 'main').length;
    },
    filteredCart() {
      return this.cart.map(o => {
        const searchCode = o.name;
        return {
          ...o,
          searchCode
        };
      }).filter(item => item.category === 'main');
    },
    bookings() {
      return this.origbookings
        .map(book => {
          const { name, room_name, status, isPaid } = book;
          const paymentStatus = isPaid === 'yes' ? 'fully-paid' : isPaid === 'no' ? 'not paid' : 'partial';
          const searchCode = `${name}~${room_name}~${status}~${paymentStatus}`;
          return {
            ...book,
            searchCode,
          };
        })
        .filter(book => book.searchCode.toLowerCase().includes(this.booksearchtext.toLowerCase()));
    },
    roomStatus() {
      return this.rooms.map(room => {
        const isVacant = this.vacantRoom(room.name);
        const searchCode = room.name + "~" + room.type + "~" + room.price;
        return {
          ...room,
          isVacant,
          searchCode
        };
      }).filter(rooms => rooms.searchCode.toString().toLowerCase().includes(this.searchText2.toLowerCase()));
    },
    filteredReservations() {
      return this.reservations.map(book => {
        const searchCode = book.name + "~" + book.checkinDate + "~" + book.checkoutDate + "~" + book.room_name;
        return {
          ...book,
          searchCode
        };
      }).filter(reservation => reservation.searchCode.toString().toLowerCase().includes(this.searchText1.toLowerCase()));
    },
    filteredItems() {
      return this.items.map(item => {
        const searchCode = item.item + "~" + item.type;
        return {
          ...item,
          searchCode
        };
      }).filter(item => item.searchCode.toString().toLowerCase().includes(this.searchText3.toLowerCase()));
    },
  },
  methods: {
    handleReceptionRoomAction(room) {
      this.$swal.fire({
        icon: 'warning',
        title: 'Room Housekeeping',
        text: 'Are you certain that this room has already been inspected?',
        confirmButtonText: 'Yes',
        cancelButtonText: 'No',
        showCancelButton: true
      }).then((result) => {
        if (result.isConfirmed) {
          axios.post(`${this.API_URL}rooms/filter/`, [
            { columnName: 'name', columnKey: room.name },
          ]).then(response => {
            axios.put(`${this.API_URL}rooms/${room.id}/`, {
              name: response.data[0].name,
              type: response.data[0].type,
              price: response.data[0].price,
              isAvailable: response.data[0].isAvailable,
              status: (response.data[0].status === 'clean') ? 'dirty' : 'clean'
            }).then(response => {
              document.location.reload();
            })
          })
        }

      })
    },
    handleReceptionDayAction(d, room) {
      if (this.booksearchtext !== "") {
        this.$swal.fire({
          icon: 'error',
          title: 'Calendar Day Selection Restricted',
          text: 'Unable to select a day on the calendar when the search query is not empty.',
          confirmButtonText: 'OK'
        });
        return;
      }
      this.reservation.status = 'vacant';
      this.reservation.clientName = "";
      this.reservation.clientEmail = "";
      this.reservation.clientAddress = "";
      this.reservation.clientNationality = "Filipino";
      this.reservation.clientType = "in-house";
      this.reservation.remarks = "";
      this.reservation.clientPhone = "";
      this.reservation.roomName = [{ name: room.name, type: room.type, price: room.price }];
      this.roomSelect = 'no';
      this.reservation.checkinDate = d.toLocaleDateString('en-GB');
      this.reservation.checkoutDate = formatDate(d);
      this.toggleItemModal();
    },
    handleReceptionItemAction(book, room) {
      this.itemIndex = this.bookings.findIndex(
        o => o.itemID === book.itemID
      );
      if (this.itemIndex !== -1) {
        this.showReservation();
      } else {
        this.reservation.status = 'vacant';
        this.reservation.clientName = "";
        this.reservation.clientEmail = "";
        this.reservation.clientAddress = "";
        this.reservation.clientNationality = "Filipino";
        this.reservation.clientType = "in-house";
        this.reservation.remarks = "";
        // this.reservation.numguests = "";
        this.reservation.clientPhone = "";
        this.reservation.roomName = [{ name: room.name, type: room.type, price: room.price }];
        this.roomSelect = 'no';
        this.reservation.checkinDate = new Date().toLocaleDateString('en-GB');
        this.reservation.checkoutDate = formatDate(new Date());
        this.toggleItemModal();
      }
    },
    handleKeyPress(event) {
      if (this.currentRouteName !== "booking") {
        return;
      }
      if (!this.activeAccountFlag) {
        return;
      }
      switch (event.key) {
        case 'Enter':
          event.preventDefault()
          if (this.total > 0) {
            this.placeOrder();
          }
          break;
        case 'F1':
          event.preventDefault()
          this.showShoppingModal();
          break;
        case 'F2':
          event.preventDefault()
          this.moveInclusionCartToMain();
          break;
        case 'F10':
          event.preventDefault()
          this.generateBillingStatement();
          break;
      }
    },
    addToCash(d) {
      this.cashAmount = isNaN(parseFloat(this.cashAmount)) ? 0 : parseFloat(this.cashAmount) + d;
    },
    updateTotalCash() {
      if (this.cashAmount === 0 || this.cashAmount.toString() === "" || this.cashAmount === NaN) {
        this.cashAmount = 0;
      } else {
        this.cashAmount = this.cashAmount.toString();
      }
      //alert(this.totalCash)
    },
    setDiscount() {
      this.$swal.fire({
        title: 'Set discount value',
        html: `
      <div>
        <input type="radio" class="form-check-input" id="fixedDiscount" name="discountType" value="fixed" checked>
        <label for="fixedDiscount" class="form-check-label">Fixed</label> &nbsp;
        <input type="radio" class="form-check-input" id="percentageDiscount" name="discountType" value="percentage">
        <label for="percentageDiscount" class="form-check-label">Percentage</label>
        <br><br>
        <input type="number" class="form-control" id="discountValue" placeholder="Enter discount value" min="0" step="any">
      </div>
    `,
        showCancelButton: true,
        confirmButtonText: 'Submit',
        cancelButtonText: 'Cancel',
        allowOutsideClick: false,
        preConfirm: () => {
          const discountType = document.querySelector('input[name="discountType"]:checked').value;
          const discountValue = document.getElementById('discountValue').value;
          return { discountType, discountValue };
        }
      }).then((result) => {
        if (result.isConfirmed) {
          const { discountType, discountValue } = result.value;
          if (discountValue !== "") {
            this.discountMode = discountType;
            this.discountValue = parseFloat(discountValue).toFixed(2);
            this.justDiscounted = true;
          }
        }
      });
    },
    setNonCash() {
      if (this.paymentMethod === 'non-cash') {
        this.$swal.fire({
          title: 'Choose non-cash type',
          html: `
      <div>
        <input type="radio" class="form-check-input" id="cat1" name="noncashType" value="gcash" checked>
        <label for="cat1" class="form-check-label">GCash</label> &nbsp;
        <input type="radio" class="form-check-input" id="cat2" name="noncashType" value="paymaya">
        <label for="cat2" class="form-check-label">PayMaya</label> &nbsp;
        <input type="radio" class="form-check-input" id="cat3" name="noncashType" value="debitcard">
        <label for="cat3" class="form-check-label">Debit Card</label> &nbsp;
        <input type="radio" class="form-check-input" id="cat4" name="noncashType" value="creditcard">
        <label for="cat4" class="form-check-label">Credit Card</label> &nbsp;
        <input type="radio" class="form-check-input" id="cat5" name="noncashType" value="bank">
        <label for="cat5" class="form-check-label">Bank</label> &nbsp;
        <br><br>
        <input type="text" class="form-control" maxlength=32 id="referenceno" placeholder="Enter reference/transaction no. here after non-cash payment.">
      </div>
    `,
          showCancelButton: true,
          confirmButtonText: 'Submit',
          cancelButtonText: 'Cancel',
          allowOutsideClick: false,
          preConfirm: () => {
            const noncashType = document.querySelector('input[name="noncashType"]:checked').value;
            const referenceno = document.getElementById('referenceno').value;
            return { noncashType, referenceno };
          }
        }).then((result) => {
          if (result.isConfirmed) {
            const { noncashType, referenceno } = result.value;
            if (noncashType !== "" || referenceno !== "") {
              this.nonCashPayPlatform = noncashType;
              this.nonCashReference = referenceno;
            } else {
              this.$swal({
                title: 'Warning',
                text: 'Please provide both the non-cash type and the reference number.',
                icon: 'warning',
              });
              return;
            }
          }
        });
      } else {
        this.nonCashPayPlatform = "";
        this.nonCashReference = "";
      }
    },
    async deleteTransaction(id) {
      axios.get(this.API_URL + `transaction/${id}/`).then(async response => {
        const data = response.data;
        const itemID = data.bookingID;
        const gkey = data.groupkey || "";
        const cname = data.clientname;
        const type = itemID.charAt(0);
        this.$swal.fire({
          title: 'Authorization Required',
          input: 'text',
          showCancelButton: true,
          allowOutsideClick: false,
          inputAttributes: {
            minlength: 6, // Minimum length of 3 characters
            maxlength: 24, // Maximum length of 24 characters
            autocomplete: "off",
            style: "text-security:disc; -webkit-text-security:disc;"
          },
          confirmButtonText: 'Submit',
          cancelButtonText: 'Cancel',
          inputPlaceholder: 'Enter authorization code',
        }).then(async (result) => {
          if (result.isConfirmed) {
            const authorizationCode = result.value;
            // Validate the authorization code and perform necessary actions
            if (authorizationCode.toLowerCase() === this.AUTHORIZATION_KEY.toLowerCase()) {
              // Code is correct, proceed with the desired action
              const confirmMessage = ' If you proceed with voiding, all associated items and booking and transaction records will be permanently deleted, and this action cannot be reversed.';
              const result = await this.$swal.fire({
                title: 'Are you sure you want to void this?',
                text: confirmMessage,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes, void it!',
                cancelButtonText: 'Cancel'
              });
              if (result.isConfirmed) {
                const countdownMessage = 'Item will be voided in <span id="countdown">5</span> seconds. Do you want to cancel?';
                let countdownResult;
                countdownResult = await this.$swal.fire({
                  title: 'Please wait',
                  html: countdownMessage,
                  icon: 'info',
                  showCancelButton: true,
                  confirmButtonColor: '#3085d6',
                  cancelButtonColor: '#d33',
                  confirmButtonText: 'Confirm now',
                  cancelButtonText: 'Cancel',
                  didOpen: () => {
                    const countdownEl = document.querySelector('#countdown');
                    let count = 5;
                    const timerId = setInterval(() => {
                      countdownEl.textContent = count;
                      count--;
                      if (count < 0) {
                        clearInterval(timerId);
                        this.$swal.close();
                      }
                    }, 1000);
                  }
                });
                if (!countdownResult.isConfirmed) {
                  return;
                }
                if (type === "f") {
                  this.voidAction(null, null, itemID, gkey, cname, false);
                } else if (type === "e") {
                  const bID = this.bookings.findIndex(
                    o => o.itemID === itemID
                  );
                  const request = await axios.post(`${this.API_URL}bookings/filter/`, [
                    { "columnName": "itemID", "columnKey": itemID },
                  ])
                  const keyID = request.data[0].id;
                  this.voidAction(bID, keyID, itemID, gkey, cname, true);
                }
              }
            } else {
              // Code is incorrect, show an error message or take appropriate action
              this.$swal.fire({
                icon: 'error',
                title: 'Incorrect Passcode',
                text: 'The entered passcode is incorrect. Please try again.',
                allowOutsideClick: false,
              });
            }
          }
        });
      })
        .catch(error => {
          console.log(error);
        });
    },
    getTime(d) {
      const date = d;
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');
      return `${hours}:${minutes}`;
    },
    async voidBook() {
      this.toggleItemModal();
      this.$swal.fire({
        title: 'Authorization Required',
        input: 'text',
        showCancelButton: true,
        allowOutsideClick: false,
        inputAttributes: {
          minlength: 6, // Minimum length of 3 characters
          maxlength: 24, // Maximum length of 24 characters
          autocomplete: "off",
          style: "text-security:disc; -webkit-text-security:disc;"
        },
        confirmButtonText: 'Submit',
        cancelButtonText: 'Cancel',
        inputPlaceholder: 'Enter authorization code',
      }).then(async (result) => {
        if (result.isConfirmed) {
          const authorizationCode = result.value;
          // Validate the authorization code and perform necessary actions
          if (authorizationCode.toLowerCase() === this.AUTHORIZATION_KEY.toLowerCase()) {
            // Code is correct, proceed with the desired action
            const confirmMessage = ' If you proceed with voiding, all associated items and transaction records will be permanently deleted, and this action cannot be reversed.';
            const result = await this.$swal.fire({
              title: 'Are you sure you want to void this?',
              text: confirmMessage,
              icon: 'warning',
              showCancelButton: true,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              confirmButtonText: 'Yes, void it!',
              cancelButtonText: 'Cancel'
            });
            if (result.isConfirmed) {
              const countdownMessage = 'Item will be voided in <span id="countdown">5</span> seconds. Do you want to cancel?';
              let countdownResult;
              countdownResult = await this.$swal.fire({
                title: 'Please wait',
                html: countdownMessage,
                icon: 'info',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Confirm now',
                cancelButtonText: 'Cancel',
                didOpen: () => {
                  const countdownEl = document.querySelector('#countdown');
                  let count = 5;
                  const timerId = setInterval(() => {
                    countdownEl.textContent = count;
                    count--;
                    if (count < 0) {
                      clearInterval(timerId);
                      this.$swal.close();
                    }
                  }, 1000);
                }
              });
              if (!countdownResult.isConfirmed) {
                return;
              }
              this.voidAction(this.itemIndex, null, null, null, null, true);
            }
          } else {
            // Code is incorrect, show an error message or take appropriate action
            this.$swal.fire({
              icon: 'error',
              title: 'Incorrect Passcode',
              text: 'The entered passcode is incorrect. Please try again.',
              allowOutsideClick: false,
            });
          }
        }
      });
    },
    async voidAction(o, keyID, bkey, gkey, name, brute) {
      let transdata_ID = null;
      let item = null;
      let bookID = null;
      let bookKey = null;
      let groupkey = null;
      let cname = null;
      let kid = null;
      if (bkey === null && gkey === null && name === null) {
        item = this.bookings[o];
        bookID = item.id;
        bookKey = item.itemID;
        groupkey = item.groupkey;
        cname = item.name;
        kid = bookID;
      } else {
        item = null;
        bookID = o;
        bookKey = bkey;
        groupkey = gkey;
        cname = name;
        kid = keyID;
      }
      if (groupkey) {
        try {
          const existingTransaction = await axios.post(`${this.API_URL}transaction/filter/`, {
            columnName: 'groupkey',
            columnKey: groupkey
          });
          transdata_ID = existingTransaction.data[0].id;
        } catch (error) {
        }
        try {
          const existingTransaction_ITEM = await axios.post(`${this.API_URL}transaction/item/filter/`, {
            columnName: 'groupkey',
            columnKey: groupkey
          });
          for (const item of existingTransaction_ITEM.data) {
            axios.get(this.API_URL + `transaction/item/delete/${item.id}/`)
          }
        } catch (error) {
        }
        try {
          if (transdata_ID) {
            const existingTransaction_RECORD = await axios.post(`${this.API_URL}transaction/record/filter/`, {
              columnName: 'transaction',
              columnKey: transdata_ID
            });
            for (const item of existingTransaction_RECORD.data) {
              axios.get(this.API_URL + `transaction/record/delete/${item.transactionrecord_id}/`)
            }
          }
        } catch (error) {
        }
        try {
          if (transdata_ID) {
            axios.get(this.API_URL + `transaction/delete/${transdata_ID}/`)
          }
        } catch (error) {
        }
        if (brute) {
          try {
            const existingBooking = await axios.post(`${this.API_URL}bookings/filter/`, {
              columnName: 'groupkey',
              columnKey: groupkey
            });
            for (const item of existingBooking.data) {
              axios.get(this.API_URL + `bookings/delete/${item.id}/`);
            }
          } catch (error) {
          }
        }
      } else {
        try {
          const existingTransaction = await axios.post(`${this.API_URL}transaction/filter/`, {
            columnName: 'bookingID',
            columnKey: bookKey
          });
          transdata_ID = existingTransaction.data[0].id;
        } catch (error) {
        }
        try {
          const existingTransaction_ITEM = await axios.post(`${this.API_URL}transaction/item/filter/`, {
            columnName: 'bookingID',
            columnKey: bookKey
          });
          for (const item of existingTransaction_ITEM.data) {
            axios.get(this.API_URL + `transaction/item/delete/${item.id}/`)
          }
        } catch (error) {
        }
        try {
          if (transdata_ID) {
            const existingTransaction_RECORD = await axios.post(`${this.API_URL}transaction/record/filter/`, {
              columnName: 'transaction',
              columnKey: transdata_ID
            });
            for (const item of existingTransaction_RECORD.data) {
              axios.get(this.API_URL + `transaction/record/delete/${item.transactionrecord_id}/`)
            }
          }
        } catch (error) {
        }
        try {
          if (transdata_ID) {
            axios.get(this.API_URL + `transaction/delete/${transdata_ID}/`)
          }
        } catch (error) {
        }
        if (brute) {
          try {
            await axios.get(this.API_URL + `bookings/delete/${kid}/`)
          } catch (error) {
          }
        }
      }
      this.taskRecord(`action:/void/client:/${cname}`);
      await this.$swal.fire({
        title: 'Success',
        text: 'Item was voided successfully!',
        icon: 'success'
      }).then(response => {
        document.location.reload();
      })
    },
    async taskRecord(msg) {
      this.socket.send(JSON.stringify({
        'message': msg
      }));
      try {
        await axios.post(`${this.API_URL}task/record/`, {
          actor: this.userdata.fName + " " + this.userdata.lName,
          task: msg,
        })
      } catch (error) {
      }
    },
    handleChange() {
      alert()
    },
    cardAction(id, room_name, room_type, room_price) {
      this.itemIndex = this.bookings.findIndex(
        o => o.itemID === id
      );
      if (this.itemIndex !== -1) {
        this.showReservation();
      } else {
        this.reservation.status = 'vacant';
        this.reservation.clientName = "";
        this.reservation.clientEmail = "";
        this.reservation.clientAddress = "";
        this.reservation.clientNationality = "Filipino";
        this.reservation.clientType = "in-house";
        this.reservation.remarks = "";
        // this.reservation.numguests = "";
        this.reservation.clientPhone = "";
        this.reservation.roomName = [{ name: room_name, type: room_type, price: room_price }];
        this.roomSelect = 'no';
        this.reservation.checkinDate = new Date().toLocaleDateString('en-GB');
        this.reservation.checkoutDate = formatDate(new Date());
        this.toggleItemModal();
      }
    },
    sendMessage() {
      console.log("Hello")
      console.log(this.socket);
      this.socket.send('{"message":"hello"}');
    },
    async loadAlldata() {
      this.reloadData();
      this.reloadItemsData();
      this.loadTransactionData();
    },
    parseDate2(dateString) {
      const [day, month, year] = dateString.split('/');
      return new Date(`${month}/${day}/${year}`).setHours(0, 0, 0, 0);
    },
    async logout() {
      const authStore = useAuthStore();
      const user = {
        username: authStore.user.username,
        FirstName: authStore.user.fName,
        LastName: authStore.user.lName,
        role: authStore.user.role
      }
      const response = await axios.put(`${this.API_URL}users/${authStore.user.id}/`, { ...user, isActive: false })
      if (response.data !== undefined) {
        authStore.logout();
        this.$router.push('/');
      } else {
        this.$swal({
          icon: "error",
          title: "Logout error. Please contact your admin for assistance!"
        });
      }
    },
    toggleAllTD() {
      this.toggleAll = !this.toggleAll;
      Object.keys(this.showTable).forEach(prop => {
        this.showTable[prop] = this.toggleAll;
      })
      $('.togglebuttons').trigger('click');
    },
    async toggleTable(transactionID, bookingID) {
      // method to toggle the visibility of the related table for the given transactionID
      this.showTable[transactionID] = !this.showTable[transactionID];
      if (this.showTable[transactionID]) {
        try {
          const response = await axios.post(`${this.API_URL}transaction/record/filter/`, [
            { "columnName": "transaction", "columnKey": transactionID },
          ])
          const response2 = await axios.post(`${this.API_URL}transaction/item/filter/`, [
            { "columnName": "bookingID", "columnKey": bookingID },
          ])
          //     return filtered.map(item => {
          //   const searchCode = Object.values(item).join("~");
          //   return {
          //     ...item,
          //     searchCode
          //   };
          // }).filter(item => item.searchCode.toString().toLowerCase().includes(this.searchTerm.toLowerCase()));
          const history = response.data;
          const itemprops = response2.data;
          this.transactions = this.transactions.map(t => {
            if (t.id === transactionID) {
              t.items = history;
              t.props = itemprops;
            }
            return t;
          });
        } catch (error) {
        }
      }
    },
    async addWalkInGuest() {
      this.billing.clientName = this.walkinreservation.clientName;
      this.billing.clientEmail = this.walkinreservation.clientEmail;
      this.billing.clientPhone = this.walkinreservation.clientPhone;
      this.billing.clientAddress = this.walkinreservation.clientAddress;
      this.billing.clientNationality = this.walkinreservation.clientNationality;
      this.billing.clientType = this.walkinreservation.clientType;
      this.isItNew = true;
      this.walkinStatus = true;
      try {
        const response = await axios.get(this.API_URL + 'transaction/');
        this.billing.bookingID = response.data[response.data.length - 1].id + 1;
      } catch {
      }
      this.toggleAddAccountModal();
    },
    showShoppingModal() {
      $("#shopModal").modal("toggle");
    },
    async moveInclusionCartToMain() {
      let bId = null;
      let gkey = null;
      const n = this.filteredInclusionCart.length;
      if (n > 0) {
        const result = await this.$swal.fire({
          title: 'Confirmation',
          text: 'This action will update your cart. Do you want to proceed?',
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Yes, do it!',
          cancelButtonText: 'Cancel'
        });
        if (result.isConfirmed) {
          try {
            bId = this.bookings[this.itemIndex].itemID
          } catch {
            bId = "walkin"
          }
          try {
            gkey = this.bookings[this.itemIndex].groupkey
          } catch {
          }
          try {
            const updatedItems = [];
            let isFind = false;
            // Loop through inclusion items in the cart
            this.cart.filter(item => item.category === 'inclusion').forEach(async (item, index) => {
              // Define the API endpoint and data for the PUT request
              const api = `${this.API_URL}transaction/item/${item.id}/`;
              const data = {
                itemName: item.name,
                itemType: item.type,
                itemPriceRate: item.priceRate,
                purchaseQty: item.purqty,
                totalCost: item.totalCartPrice,
                category: 'main',
                itemOption: 'addons',
              };
              const numBookedRooms = this.cart.filter(o => (o.type.toLowerCase() === 'beach room' || o.type.toLowerCase() === 'pool room' || o.type.toLowerCase() === 'leisures') && o.category === 'main').length;
              const numGuestsCard = this.cart.filter(o => o.name.toLowerCase() === 'general entrance' && o.category === 'main').length;
              const entranceFee = parseFloat(this.items.filter(o => o.item.toLowerCase() === 'general entrance')[0].priceRate);
              if (numGuestsCard === 0 && numBookedRooms > 0 && item.name.toLowerCase() === 'general entrance' && isFind === false) {
                const totalGuests = this.cart.filter(o => o.name.toLowerCase() === 'general entrance').reduce((acc, item) => acc + parseFloat(item.purqty), 0);
                if (totalGuests === 1) {
                  data.totalCost = parseFloat(data.totalCost) - entranceFee;
                } else if (totalGuests >= 2) {
                  data.totalCost = parseFloat(data.totalCost) - 2 * entranceFee;
                }
                item.totalCartPrice = data.totalCost;
                isFind = true;
              }
              try {
                data.bookingID = bId;
                data.groupkey = gkey;
                // Send PUT request to update the item
                const response = await axios.put(api, data);
                updatedItems.push(response.data);
              } catch (error) {
                data.bookingID = "walkin"
                bId = data.bookingID;
                updatedItems.push(data);
              }
            });
            // Wait for all PUT requests to finish before updating the local cart
            await Promise.all(this.cart.filter(item => item.category === 'inclusion').map(async (item) => {
              // Update the category of each inclusion item to 'main'
              item.category = 'main';
              // Find the updated version of the item in the list of updated items
              const updatedItem = updatedItems.find(updatedItem => updatedItem.id === item.id);
              // If the item was successfully updated, update the local cart with the new data
              if (updatedItem) {
                Object.assign(item, updatedItem);
              }
            }));
            if (bId !== "walkin") {
              const resId = this.bookings[this.itemIndex].id;
              this.bookings[this.itemIndex].isPaid = "partial";
              this.updateBookings(resId);
              this.populateCalendarItems();
            }
          } catch (error) {
            console.error(error);
          }
        }
      }
    },
    resetSummary(no) {
      this.cart = [];
      this.billing = {
        clientName: "",
        clientEmail: "",
        clientPhone: "",
        clientAddress: "",
        clientNationality: "Filipino",
        clientType: "walkin",
        bookingID: ""
      };
      this.cashHistory = [];
      this.walkinreservation = {
        clientName: "",
        clientEmail: "",
        clientPhone: "",
        clientAddress: "",
        clientNationality: "Filipino",
        clientType: "walkin"
      }
      this.subtotal = 0;
      this.partialPayment = 0;
      this.total = 0;
      this.discountValue = 0;
      this.change = 0;
      this.paymentMethod = "cash";
      this.nonCashPayPlatform = "";
      this.nonCashReference = "";
      this.itemCart = {
        id: 0,
        name: "",
        type: "",
        priceRate: "",
        rate: "",
        counter: "",
        purqty: "",
        totalCartPrice: "",
        category: ""
      }
      this.justDiscounted = false;
      this.alreadyDiscounted = false;
      this.itemIndex = -1;
      this.walkinStatus = false;
      this.isItNew = false;
      if (no === 1) {
        this.$refs.searchQuery.focus();
        this.$refs.searchQuery.blur();
      }
      if (no === 2 && this.billing.clientName === "") {
        this.activeAccountFlag = true;
        // this.toggleAddAccountModal();
      }
      if (no !== 2) {
        this.activeAccountFlag = false;
      }
    },
    changeTab(tab) {
      this.activeTab = tab
    },
    //generic methods
    optionClicked1(event) {
      const item = event.item;
      const uniqID = item.substring(item.toString().indexOf("~") + 1, item.toString().lastIndexOf("~"));
      const action = event.option.slug;
      window.alert(action);
    },
    toggledayMenuModal() {
      $("#dayMenuModal").modal("toggle");
    },
    toggleAddAccountModal() {
      $("#addAccountModal").modal("toggle");
    },
    toggleItemModal() {
      this.disablebutton = false;
      $("#BookDayModal").modal("toggle");
    },
    toggleSettingsModal() {
      $("#settings-modal").modal("toggle");
    },
    toggleShowAllModal() {
      $("#showall-modal").modal("toggle");
    },
    changeItemColor(status) {
      let item = this.calendarItems[this.calendarItems.findIndex(o => o.id === this.bookings[this.itemIndex].itemID)];
      if (status === "checkedin") {
        item.classes = ["custom-date-class-green"];
      } else if (status === "cancelled") {
        item.classes = ["custom-date-class-gray"];
      } else if (status === "checkedout") {
        item.classes = ["custom-date-class-orange"];
      }
    },
    async viewSummary() {
      this.movetocartFlag = false;
      const item = this.bookings[this.itemIndex];
      const bookingID = item.itemID;
      let existingTransaction = null;
      let transaction = null;
      let gkey = "";
      let groupbookings = [];
      item.remarks = this.reservation.remarks;
      this.updateBookings(item.id)
      try {
        gkey = (this.bookings[this.itemIndex].groupkey || "x");
        try {
          const o = await axios.post(`${this.API_URL}bookings/filter/`, [
            { "columnName": "groupkey", "columnKey": gkey },
          ])
          groupbookings = o.data;
        } catch (error) {
        }
      } catch (error) {
      }
      if (groupbookings.length > 0) {
        existingTransaction = await axios.post(`${this.API_URL}transaction/filter/`, {
          columnName: 'groupkey',
          columnKey: gkey
        });
      } else {
        existingTransaction = await axios.post(`${this.API_URL}transaction/filter/`, {
          columnName: 'bookingID',
          columnKey: bookingID
        });
      }
      try {
        if (existingTransaction.length !== 0) {
          transaction = existingTransaction.data[0];
          this.discountMode = transaction.discountMode;
          this.discountValue = transaction.discountValue;
          this.cashRemarks = transaction.cashRemarks;
          if (transaction.discountValue > 0) {
            this.alreadyDiscounted = true;
          }
        }
      } catch (error) {
      }
      const response = await axios.post(`${this.API_URL}transaction/item/filter/`, [
        { "columnName": "bookingID", "columnKey": bookingID },
        { "columnName": "itemName", "columnKey": item.room_name }
      ])
      if (response.data.length > 0) {
        //show instead
        //update this.cart
        this.cart = [];
        if (groupbookings.length > 0) {
          const response = await axios.post(`${this.API_URL}transaction/item/filter/`, [
            { "columnName": "groupkey", "columnKey": gkey },
          ])
          response.data.forEach(item => {
            let newItem = {
              id: item.id,
              name: item.itemName,
              type: item.itemType,
              priceRate: item.itemPriceRate,
              purqty: item.purchaseQty,
              totalCartPrice: item.totalCost,
              category: item.category,
              itemOption: item.itemOption
            };
            this.cart.push(newItem);
          });
        } else {
          const response = await axios.post(`${this.API_URL}transaction/item/filter/`, [
            { "columnName": "bookingID", "columnKey": bookingID },
          ])
          if (response.data.length > 0) {
            try {
              response.data.forEach(item => {
                let newItem = {
                  id: item.id,
                  name: item.itemName,
                  type: item.itemType,
                  priceRate: item.itemPriceRate,
                  purqty: item.purchaseQty,
                  totalCartPrice: item.totalCost,
                  category: item.category,
                  itemOption: item.itemOption
                };
                this.cart.push(newItem);
              });
            } catch (error) {
              console.log(error);
            }
          }
        }
      }
      this.billing.clientName = item.name;
      this.billing.clientAddress = item.clientaddress;
      this.billing.clientPhone = item.contactNumber;
      this.billing.clientEmail = item.clientemail;
      this.billing.clientNationality = item.clientnationality;
      this.billing.clientType = item.clientType;
      if (existingTransaction.data[0] !== undefined) {
        this.billing.bookingID = existingTransaction.data[0].id;
        this.isItNew = true;
      } else {
        this.billing.bookingID = "";
      }
      try {
        this.partialPayment = (groupbookings.length === 0) ? item.partialPayment : transaction.cashAmountPay;
        const response = await axios.post(`${this.API_URL}transaction/record/filter/`, [
          { "columnName": "transaction", "columnKey": transaction.id },
        ]);
        this.cashHistory = response.data;
        this.gbookingscount = (groupbookings.length === 0) ? 1 : groupbookings.length;
      } catch (error) {
      }
      this.toggleItemModal();
      $("#others-tab").tab('show');
      this.movetocartFlag = true;
      this.activeAccountFlag = true;
      this.itemCart = {
        id: 0,
        name: "",
        priceRate: "",
        rate: "",
        counter: "",
        purqty: "",
        totalCartPrice: "",
        category: "",
        groupkey: "",
      }
    },
    removeDuplicates(groupBookings) {
      if (!groupBookings) {
        return [];
      }
      const uniqueBookings = [];
      const roomNames = new Set();
      groupBookings.forEach((booking) => {
        if (!roomNames.has(booking.room_name)) {
          roomNames.add(booking.room_name);
          uniqueBookings.push(booking);
        }
      });
      return uniqueBookings;
    },
    async moveToCart() {
      this.movetocartFlag = false;
      const item = this.bookings[this.itemIndex];
      const bookingID = item.itemID;
      let existingTransaction = null;
      let transaction = null;
      let gkey = "";
      let groupbookings = [];
      item.remarks = this.reservation.remarks;
      this.updateBookings(item.id)
      try {
        gkey = (this.bookings[this.itemIndex].groupkey || "x");
        try {
          const o = await axios.post(`${this.API_URL}bookings/filter/`, [
            { "columnName": "groupkey", "columnKey": gkey },
          ])
          groupbookings = o.data;
        } catch (error) {
        }
      } catch (error) {
      }
      if (groupbookings.length > 0) {
        existingTransaction = await axios.post(`${this.API_URL}transaction/filter/`, {
          columnName: 'groupkey',
          columnKey: gkey
        });
      } else {
        existingTransaction = await axios.post(`${this.API_URL}transaction/filter/`, {
          columnName: 'bookingID',
          columnKey: bookingID
        });
      }
      try {
        if (existingTransaction.length !== 0) {
          transaction = existingTransaction.data[0];
          this.discountMode = transaction.discountMode;
          this.discountValue = transaction.discountValue;
          this.cashRemarks = transaction.cashRemarks;
          if (transaction.discountValue > 0) {
            this.alreadyDiscounted = true;
          }
        }
      } catch (error) {
      }
      const response = await axios.post(`${this.API_URL}transaction/item/filter/`, [
        { "columnName": "bookingID", "columnKey": bookingID },
        { "columnName": "itemName", "columnKey": item.room_name }
      ])
      if (response.data.length === 0) {
        if (groupbookings.length > 0) {
          groupbookings.forEach(async res => {
            const numDays = Math.ceil((new Date(res.checkoutDate.split('/')[2] + "-" + res.checkoutDate.split('/')[1] + "-" + res.checkoutDate.split('/')[0]).setHours(0, 0, 0, 0) - new Date(res.checkinDate.split('/')[2] + "-" + res.checkinDate.split('/')[1] + "-" + res.checkinDate.split('/')[0]).setHours(0, 0, 0, 0)) / (1000 * 60 * 60 * 24));
            this.itemCart.id = this.cart.length + 1;
            this.itemCart.name = res.room_name;
            this.itemCart.type = res.room_type;
            this.itemCart.priceRate = res.room_price + "/check-in";
            this.itemCart.purqty = numDays + 1;
            this.itemCart.totalCartPrice = parseFloat(res.room_price) * (numDays + 1);
            this.itemCart.category = "main";
            this.itemCart.itemOption = "room";
            const data = {
              bookingID: res.itemID,
              itemName: this.itemCart.name,
              itemType: this.itemCart.type,
              itemPriceRate: this.itemCart.priceRate,
              purchaseQty: this.itemCart.purqty,
              totalCost: this.itemCart.totalCartPrice,
              category: this.itemCart.category,
              itemOption: this.itemCart.itemOption,
              dateCreated: new Date(), // Set the dateCreated field to the current date and time
              groupkey: gkey,
            };
            // Make a POST request to the API to save the data
            await axios.post(this.API_URL + 'transaction/item/', data)
              .then(response => {
                // Log a success message to the console
                this.itemCart = {}
                this.itemCart.id = response.data.id;
                this.itemCart.name = response.data.itemName;
                this.itemCart.type = response.data.itemType;
                this.itemCart.priceRate = response.data.itemPriceRate;
                this.itemCart.purqty = response.data.purchaseQty;
                this.itemCart.totalCartPrice = response.data.totalCost;
                this.itemCart.category = response.data.category;
                this.itemCart.itemOption = response.data.itemOption;
                this.itemCart.groupkey = response.data.groupkey;
                this.cart.push(this.itemCart)
              })
              .catch(error => {
                // Log an error message to the console
                console.error('Error saving data:', error);
              });
          })
        } else {
          const numDays = Math.ceil((new Date(item.checkoutDate.split('/')[2] + "-" + item.checkoutDate.split('/')[1] + "-" + item.checkoutDate.split('/')[0]).setHours(0, 0, 0, 0) - new Date(item.checkinDate.split('/')[2] + "-" + item.checkinDate.split('/')[1] + "-" + item.checkinDate.split('/')[0]).setHours(0, 0, 0, 0)) / (1000 * 60 * 60 * 24));
          this.itemCart.id = this.cart.length + 1;
          this.itemCart.name = item.room_name;
          this.itemCart.type = item.room_type;
          this.itemCart.priceRate = item.room_price + "/check-in";
          this.itemCart.purqty = numDays + 1;
          this.itemCart.totalCartPrice = parseFloat(item.room_price) * (numDays + 1);
          this.itemCart.category = "main";
          this.itemCart.itemOption = "room";
          const data = {
            bookingID: this.bookings[this.itemIndex].itemID,
            itemName: this.itemCart.name,
            itemType: this.itemCart.type,
            itemPriceRate: this.itemCart.priceRate,
            purchaseQty: this.itemCart.purqty,
            totalCost: this.itemCart.totalCartPrice,
            category: this.itemCart.category,
            itemOption: this.itemCart.itemOption,
            dateCreated: new Date(), // Set the dateCreated field to the current date and time
          };
          // Make a POST request to the API to save the data
          await axios.post(this.API_URL + 'transaction/item/', data)
            .then(response => {
              // Log a success message to the console
              console.log('Data saved:', response.data);
            })
            .catch(error => {
              // Log an error message to the console
              console.error('Error saving data:', error);
            });
          this.cart.push(this.itemCart);
        }
      } else {
        //show instead
        //update this.cart
        this.cart = [];
        if (groupbookings.length > 0) {
          const response = await axios.post(`${this.API_URL}transaction/item/filter/`, [
            { "columnName": "groupkey", "columnKey": gkey },
          ])
          response.data.forEach(item => {
            let newItem = {
              id: item.id,
              name: item.itemName,
              type: item.itemType,
              priceRate: item.itemPriceRate,
              purqty: item.purchaseQty,
              totalCartPrice: item.totalCost,
              category: item.category,
              itemOption: item.itemOption
            };
            this.cart.push(newItem);
          });
        } else {
          const response = await axios.post(`${this.API_URL}transaction/item/filter/`, [
            { "columnName": "bookingID", "columnKey": bookingID },
          ])
          if (response.data.length > 0) {
            try {
              response.data.forEach(item => {
                let newItem = {
                  id: item.id,
                  name: item.itemName,
                  type: item.itemType,
                  priceRate: item.itemPriceRate,
                  purqty: item.purchaseQty,
                  totalCartPrice: item.totalCost,
                  category: item.category,
                  itemOption: item.itemOption
                };
                this.cart.push(newItem);
              });
            } catch (error) {
              console.log(error);
            }
          }
        }
      }
      this.billing.clientName = item.name;
      this.billing.clientAddress = item.clientaddress;
      this.billing.clientPhone = item.contactNumber;
      this.billing.clientEmail = item.clientemail;
      this.billing.clientNationality = item.clientnationality;
      this.billing.clientType = item.clientType;
      if (existingTransaction.data[0] !== undefined) {
        this.billing.bookingID = existingTransaction.data[0].id;
        this.isItNew = true;
      } else {
        this.billing.bookingID = "";
      }
      try {
        this.partialPayment = (groupbookings.length === 0) ? item.partialPayment : transaction.cashAmountPay;
        const response = await axios.post(`${this.API_URL}transaction/record/filter/`, [
          { "columnName": "transaction", "columnKey": transaction.id },
        ]);
        this.cashHistory = response.data;
        this.gbookingscount = (groupbookings.length === 0) ? 1 : groupbookings.length;
      } catch (error) {
      }
      this.toggleItemModal();
      $("#others-tab").tab('show');
      this.movetocartFlag = true;
      this.activeAccountFlag = true;
      this.itemCart = {
        id: 0,
        name: "",
        priceRate: "",
        rate: "",
        counter: "",
        purqty: "",
        totalCartPrice: "",
        category: "",
        groupkey: "",
      }
    },
    cancelReservation() {
      this.$swal.fire({
        icon: 'warning',
        title: 'Are you sure?',
        text: 'Are you sure you want to cancel this reservation?',
        confirmButtonText: 'Yes',
        cancelButtonText: 'No',
        showCancelButton: true
      }).then((result) => {
        // Check if user confirmed the cancellation
        if (result.isConfirmed) {
          // Perform reservation cancellation logic here
          this.bookings[this.itemIndex].status = 'cancelled';
          this.bookings[this.itemIndex].cancellationDate = new Date();
          this.updateBookings(this.bookings[this.itemIndex].id);
          this.changeItemColor("cancelled");
          this.taskRecord(`action:/cancel reservation/client:/${this.bookings[this.itemIndex].name}`)
          this.toggleItemModal();
          // Display success message using SweetAlert
          this.$swal.fire({
            icon: 'success',
            title: 'Reservation Canceled!',
            text: 'The reservation has been canceled.',
            confirmButtonText: 'OK'
          }).then(response => {
            document.location.reload();
          })
        }
      })
    },
    async transferRoom() {
      if (this.toggleselect === false) {
        this.reservation.roomName = "";
        this.toggleselect = true;
        this.roomSelect = "ok";
      } else {
        const item = this.bookings[this.itemIndex];
        const room = this.reservation.roomName;
        if (room.name === undefined) {
          return;
        }
        const oldroom = {
          name: this.bookings[this.itemIndex].room_name,
          type: this.bookings[this.itemIndex].room_type,
          price: this.bookings[this.itemIndex].room_price
        }
        const newroom = {
          name: room.name,
          type: room.type,
          price: room.price
        }
        const result = await this.$swal.fire({
          icon: 'warning',
          title: 'Are you sure?',
          text: 'Are you sure you want to transfer from ' + oldroom.name + ' to ' + newroom.name + '?',
          confirmButtonText: 'Yes',
          cancelButtonText: 'No',
          showCancelButton: true
        })
        if (!result.isConfirmed) {
          return;
        }
        if (oldroom.type !== newroom.type && (oldroom.type !== 'BEACH COTTAGE' && newroom.type !== 'BEACH COTTAGE')) {
          this.$swal({
            title: "Transfer Error",
            text: "Room types do not match. Unable to transfer room.",
            icon: "error",
            buttons: {
              confirm: {
                text: "OK",
                value: true,
                visible: true,
                className: "confirm-button",
                closeModal: true
              }
            }
          });
          return;
        }
        if (oldroom.price !== newroom.price) {
          this.$swal({
            title: "Transfer Error",
            text: "Room prices do not match. Unable to transfer room.",
            icon: "error",
            buttons: {
              confirm: {
                text: "OK",
                value: true,
                visible: true,
                className: "confirm-button",
                closeModal: true
              }
            }
          });
          return;
        }
        item.room_name = newroom.name;
        item.room_price = newroom.price;
        item.room_type = newroom.type;
        item.remarks = "transferred from: " + oldroom.name + " on " + formatDate();
        this.updateBookings(item.id);
        const existingTransactionItems = await axios.post(`${this.API_URL}transaction/item/filter/`, {
          columnName: 'bookingID',
          columnKey: item.itemID
        });
        try {
          await axios.put(`${this.API_URL}transaction/item/${existingTransactionItems.data[0].id}/`, {
            bookingID: existingTransactionItems.data[0].bookingID,
            itemName: newroom.name,
            itemType: existingTransactionItems.data[0].itemType,
            itemPriceRate: existingTransactionItems.data[0].itemPriceRate,
            purchaseQty: existingTransactionItems.data[0].purchaseQty,
            totalCost: existingTransactionItems.data[0].totalCost,
            category: existingTransactionItems.data[0].category,
            itemOption: existingTransactionItems.data[0].itemOption,
          });
        } catch (error) {
        }
        this.taskRecord(`action:/transfer guest/client:/${item.name}`)
        this.$swal.fire({
          icon: 'success',
          title: 'Room Transfer',
          text: 'Room transferred successfully.',
          confirmButtonText: 'OK'
        }).then(response => {
          document.location.reload();
        })
      }
    },
    async extendBooking() {
      const result = await this.$swal.fire({
        icon: 'warning',
        title: 'Are you sure?',
        text: 'Are you sure you want to extend this guest?',
        confirmButtonText: 'Yes',
        cancelButtonText: 'No',
        showCancelButton: true
      })
      if (!result.isConfirmed) {
        return;
      }
      const item = this.bookings[this.itemIndex];
      const bId = item.id;
      const bookingID = item.itemID;
      const groupkey = (item.groupkey || '');
      const roomPrice = parseFloat(item.room_price);
      let groupbookings = [];
      let existingTransactionItems = [];
      // if (groupkey.length > 0) {
      //   try {
      //     const o = await axios.post(`${this.API_URL}bookings/filter/`, [
      //       { "columnName": "groupkey", "columnKey": groupkey },
      //     ])
      //     groupbookings = o.data;
      //   } catch (error) {
      //   }
      // }
      // if (groupbookings.length > 0) {
      //   existingTransactionItems = await axios.post(`${this.API_URL}transaction/item/filter/`, {
      //     columnName: 'groupkey',
      //     columnKey: groupkey
      //   });
      // } else {
      //   existingTransactionItems = await axios.post(`${this.API_URL}transaction/item/filter/`, {
      //     columnName: 'bookingID',
      //     columnKey: bookingID
      //   });
      // }
      existingTransactionItems = await axios.post(`${this.API_URL}transaction/item/filter/`, {
        columnName: 'bookingID',
        columnKey: bookingID
      });
      // if (groupbookings.length > 0) {
      //   groupbookings.forEach(async item => {
      //     let itemIndex = this.bookings.findIndex(
      //       o => o.itemID === item.itemID
      //     );
      //     const bookingData = null;
      //     const itemCheckout = new Date(parseDate(item.checkoutDate));
      //     const extendItemCheckout = new Date(itemCheckout.setDate(itemCheckout.getDate() + 1))
      //     const newCheckoutString = extendItemCheckout.toLocaleDateString("en-GB")
      //     const newTotalPrice = parseFloat(this.bookings[itemIndex].totalPrice) + parseFloat(this.bookings[itemIndex].room_price);
      //     try {
      //       bookingData = {
      //         itemID: this.bookings[itemIndex].itemID,
      //         status: this.bookings[itemIndex].status,
      //         name: this.bookings[itemIndex].name,
      //         clientemail: this.bookings[itemIndex].clientemail,
      //         clientaddress: this.bookings[itemIndex].clientaddress,
      //         clientnationality: this.bookings[itemIndex].clientnationality,
      //         clientType: this.bookings[itemIndex].clientType,
      //         checkinDate: this.bookings[itemIndex].checkinDate,
      //         checkoutDate: newCheckoutString,
      //         room_name: this.bookings[itemIndex].room_name,
      //         room_price: this.bookings[itemIndex].room_price,
      //         room_type: this.bookings[itemIndex].room_type,
      //         remarks: this.bookings[itemIndex].remarks,
      //         contactNumber: this.bookings[itemIndex].contactNumber,
      //         actualCheckoutDate: this.bookings[itemIndex].actualCheckoutDate,
      //         cancellationDate: this.bookings[itemIndex].cancellationDate,
      //         isPaid: "partial",
      //         totalPrice: newTotalPrice,
      //         partialPayment: this.bookings[itemIndex].partialPayment,
      //         processedBy: this.userdata.fName + " " + this.userdata.lName,
      //         groupkey: this.bookings[itemIndex].groupkey,
      //       };
      //       await axios.put(this.API_URL + `bookings/${this.bookings[itemIndex].id}/`, bookingData);
      //     } catch (error) {
      //       console.log(error);
      //     }
      //   })
      // } else {
      //   const itemCheckout = new Date(parseDate(this.bookings[this.itemIndex].checkoutDate));
      //   const extendItemCheckout = new Date(itemCheckout.setDate(itemCheckout.getDate() + 1))
      //   const newCheckoutString = extendItemCheckout.toLocaleDateString("en-GB")
      //   const newTotalPrice = parseFloat(this.bookings[this.itemIndex].totalPrice) + parseFloat(this.bookings[this.itemIndex].room_price);
      //   this.bookings[this.itemIndex].checkoutDate = newCheckoutString;
      //   this.bookings[this.itemIndex].isPaid = "partial";
      //   this.bookings[this.itemIndex].totalPrice = newTotalPrice;
      //   this.updateBookings(bId);
      // }
      const itemCheckout = new Date(parseDate(this.bookings[this.itemIndex].checkoutDate));
      const extendItemCheckout = new Date(itemCheckout.setDate(itemCheckout.getDate() + 1))
      const newCheckoutString = extendItemCheckout.toLocaleDateString("en-GB")
      const newTotalPrice = parseFloat(this.bookings[this.itemIndex].totalPrice) + parseFloat(this.bookings[this.itemIndex].room_price);
      this.bookings[this.itemIndex].checkoutDate = newCheckoutString;
      this.bookings[this.itemIndex].isPaid = "partial";
      this.bookings[this.itemIndex].totalPrice = newTotalPrice;
      this.updateBookings(bId);
      existingTransactionItems.data.filter(o => o.itemOption === 'room').forEach(async item => {
        try {
          await axios.put(`${this.API_URL}transaction/item/${item.id}/`, {
            bookingID: item.bookingID,
            itemName: item.itemName,
            itemType: item.itemType,
            itemPriceRate: item.itemPriceRate,
            purchaseQty: parseFloat(item.purchaseQty) + 1,
            totalCost: parseFloat(item.totalCost) + roomPrice,
            category: item.category,
            itemOption: item.itemOption,
          });
        } catch (error) {
        }
      });
      this.taskRecord(`action:/extend guest/client:/${this.bookings[this.itemIndex].name}`)
      // this.updateBookings(this.bookings[bId].id);
      this.toggleItemModal();
      this.$swal.fire({
        icon: 'success',
        title: 'Guest Extended!',
        text: 'Thank you for extending the guest.',
        confirmButtonText: 'OK'
      }).then(response => {
        document.location.reload();
      })
    },
    checkinGuest() {
      this.$swal.fire({
        icon: 'warning',
        title: 'Are you sure?',
        text: 'Are you sure you want to check in this guest?',
        confirmButtonText: 'Yes',
        cancelButtonText: 'No',
        showCancelButton: true
      }).then((result) => {
        if (result.isConfirmed) {

          axios.post(`${this.API_URL}rooms/filter/`, [
            { columnName: 'name', columnKey: this.bookings[this.itemIndex].room_name },
          ]).then(response => {
            const status = response.data[0].status;
            const category = response.data[0].type;
            if (status === 'dirty' && (category === 'BEACH ROOM' || category === 'POOL ROOM')) {
              this.$swal({
                title: "Error!",
                text: "Uncleaned room, not ready for check-in. Contact housekeeping first.",
                icon: "error",
              }).then((result) => {
                this.toggleItemModal();
                return;
              })
            } else {
              const item = this.bookings[this.itemIndex];
              item.remarks = this.reservation.remarks;
              item.status = "checkedin";
              this.updateBookings(item.id);
              this.populateCalendarItems();
              //this.changeItemColor("checkedin");
              this.toggleItemModal();
              this.taskRecord(`action:/checked-in guest/client:/${item.name}`)
              this.$swal.fire({
                icon: 'success',
                title: 'Guest Checked In!',
                text: 'Thank you for checking in the guest.',
                confirmButtonText: 'OK'
              }).then(response => {
                document.location.reload();
              })
            }
          })

        }
      })
    },
    checkOutGuest() {
      this.$swal.fire({
        icon: 'warning',
        title: 'Are you sure?',
        text: 'Are you sure you want to check out this guest?',
        confirmButtonText: 'Yes',
        cancelButtonText: 'No',
        showCancelButton: true
      }).then((result) => {
        // Check if user confirmed the cancellation
        if (result.isConfirmed) {
          // Perform reservation cancellation logic here
          axios.post(`${this.API_URL}restoorders/filter/`, [
            { columnName: 'customer_name', columnKey: this.bookings[this.itemIndex].room_name },
            { columnName: 'status', columnKey: 'closed' },
          ])
            .then(response => {
              let checkTable = null;
              let restoStatus = null;
              try {
                const tableID = response.data[0].table_id;
                restoStatus = response.data[0].status;
                checkTable = this.rooms.find(table => table.id === tableID).name;
              } catch (error) {
                checkTable = this.bookings[this.itemIndex].room_name;
                restoStatus = "closed";
              }
              if (checkTable === this.bookings[this.itemIndex].room_name) {
                if (restoStatus !== "closed") {
                  this.$swal.fire({
                    icon: 'error',
                    title: 'Customer Checkout Restricted',
                    text: 'Customer has outstanding payables in the restaurant; cannot be checked out yet!',
                    confirmButtonText: 'OK'
                  });
                  return
                } else {
                  let roomId = -1;
                  axios.post(`${this.API_URL}rooms/filter/`, [
                    { columnName: 'name', columnKey: this.bookings[this.itemIndex].room_name },
                  ]).then(response => {
                    roomId = response.data[0].id;
                    axios.put(`${this.API_URL}rooms/${roomId}/`, {
                      name: response.data[0].name,
                      type: response.data[0].type,
                      price: response.data[0].price,
                      isAvailable: response.data[0].isAvailable,
                      status: 'dirty'
                    }).then(response => {
                      this.bookings[this.itemIndex].status = "checkedout";
                      this.bookings[this.itemIndex].actualCheckoutDate = new Date();
                      this.reservation.status = "vacant";
                      this.updateBookings(this.bookings[this.itemIndex].id);
                      this.populateCalendarItems();
                      //this.changeItemColor("checkedout");
                      this.toggleItemModal();
                      this.taskRecord(`action:/checked-out guest/client:/${this.bookings[this.itemIndex].name}`)
                      // Display success message using SweetAlert
                      this.$swal.fire({
                        icon: 'success',
                        title: 'Guest Checked Out!',
                        text: 'The guest has been checked out.',
                        confirmButtonText: 'OK'
                      }).then(response => {
                        document.location.reload();
                      })
                    })
                  })

                }
              }
            })
        }
      });
    },
    //methods for calendar items
    periodChanged() {
      // range, eventSource) {
      // Demo does nothing with this information, just including the method to demonstrate how
      // you can listen for changes to the displayed range and react to them (by loading items, etc.)
      //console.log(eventSource)
      //console.log(range)
    },
    thisMonth(d, h, m) {
      const t = new Date()
      return new Date(t.getFullYear(), t.getMonth(), d, h || 0, m || 0)
    },
    clickDay() {
      let today = new Date();
      if (this.dayreserve.setHours(0, 0, 0, 0) >= today.setHours(0, 0, 0, 0)) {
        this.selectionStart = null
        this.selectionEnd = null
        this.toggledayMenuModal();
        this.toggleItemModal();
        this.toggleselect = false;
        this.roomSelect = "ok";
        this.reservation.clientName = "";
        this.reservation.clientEmail = "";
        this.reservation.clientAddress = "";
        this.reservation.clientNationality = "Filipino";
        this.reservation.clientType = "in-house";
        this.reservation.roomName = "";
        this.reservation.remarks = "";
        // this.reservation.numguests = "";
        this.reservation.clientPhone = "";
        this.reservation.checkinDate = this.dayreserve.toLocaleDateString('en-GB');
        this.reservation.checkoutDate = formatDate(this.dayreserve);
        this.reservation.status = "vacant";
      }
    },
    viewAllReservation() {
      this.convDate = this.dayreserve.toLocaleDateString('en-GB');
      this.toggledayMenuModal();
      this.toggleShowAllModal();
    },
    onClickDay(d) {
      if (this.booksearchtext !== "") {
        this.$swal.fire({
          icon: 'error',
          title: 'Calendar Day Selection Restricted',
          text: 'Unable to select a day on the calendar when the search query is not empty.',
          confirmButtonText: 'OK'
        });
        return;
      }
      this.dayreserve = d;
      this.roomSelect = "ok";
      this.toggledayMenuModal();
    },
    onClickItem(e) {
      if (this.booksearchtext !== "") {
        this.$swal.fire({
          icon: 'error',
          title: 'Calendar Item Selection Restricted',
          text: 'Unable to select an item on the calendar when the search query is not empty.',
          confirmButtonText: 'OK'
        });
        return;
      }
      this.itemIndex = this.bookings.findIndex(
        o => o.itemID === e.id
      );
      this.showReservation();
    },
    showReservation() {
      this.toggleselect = false;
      this.roomSelect = "ok";
      this.reservation.clientName = this.bookings[this.itemIndex].name;
      this.reservation.clientEmail = this.bookings[this.itemIndex].clientemail;
      this.reservation.clientAddress = this.bookings[this.itemIndex].clientaddress;
      this.reservation.clientNationality = this.bookings[this.itemIndex].clientnationality;
      this.reservation.clientType = this.bookings[this.itemIndex].clientType;
      this.reservation.checkinDate = this.bookings[this.itemIndex].checkinDate;
      this.reservation.checkoutDate = this.bookings[this.itemIndex].checkoutDate;
      this.reservation.roomName = this.bookings[this.itemIndex].room_name;
      this.reservation.remarks = this.bookings[this.itemIndex].remarks;
      this.reservation.clientPhone = this.bookings[this.itemIndex].contactNumber;
      this.reservation.status = this.bookings[this.itemIndex].status;
      this.reservation.isPaid = this.bookings[this.itemIndex].isPaid;
      // this.reservation.numguests = this.bookings[this.itemIndex].numguests;
      this.toggleItemModal();
    },
    setShowDate(d) {
      this.message = `Changing calendar view to ${d.toLocaleDateString()}`
      this.showDate = d
    },
    setSelection(dateRange) {
      this.selectionEnd = dateRange[1]
      this.selectionStart = dateRange[0]
    },
    finishSelection(dateRange) {
      const currentDate = new Date(); // get current date
      if (dateRange[0].setHours(0, 0, 0, 0) < currentDate.setHours(0, 0, 0, 0)) { // check if start date is before current date
        // prompt user to select a valid start date
        return;
      }
      this.setSelection(dateRange)
      this.message = `You selected: ${this.selectionStart.toLocaleDateString()} -${this.selectionEnd.toLocaleDateString()}`
      this.toggleselect = false;
      this.roomSelect = "ok";
      this.reservation.status = "vacant";
      this.reservation.clientName = "";
      this.reservation.clientEmail = "";
      this.reservation.clientAddress = "";
      this.reservation.clientNationality = "Filipino";
      this.reservation.clientType = "in-house";
      this.reservation.roomName = "";
      this.reservation.roomPrice = "";
      this.reservation.roomType = "";
      this.reservation.roomPrice = "";
      // this.reservation.numguests = "";
      this.reservation.remarks = "";
      this.reservation.clientPhone = "";
      this.toggleItemModal();
      this.reservation.checkinDate = this.selectionStart.toLocaleDateString('en-GB');
      this.reservation.checkoutDate = formatDate(new Date(parseDate(this.selectionEnd.toLocaleDateString('en-GB'))));
    },
    onDrop(item, date) {
      const currentDate = new Date(); // get current date
      if (date.setHours(0, 0, 0, 0) < currentDate.setHours(0, 0, 0, 0)) { // check if start date is before current date
        // prompt user to select a valid start date
        return;
      }
      this.itemIndex = this.bookings.findIndex(
        o => o.itemID === item.id
      );
      //issue in reloading
      const itemStatus = this.bookings[this.itemIndex].status;
      if (itemStatus === "reserved") {
        const eLength = CalendarMath.dayDiff(item.startDate, date)
        let landingDateCheckin = CalendarMath.addDays(item.startDate, eLength);
        let landingDateCheckout = CalendarMath.addDays(item.endDate, eLength);
        let filteredBookings = this.bookings.filter(booking => booking.status === 'reserved' && booking.itemID !== this.bookings[this.itemIndex].itemID && booking.room_name === this.bookings[this.itemIndex].room_name && new Date(booking.checkinDate.split('/')[2] + "-" + booking.checkinDate.split('/')[1] + "-" + booking.checkinDate.split('/')[0]).setHours(0, 0, 0, 0) <= landingDateCheckout.setHours(0, 0, 0, 0)
          && new Date(booking.checkoutDate.split('/')[2] + "-" + booking.checkoutDate.split('/')[1] + "-" + booking.checkoutDate.split('/')[0]).setHours(0, 0, 0, 0) >= landingDateCheckin.setHours(0, 0, 0, 0));
        if (filteredBookings.length === 0) {
          if (event.ctrlKey) {
            let sd = CalendarMath.addDays(item.startDate, 0)
            let ed = CalendarMath.addDays(item.endDate, eLength - CalendarMath.dayDiff(item.startDate, item.endDate))
            if (ed >= sd) {
              item.originalItem.startDate = sd
              item.originalItem.endDate = ed
            } else {
              item.originalItem.endDate = item.endDate
              item.originalItem.startDate = ed
            }
          } else {
            item.originalItem.startDate = CalendarMath.addDays(item.startDate, eLength)
            item.originalItem.endDate = CalendarMath.addDays(item.endDate, eLength)
          }
          this.bookings[this.itemIndex].checkinDate = item.originalItem.startDate.toLocaleDateString('en-GB');
          this.bookings[this.itemIndex].checkoutDate = item.originalItem.endDate.toLocaleDateString('en-GB');
          this.updateBookings(this.bookings[this.itemIndex].id);
          //this.reloadData();
          this.populateCalendarItems();
          this.taskRecord(`action:/adjust date reservation/client:/${this.bookings[this.itemIndex].name}`)
        } else {
          this.$swal.fire({
            icon: 'error',
            title: 'Cannot Adjust Reservation',
            text: 'Dates conflict with an existing room reservation.',
            confirmButtonText: 'OK'
          });
        }
      }
    },
    async updateBookings(pk) {
      try {
        const response = await axios.put(this.API_URL + `bookings/${pk}/`, {
          itemID: this.bookings[this.itemIndex].itemID,
          status: this.bookings[this.itemIndex].status,
          name: this.bookings[this.itemIndex].name,
          clientemail: this.bookings[this.itemIndex].clientemail,
          clientaddress: this.bookings[this.itemIndex].clientaddress,
          clientnationality: this.bookings[this.itemIndex].clientnationality,
          clientType: this.bookings[this.itemIndex].clientType,
          checkinDate: this.bookings[this.itemIndex].checkinDate,
          checkoutDate: this.bookings[this.itemIndex].checkoutDate,
          room_name: this.bookings[this.itemIndex].room_name,
          room_price: this.bookings[this.itemIndex].room_price,
          room_type: this.bookings[this.itemIndex].room_type,
          remarks: this.bookings[this.itemIndex].remarks,
          contactNumber: this.bookings[this.itemIndex].contactNumber,
          actualCheckoutDate: this.bookings[this.itemIndex].actualCheckoutDate,
          cancellationDate: this.bookings[this.itemIndex].cancellationDate,
          isPaid: this.bookings[this.itemIndex].isPaid,
          totalPrice: this.bookings[this.itemIndex].totalPrice,
          partialPayment: this.bookings[this.itemIndex].partialPayment,
          processedBy: this.userdata.fName + " " + this.userdata.lName,
          groupkey: this.bookings[this.itemIndex].groupkey,
        });
      } catch (error) {
        console.log(error);
      }
    },
    populateCalendarItems() {
      this.calendarItems = this.bookings.map(booking => {
        const startDate = booking.checkinDate.split('/')[2] + "-" + booking.checkinDate.split('/')[1] + "-" + booking.checkinDate.split('/')[0];
        const endDate = booking.checkoutDate.split('/')[2] + "-" + booking.checkoutDate.split('/')[1] + "-" + booking.checkoutDate.split('/')[0];
        const title = `${booking.room_name}-${(booking.groupkey === null) ? '' : '<span class="text-white">group</span>-'}${booking.name}<span style="display:none">~${booking.itemID}~</span>`;
        const id = booking.itemID;
        const tooltip = `${booking.room_name}-${booking.name}\n*${booking.status}-${(booking.isPaid === 'yes') ? 'fully paid' : (booking.isPaid === 'no') ? 'not paid' : 'partial'}`;
        let classes = '';
        if (booking.status === 'reserved') {
          if (booking.isPaid === 'partial' || booking.isPaid === 'yes') {
            classes = ['hotel-reserved'];
          } else {
            classes = ['hotel-reserved-unpaid'];
          }
        } else if (booking.status === 'checkedin') {
          if (booking.isPaid === 'no' || booking.isPaid === '') {
            classes = ['hotel-checkedin-unpaid'];
          } else if (booking.isPaid === 'partial') {
            classes = ['hotel-checkedin-partial'];
          } else {
            classes = ['hotel-checkedin-paid'];
          }
        } else if (booking.status === 'cancelled') {
          classes = ['hotel-cancelled'];
        } else if (booking.status === 'checkedout') {
          classes = ['hotel-checkedout'];
        }
        return { startDate, endDate, title, id, classes, tooltip };
      });
      let suggestionsArray = this.rooms.map(room => room.name);
      const roomStatus = ["cancelled", "reserved", "checkedin", "checkedout"];
      suggestionsArray = roomStatus.concat(suggestionsArray);
      // Filter the suggestions based on the search text
      this.autosuggestions = suggestionsArray.filter(suggestion =>
        suggestion.toLowerCase().includes(this.booksearchtext.toLowerCase())
      );
      this.autosuggestions = this.autosuggestions.slice(0, 15);
      // this.showAutosuggestions = true;
    },
    selectSuggestion(suggestion) {
      this.booksearchtext = suggestion;
      this.showAutosuggestions = false;
      this.populateCalendarItems();
    },
    hideAutosuggestions() {
      // Delay hiding the autosuggestions to allow the click on the suggestion to trigger before hiding
      setTimeout(() => {
        this.showAutosuggestions = true;
      }, 200);
    },
    generateUniqueString() {
      let randomString = '';
      while (randomString.length < 64) {
        randomString += Math.random().toString(36).substr(2, 36);
      }
      randomString = randomString.substr(0, 64);
      return randomString;
    },
    async clickTestAddItem() {
      this.bookNowFlag = false;
      const checkin = parseDate(this.reservation.checkinDate);
      const checkout = parseDate(formatDate2(this.reservation.checkoutDate));
      if (checkout < checkin) {
        this.$swal.fire({
          title: "error",
          text: "Check-out date ≥ Check-in date.",
          icon: "error",
        });
        return false;
      }
      for (const res of this.reservation.roomName) {
        const hasExistingBooking = this.bookings.filter(item => item.status !== 'checkedout').filter(item => item.status !== 'cancelled').filter(booking =>
          booking.room_name === res.name && booking.checkinDate === this.reservation.checkinDate
        );
        if (hasExistingBooking.length > 0) {
          await this.$swal.fire({
            icon: 'error',
            title: 'Booking Error',
            text: `There is already a booking for ${res.name} on ${this.reservation.checkinDate}. Please choose another date or room.`,
          });
          this.reservation.roomName = "";
          return;
        }
      }
      try {
        let gkey = null;
        let roomBooked = this.reservation.roomName;
        if (roomBooked.length > 1) {
          gkey = "group-" + this.generateUniqueString();
        }
        roomBooked.forEach(async res => {
          //change id format
          let id = "e" + new Date().getTime().toString() + this.generateUniqueString();
          let startDate = this.reservation.checkinDate.split('/')[2] + "-" + this.reservation.checkinDate.split('/')[1] + "-" + this.reservation.checkinDate.split('/')[0];
          let endDate = this.reservation.checkoutDate.split('/')[2] + "-" + this.reservation.checkoutDate.split('/')[1] + "-" + this.reservation.checkoutDate.split('/')[0];
          let title = res.name + "-" + this.reservation.clientName;
          const numDays = Math.ceil((
            new Date(this.reservation.checkoutDate.split('/')[2] + "-" + this.reservation.checkoutDate.split('/')[1] + "-" + this.reservation.checkoutDate.split('/')[0]).setHours(0, 0, 0, 0)
            -
            new Date(this.reservation.checkinDate.split('/')[2] + "-" + this.reservation.checkinDate.split('/')[1] + "-" + this.reservation.checkinDate.split('/')[0]).setHours(0, 0, 0, 0)
          ) / (1000 * 60 * 60 * 24));
          const roomPrice = (this.rooms.findIndex(o => o.name === res.name) !== -1) ? this.rooms[this.rooms.findIndex(o => o.name === res.name)].price : 0;
          const roomType = (this.rooms.findIndex(o => o.name === res.name) !== -1) ? this.rooms[this.rooms.findIndex(o => o.name === res.name)].type : '';
          const response = await axios.post(this.API_URL + "bookings/", {
            itemID: id,
            status: "reserved",
            name: this.reservation.clientName,
            clientemail: this.reservation.clientEmail,
            clientaddress: this.reservation.clientAddress,
            clientnationality: this.reservation.clientNationality,
            clientType: this.reservation.clientType,
            checkinDate: this.reservation.checkinDate,
            checkoutDate: formatDate2(this.reservation.checkoutDate),
            room_name: res.name,
            room_price: roomPrice,
            room_type: roomType,
            remarks: this.reservation.remarks,
            // numguests: this.reservation.numguests,
            contactNumber: this.reservation.clientPhone,
            isPaid: 'no',
            created_at: moment().format('YYYY-MM-DD hh:mm:ss'),
            totalPrice: (numDays + 1) * parseFloat(roomPrice),
            partialPayment: 0,
            processedBy: this.userdata.fName + " " + this.userdata.lName,
            groupkey: gkey,
          });
          this.bookings.push({
            itemID: id,
            status: "reserved",
            name: this.reservation.clientName,
            clientemail: this.reservation.clientEmail,
            clientaddress: this.reservation.clientAddress,
            clientnationality: this.reservation.clientNationality,
            clienttype: this.reservation.clientType,
            checkinDate: this.reservation.checkinDate,
            checkoutDate: this.reservation.checkoutDate,
            room_name: res.name,
            room_price: roomPrice,
            room_type: roomType,
            remarks: this.reservation.remarks,
            // numguests: this.reservation.numguests,
            contactNumber: this.reservation.clientPhone,
            processedBy: this.userdata.fName + " " + this.userdata.lName,
            groupkey: gkey,
          })
        });
        this.reloadData();
        this.populateCalendarItems();
        this.taskRecord(`action:/added reservation/client:/${this.reservation.clientName}`)
        this.toggleItemModal();
        this.reservation.clientName = "";
        this.reservation.clientEmail = "";
        this.reservation.clientAddress = "";
        this.reservation.clientNationality = "";
        this.reservation.clientType = "";
        this.reservation.checkinDate = "";
        this.reservation.checkoutDate = "";
        this.reservation.roomName = "";
        this.reservation.roomPrice = "";
        this.reservation.roomType = "";
        this.reservation.roomPrice = "";
        this.reservation.remarks = "";
        // this.reservation.numguests = "";
        this.reservation.clientPhone = "";
        this.walkinStatus = false;
        this.$swal.fire({
          title: "Success!",
          text: "Booking successful!",
          icon: "success",
        }).then(response => {
          document.location.reload();
        })
      } catch (error) {
        console.log(error);
        this.$swal.fire({
          title: "error",
          text: "There is an error!",
          icon: "error",
        });
        this.toggleItemModal();
      }
      this.bookNowFlag = true;
    },
    removeItem() {
      this.calendarItems = this.calendarItems.filter(
        o => o.id !== this.bookings[this.itemIndex].itemID
      );
      this.bookings = this.bookings.filter(
        o => o.itemID !== this.bookings[this.itemIndex].itemID
      );
    },
    async loadTransactionData() {
      try {
        const response = await axios.get(this.API_URL + 'transactions_itemizer/0/');
        this.transactions = response.data;
        // this.transactions.forEach(async (item, index) => {
        //   try {
        //     let a = null;
        //     const gkey = (item.groupkey || "x")
        //     try {
        //       if (gkey === "x") {
        //         a = await axios.post(`${this.API_URL}transaction/item/filter/`, [
        //           { "columnName": 'bookingID', "columnKey": item.bookingID },
        //         ]);
        //       } else {
        //         a = await axios.post(`${this.API_URL}transaction/item/filter/`, [
        //           { "columnName": 'groupkey', "columnKey": gkey },
        //         ]);
        //       }
        //     } catch (error) {
        //     }
        //     const b = await axios.post(`${this.API_URL}transaction/record/filter/`, [
        //       { "columnName": "transaction", "columnKey": item.id },
        //     ])
        //     this.transactions[index].items = a.data;
        //     this.transactions[index].items2 = b.data;
        //   } catch (error) {
        //   }
        // });
      } catch (error) {
        console.error(error); // log any errors
        this.transactions = []; // return an empty array in case of errors
      }
    },
    async placeOrder() {
      if (parseFloat(this.cashAmount) > 0) {
        let bookid = null;
        let groupid = null;
        const item = this.bookings[this.itemIndex];
        let reserveStatus = null;
        try {
          bookid = this.bookings[this.itemIndex].itemID;
          groupid = this.bookings[this.itemIndex].groupkey;
          reserveStatus = this.bookings[this.itemIndex].status
        } catch (error) {
          bookid = "f";
        }
        let gkey = "";
        let groupbookings = [];
        try {
          gkey = (this.bookings[this.itemIndex].groupkey || "x");
          try {
            const o = await axios.post(`${this.API_URL}bookings/filter/`, [
              { "columnName": "groupkey", "columnKey": gkey },
            ])
            groupbookings = o.data;
          } catch (error) {
          }
        } catch (error) {
        }
        if (this.walkinStatus && parseFloat(this.cashAmount) < parseFloat(this.total)) {
          await this.$swal.fire({
            title: 'Error',
            text: 'There is no partial payment for walkin guests.',
            icon: 'error'
          });
          return false;
        }
        const numGuests = this.cart.filter(o => o.type.toLowerCase() === 'entrance').length;
        if (bookid === "f") {
          if (numGuests === 0) {
            await this.$swal.fire({
              title: 'Error',
              text: 'Kindly specify the number of guests by providing the quantity within the general/pool entrance fee.',
              icon: 'error'
            });
            return false;
          }
        } else {
          if (numGuests === 0 && this.bookings[this.itemIndex].status === 'checkedin') {
            await this.$swal.fire({
              title: 'Error',
              text: 'Kindly specify the number of guests by providing the quantity within the general/pool entrance fee.',
              icon: 'error'
            });
            return false;
          }
        }
        // if (reserveStatus === "reserved" && parseFloat(this.cashAmount) > parseFloat(this.total) * 0.50) {
        //   await this.$swal.fire({
        //     title: 'Error',
        //     text: 'The maximum allowable downpayment/partial payment is 50% of the total cost, and it cannot exceed this limit.',
        //     icon: 'error'
        //   });
        //   return false;
        // }
        const confirmMessage = 'Are you sure you want to save this transaction?';
        const result = await this.$swal.fire({
          title: 'Confirmation',
          text: confirmMessage,
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Yes, save it!',
          cancelButtonText: 'Cancel'
        });
        if (result.isConfirmed) {
          const countdownMessage = 'Transaction will be saved in <span id="countdown">5</span> seconds. Do you want to cancel?';
          let countdownResult;
          countdownResult = await this.$swal.fire({
            title: 'Please wait',
            html: countdownMessage,
            icon: 'info',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Confirm now',
            cancelButtonText: 'Cancel',
            didOpen: () => {
              const countdownEl = document.querySelector('#countdown');
              let count = 5;
              const timerId = setInterval(() => {
                countdownEl.textContent = count;
                count--;
                if (count < 0) {
                  clearInterval(timerId);
                  this.$swal.close();
                }
              }, 1000);
            }
          });
          if (!countdownResult.isConfirmed) {
            return;
          }
          try {
            let existingTransaction = {
              data: []
            };
            if (bookid.charAt(0) !== "f") {
              existingTransaction = await axios.post(`${this.API_URL}transaction/filter/`, {
                columnName: 'groupkey',
                columnKey: gkey
              });
              if (existingTransaction.data.length === 0) {
                existingTransaction = {
                  data: []
                };
                existingTransaction = await axios.post(`${this.API_URL}transaction/filter/`, {
                  columnName: 'bookingID',
                  columnKey: bookid
                });
              }
            }
            let payStatus = null;
            if (existingTransaction.data.length === 0) {
              // Create a new transaction if it doesn't exist yet
              if (bookid.charAt(0) === "f") {
                bookid = "f" + existingTransaction.data.length + this.generateUniqueString();
              }
              payStatus = (parseFloat(this.total) - parseFloat(this.cashAmount)) <= 0 ? 'full' : 'partial';
              const updatedcashamount = parseFloat(this.cashAmount) > parseFloat(this.total) ? parseFloat(this.total) : parseFloat(this.cashAmount);
              const transactionData = {
                clientname: this.billing.clientName,
                clientemail: this.billing.clientEmail,
                clientcontact: this.billing.clientPhone,
                clientaddress: this.billing.clientAddress,
                clientnationality: this.billing.clientNationality,
                clientType: this.billing.clientType,
                nonCashReference: this.nonCashPayPlatform + '-' + this.nonCashReference,
                totalAmountToPay: parseFloat(this.total),
                paymentMethod: this.paymentMethod,
                cashAmountPay: updatedcashamount,
                balance: parseFloat(this.total) - updatedcashamount,
                payStatus: payStatus,
                discountMode: this.discountMode,
                discountValue: this.discountValue,
                bookingID: bookid,
                processedBy: this.userdata.fName + " " + this.userdata.lName,
                groupkey: groupid,
                cashRemarks: this.cashRemarks,
              };
              let doneTransaction = await axios.post(`${this.API_URL}transaction/`, transactionData);
              let transactionRecordData = {
                transaction: doneTransaction.data.id,
                transaction_date: doneTransaction.data.transaction_date,
                paymentMethod: doneTransaction.data.paymentMethod,
                nonCashReference: doneTransaction.data.nonCashReference,
                totalAmountToPay: doneTransaction.data.totalAmountToPay,
                cashAmountPay: doneTransaction.data.cashAmountPay,
                balance: doneTransaction.data.balance,
                discountMode: doneTransaction.data.discountMode,
                discountValue: doneTransaction.data.discountValue,
                processedBy: this.userdata.fName + " " + this.userdata.lName,
                payStatus: doneTransaction.data.payStatus
              }
              await axios.post(`${this.API_URL}transaction/record/`, transactionRecordData);
              if (bookid.charAt(0) === "f") {
                this.cart.forEach(async (item, index) => {
                  // Define the API endpoint and data for the PUT request
                  const api = `${this.API_URL}transaction/item/`;
                  const data = {
                    itemName: item.name,
                    itemType: item.type,
                    itemPriceRate: item.priceRate,
                    purchaseQty: item.purqty,
                    totalCost: item.totalCartPrice,
                    category: 'main',
                    itemOption: 'addons',
                    bookingID: bookid
                  };
                  try {
                    await axios.post(api, data);
                  } catch (error) {
                  }
                });
              }
              if (bookid.charAt(0) !== "f") {
                if (groupbookings.length > 0) {
                  groupbookings.forEach(async item => {
                    let itemIndex = this.bookings.findIndex(
                      o => o.itemID === item.itemID
                    );
                    this.bookings[itemIndex].totalPrice = transactionData.totalAmountToPay;
                    this.bookings[itemIndex].partialPayment = transactionData.cashAmountPay;
                    if (payStatus === "partial") {
                      this.bookings[itemIndex].isPaid = "partial";
                    } else {
                      this.bookings[itemIndex].isPaid = "yes";
                    }
                    try {
                      const response = await axios.put(this.API_URL + `bookings/${this.bookings[itemIndex].id}/`, {
                        itemID: this.bookings[itemIndex].itemID,
                        status: this.bookings[itemIndex].status,
                        name: this.bookings[itemIndex].name,
                        clientemail: this.bookings[itemIndex].clientemail,
                        clientaddress: this.bookings[itemIndex].clientaddress,
                        clientnationality: this.bookings[itemIndex].clientnationality,
                        clientType: this.bookings[itemIndex].clientType,
                        checkinDate: this.bookings[itemIndex].checkinDate,
                        checkoutDate: this.bookings[itemIndex].checkoutDate,
                        room_name: this.bookings[itemIndex].room_name,
                        room_price: this.bookings[itemIndex].room_price,
                        room_type: this.bookings[itemIndex].room_type,
                        remarks: this.bookings[itemIndex].remarks,
                        contactNumber: this.bookings[itemIndex].contactNumber,
                        actualCheckoutDate: this.bookings[itemIndex].actualCheckoutDate,
                        cancellationDate: this.bookings[itemIndex].cancellationDate,
                        isPaid: this.bookings[itemIndex].isPaid,
                        totalPrice: this.bookings[itemIndex].totalPrice,
                        partialPayment: this.bookings[itemIndex].partialPayment,
                        processedBy: this.userdata.fName + " " + this.userdata.lName,
                        groupkey: this.bookings[itemIndex].groupkey,
                      });
                    } catch (error) {
                      console.log(error);
                    }
                  })
                } else {
                  this.bookings[this.itemIndex].totalPrice = transactionData.totalAmountToPay;
                  this.bookings[this.itemIndex].partialPayment = transactionData.cashAmountPay;
                  if (payStatus === "partial") {
                    this.bookings[this.itemIndex].isPaid = "partial";
                  } else {
                    this.bookings[this.itemIndex].isPaid = "yes";
                  }
                  this.updateBookings(this.bookings[this.itemIndex].id);
                }
              }
              try {
                this.partialPayment = doneTransaction.data.cashAmountPay;
                const response = await axios.post(`${this.API_URL}transaction/record/filter/`, [
                  { "columnName": "transaction", "columnKey": doneTransaction.data.id },
                ]);
                this.cashHistory = response.data;
                this.gbookingscount = (groupbookings.length === 0) ? 1 : groupbookings.length;

              } catch (error) {
              }
              this.billing.bookingID = doneTransaction.data.id;
            } else {
              // Update the transaction if it already exists
              payStatus = (parseFloat(this.total) - parseFloat(this.cashAmount)) <= 0 ? 'full' : 'partial';
              const transaction = existingTransaction.data[0];
              const existingCashAmountPay = parseFloat(transaction.cashAmountPay);
              const newcashAmountPay = (existingCashAmountPay + parseFloat(this.cashAmount) < parseFloat(this.subtotal)) ? existingCashAmountPay + parseFloat(this.cashAmount) : parseFloat(this.subtotal);
              const existingbalance = transaction.balance;
              let origCash = parseFloat(this.cashAmount) > parseFloat(this.total) ? parseFloat(this.total) : parseFloat(this.cashAmount);
              const newbalance = (existingCashAmountPay + parseFloat(this.cashAmount) < parseFloat(this.subtotal)) ? parseFloat(transaction.totalAmountToPay) - parseFloat(newcashAmountPay) : 0;
              const origbal = parseFloat(this.subtotal) - newcashAmountPay;
              // const payamountnow = (existingbalance - newbalance <= 0) ? origCash : existingbalance - newbalance;
              const payamountnow = origCash;
              const transactionData = {
                clientname: this.billing.clientName,
                clientemail: this.billing.clientEmail,
                clientcontact: this.billing.clientPhone,
                clientaddress: this.billing.clientAddress,
                clientnationality: this.billing.clientNationality,
                clientType: this.billing.clientType,
                totalAmountToPay: parseFloat(this.subtotal),
                paymentMethod: this.paymentMethod,
                nonCashReference: this.nonCashPayPlatform + '-' + this.nonCashReference,
                cashAmountPay: newcashAmountPay,
                balance: origbal,
                payStatus: payStatus,
                discountMode: this.discountMode,
                discountValue: this.discountValue,
                bookingID: bookid,
                processedBy: this.userdata.fName + " " + this.userdata.lName,
                groupkey: groupid,
                cashRemarks: this.cashRemarks,
              };
              let doneTransaction = await axios.put(`${this.API_URL}transaction/${existingTransaction.data[0].id}/`, transactionData);
              let transactionRecordData = {
                transaction: doneTransaction.data.id,
                transaction_date: doneTransaction.data.transaction_date,
                paymentMethod: doneTransaction.data.paymentMethod,
                nonCashReference: doneTransaction.data.nonCashReference,
                totalAmountToPay: doneTransaction.data.totalAmountToPay,
                cashAmountPay: payamountnow,
                balance: parseFloat(doneTransaction.data.balance),
                discountMode: doneTransaction.data.discountMode,
                discountValue: doneTransaction.data.discountValue,
                processedBy: this.userdata.fName + " " + this.userdata.lName,
                payStatus: doneTransaction.data.payStatus
              }
              await axios.post(`${this.API_URL}transaction/record/`, transactionRecordData);
              if (groupbookings.length > 0) {
                groupbookings.forEach(async item => {
                  let itemIndex = this.bookings.findIndex(
                    o => o.itemID === item.itemID
                  );
                  this.bookings[itemIndex].totalPrice = transactionRecordData.totalAmountToPay;
                  this.bookings[itemIndex].partialPayment = newcashAmountPay;
                  if (payStatus === "partial") {
                    this.bookings[itemIndex].isPaid = "partial";
                  } else {
                    this.bookings[itemIndex].isPaid = "yes";
                  }
                  try {
                    const response = await axios.put(this.API_URL + `bookings/${this.bookings[itemIndex].id}/`, {
                      itemID: this.bookings[itemIndex].itemID,
                      status: this.bookings[itemIndex].status,
                      name: this.bookings[itemIndex].name,
                      clientemail: this.bookings[itemIndex].clientemail,
                      clientaddress: this.bookings[itemIndex].clientaddress,
                      clientnationality: this.bookings[itemIndex].clientnationality,
                      clientType: this.bookings[itemIndex].clientType,
                      checkinDate: this.bookings[itemIndex].checkinDate,
                      checkoutDate: this.bookings[itemIndex].checkoutDate,
                      room_name: this.bookings[itemIndex].room_name,
                      room_price: this.bookings[itemIndex].room_price,
                      room_type: this.bookings[itemIndex].room_type,
                      remarks: this.bookings[itemIndex].remarks,
                      contactNumber: this.bookings[itemIndex].contactNumber,
                      actualCheckoutDate: this.bookings[itemIndex].actualCheckoutDate,
                      cancellationDate: this.bookings[itemIndex].cancellationDate,
                      isPaid: this.bookings[itemIndex].isPaid,
                      totalPrice: this.bookings[itemIndex].totalPrice,
                      partialPayment: this.bookings[itemIndex].partialPayment,
                      processedBy: this.userdata.fName + " " + this.userdata.lName,
                      groupkey: this.bookings[itemIndex].groupkey,
                    });
                  } catch (error) {
                    console.log(error);
                  }
                })
              } else {
                this.bookings[this.itemIndex].totalPrice = transactionRecordData.totalAmountToPay;
                this.bookings[this.itemIndex].partialPayment = newcashAmountPay;
                if (payStatus === "partial") {
                  this.bookings[this.itemIndex].isPaid = "partial";
                } else {
                  this.bookings[this.itemIndex].isPaid = "yes";
                }
                this.updateBookings(this.bookings[this.itemIndex].id);
              }
              try {
                this.partialPayment = newcashAmountPay;
                const response = await axios.post(`${this.API_URL}transaction/record/filter/`, [
                  { "columnName": "transaction", "columnKey": transactionRecordData.transaction },
                ]);
                this.cashHistory = response.data;
                this.gbookingscount = (groupbookings.length === 0) ? 1 : groupbookings.length;
              } catch (error) {
              }
            }
            this.taskRecord(`action:/transaction added/client:/${this.billing.clientName}`)
            this.walkinStatus = false;
            await this.$swal.fire({
              title: 'Success',
              text: 'Transaction saved successfully!',
              icon: 'success'
            }).then(response => {
              setTimeout(() => {
                this.generateBillingStatement();
              }, 500);
              //document.location.reload();
            })
          } catch (error) {
            // Show an error message using SweetAlert
            await this.$swal.fire({
              title: 'Error',
              text: 'An error occurred while saving the transaction.',
              icon: 'error'
            });
            console.log(error);
          }
        }
      } else {
        await this.$swal.fire({
          title: 'Error',
          text: 'Invalid entry for cash tendered.',
          icon: 'error'
        });
      }
    },
    async printSection(idstring, pLength, pWidth, ft) {
      const section = document.getElementById(idstring);
      const sectionHTML = section.outerHTML;
      const printBtn = '<div class="row no-print"><div class="col-md-12 text-right"><button class="btn btn-danger" onclick="window.print()">Print Now</button></div></div>';
      const footerContent = `<p class="text-right">Total = ${this.filteredTransactionsTotal}</p><p class="text-right">Collectibles = ${this.filteredTransactionsBalance}</p>`;
      const footerSummary = (ft) ? footerContent : '';
      const bootstrapCSS = `<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"><style>.highlight {background-color: yellow;}body {font-family: Arial, sans-serif;line-height: 1.25;padding: 0.5in;font-size:16px} hr {margin-top: 0.5px;;margin-bottom: 0.5px;} p {margin-top: 0.5px;;margin-bottom: 0.5px;} table {table-layout: auto;width:100%;margin:0 auto;border-collapse:collapse;margin-top: 1px;margin-bottom: 1px;} tr td:last-child{width:1%;white-space:nowrap;} .container {width: ${pWidth}px;height: ${pLength}px;padding-top: 0.25in;padding-bottom: 0.25in;background-color: #fff;box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);margin: auto;}.text-center {text-align: center;}.text-right {text-align: right;}@media print {.no-print {display: none;}}html, body {width: ${pWidth}px;height: ${pLength}px;margin: 0;padding: 0;}}</style>`;
      const bootstrapJS = '<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"><script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"><script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js">';
      const html = `<!doctype html><html><head>${bootstrapCSS}</head><body>${printBtn}${sectionHTML}${footerSummary}${bootstrapJS}<script>setTimeout('alert()',1000)<\/script></body></html>`;
      // Create a new jsPDF instance
      function printAndDetect() {
        const options = 'height=500,width=800,scrollbars=no,status=no,toolbar=no,location=no';
        const printWindow = window.open('', options);
        printWindow.document.write(html);
        printWindow.document.close();
        printWindow.addEventListener('load', function () {
          printWindow.focus();
          printWindow.print();
          printWindow.close();
          document.location.reload();
        });
      }
      printAndDetect();
    },
    async generateBillingStatement() {
      // const response = await axios.get(this.API_URL + "transaction/");
      // this.billing.bookingID = response.data.length.toString()
      this.printSection('billing-details', 1300, 850, false);
    },
    // printReservationHistory() {
    //   this.printSection('reservationHistory', 850, 1300, true);
    // },
    // printTransactionHistory() {
    //   this.printSection('transactionHistory', 850, 1500, true);
    // },
    // printViewReservation() {
    //   this.printSection(this.activeTab, 850, 1400, false);
    // },
    async reloadItemsData() {
      try {
        const response = await axios.get(this.API_URL + "leisures/");
        this.items = response.data.filter(item => item.isAvailable === true);
      } catch (error) {
        console.log(error);
      }
    },
    async reloadData() {
      try {
        const roomsResponse = await axios.get(this.API_URL + "rooms/");
        this.rooms = roomsResponse.data.filter(item => item.isAvailable === true);
        /*
this.bookings.filter(booking => booking.room_name === this.bookings[this.itemIndex].room_name );
        */
        const reservationsResponse = await axios.get(this.API_URL + "bookings/");
        this.origbookings = reservationsResponse.data;
        this.populateCalendarItems()
      } catch (error) {
        console.log(error);
      }
    },
    vacantRoom(roomNumber) {
      const bookingIndex = this.reservations.findIndex(
        reservation =>
          reservation.room_name === roomNumber &&
          new Date(reservation.checkinDate) < new Date() &&
          new Date(reservation.checkoutDate) > new Date()
      );
      return bookingIndex === -1;
    },
    isItemAvailableInCart(item) {
      const itemIndex = this.cart.findIndex(
        o =>
          o.name === item
      );
      return itemIndex === -1;
    },
    isRoomAvailable(room, checkinDate, checkoutDate) {
      // Get all reservations for the given room
      const roomReservations = this.bookings.filter(reservation => reservation.room_name === room);
      // Check if the room is available for the given date range
      for (let i = 0; i < roomReservations.length; i++) {
        const reservation = roomReservations[i];
        if (
          checkinDate < new Date(reservation.checkoutDate) &&
          checkoutDate > new Date(reservation.checkinDate)
        ) {
          return false; // Room is not available
        }
      }
      return true; // Room is available
    },
    async addToCart(item, index) {
      if (this.billing.clientName !== "") {
        // if (this.isItemAvailableInCart(item.item)) {
        let reserveStatus = null;
        try {
          reserveStatus = this.bookings[this.itemIndex].status
        } catch (error) {
          reserveStatus = "n/a";
        }
        if (reserveStatus === "reserved") {
          await this.$swal.fire({
            title: 'Error',
            text: 'No purchase of add-ons until guest is checked in.',
            icon: 'error'
          });
          return false;
        }
        if (this.howMany[index] > 0) {
          this.itemCart.name = item.item;
          this.itemCart.type = item.type;
          this.itemCart.rate = item.rate;
          this.itemCart.counter = item.counter;
          this.itemCart.priceRate = item.priceRate + "/" + item.counter;
          this.itemCart.purqty = this.howMany[index];
          this.itemCart.category = "inclusion";
          this.itemCart.itemOption = "addons";
          this.itemCart.totalCartPrice = parseFloat(item.priceRate) * parseFloat(this.howMany[index]);
          this.$swal.fire({
            title: "Success!",
            text: "Added to cart!",
            icon: "success",
          });
          // Define the data to be sent to the API
          const data = {
            itemName: this.itemCart.name,
            itemType: this.itemCart.type,
            itemPriceRate: this.itemCart.priceRate,
            purchaseQty: this.itemCart.purqty,
            totalCost: this.itemCart.totalCartPrice,
            category: this.itemCart.category,
            itemOption: this.itemCart.itemOption,
            dateCreated: new Date(), // Set the dateCreated field to the current date and time
          };
          try {
            // Access property here
            data.bookingID = this.bookings[this.itemIndex].itemID;
            // Make a POST request to the API to save the data
            await axios.post(this.API_URL + 'transaction/item/', data)
              .then(response => {
                // Log a success message to the console
                this.itemCart.id = response.data.id;
              })
              .catch(error => {
                // Log an error message to the console
                console.error('Error saving data:', error);
              });
          } catch (e) {
            // Handle the error here
            data.bookingID = "walkin";
          }
          console.log(this.itemCart)
          this.cart.push(this.itemCart);
          $("#shopModal").modal("toggle");
          this.howMany[index] = '';
          this.itemCart = {
            id: 0,
            name: "",
            priceRate: "",
            rate: "",
            counter: "",
            purqty: "",
            totalCartPrice: "",
            category: ""
          }
        } else {
          this.$swal.fire({
            title: "Error!",
            text: "Invalid entry for quantity.",
            icon: "error",
          });
        }
        // } else {
        //   this.$swal.fire({
        //     title: "Error!",
        //     text: "Item is already in the cart.",
        //     icon: "error",
        //   });
        // }
      } else {
        this.$swal.fire({
          title: "Error!",
          text: "Supply first client's info.",
          icon: "error",
        }).then((result) => {
          this.howMany[index] = '';
          this.toggleAddAccountModal();
        });
      }
    },
    cancelItem(item) {
      this.$swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Yes, delete it!'
      }).then((result) => {
        if (result.isConfirmed) {
          this.cart = this.cart.filter(
            o => o.id !== item.id
          );
          if (this.itemIndex !== -1) {
            axios.get(this.API_URL + `transaction/item/delete/${item.id}/`)
              .then(response => {
                this.$swal.fire(
                  'Deleted!',
                  'Your item has been deleted.',
                  'success'
                )
                // perform any additional operations after successful delete
              })
              .catch(error => {
                console.log(error)
                this.$swal.fire(
                  'Error!',
                  'Failed to delete item.',
                  'error'
                )
              })
          } {
          }
        }
      })
    },
    async bookRoom(room) {
      const checkinDate = new Date(this.reservation.checkinDate);
      const checkoutDate = new Date(this.reservation.checkoutDate);
      const numDays = Math.ceil((checkoutDate - checkinDate) / (1000 * 60 * 60 * 24));
      if (this.isRoomAvailable(this.choice_room, checkinDate, checkoutDate)) {
        this.reservation.name = this.clientName;
        this.reservation.contactNumber = this.clientPhone;
        this.reservation.room_name = this.choice_room.name;
        this.reservation.room_price = this.choice_room.price;
        this.reservation.room_type = this.choice_room.type;
        this.reservation.totalPrice = this.reservation.room_price * numDays;
        try {
          const response = await axios.post(this.API_URL + "bookings/", {
            name: this.reservation.name,
            checkinDate: this.reservation.checkinDate,
            checkoutDate: this.reservation.checkoutDate,
            room_name: this.reservation.room_name,
            room_type: this.reservation.room_type,
            room_price: this.reservation.room_price,
            remarks: this.reservation.remarks,
            contactNumber: this.reservation.contactNumber,
            totalPrice: this.reservation.totalPrice
          });
          this.reservations.push(this.reservation);
          this.reloadData();
          this.reservation = {
            name: "",
            room_name: "",
            room_type: "",
            room_price: "",
            contactNumber: "",
            totalPrice: 0
          };
          this.$swal.fire({
            title: "Success!",
            text: "Booking successful!",
            icon: "success",
          });
        } catch (error) {
          console.error(error);
          this.$swal.fire({
            title: "Error!",
            text: "An error occurred while booking the room.",
            icon: "error",
          });
        }
      } else {
        this.$swal.fire({
          title: "Error!",
          text: "Sorry, the room is already occupied.",
          icon: "error",
        });
      }
    },
    printReservation(reservation) {
      const doc = new jsPDF();
      const content = `Booking Slip
      ----------------
      Name: <b>${reservation.name}</b>
      Room: ${reservation.room_name}
      Check-in: ${reservation.checkinDate}
      Check-out: ${reservation.checkoutDate}
      Remarks: ${reservation.remarks}
      Contact: ${reservation.contactNumber}`;
      doc.text(content, 10, 10);
      doc.save(`Booking Slip - ${reservation.name}.pdf`);
    },
    handleContextMenu(event) {
      event.preventDefault();
      if (event.target.classList.contains('cv-item')) {
        //this.$refs.vueSimpleContextMenu1.showMenu(event, event.target.innerHTML);
      } else if (event.target.classList.contains('cv-day')) {
        // const item = event.target.outerHTML.toString()
        // const strDate = item.split(" ")[4].replace('d', '');
        // const strDateDay = strDate.split("-")[2];
        // const strDateMos = strDate.split("-")[1];
        // const strDateYer = strDate.split("-")[0];
        // const convDate = strDateDay + "/" + strDateMos + "/" + strDateYer
        // this.convDate = convDate;
        // this.toggleShowAllModal();
      }
    },
    handleModalClosed() {
      if (!this.movetocartFlag || !this.bookNowFlag) {
        document.location.reload();
      }
    },
    // sendMessage(){
    //   socket.send(JSON.stringify(
    //     {
    //       "message": "hi micaroz!",
    //     }));
    // },
  },
  async mounted() {
    this.$refs.searchQuery.focus();
    this.$refs.searchQuery.blur();
    $('.currentPeriod').click();
    $('#suglist').hide();
    this.newItemStartDate = CalendarMath.isoYearMonthDay(CalendarMath.today())
    this.newItemEndDate = CalendarMath.isoYearMonthDay(CalendarMath.today())
    this.$nextTick(() => {
      // document.body.addEventListener('contextmenu', this.handleContextMenu);
    });
    document.addEventListener('keydown', this.handleKeyPress);
    const modal = this.$refs.modal;
    // Attach event listener for modal hidden event
    modal.addEventListener("hidden.bs.modal", this.handleModalClosed);
    this.socket = new WebSocket(`ws://${this.API_URL.replace(/^https?:\/\//, '')}ws/realtime/`);
    //this.socket = new WebSocket('ws://192.168.1.222:8081/ws/realtime/');
    const vm = this;
    this.socket.onmessage = function (e) {
      const data = JSON.parse(e.data);
      console.log(data.message)
      // $("#BookDayModal").modal("hide");
      vm.loadAlldata();
      vm.componentKey += 1;
    };
  }
};
</script>
<style>
@import "vue-select/dist/vue-select.css";

html,
body {
  background-color: #f7fcff;
}

#app {
  font-family: Calibri, sans-serif;
  width: 95vw;
  min-width: 30rem;
  max-width: 100rem;
  min-height: 40rem;
  margin-left: auto;
  margin-right: auto;
}

.calendar-parent {
  overflow-x: hidden;
  overflow-y: hidden;
  height: 800px;
  max-height: 800px;
  background-color: white;
}

/* For long calendars, ensure each week gets sufficient height. The body of the calendar will scroll if needed */
.cv-wrapper.period-month.periodCount-2 .cv-week,
.cv-wrapper.period-month.periodCount-3 .cv-week,
.cv-wrapper.period-year .cv-week {
  min-height: 6rem;
}

/* These styles are optional, to illustrate the flexbility of styling the calendar purely with CSS. */
/* Add some styling for items tagged with the "birthday" class */
.theme-default .cv-item.birthday {
  background-color: #e0f0e0;
  border-color: #d7e7d7;
}

.theme-default .cv-item.birthday::before {
  content: "\1F382";
  /* Birthday cake */
  margin-right: 0.5em;
}

/* The following classes style the classes computed in myDateClasses and passed to the component's dateClasses prop. */
.theme-default .cv-day.ides {
  background-color: #ffe0e0;
}

img {
  max-width: 100%;
  height: auto;
}

.wrapper-content {
  overflow-y: auto;
  overflow-x: hidden;
  padding-right: 1px;
}

.wrapper {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 80px;
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

.item-count,
.total-price {
  font-weight: bold;
}

.cart-button button {
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  margin-right: 10px;
  cursor: pointer;
}

.cart-button a {
  text-decoration: none;
  font-weight: bold;
}

.contents-left {
  display: flex;
  justify-content: flex-end;
}

#billing-details {
  display: none;
}

@media screen and (max-width: 767px) {
  .modal-dialog-sidebar {
    max-width: 100%;
  }
}

* {
  touch-action: manipulation;
}

.cv-item.custom-date-class-gray {
  background-color: rgb(219, 212, 212);
  color: rgb(37, 36, 35);
}

.cv-item.custom-date-class-orange {
  background-color: rgb(240, 169, 18);
  color: antiquewhite;
}

.cv-item.custom-date-class-blue {
  background-color: rgb(11, 14, 214);
  color: antiquewhite;
}

.cv-item.custom-date-class-violet {
  background-color: rgb(219, 13, 175);
  color: antiquewhite;
}

.cv-item.custom-date-class-red {
  background-color: #f66;
  color: antiquewhite;
}

.cv-item.custom-date-class-green {
  background-color: #0b9d17;
  color: antiquewhite;
}

.cv-item.custom-date-class-yellow {
  background-color: #bce40c;
  color: antiquewhite;
}

.rotated-text {
  writing-mode: vertical-lr;
  /* For modern browsers */
  transform: rotate(180deg);
  /* For older browsers */
}

.rotated-text2 {
  writing-mode: vertical-lr;
  /* For modern browsers */
  transform: rotate(270deg);
  /* For older browsers */
}

.cv-item.hotel-reserved {
  background-color: #5c6bc0;
  /* adjust the color as needed */
}

.cv-item.hotel-reserved-unpaid {
  background-color: #ef5350;
  /* adjust the color as needed */
}

.cv-item.hotel-checkedin-unpaid {
  background-color: #66bb6a;
  /* adjust the color as needed */
}

.cv-item.hotel-checkedin-partial {
  background-color: #42a5f5;
  /* adjust the color as needed */
}

.cv-item.hotel-checkedin-paid {
  background-color: #ffee58;
  /* adjust the color as needed */
}

.cv-item.hotel-cancelled {
  background-color: #bdbdbd;
  /* adjust the color as needed */
}

.cv-item.hotel-checkedout {
  background-color: #ff7043;
  /* adjust the color as needed */
}

.cv-item {
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
  border: 1px solid #dee2e6;
  border-radius: 0.25rem;
  transition: all 0.2s ease-in-out;
}

.cv-item:hover {
  cursor: pointer;
  transform: translateY(-5px);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
}

.card {
  margin: 5px;
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
  border: 1px solid #dee2e6;
  border-radius: 0.25rem;
  transition: all 0.2s ease-in-out;
}

.card:hover {
  cursor: pointer;
  transform: translateY(-5px);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
}

.loading-spinner {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
  /* Adjust the height as needed */
}

.loading-text {
  margin-top: 10px;
  /* Adjust the margin as needed */
}

.autosuggestions {
  list-style: none;
  padding: 0;
  margin: 0;
  background: white;
  border: 1px solid #ccc;
  position: absolute;
  z-index: 9999;
}

.autosuggestions li {
  padding: 8px;
  cursor: pointer;
}

.autosuggestions li:hover {
  background-color: #f2f2f2;
}

.btn-margin {
  margin-right: 10px;
}

.come-from-modal.left .modal-dialog,
.come-from-modal.right .modal-dialog {
  position: fixed;
  margin: auto;
  width: 320px;
  height: 100%;
  -webkit-transform: translate3d(0%, 0, 0);
  -ms-transform: translate3d(0%, 0, 0);
  -o-transform: translate3d(0%, 0, 0);
  transform: translate3d(0%, 0, 0);
}

.come-from-modal.left .modal-content,
.come-from-modal.right .modal-content {
  height: 100%;
  overflow-y: auto;
  border-radius: 0px;
}

.come-from-modal.left .modal-body,
.come-from-modal.right .modal-body {
  padding: 15px 15px 80px;
}

.come-from-modal.right.fade .modal-dialog {
  right: -320px;
  -webkit-transition: opacity 0.3s linear, right 0.3s ease-out;
  -moz-transition: opacity 0.3s linear, right 0.3s ease-out;
  -o-transition: opacity 0.3s linear, right 0.3s ease-out;
  transition: opacity 0.3s linear, right 0.3s ease-out;
}

.come-from-modal.right.fade.in .modal-dialog {
  right: 0;
}

/* CSS for the continuous wiggle animation */
@keyframes wiggle {
  0% {
    transform: rotate(0deg);
  }

  25% {
    transform: rotate(5deg);
  }

  50% {
    transform: rotate(-5deg);
  }

  75% {
    transform: rotate(5deg);
  }

  100% {
    transform: rotate(0deg);
  }
}

/* Apply the animation to the button */
.wiggle-animation {
  animation: wiggle 1.5s infinite;
  /* Adjust animation duration as needed */
}
</style>