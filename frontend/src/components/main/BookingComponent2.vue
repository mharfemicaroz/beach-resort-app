<template :key="componentKey">
  <TopNavBarComponent />
  <div class="container-fluid main">
    <div>
      <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li v-if="userdata.role === 'superuser'" class="nav-item" role="presentation">
          <button class="nav-link" id="dashboard-tab" data-bs-toggle="tab" data-bs-target="#dashboard" type="button"
            role="tab" aria-controls="dashboard" aria-selected="true" @click="resetSummary(0)">
            Dashboard
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link active" id="booking-tab" data-bs-toggle="tab" data-bs-target="#booking" type="button"
            role="tab" aria-controls="booking" aria-selected="true" @click="resetSummary(1)">
            Calendar
          </button>
        </li>
        <li v-if="userdata.role !== 'reservationist'" class="nav-item" role="presentation">
          <button class="nav-link" id="monitor-tab" data-bs-toggle="tab" data-bs-target="#monitor" type="button"
            role="tab" aria-controls="monitor" aria-selected="false" @click="resetSummary(4)">
            Front Desk
          </button>
        </li>
        <li v-if="userdata.role !== 'reservationist'" class="nav-item" role="presentation">
          <button class="nav-link" id="reception-tab" data-bs-toggle="tab" data-bs-target="#reception" type="button"
            role="tab" aria-controls="reception" aria-selected="false" @click="resetSummary(5)">
            Reservation Chart
          </button>
        </li>
        <li v-if="userdata.role !== 'reservationist'" class="nav-item" role="presentation">
          <button class="nav-link" id="others-tab" data-bs-toggle="tab" data-bs-target="#others" type="button" role="tab"
            aria-controls="others" aria-selected="false" @click="resetSummary(2)">
            Account
          </button>
        </li>
        <li v-if="userdata.role === 'superuser'" class="nav-item" role="presentation">
          <button class="nav-link" id="reports-tab" data-bs-toggle="tab" data-bs-target="#reports" type="button"
            role="tab" aria-controls="reports" aria-selected="false" @click="resetSummary(3)">
            Reports
          </button>
        </li>
      </ul>
      <div class="tab-content mt-3" id="myTabContent">
        <div v-if="userdata.role === 'superuser'" class="tab-pane fade" id="dashboard" role="tabpanel"
          aria-labelledby="dashboard-tab">
          <div class="container-fluid">
            <div class="row">
              <div class="col-md-12">
                <BookingDashboard v-if="dashboardStatus" :active="dashboardStatus" :key="componentKey" />
              </div>
            </div>
          </div>
        </div>
        <div class="tab-pane fade show active" id="booking" role="tabpanel" aria-labelledby="booking-tab">
          <div class="container-fluid">
            <div class="row">
              <div class="col-md-12">
                <div class="d-flex justify-content-between">
                  <h2>
                    Calendar
                    <a href="#" class="btn btn-link text-decoration-none" @click="toggleSettingsModal()"><i
                        class="fa fa-bars" style="font-size: 1.25em"></i></a>
                  </h2>
                  <div class="form-outline col-md-3">
                    <div class="input-group">
                      <span class="input-group-prepend">
                        <button class="btn btn-primary" @click="insertNewBooking">
                          <i class="fa fa-plus"></i>
                          &nbsp; Add new
                        </button>
                        &nbsp;
                      </span>
                      <input type="search" id="form1" class="form-control" placeholder="Type query"
                        v-model="booksearchtext" @input="populateCalendarItems" @click="showAutosuggestions = false"
                        @blur="hideAutosuggestions" aria-label="Search" ref="searchQuery" autocomplete="off"
                        aria-autocomplete="off" />
                    </div>

                    <!-- <ul
                      id="suglist"
                      class="autosuggestions"
                      v-if="!showAutosuggestions"
                    >
                      <li
                        v-for="suggestion in autosuggestions"
                        @click="selectSuggestion(suggestion)"
                      >
                        {{ suggestion }}
                      </li>
                    </ul> -->
                  </div>
                </div>
                <!-- <div
                  class="d-flex justify-content-center align-items-center"
                  v-if="calendarItems.length === 0"
                >
                  <img src="/src/assets/loading.gif" />
                </div> -->
                <div class="calendar-parent c-p">
                  <calendar-view :items="calendarItems" :show-date="showDate" :time-format-options="{
                    hour: 'numeric',
                    minute: '2-digit',
                  }" :enable-drag-drop="true" :disable-past="disablePast" :disable-future="disableFuture"
                    :show-times="showTimes" :date-classes="myDateClasses" :display-period-uom="displayPeriodUom"
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
              <div class="card" style="height: 60px !important"></div>
            </div>
          </div>
        </div>
        <div class="tab-pane fade" id="monitor" role="tabpanel" aria-labelledby="monitor-tab">
          <div class="container-fluid">
            <div class="row">
              <div class="col-sm-2">
                <ul class="nav nav-tabs flex-column" id="propertyTab" role="tablist">
                  <li class="nav-item">
                    <a class="nav-link active" data-bs-toggle="tab" @click="activeMainTab = 'all'"
                      href="#roomcategoryall">All</a>
                  </li>
                  <li class="nav-item" v-for="(category, index) in roomcategories" :key="category.id">
                    <a class="nav-link" data-bs-toggle="tab" @click="activeMainTab = `${category.name}`"
                      :href="`#roomcategory${index}`">{{ category.name }}</a>
                  </li>
                </ul>
              </div>
              <div class="col-sm-10">
                <div class="tab-content mt-3" id="propertyTabContent">
                  <div class="tab-pane fade show active" id="#roomcategoryall" role="tabpanel">
                    <div class="container-fluid">
                      <div class="row" style="margin-left: 0.1%">
                        <div class="col-md-3">
                          <button class="btn btn-primary" @click="generateAllStabs">
                            <i class="fa fa-cutlery"></i> &nbsp;Generate
                            Mealstabs
                          </button>
                        </div>
                      </div>
                      <div class="row mt-2">
                        <div class="col-md-12">
                          <CardBookings2Vue :roomData="roomsjoinbookings"
                            :departingRoomData="roomsjoinbookingsfordeparting" v-on:click-action="cardAction" />
                        </div>
                      </div>
                    </div>
                  </div>
                  <div v-for="(category, index) in roomcategories" :key="category.id" class="tab-pane fade"
                    :id="`#roomcategory${index}`" role="tabpanel">
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
              <ReceptionHotel :bookingsdata="bookings" :roomsdata="rooms" :roomcategoriesdata="roomcategories"
                @clickItem-action="handleReceptionItemAction" @clickDay-action="handleReceptionDayAction"
                @clickRoom-action="handleReceptionRoomAction" @dragstart-action="handledragstart"
                @dragend-action="handledragend" @dragover-action="handleDragOver" @dragdrop-action="handleDragDrop"
                @dragstartday-action="handledragstartday" />
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
                      style="font-size: 0.75rem">
                      {{ numItemCart }}
                      <span class="visually-hidden">items in cart</span>
                    </span>
                  </h2>
                  <div class="ms-auto d-flex align-items-center">
                    <!-- Wrap the buttons in a flex container -->
                    <button type="button" class="btn btn-primary me-2" v-show="(reservation.status !== 'checkedout' || walkinStatus) &&
                      !walkinview
                      " :class="{ 'wiggle-animation': countInclusion === 0 }" @click="showShoppingModal()">
                      <i class="fa fa-shopping-cart"><br />
                        <span style="font-size: 8px">[F1]</span></i>
                    </button>
                    <button type="button" v-show="(reservation.status !== 'checkedout' || walkinStatus) &&
                      !walkinview
                      " class="btn btn-primary" :class="{ 'wiggle-animation': countInclusion > 0 }"
                      @click="moveInclusionCartToMain()">
                      <i class="fas fa-thumbs-up" style="position: relative"><br />
                        <span style="font-size: 8px">[F2]</span>
                        <span class="position-absolute start-1000 translate-middle badge rounded-pill bg-danger"
                          style="font-size: 0.5rem; top: -25%; left: 120%">
                          {{ countInclusion }}
                          <span class="visually-hidden">items in cart</span>
                        </span>
                      </i>
                    </button>
                  </div>
                </div>
                <div class="card-deck"
                  :style="`height:${calcMeasure.height2};overflow-y: auto;overflow-x: hidden;padding-right: 1px;`">
                  <div class="card" v-for="(item, index) in cart.sort((a, b) =>
                    a.category.localeCompare(b.category)
                  )" :key="item.id">
                    <div class="card-header d-flex justify-content-between align-items-center">
                      <h5 class="card-title">
                        {{
                          item.name.toLowerCase() === "room guest"
                          ? "Room Guest-" + item.currentroom
                          : item.name
                        }}
                        <span v-html="item.category === 'main'
                              ? '<i class=\'fas fa-check text-success\'></i>'
                              : '<i class=\'fas fa-hourglass-start text-warning\'></i>'
                            "></span>
                      </h5>
                      <span>
                        <button class="btn btn-primary" v-if="item.category === 'main' &&
                          item.name.toLowerCase() === 'room guest'
                          " type="button" @click="addNewGuest(item)">
                          <i class="fas fa-user"></i>
                        </button>
                        &nbsp;
                        <button v-if="item.category === 'inclusions' ||
                          item.itemOption === 'addons'
                          " v-show="(reservation.status !== 'checkedout' ||
      walkinStatus) &&
    !walkinview
    " type="button" class="btn btn-danger" @click="cancelItem(item)">
                          <i class="fas fa-times"></i>
                        </button>
                      </span>
                    </div>
                    <div class="card-body">
                      <p class="card-text">Type: {{ item.type }}</p>
                      <p class="card-text">Price Rate: {{ item.priceRate }}</p>
                      <p class="card-text">Purchase Qty.:{{ item.purqty }}</p>
                      <p class="card-text">
                        Total Price: {{ item.totalCartPrice }}
                      </p>
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
              <div class="col-md-9 printform">
                <div class="mt-0 mb-1 d-flex justify-content-between">
                  <div class="col-md-3">
                    <ul class="nav bg radius nav-pills nav-fill" role="tablist">
                      <li class="nav-item">
                        <a class="nav-link active show" id="linkview1" data-bs-toggle="tab" @click="reportview = 1"
                          role="tab" href="#view1">
                          <i class="fa fa-tags"></i>1</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link" id="linkview2" data-bs-toggle="tab" role="tab" @click="
                          reportview = 2;
                        passwordProtectTab(2);
                        " href="#view2">
                          <i class="fa fa-tags"></i>2</a>
                      </li>
                      <li class="nav-item">
                        <a class="nav-link" id="linkview3" data-bs-toggle="tab" role="tab" @click="
                          reportview = 3;
                        passwordProtectTab(3);
                        " href="#view3">
                          <i class="fa fa-tags"></i>3</a>
                      </li>
                    </ul>
                  </div>
                  <div class="d-flex align-items-center">
                    <!-- Wrap the buttons in a flex container -->
                    <button type="button" class="btn btn-primary" v-show="countInclusion === 0" v-if="(!this.walkinStatus || this.walkinview) &&
                      !this.justDiscounted
                      " @click="generateBillingStatement()">
                      <i class="fas fa-print"><br />
                        <span style="font-size: 8px">[F10]</span></i>
                    </button>
                    &nbsp;
                    <button type="button" class="btn btn-primary" @click="extendView">
                      <i :class="isExtended ? 'fas fa-compress' : 'fas fa-expand'
                        "><br />
                        <span style="font-size: 8px">[F11]</span></i>
                    </button>
                  </div>
                </div>
                <div class="tab-content" id="myTabContent">
                  <div class="tab-pane fade show active" id="view1" role="tabpanel">
                    <div id="rview1" class="bg-light"
                      :style="`height:${calcMeasure.height3}!important;overflow-y: auto;overflow-x: hidden;font-size: 100%;padding: 20px;box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);`">
                      <div class="container">
                        <div class="row">
                          <div class="col-12">
                            <div class="row justify-content-between">
                              <div class="col-4">
                                <img :src="`/src/assets/${this.APP_LOGO_NAME}`" width="60" height="60" alt="Company Logo"
                                  class="logo" />
                              </div>
                              <div class="col-4 text-center">
                                <span class="h4">Guest Folio</span>
                              </div>
                            </div>
                            <hr style="margin-bottom: 0px; margin-top: 0px" />
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-12">
                            <div class="row">
                              <div class="col-6">
                                <span style="font-size: small">Client Details:</span>
                                <p style="margin-bottom: 0px">
                                  Name: {{ this.billing.clientName }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Email: {{ this.billing.clientEmail }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Contact No.: {{ this.billing.clientPhone }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Address: {{ this.billing.clientAddress }}
                                </p>
                              </div>
                              <div class="col-6" v-if="!walkinStatus">
                                <span style="font-size: small">Booking Details:</span>
                                <p style="margin-bottom: 0px">
                                  Checkin Date:
                                  {{ this.reservation.checkinDate }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Checkout Date: {{ setCheckoutDate() }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Total Pax: {{ sumtotalPax() }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Total Guest(s): {{ sumTotalGuests() }}
                                </p>
                              </div>
                            </div>
                            <hr style="margin-bottom: 0px; margin-top: 0px" />
                            <div id="billing-details-preview-view1">
                              <div class="row">
                                <div class="col-12">
                                  <span style="font-size: small">Order Details:</span>
                                  <table class="table">
                                    <thead>
                                      <tr>
                                        <th>Item Name</th>
                                        <th>Category</th>
                                        <th>Qty</th>
                                        <th>Pax</th>
                                      </tr>
                                    </thead>
                                    <tbody>
                                      <tr v-for="item in combinedcart" :key="item.id">
                                        <td>
                                          {{
                                            item.name.toLowerCase() ===
                                            "room guest"
                                            ? (parseFloat(item.totalguest) <= parseFloat(item.totalpax) ? item.name
                                              : "Excess Person") + "-" + item.currentroom : item.name }} </td>
                                        <td>{{ item.type }}</td>
                                        <td>
                                          {{ item.purqty }}
                                        </td>
                                        <td>
                                          {{
                                            item.totalCartPrice < item.purqty * parseFloat(item.priceRate.split("/")[0]) *
                                            item.numdays && item.itemOption !== "room" ? "(free " +
                                            (parseFloat(item.totalpax) - parseFloat(item.totalguest) +
                                              parseFloat(item.purqty)) + ")=" + (item.totalguest < item.totalpax ? 0 :
                                                item.totalguest - item.totalpax) : item.itemOption === "room" &&
                                                  howmanyPax(item.name) > 0
                                            ? "Good for " +
                                            howmanyPax(item.name)
                                            : ""
                                          }}
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
                  </div>
                  <div class="tab-pane fade" id="view2" role="tabpanel">
                    <div id="rview2" class="bg-light"
                      :style="`height:${calcMeasure.height3}!important;overflow-y: auto;overflow-x: hidden;font-size: 100%;padding: 20px;box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);`">
                      <div class="container">
                        <div class="row">
                          <div class="col-12">
                            <div class="row justify-content-between">
                              <div class="col-4">
                                <img :src="`/src/assets/${this.APP_LOGO_NAME}`" width="60" height="60" alt="Company Logo"
                                  class="logo" />
                              </div>
                              <div class="col-4 text-center">
                                <span class="h4">Guest Folio</span>
                              </div>
                              <div class="col-3 text-right">
                                <span style="font-size: small">Tracking No.:
                                  {{ this.billing.bookingID }}</span>
                              </div>
                            </div>
                            <hr style="margin-bottom: 0px; margin-top: 0px" />
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-12">
                            <div class="row">
                              <div class="col-6">
                                <span style="font-size: small">Client Details:</span>
                                <p style="margin-bottom: 0px">
                                  Name: {{ this.billing.clientName }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Email: {{ this.billing.clientEmail }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Contact No.: {{ this.billing.clientPhone }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Address: {{ this.billing.clientAddress }}
                                </p>
                              </div>
                              <div class="col-6" v-if="!walkinStatus">
                                <span style="font-size: small">Booking Details:</span>
                                <p style="margin-bottom: 0px">
                                  Checkin Date:
                                  {{ this.reservation.checkinDate }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Checkout Date: {{ setCheckoutDate() }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Total Pax: {{ sumtotalPax() }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Total Guest(s): {{ sumTotalGuests() }}
                                </p>
                              </div>
                            </div>
                            <hr style="margin-bottom: 0px; margin-top: 0px" />
                            <div id="billing-details-preview-view2">
                              <div class="row">
                                <div class="col-12">
                                  <span style="font-size: small">Account History:</span>
                                  <table class="table">
                                    <tr>
                                      <td class="">
                                        <strong>Sub-total:</strong>
                                      </td>
                                      <td class="d-flex flex-row-reverse">
                                        Php
                                        {{ subtotal }}
                                      </td>
                                    </tr>
                                    <tr>
                                      <td class="">
                                        <strong>Partial Payment:</strong>
                                      </td>
                                      <td class="d-flex flex-row-reverse">
                                        -Php
                                        {{ partialPayment }}
                                      </td>
                                    </tr>
                                    <tr>
                                      <td class="">
                                        <strong>Total Due:</strong>
                                      </td>
                                      <td class="d-flex flex-row-reverse">
                                        Php
                                        {{ total }}
                                      </td>
                                    </tr>
                                  </table>
                                  <table class="table">
                                    <thead>
                                      <tr>
                                        <th>Date</th>
                                        <th>Type</th>
                                        <th>Reference #</th>
                                        <th>Description</th>
                                        <th>Amount</th>
                                        <th>Balance</th>
                                      </tr>
                                    </thead>
                                    <tbody>
                                      <tr v-for="(item, index) in cashHistory" :key="item.id">
                                        <td>
                                          {{
                                            new Date(
                                              item.transaction_date
                                            ).toLocaleDateString()
                                          }},
                                          {{
                                            getTime(
                                              new Date(item.transaction_date)
                                            )
                                          }}
                                        </td>
                                        <td>
                                          {{ item.paymentMethod }}
                                        </td>
                                        <td>
                                          {{
                                            item.nonCashReference
                                              .toString()
                                              .replace("-", "") === ""
                                            ? item.id
                                            : item.id +
                                            "-" +
                                            item.nonCashReference
                                          }}
                                        </td>
                                        <td>
                                          {{
                                            index === 0
                                            ? "Init/DP"
                                            : parseFloat(item.balance) === 0
                                              ? "Full"
                                              : "Partial"
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
                  </div>
                  <div class="tab-pane fade" id="view3" role="tabpanel">
                    <div id="rview3" class="bg-light"
                      :style="`height:${calcMeasure.height3}!important;overflow-y: auto;overflow-x: hidden;font-size: 100%;padding: 20px;box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);`">
                      <div class="container">
                        <div class="row">
                          <div class="col-12">
                            <div class="row justify-content-between">
                              <div class="col-4">
                                <img :src="`/src/assets/${this.APP_LOGO_NAME}`" width="60" height="60" alt="Company Logo"
                                  class="logo" />
                              </div>
                              <div class="col-4 text-center">
                                <span class="h4">Guest Folio</span>
                              </div>
                              <div class="col-3 text-right">
                                <span style="font-size: small">Registration No.:
                                  {{ this.billing.bookingID }}</span>
                              </div>
                            </div>
                            <hr style="margin-bottom: 0px; margin-top: 0px" />
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-12">
                            <div class="row">
                              <div class="col-6">
                                <span style="font-size: small">Client Details:</span>
                                <p style="margin-bottom: 0px">
                                  Name: {{ this.billing.clientName }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Email: {{ this.billing.clientEmail }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Contact No.: {{ this.billing.clientPhone }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Address: {{ this.billing.clientAddress }}
                                </p>
                              </div>
                              <div class="col-6" v-if="!walkinStatus">
                                <span style="font-size: small">Booking Details:</span>
                                <p style="margin-bottom: 0px">
                                  Checkin Date:
                                  {{ this.reservation.checkinDate }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Checkout Date: {{ setCheckoutDate() }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Total Pax: {{ sumtotalPax() }}
                                </p>
                                <p style="margin-bottom: 0px">
                                  Total Guest(s): {{ sumTotalGuests() }}
                                </p>
                              </div>
                            </div>
                            <hr style="margin-bottom: 0px; margin-top: 0px" />
                            <div id="billing-details-preview-view3">
                              <div class="row">
                                <div class="col-12">
                                  <span style="font-size: small">Order Details:</span>
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
                                        <td>
                                          {{
                                            item.name.toLowerCase() ===
                                            "room guest"
                                            ? (parseFloat(item.totalguest) <= parseFloat(item.totalpax) ? item.name
                                              : "Excess Person") + "-" + item.currentroom : item.name }} </td>
                                        <td>{{ item.type }}</td>
                                        <td>{{ item.priceRate }}</td>
                                        <td>
                                          {{
                                            item.totalCartPrice < item.purqty * parseFloat(item.priceRate.split("/")[0]) *
                                            item.numdays && item.itemOption !== "room" ? item.purqty + "(free " +
                                            item.totalpax + ")=" + (item.totalguest < item.totalpax ? 0 : item.totalguest
                                              - item.totalpax) + `&times;${item.numdays}` : item.purqty +
                                              (item.itemOption === "room" || item.name.toLowerCase() !== "room guest" ? "" :
                                                `&times;${item.numdays}`) }} </td>
                                        <td v-if="item.itemOption !== 'room'">
                                          {{ item.totalCartPrice }}
                                        </td>
                                        <td v-else>
                                          <span v-if="!isNaN(subroom.discountValue)" v-html="`${item.totalCartPrice
                                            } <sup class='text-danger font-weight-bold'>${subroom.discountMode ===
                                              'percentage'
                                              ? subroom.discountValue + '%'
                                              : (
                                                subroom.discountValue /
                                                combinedcart.filter(
                                                  (o) =>
                                                    o.itemOption ===
                                                    'room'
                                                ).length
                                              ).toFixed(2)
                                            } off</sup> <span class='text-success font-weight-bold'>${subroom.discountMode ===
                                              'percentage'
                                              ? item.totalCartPrice *
                                              (1 -
                                                parseFloat(
                                                  subroom.discountValue /
                                                  100
                                                ))
                                              : item.totalCartPrice -
                                              (
                                                subroom.discountValue /
                                                combinedcart.filter(
                                                  (o) =>
                                                    o.itemOption ===
                                                    'room'
                                                ).length
                                              ).toFixed(2)
                                            }</span>`
                                            "></span>
                                          <span v-else v-html="`${item.totalCartPrice}`"></span>
                                        </td>
                                      </tr>
                                      <tr>
                                        <td colspan="4" class="text-right">
                                          <strong>Partial Payment:</strong>
                                        </td>
                                        <td class="text-danger">
                                          <strong>-Php {{ partialPayment }}</strong>
                                        </td>
                                      </tr>
                                      <tr>
                                        <td colspan="4" class="text-right">
                                          <strong>Total Due:</strong>
                                        </td>
                                        <td>
                                          <strong>Php {{ total }}</strong>
                                        </td>
                                      </tr>
                                    </tbody>
                                  </table>
                                </div>
                              </div>
                              <hr style="margin-bottom: 0px; margin-top: 0px" />
                              <div class="row">
                                <div class="col-12">
                                  <span style="font-size: small">Account History:</span>
                                  <table class="table">
                                    <thead>
                                      <tr>
                                        <th>Date</th>
                                        <th>Type</th>
                                        <th>Reference #</th>
                                        <th>Description</th>
                                        <th>Amount</th>
                                        <th>Balance</th>
                                      </tr>
                                    </thead>
                                    <tbody>
                                      <tr v-for="(item, index) in cashHistory" :key="item.id">
                                        <td>
                                          {{
                                            new Date(
                                              item.transaction_date
                                            ).toLocaleDateString()
                                          }},
                                          {{
                                            getTime(
                                              new Date(item.transaction_date)
                                            )
                                          }}
                                        </td>
                                        <td>
                                          {{ item.paymentMethod }}
                                        </td>
                                        <td>
                                          {{
                                            item.nonCashReference
                                              .toString()
                                              .replace("-", "") === ""
                                            ? item.id
                                            : item.id +
                                            "-" +
                                            item.nonCashReference
                                          }}
                                        </td>
                                        <td>
                                          {{
                                            index === 0
                                            ? "Init/DP"
                                            : parseFloat(item.balance) === 0
                                              ? "Full"
                                              : "Partial"
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
                  </div>
                </div>
              </div>

              <div class="paymentmodal col-md-3"
                :style="`height:${calcMeasure.height4}!important;overflow-y: auto;overflow-x: hidden;`">
                <div class="d-flex align-items-center" style="padding: 10px">
                  <h2 class="position-relative">Payment</h2>
                  <div class="ms-auto d-flex align-items-center">
                    <!-- Wrap the buttons in a flex container -->
                    <button type="button" class="btn btn-primary" v-show="(reservation.status !== 'checkedout' || walkinStatus) &&
                      !walkinview
                      " @click="initializePlaceOrder" :disabled="total <= 0 || countInclusion > 0" style="
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                      ">
                      <i class="fas fa-money-bill"></i>
                      <span style="font-size: 8px">[Enter]</span>
                    </button>
                  </div>
                </div>
                <div class="container">
                  <div class="row">
                    <div class="col-12">
                      <form>
                        <div class="form-group mb-2 mt-0">
                          <div class="input-group">
                            <input type="text" class="form-control" :value="this.billing.clientName" readonly />
                            <button type="button" class="btn btn-primary" v-show="reservation.status !== 'checkedout' ||
                              walkinStatus
                              " @click="toggleAddAccountModal">
                              <i :class="this.billing.clientName === ''
                                  ? 'fa fa-user-plus'
                                  : 'fas fa-user-edit'
                                "></i>
                            </button>
                          </div>
                        </div>
                        <div class="form-group mb-2">
                          <div class="form-control p-3">
                            <div class="row">
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
                              <div class="col-6 text-right">
                                {{ discountValue
                                }}{{
  discountMode === "percentage" ? "%" : " off"
}}
                              </div>
                            </div>

                            <div class="row">
                              <div class="col-6">
                                <strong>Reservation:</strong>
                              </div>
                              <div class="col-6 text-right" v-html="subroom.original + ' ' + subroom.discounted
                                "></div>
                            </div>
                            <div class="row">
                              <div class="col-6"><strong>Add-ons:</strong></div>
                              <div class="col-6 text-right">
                                {{ subaddons }}
                              </div>
                            </div>

                            <div class="row" v-if="paymentMethod === 'non-cash'">
                              <div class="col-6">
                                <strong>Reference No.:</strong>
                              </div>
                              <div class="col-6 text-right">
                                {{ nonCashPayPlatform }} -
                                {{ nonCashReference }}
                              </div>
                            </div>
                            <div class="row" v-if="paymentMethod === 'agentcredit' ||
                              paymentMethod === 'agentnocredit'
                              ">
                              <div class="col-6">
                                <strong>Reference No.:</strong>
                              </div>
                              <div class="col-6 text-right">
                                {{ agentPayPlatform }} - {{ nonCashReference }}
                              </div>
                              <div class="col-6">
                                <strong>Agent payment:</strong>
                              </div>
                              <div class="col-6 text-right">
                                {{ agentPayment.toFixed(2) }}
                              </div>
                            </div>
                            <div class="row">
                              <div class="col-6">
                                <strong>Subtotal:</strong>
                              </div>
                              <div class="col-6 text-right">{{ subtotal }}</div>
                            </div>
                            <div class="row">
                              <div class="col-6"><strong>Partial:</strong></div>
                              <div class="col-6 text-right">
                                {{ partialPayment }}
                              </div>
                            </div>
                            <div class="row mb-0">
                              <div class="col-6">
                                <strong class="text-primary">Total:</strong>
                              </div>
                              <div class="col-6 text-right">
                                <strong>{{ total }}</strong>&nbsp;
                                <a v-if="total < 0" href="#" @click="refundPayment"><i>for refund→</i></a>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="form-group">
                          <div class="input-group">
                            <select id="payment-method" v-model="paymentMethod" v-show="reservation.status !== 'checkedout' ||
                              walkinStatus
                              " class="form-control" style="font-weight: bolder" @change="setNonCash">
                              <option value="cash">Cash</option>
                              <option value="non-cash">Non-cash</option>
                              <option value="agentcredit">
                                Agent w/ Credit
                              </option>
                              <option value="agentnocredit">
                                Agent w/ No Credit
                              </option>
                            </select>
                            <span class="input-group-text">₱</span>
                            <input type="number" class="form-control" id="cashAmount" v-model.number="cashAmount"
                              step="0.01" @keyup="updateTotalCash" @keydown="updateTotalCash" />
                            <span class="input-group-text">{{
                              (cashAmount - Math.floor(cashAmount))
                                .toFixed(2)
                                .substr(1)
                            }}</span>
                          </div>
                        </div>
                        <div class="row mt-2 mb-2">
                          <div class="col-md-12">
                            <div class="row row-cols-1 row-cols-md-4">
                              <div class="col mb-1" v-for="item in cashDenominations" :key="item.id">
                                <button type="button"
                                  class="btn bg-white rounded-lg shadow hover:shadow-xs focus:outline-none inline-block px-0 py-0 text-sm"
                                  @click="addToCash(item.value)">
                                  <span>{{ item.label }}</span>
                                </button>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="form-group" v-if="this.paymentMethod === 'cash'">
                          <div class="input-group">
                            <span class="input-group-text" style="width: 75px">OR #:</span>
                            <input type="text" class="form-control" v-model="cashOR" />
                            <span class="input-group-text" style="width: 75px">OS #:</span>
                            <input type="text" class="form-control" v-model="cashOS" />
                          </div>
                        </div>
                        <div class="form-group">
                          <div class="input-group">
                            <span class="input-group-text" style="width: 75px">Remarks</span>
                            <textarea class="form-control" v-model="cashRemarks" rows="2"></textarea>
                          </div>
                        </div>
                        <div class="row mt-2 mb-2 bg-light">
                          <div class="col-md-6">
                            <dt v-if="change >= 0">Change:</dt>
                          </div>
                          <div class="col-md-6 d-flex flex-row-reverse">
                            <dd class="text-right h4 b">₱{{ change }}</dd>
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
                                  <input type="date" class="form-control" v-model="resfromDate" />
                                </div>
                                <div class="form-group">
                                  <input type="date" class="form-control" v-model="restoDate" />
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
                            <table-component :mainHeaders="reservationsOptions" :mainItems="filteredReservationsHistory"
                              :editable="false" :toggleable="false" />
                          </div>
                        </div>
                      </div>
                    </div>
                    <div id="transactions" class="tab-pane">
                      <div class="row">
                        <div class="col-md-2">
                          <div>
                            <div class="form-group">
                              <label for="date-filter">Date Filter:</label>
                              <select class="form-control" id="date-filter" v-model="dateFilter">
                                <option value="any">Any</option>
                                <option value="range">Date Range</option>
                              </select>
                              <div v-if="dateFilter === 'range'">
                                <div class="form-group">
                                  <input type="date" class="form-control" v-model="fromDate" />
                                </div>
                                <div class="form-group">
                                  <input type="date" class="form-control" v-model="toDate" />
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
                            <table-component :mainHeaders="transactionsOptions" :mainItems="filteredTransactions"
                              :subHeaders2="transactionhistory" :subHeaders="transactionitem" :editable="false"
                              :toggleable="true">
                              <template #custombtn="data">
                                <button type="button" class="btn btn-lg badge rounded-pill d-inline btn-danger"
                                  @click="deleteTransaction(data.data.dt.id)">
                                  <i class="fa fa-times"></i>
                                </button>
                                &nbsp;
                                <button type="button" class="btn btn-lg badge rounded-pill d-inline btn-primary"
                                  @click="openToCart(data.data.dt.id)">
                                  <i class="fa fa-share"></i>
                                </button>
                              </template>
                            </table-component>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="card" style="height: 60px !important"></div>
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
      <div id="billing-details" class="container-fluid billing" style="font-size: 100%">
        <div class="container">
          <div class="row">
            <div class="col-12">
              <div class="row justify-content-between" :style="!isThereLeisures ? 'border-right: dotted;' : ''">
                <div class="col-4">
                  <img :src="`/src/assets/${this.APP_LOGO_NAME}`" width="60" height="60" alt="Company Logo"
                    class="logo" />
                </div>
                <div class="col-4 text-center">
                  <span class="h2">Guest Folio</span>
                </div>
                <div class="col-4 text-right">
                  <span style="font-size: small" v-if="reportview === 3">Registration No.: {{ this.billing.bookingID
                  }}</span>
                </div>
              </div>
              <hr />
            </div>
          </div>
          <div class="row">
            <div class="col-12" :style="!isThereLeisures ? 'border-right: dotted;' : ''">
              <div class="row">
                <div class="col-6">
                  <span style="font-size: small">Client Details:</span>
                  <p style="margin-bottom: 0px">
                    Name: {{ this.billing.clientName }}
                  </p>
                  <p style="margin-bottom: 0px">
                    Email: {{ this.billing.clientEmail }}
                  </p>
                  <p style="margin-bottom: 0px">
                    Contact No.: {{ this.billing.clientPhone }}
                  </p>
                  <p style="margin-bottom: 0px">
                    Address: {{ this.billing.clientAddress }}
                  </p>
                </div>
                <div class="col-6" v-if="!walkinStatus">
                  <span style="font-size: small">Booking Details:</span>
                  <p style="margin-bottom: 0px">
                    Checkin Date: {{ this.reservation.checkinDate }}
                  </p>
                  <p style="margin-bottom: 0px">
                    Checkout Date: {{ setCheckoutDate() }}
                  </p>
                  <p style="margin-bottom: 0px">
                    Total Pax: {{ sumtotalPax() }}
                  </p>
                  <p style="margin-bottom: 0px">
                    Total Guest(s): {{ sumTotalGuests() }}
                  </p>
                </div>
              </div>
              <hr />
              <div id="reportGenerator"></div>
              <!-- <div class="row">
              <div class="col-12">
                <span style="font-size: small">Order Details:</span>
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
                      <td>
                        {{
                          item.name.toLowerCase() === "room guest"
                            ? item.purqty > item.totalpax
                              ? item.name
                              : "Excess Person" + "-" + item.currentroom
                            : item.name
                        }}
                      </td>
                      <td>{{ item.type }}</td>
                      <td>{{ item.priceRate }}</td>
                      <td>
                        {{
                          item.totalCartPrice <
                            item.purqty *
                              parseFloat(item.priceRate.split("/")[0]) *
                              item.numdays && item.itemOption !== "room"
                            ? item.purqty +
                              "(free " +
                              item.totalpax +
                              ")=" +
                              (item.purqty < item.totalpax
                                ? 0
                                : item.purqty - item.totalpax) +
                              `&times;${item.numdays}`
                            : item.purqty +
                              (item.itemOption === "room" ||
                              item.itemOption === "addons"
                                ? ""
                                : `&times;${item.numdays}`)
                        }}
                      </td>
                      <td v-if="item.itemOption !== 'room'">
                        {{ item.totalCartPrice }}
                      </td>
                      <td v-else>
                        <span
                          v-if="!isNaN(subroom.discountValue)"
                          v-html="
                            `${
                              item.totalCartPrice
                            } <sup class='text-danger font-weight-bold'>${
                              subroom.discountMode === 'percentage'
                                ? subroom.discountValue + '%'
                                : (
                                    subroom.discountValue /
                                    combinedcart.filter(
                                      (o) => o.itemOption === 'room'
                                    ).length
                                  ).toFixed(2)
                            } off</sup> <span class='text-success font-weight-bold'>${
                              subroom.discountMode === 'percentage'
                                ? item.totalCartPrice *
                                  (1 - parseFloat(subroom.discountValue / 100))
                                : item.totalCartPrice -
                                  (
                                    subroom.discountValue /
                                    combinedcart.filter(
                                      (o) => o.itemOption === 'room'
                                    ).length
                                  ).toFixed(2)
                            }</span>`
                          "
                        ></span>
                        <span v-else v-html="`${item.totalCartPrice}`"></span>
                      </td>
                    </tr>
                    <tr>
                      <td colspan="4" class="text-right">
                        <strong>Partial Payment:</strong>
                      </td>
                      <td class="text-danger">
                        <strong>-Php {{ partialPayment }}</strong>
                      </td>
                    </tr>
                    <tr>
                      <td colspan="4" class="text-right">
                        <strong>Total Due:</strong>
                      </td>
                      <td>
                        <strong>Php {{ total }}</strong>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <hr />
            <div class="row">
              <div class="col-12">
                <span style="font-size: small">Account History:</span>
                <table border="1">
                  <thead>
                    <tr>
                      <th>Date</th>
                      <th>Type</th>
                      <th>Reference #</th>
                      <th>Description</th>
                      <th>Amount</th>
                      <th>Balance</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, index) in cashHistory" :key="item.id">
                      <td>
                        {{
                          new Date(item.transaction_date).toLocaleDateString()
                        }},
                        {{ getTime(new Date(item.transaction_date)) }}
                      </td>
                      <td>
                        {{ item.paymentMethod }}
                      </td>
                      <td>
                        {{
                          item.nonCashReference.toString().replace("-", "") ===
                          ""
                            ? item.id
                            : item.id + "-" + item.nonCashReference
                        }}
                      </td>
                      <td>
                        {{
                          index === 0
                            ? "Init/DP"
                            : parseFloat(item.balance) === 0
                            ? "Full"
                            : "Partial"
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
            </div> -->

              <hr />
              <div class="row">
                <div class="col-12">
                  <span style="font-size: small">TO OUR VALUED GUESTS</span>
                  <p>
                    Thank you for choosing {{ APP_NAME }}! It is our main
                    priority to meet up with your expectations. We would like to
                    remind you of our minimal Rules and Regulations to make your
                    stay satisfying.
                  </p>
                  <p>
                    1. The resort is not liable for any injury and/or death due
                    to sickness or negligence of the guest.
                  </p>
                  <p>2. Safety deposit box is available at the Cashier Area.</p>
                  <p>
                    3. The resort is not liable in loss of valuables in the room
                    or within the resort premises.
                  </p>
                  <p>
                    4. Cancellation of bookings upon arrival is Non-Refundable.
                    Payments made shall not be refunded.
                  </p>
                  <p>
                    5. Room is good for 2 persons and maximum of 4 persons only.
                    Extra person/s will be charged.
                  </p>
                  <p>
                    6. Check-in time is 3:00PM. Check-out is 11:00AM. Excess
                    hour will be charged Php 350 per hour. Stay beyond 4:00PM
                    will be charged full or overnight rate.
                  </p>
                  <p>
                    7. Bringing of food is strictly not allowed. We charge
                    corkage of Php 500 per dish and Php 500 per bottle for
                    drinks
                  </p>
                  <p>
                    8. Any delivery of food from outside, we charge corkage
                    500.00 per order.
                  </p>
                  <p>9. Lost key is charge Php 1,000.</p>
                  <p>
                    10. Stains such as Henna, Ink, Dye, Oil or any sort of
                    stains on linen shall be charged to guest.
                  </p>
                  <p>11. Unavailed package inclusions are non-refundable.</p>
                  <p>12. Breakfast is served from 6:00AM to 9:00AM.</p>
                  <hr />
                  <p>
                    We agree to abide the safety rules and regulations imposed
                    by
                    {{ APP_NAME }}. Should any accident or any incident occurs
                    while in the premises, I/We hereby voluntarily release and
                    discharge Marilou Resort from any and all liabilities that
                    may arise from any accident whether or not such may result
                    to bodily injury or loss of life. I/We also solemnly
                    undertake to refrain from filing in any court or
                    quasi-judicial government body any and all kinds of legal
                    action, whether civil, criminal and/or administrative by
                    reason of such incident against the resort, its owner,
                    officers and employees.
                  </p>
                  <hr />
                  <p>
                    I have gone through the terms and conditions of my stay in
                    the resort and I agree to same.
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div v-if="isThereLeisures" :class="isThereLeisures ? 'col-12' : 'col-0'">
              <span style="font-size: small">WAIVER AND AGREEMENT TO LEASE WATER SPORTS</span>
              <p>
                The undersigned
                <span style="text-decoration: underline">{{
                  this.billing.clientName
                }}</span>
                further states and affirms that he/she has been fully advised
                and thoroughly informed of the dangers of using WATER SPORTS. By
                fixing his/her signature hereunder, he/she attests and certifies
                that he/she is fully aware of such basic risks.
              </p>
              <p>
                The UNDERSIGNED herein agrees and acknowledge that neither
                {{ APP_NAME }} located at {{ SITE_ADDRESS }}
                nor any of its officers, employees and staff or representative
                may not be held responsible or liable in any way what so ever
                for any incident, mishap or other occurrence in connection with
                the use of the WATER SPORTS which may result in injury, death
                illness or other physical or mental damages to the undersigned
                or company.
              </p>
              <p>
                The UNDERSIGNED finally declares that he/she is of legal age and
                legally competent to sign this waiver and release: he/she has
                acquired the consent of his/her parents or guardians and that
                he/she fully completely agrees without any qualification or
                reservation having signed and same voluntary and or his/her own
                freewill.
              </p>
              <p>
                In witness thereof; this Waiver and Release is voluntary signed
                at
                <span style="text-decoration: underline">{{ APP_NAME }}</span>
                on this day of
                <span style="text-decoration: underline">{{
                  currentDate
                }}</span>
              </p>
              <hr />
              <div class="row">
                <div class="col-12">
                  <span style="font-size: small">Terms &amp; Conditions:</span>
                  <p>
                    1. Since water sport needs the skill and know-how of the
                    operator, the lessee warrants that he/she can properly
                    operate the water sport.
                  </p>
                  <p>
                    2. In no case shall Water Sport be used by any other person
                    other than the lessee.
                  </p>
                  <p>
                    3. The Water Sports shall be operated only 300 meters radius
                    from the resort.
                  </p>
                  <p>
                    4. In the event of any wrong use, abuse or negligence on the
                    part of the lessee and the Water Sport suffers any damage,
                    the lessee/s hold himself/herself/themselves personally
                    liable for the cost of damage, repairs spare parts and loss
                    on income.
                  </p>
                  <p>
                    5. The lessee/s shall abide by all laws, rules and
                    guidelines in the operation of Water Sports.
                  </p>
                  <p>
                    6. Any untoward incident resulting to the Operation of Water
                    Sports
                  </p>
                  <p>
                    7. Never start the engine if you are less than 3 feet deep.
                    Otherwise, pebbles and sands could be sucked into the jet
                    intake, causing impelled damage.
                  </p>
                  <p>
                    8. Your are advised to slow down if you are still on the
                    shallow area.
                  </p>
                  <p>
                    9. Be careful with the swimmers, boat, people, sharp
                    objects, ropes and floating debris.
                  </p>
                  <p>
                    10. Observed distance to any WATER SPORTS to prevent any
                    collision.
                  </p>
                  <p>
                    11. The lessor has the right to stop the operation of the
                    WATER SPORT and the amount paid or deposit shall be
                    forfeited if the rules and regulations are not followed
                    accordingly.
                  </p>
                  <p>
                    12. No one is allowed to operate the WATER SPORTS if the
                    person is under the influence of liquor/drugs.
                  </p>
                  <p>
                    13. Upon signing hereof, the lessee/s hereby agree/s to all
                    the above terms and conditions.
                  </p>
                </div>
              </div>
              <div class="row">
                <div class="col-12">
                  <span style="font-size: small">List of Participants with Signature:</span>
                  <table border="0" cellpadding="0" cellspcing="0">
                    <tr>
                      <td>
                        <p>
                          1.
                          <span style="text-decoration: underline">{{
                            this.billing.clientName
                          }}</span>
                        </p>
                        <p>2._____________________________</p>
                        <p>3._____________________________</p>
                        <p>4._____________________________</p>
                        <p>5._____________________________</p>
                      </td>
                      <td>
                        <p>6._____________________________</p>
                        <p>7._____________________________</p>
                        <p>8._____________________________</p>
                        <p>9._____________________________</p>
                        <p>10._____________________________</p>
                      </td>
                    </tr>
                  </table>
                </div>
              </div>
            </div>
          </div>
          <div class="row mt-2">
            <div class="col-12" :style="!isThereLeisures ? 'border-right: dotted;' : ''">
              <hr />
              <div class="row">
                <div class="col-6">
                  <span style="font-size: small">Check-In Staff Signature:</span>
                </div>
                <div class="col-6 text-right">
                  <span style="font-size: small">Customer Signature:</span>
                  <p class="mt-2">Date: {{ currentDate }}</p>
                </div>
              </div>
              <hr style="border-bottom: dotted" />
            </div>
          </div>
          <hr />
          <div class="row">
            <div class="col-12">
              <span style="font-size: small; font-weight: bold">Disclaimer: This Form is Not an Official
                Receipt</span><br />
              <span style="font-size: smaller" class="text-muted d-flex justify-content-between">This document is not an
                official receipt. It is provided for
                reference and informational purposes only and does not represent
                a formal acknowledgment of payment. For official transactions or
                receipts, please obtain the appropriate documentation from the
                authorized source.</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- Modals -->
  <div class="modal fade show" id="showall-modal" tabindex="-1" role="dialog" aria-labelledby="showall-modalLabel"
    style="display: none; padding-right: 17px" aria-modal="true">
    <div class="modal-dialog modal-xl" style="max-width: 1200px !important" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="showall-modalLabel">Room Status</h4>
          <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <ul class="nav nav-tabs" id="roomTab" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="cancelled-tab" data-bs-toggle="tab" data-bs-target="#cancelled" type="button"
                role="tab" aria-controls="cancelled" aria-selected="true" @click="activeTab = 'cancelled'">
                Cancelled
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="reserved-tab" data-bs-toggle="tab" data-bs-target="#reserved" type="button"
                role="tab" aria-controls="reserved" aria-selected="true" @click="activeTab = 'reserved'">
                Reserved
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="occupied-tab" data-bs-toggle="tab" data-bs-target="#occupied" type="button"
                role="tab" aria-controls="occupied" aria-selected="false" @click="activeTab = 'occupied'">
                Occupied
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="checkedout-tab" data-bs-toggle="tab" data-bs-target="#checkedout" type="button"
                role="tab" aria-controls="checkedout" aria-selected="false" @click="activeTab = 'checkedout'">
                Checked Out
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="all-tab" data-bs-toggle="tab" data-bs-target="#all" type="button"
                role="tab" aria-controls="all" aria-selected="false" @click="activeTab = 'all'">
                All
              </button>
            </li>
          </ul>
          <div class="tab-content mt-3" id="roomTabContent">
            <div class="tab-pane fade" :class="{ 'show active': activeTab === 'cancelled' }" id="cancelled"
              role="tabpanel" aria-labelledby="cancelled-tab">
              <div class="container-fluid">
                <table-component :mainHeaders="bookingsOptions" :mainItems="filteredRoomBookings" :editable="false"
                  :toggleable="false" />
              </div>
            </div>
            <div class="tab-pane fade" :class="{ 'show active': activeTab === 'reserved' }" id="reserved" role="tabpanel"
              aria-labelledby="reserved-tab">
              <div class="container-fluid">
                <table-component :mainHeaders="bookingsOptions" :mainItems="filteredRoomBookings" :editable="false"
                  :toggleable="false" />
              </div>
            </div>
            <div class="tab-pane fade" :class="{ 'show active': activeTab === 'occupied' }" id="occupied" role="tabpanel"
              aria-labelledby="occupied-tab">
              <div class="container-fluid">
                <table-component :mainHeaders="bookingsOptions" :mainItems="filteredRoomBookings" :editable="false"
                  :toggleable="false" />
              </div>
            </div>
            <div class="tab-pane fade" :class="{ 'show active': activeTab === 'checkedout' }" id="checkedout"
              role="tabpanel" aria-labelledby="checkedout-tab">
              <div class="container-fluid">
                <table-component :mainHeaders="bookingsOptions" :mainItems="filteredRoomBookings" :editable="false"
                  :toggleable="false" />
              </div>
            </div>
            <div class="tab-pane fade" :class="{ 'show active': activeTab === 'all' }" id="all" role="tabpanel"
              aria-labelledby="all-tab" style="height: 475px; overflow-y: auto">
              <div class="container-fluid">
                <table-component :mainHeaders="bookingsAllOptions" :mainItems="filteredRoomBookings" :editable="false"
                  :toggleable="false" @custombtn-action="viewBooking" :custombtn="true">
                  <template #content="data">
                    <!-- {{ data.data.id  }} -->
                  </template>
                </table-component>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" data-bs-dismiss="modal">
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade show" id="addAccountModal" tabindex="-1" role="dialog" aria-labelledby="addAccountModalLabel"
    style="display: none; padding-right: 17px" aria-modal="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="addAccountModalLabel">Add Account</h4>
          <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="addWalkInGuest">
            <!-- Client Information -->
            <div class="form-group row">
              <label for="name" class="col-sm-2 col-form-label">Name:*</label>
              <div class="col-sm-4">
                <input type="text" class="form-control" id="name" v-model="walkinreservation.clientName" required
                  autocomplete="off" />
              </div>
              <label for="email" class="col-sm-2 col-form-label">Email:</label>
              <div class="col-sm-4">
                <input type="email" class="form-control" id="email" v-model="walkinreservation.clientEmail"
                  autocomplete="off" />
              </div>
            </div>
            <div class="form-group row">
              <label for="address" class="col-sm-2 col-form-label">Address:</label>
              <div class="col-sm-4">
                <input type="text" class="form-control" id="address" v-model="walkinreservation.clientAddress"
                  autocomplete="off" />
              </div>
              <label for="phone" class="col-sm-2 col-form-label">Phone:</label>
              <div class="col-sm-4">
                <input type="tel" class="form-control" id="phone" v-model="walkinreservation.clientPhone"
                  autocomplete="off" />
              </div>
            </div>
            <div class="form-group row">
              <label for="nationality" class="col-sm-2 col-form-label">Nationality:*</label>
              <div class="col-sm-4">
                <select class="form-control" id="nationality" v-model="walkinreservation.clientNationality" required>
                  <option value="">-- Please select --</option>
                  <option value="Filipino">Filipino</option>
                  <option value="American">American</option>
                  <option value="South Korean">South Korean</option>
                  <option value="Indian">Indian</option>
                  <option value="Afghan">Afghan</option>
                  <option value="Albanian">Albanian</option>
                  <option value="Algerian">Algerian</option>
                  <option value="Andorran">Andorran</option>
                  <option value="Angolan">Angolan</option>
                  <option value="Antiguan/Barbudan">Antiguan/Barbudan</option>
                  <option value="Argentine">Argentine</option>
                  <option value="Armenian">Armenian</option>
                  <option value="Australian">Australian</option>
                  <option value="Austrian">Austrian</option>
                  <option value="Azerbaijani">Azerbaijani</option>
                  <option value="Bahamian">Bahamian</option>
                  <option value="Bahraini">Bahraini</option>
                  <option value="Bangladeshi">Bangladeshi</option>
                  <option value="Barbadian">Barbadian</option>
                  <option value="Belarusian">Belarusian</option>
                  <option value="Belgian">Belgian</option>
                  <option value="Belizean">Belizean</option>
                  <option value="Beninese">Beninese</option>
                  <option value="Bhutanese">Bhutanese</option>
                  <option value="Bolivian">Bolivian</option>
                  <option value="Bosnian and Herzegovinian">
                    Bosnian and Herzegovinian
                  </option>
                  <option value="Botswanan">Botswanan</option>
                  <option value="Brazilian">Brazilian</option>
                  <option value="British">British</option>
                  <option value="Bruneian">Bruneian</option>
                  <option value="Bulgarian">Bulgarian</option>
                  <option value="Burkinabe">Burkinabe</option>
                  <option value="Burmese">Burmese</option>
                  <option value="Burundian">Burundian</option>
                  <option value="Cambodian">Cambodian</option>
                  <option value="Cameroonian">Cameroonian</option>
                  <option value="Canadian">Canadian</option>
                  <option value="Cape Verdean">Cape Verdean</option>
                  <option value="Central African">Central African</option>
                  <option value="Chadian">Chadian</option>
                  <option value="Chilean">Chilean</option>
                  <option value="Chinese">Chinese</option>
                  <option value="Colombian">Colombian</option>
                  <option value="Comorian">Comorian</option>
                  <option value="Congolese">Congolese</option>
                  <option value="Costa Rican">Costa Rican</option>
                  <option value="Croatian">Croatian</option>
                  <option value="Cuban">Cuban</option>
                  <option value="Cypriot">Cypriot</option>
                  <option value="Czech">Czech</option>
                  <option value="Danish">Danish</option>
                  <option value="Djiboutian">Djiboutian</option>
                  <option value="Dominican">Dominican</option>
                  <option value="Ecuadorian">Ecuadorian</option>
                  <option value="Egyptian">Egyptian</option>
                  <option value="Salvadoran">Salvadoran</option>
                  <option value="Equatorial Guinean">Equatorial Guinean</option>
                  <option value="Eritrean">Eritrean</option>
                  <option value="Estonian">Estonian</option>
                  <option value="Eswatini">Eswatini</option>
                  <option value="Ethiopian">Ethiopian</option>
                  <option value="Fijian">Fijian</option>
                  <option value="Finnish">Finnish</option>
                  <option value="French">French</option>
                  <option value="Gabonese">Gabonese</option>
                  <option value="Gambian">Gambian</option>
                  <option value="Georgian">Georgian</option>
                  <option value="German">German</option>
                  <option value="Ghanaian">Ghanaian</option>
                  <option value="Greek">Greek</option>
                  <option value="Grenadian">Grenadian</option>
                  <option value="Guatemalan">Guatemalan</option>
                  <option value="Guinea-Bissauan">Guinea-Bissauan</option>
                  <option value="Guinean">Guinean</option>
                  <option value="Guyanese">Guyanese</option>
                  <option value="Haitian">Haitian</option>
                  <option value="Honduran">Honduran</option>
                  <option value="Hungarian">Hungarian</option>
                  <option value="Icelandic">Icelandic</option>
                  <option value="Indonesian">Indonesian</option>
                  <option value="Iranian">Iranian</option>
                  <option value="Iraqi">Iraqi</option>
                  <option value="Irish">Irish</option>
                  <option value="Israeli">Israeli</option>
                  <option value="Italian">Italian</option>
                  <option value="Ivorian">Ivorian</option>
                  <option value="Jamaican">Jamaican</option>
                  <option value="Japanese">Japanese</option>
                  <option value="Jordanian">Jordanian</option>
                  <option value="Kazakhstani">Kazakhstani</option>
                  <option value="Kenyan">Kenyan</option>
                  <option value="Kittitian and Nevisian">
                    Kittitian and Nevisian
                  </option>
                  <option value="Kuwaiti">Kuwaiti</option>
                  <option value="Kyrgyz">Kyrgyz</option>
                  <option value="Laotian">Laotian</option>
                  <option value="Latvian">Latvian</option>
                  <option value="Lebanese">Lebanese</option>
                  <option value="Liberian">Liberian</option>
                  <option value="Libyan">Libyan</option>
                  <option value="Liechtensteiner">Liechtensteiner</option>
                  <option value="Lithuanian">Lithuanian</option>
                  <option value="Luxembourgish">Luxembourgish</option>
                  <option value="Macedonian">Macedonian</option>
                  <option value="Malagasy">Malagasy</option>
                  <option value="Malawian">Malawian</option>
                  <option value="Malaysian">Malaysian</option>
                  <option value="Maldivian">Maldivian</option>
                  <option value="Malian">Malian</option>
                  <option value="Maltese">Maltese</option>
                  <option value="Marshallese">Marshallese</option>
                  <option value="Mauritanian">Mauritanian</option>
                  <option value="Mauritian">Mauritian</option>
                  <option value="Mexican">Mexican</option>
                  <option value="Micronesian">Micronesian</option>
                  <option value="Moldovan">Moldovan</option>
                  <option value="Monacan">Monacan</option>
                  <option value="Mongolian">Mongolian</option>
                  <option value="Montenegrin">Montenegrin</option>
                  <option value="Moroccan">Moroccan</option>
                  <option value="Mozambican">Mozambican</option>
                  <option value="Namibian">Namibian</option>
                  <option value="Nauruan">Nauruan</option>
                  <option value="Nepalese">Nepalese</option>
                  <option value="New Zealander">New Zealander</option>
                  <option value="Nicaraguan">Nicaraguan</option>
                  <option value="Nigerien">Nigerien</option>
                  <option value="Nigerian">Nigerian</option>
                  <option value="North Korean">North Korean</option>
                  <option value="Norwegian">Norwegian</option>
                  <option value="Omani">Omani</option>
                  <option value="Pakistani">Pakistani</option>
                  <option value="Palauan">Palauan</option>
                  <option value="Palestinian">Palestinian</option>
                  <option value="Panamanian">Panamanian</option>
                  <option value="Papua New Guinean">Papua New Guinean</option>
                  <option value="Paraguayan">Paraguayan</option>
                  <option value="Peruvian">Peruvian</option>
                  <option value="Polish">Polish</option>
                  <option value="Portuguese">Portuguese</option>
                  <option value="Qatari">Qatari</option>
                  <option value="Romanian">Romanian</option>
                  <option value="Russian">Russian</option>
                  <option value="Rwandan">Rwandan</option>
                  <option value="Saint Lucian">Saint Lucian</option>
                  <option value="Salvadoran">Salvadoran</option>
                  <option value="Samoan">Samoan</option>
                  <option value="San Marinese">San Marinese</option>
                  <option value="Sao Tomean">Sao Tomean</option>
                  <option value="Saudi">Saudi</option>
                  <option value="Senegalese">Senegalese</option>
                  <option value="Serbian">Serbian</option>
                  <option value="Seychellois">Seychellois</option>
                  <option value="Sierra Leonean">Sierra Leonean</option>
                  <option value="Singaporean">Singaporean</option>
                  <option value="Slovakian">Slovakian</option>
                  <option value="Slovenian">Slovenian</option>
                  <option value="Solomon Islander">Solomon Islander</option>
                  <option value="Somali">Somali</option>
                  <option value="South African">South African</option>
                  <option value="Spanish">Spanish</option>
                  <option value="Sri Lankan">Sri Lankan</option>
                  <option value="Sudanese">Sudanese</option>
                  <option value="Surinamese">Surinamese</option>
                  <option value="Swazi">Swazi</option>
                  <option value="Swedish">Swedish</option>
                  <option value="Swiss">Swiss</option>
                  <option value="Syrian">Syrian</option>
                  <option value="Taiwanese">Taiwanese</option>
                  <option value="Tajik">Tajik</option>
                  <option value="Tanzanian">Tanzanian</option>
                  <option value="Thai">Thai</option>
                  <option value="Togolese">Togolese</option>
                  <option value="Tongan">Tongan</option>
                  <option value="Trinidadian or Tobagonian">
                    Trinidadian or Tobagonian
                  </option>
                  <option value="Tunisian">Tunisian</option>
                  <option value="Turkish">Turkish</option>
                  <option value="Tuvaluan">Tuvaluan</option>
                  <option value="Ugandan">Ugandan</option>
                  <option value="Ukrainian">Ukrainian</option>
                  <option value="Uruguayan">Uruguayan</option>
                  <option value="Uzbekistani">Uzbekistani</option>
                  <option value="Vanuatuan">Vanuatuan</option>
                  <option value="Venezuelan">Venezuelan</option>
                  <option value="Vietnamese">Vietnamese</option>
                  <option value="Vincentian">Vincentian</option>
                  <option value="Yemenite">Yemenite</option>
                  <option value="Zambian">Zambian</option>
                  <option value="Zimbabwean">Zimbabwean</option>
                  <option value="Other">Other</option>
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
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">
                  Close
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade show" id="settings-modal" tabindex="-1" role="dialog" aria-labelledby="settings-modalLabel"
    style="display: none; padding-right: 17px" aria-modal="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="settings-modalLabel">Settings</h4>
          <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
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
                <table class="table" style="table-layout: fixed; word-wrap: break-word">
                  <thead>
                    <tr>
                      <th scope="col">Status</th>
                      <th scope="col">Color</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Cancelled</td>
                      <td style="background-color: #bdbdbd; width: 25px"></td>
                    </tr>
                    <tr>
                      <td>Reserved</td>
                      <td style="background-color: #ef5350; width: 25px"></td>
                    </tr>
                    <tr>
                      <td>Reserved (partially paid)</td>
                      <td style="background-color: #5c6bc0; width: 25px"></td>
                    </tr>
                    <tr>
                      <td>Checked In</td>
                      <td style="background-color: #66bb6a; width: 25px"></td>
                    </tr>
                    <tr>
                      <td>Checked In (partially paid)</td>
                      <td style="background-color: #42a5f5; width: 25px"></td>
                    </tr>
                    <tr>
                      <td>Checked In (paid)</td>
                      <td style="background-color: #ffee58; width: 25px"></td>
                    </tr>
                    <tr>
                      <td>Checked Out (paid)</td>
                      <td style="background-color: #ff7043; width: 25px"></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" data-bs-dismiss="modal">
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade come-from-modal left" id="shopModal" tabindex="-1" aria-labelledby="shopModalLabel"
    aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="shopModalLabel">Add-ons</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-12">
              <ul class="nav nav-tabs justify-content-left">
                <li class="nav-item">
                  <a class="nav-link active show" data-bs-toggle="tab" href="#add_items">
                    Items
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-bs-toggle="tab" href="#add_packages">
                    Packages
                  </a>
                </li>
              </ul>
            </div>
          </div>

          <div class="tab-content">
            <div id="add_items" class="tab-pane active">
              <div class="row">
                <div class="col-md-12">
                  <input type="text" class="form-control mb-3" placeholder="Search item" v-model="searchText3" />
                  <div class="wrapper-content">
                    <table class="table" style="table-layout: fixed; word-wrap: break-word">
                      <tbody>
                        <tr v-for="(item, index) in filteredItems" :key="index">
                          <td>
                            {{ item.item }} ({{ item.priceRate }}/{{
                              item.counter
                            }})
                          </td>
                          <td>
                            <input style="width: 75px !important" class="form-control input-sm" type="number" min="0"
                              v-model.number="howMany[index]" />
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
            <div id="add_packages" class="tab-pane">
              <div class="row">
                <div class="col-md-12">
                  <input type="text" class="form-control mb-3" placeholder="Search package" v-model="searchPackage" />
                  <div class="wrapper-content">
                    <div v-for="item in packages" v-show="items.filter((o) => o.package_name == item.id).length >
                      0
                      " :key="item.id" class="card" style="transition: transform 0.2s ease-in-out"
                      @click="loadPackageItems(item)">
                      <div class="card-header d-flex justify-content-between align-items-center">
                        <h5 class="card-title">
                          {{ item.name }}
                        </h5>
                      </div>
                      <div class="card-body">
                        <ul>
                          <li v-for="leisure in items.filter(
                            (o) => o.package_name == item.id
                          )">
                            {{ leisure.item }}
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="availableRoomsModal" tabindex="-1" aria-labelledby="availableRoomsLabel" aria-hidden="true">
    <div class="modal-dialog modal-xl">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="availableRoomsLabel">
            Available Rooms/Cottages from
            {{ selectionStart.toLocaleDateString() }} to
            {{ selectionEnd.toLocaleDateString() }}
          </h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body" style="height: 500px; overflow-y: auto; overflow-x: hidden">
          <div class="row d-flex justify-content-start">
            <div class="col-md-3">
              <select class="form-select" id="type" v-model="filter.roompax">
                <option value="">How many Room pax?</option>
                <option value="2">2 pax</option>
                <option value="3">3 pax</option>
                <option value="4">4 pax</option>
                <option value="5">5 pax</option>
                <option value="10">10 pax</option>
              </select>
            </div>
            <div class="col-md-3">
              <select class="form-select" id="type" v-model="filter.bedtype">
                <option value="">Which Bed Type?</option>
                <option value="King Size">King Size</option>
                <option value="Queen Size">Queen Size</option>
                <option value="Twin Beds">Twin Beds</option>
                <option value="Mix">Mix</option>
                <option value="N/A">Not Applicable</option>
              </select>
            </div>
            <div class="col-md-3">
              <select class="form-select" id="type" v-model="filter.nearat">
                <option value="">Near At?</option>
                <option value="Beach">Near at the Beach</option>
                <option value="Restaurant">Near at the Restaurant</option>
                <option value="Pool">Near at the Pool</option>
                <option value="Garden">Near at the Garden</option>
                <option value="Scenery">Near at the Scenery</option>
                <option value="Parking Space">Near at the Parking Space</option>
              </select>
            </div>
            <div class="col-md-3">
              <input placeholder="Specific details?" type="text" class="form-control" v-model="filter.desc" />
            </div>
          </div>
          <div class="row">
            <div :class="cartItems.length > 0 ? 'col-md-9' : 'col-md-12'">
              <div class="col-md-12">
                <ul class="nav bg radius nav-pills nav-fill mb-3 bg mt-3" role="tablist">
                  <li class="nav-item">
                    <a class="nav-link active" data-bs-toggle="tab" href="#roomcategoryallops">All</a>
                  </li>
                  <li class="nav-item" v-for="(category, index) in roomcategories" :key="category.id">
                    <a class="nav-link" data-bs-toggle="tab" :href="`#roomcategory${index}`">{{ category.name }}</a>
                  </li>
                </ul>
              </div>
              <div class="tab-content" id="myTabContent">
                <div class="tab-pane fade show active" id="roomcategoryallops" role="tabpanel">
                  <div class="container-fluid">
                    <div class="row">
                      <div class="col-md-12">
                        <div class="row row-cols-1" :class="cartItems.length > 0
                            ? 'row-cols-md-4'
                            : 'row-cols-md-5'
                          ">
                          <div class="col mb-6" v-for="(item, index) in filteredupdatedRooms.filter(
                            (r) => {
                              if (r.type) {
                                const isDataExist = !(
                                  this.cartItems.findIndex(
                                    (o) => o.id === r.id
                                  ) === -1
                                );
                                return !isDataExist;
                              }
                              return true;
                            }
                          )" :key="item.id">
                            <div class="card" style="transition: transform 0.2s ease-in-out" @click="addToCartItem(item)">
                              <div class="card-header d-flex justify-content-between align-items-center">
                                <h5 class="card-title">
                                  <i class="fas fa-table"></i>
                                  {{ item.name }}
                                </h5>
                                <h5>
                                  <i>pax:{{ item.pax }}</i>
                                </h5>
                              </div>
                              <div class="card-body">
                                <h6 class="text-dark">
                                  <i class="fas fa-info-circle"></i>
                                  available
                                </h6>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div v-for="(category, index) in roomcategories" :key="category.id" class="tab-pane fade"
                  :id="`roomcategory${index}`" role="tabpanel">
                  <div class="container-fluid">
                    <div class="row">
                      <div class="col-md-12">
                        <div class="row row-cols-1" :class="cartItems.filter((o) => o.type === category.name)
                            .length > 0
                            ? 'row-cols-md-4'
                            : 'row-cols-md-5'
                          ">
                          <div class="col mb-6" v-for="(item, index) in filteredupdatedRooms.filter(
                            (r) => {
                              if (r.type) {
                                const isDataExist = !(
                                  this.cartItems.findIndex(
                                    (o) => o.id === r.id
                                  ) === -1
                                );
                                return (
                                  r.type === category.name && !isDataExist
                                );
                              }
                              return true;
                            }
                          )" :key="item.id">
                            <div class="card" style="transition: transform 0.2s ease-in-out" @click="addToCartItem(item)">
                              <div class="card-header d-flex justify-content-between align-items-center">
                                <h5 class="card-title">
                                  <i class="fas fa-table"></i>
                                  {{ item.name }}
                                </h5>
                                <h5>
                                  <i>pax:{{ item.pax }}</i>
                                </h5>
                              </div>
                              <div class="card-body">
                                <h6 class="text-dark">
                                  <i class="fas fa-info-circle"></i>
                                  available
                                </h6>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div v-if="cartItems.length > 0" :class="cartItems.length > 0 ? 'col-md-3' : 'col-md-0'">
              <div ref="itemCart" class="card" style="height: 450px; overflow-y: auto; overflow-x: hidden">
                <div class="row">
                  <div class="col-md-12 px-3">
                    <table class="table">
                      <thead>
                        <tr>
                          <th scope="col">
                            Item
                            <span v-if="cartItems.length > 0" class="badge-pill badge-danger">{{ cartItems.length
                            }}</span>
                          </th>
                          <th scope="col">
                            <span class="d-flex flex-row-reverse">
                              <button v-if="cartItems.length > 0" type="button" @click="bookAll"
                                class="btn btn-sm bg-primary text-white">
                                <i class="fas fa-check"></i>
                              </button>
                              &nbsp;
                              <button v-if="cartItems.length > 0" type="button" @click="clearAll"
                                class="btn btn-sm btn-danger">
                                <i class="fas fa-trash-alt"></i>
                              </button>
                            </span>
                          </th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(item, index) in cartItems" :key="index">
                          <td>
                            {{ item.name }}
                          </td>

                          <td align="right">
                            <button class="btn btn-outline-danger btn-sm" type="button" @click="removeFromCart(item)">
                              <i class="fas fa-times"></i>
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
    </div>
  </div>
  <div class="modal fade" id="guestListModal" tabindex="-1" aria-labelledby="guestListModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-xl">
      <div class="modal-content p-3">
        <div class="modal-header">
          <h5 class="modal-title" id="guestListModalLabel">Guest List</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div id="printstab">
            <div class="container-fluid">
              <div class="row">
                <div class="col-md-12">
                  <div class="row row-cols-1 row-cols-md-4">
                    <template v-for="(item, index) in currentMealStabs" :key="index">
                      <div class="col mb-4">
                        <div class="card p-0">
                          <div class="card-header text-center p-0">
                            <h6 style="font-family: Fantasy">
                              {{ this.APP_NAME }} - RestoBar
                            </h6>
                          </div>
                          <div class="card-body py-0">
                            <div class="row">
                              <div class="col-md-4 d-flex justify-content-center p-0">
                                <img :src="`/src/assets/${this.APP_LOGO_NAME}`" width="75" height="75"
                                  class="d-inline-block align-top" alt="Logo" style="margin-right: 10px" />
                              </div>
                              <div class="col-md-8 text-center p-0">
                                <span style="font-size: smaller" class="mb-0">Breakfast Buffet Meal Stab</span><br />
                                <span style="font-size: smaller" class="mb-0 mt-0">{{ item.validdate }}
                                  (7-9am)</span><br />
                                <div class="row mb-0 mt-0">
                                  <div class="col-md-12">
                                    <span style="font-size: smaller">Guest: {{ item.person }}</span>
                                  </div>
                                </div>
                                <div class="row mb-0 mt-0">
                                  <div class="col-md-12">
                                    <span style="font-size: smaller">Ticket No: {{ item.ticketno }}</span>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </template>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <table class="table">
              <thead>
                <th>Name</th>
                <th>Gender</th>
                <th>Type</th>
                <th>Address</th>
                <th>Contact no.</th>
                <th>Email</th>
              </thead>
              <tbody>
                <tr v-for="index in currentTotalGuest" :key="index">
                  <td>
                    <input type="text" class="form-control" v-model="guestdetails.names[index - 1]" />
                  </td>
                  <td>
                    <select class="form-control" v-model="guestdetails.genders[index - 1]">
                      <option value="male">Male</option>
                      <option value="female">Female</option>
                      <option value="lgbtq">LGBTQ+</option>
                    </select>
                  </td>
                  <td>
                    <select class="form-control" v-model="guestdetails.types[index - 1]">
                      <option value="Regular Adult" selected>
                        Regular Adult
                      </option>
                      <option value="Regular Kid">Regular Kid</option>
                      <option value="Senior">Senior</option>
                      <option value="PWD">PWD</option>
                    </select>
                  </td>
                  <td>
                    <textarea rows="2" class="form-control" v-model="guestdetails.addresses[index - 1]">
                    </textarea>
                  </td>
                  <td>
                    <input type="text" class="form-control" v-model="guestdetails.contactnos[index - 1]" />
                  </td>
                  <td>
                    <input type="text" class="form-control" v-model="guestdetails.emails[index - 1]" />
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="form-group row">
            <div class="d-flex justify-content-end">
              <button type="button" class="btn btn-primary" @click="postGuest">
                <span><i class="fa fa-save"></i> Save Guests</span>
              </button>
              &nbsp;
              <button v-if="isReadyToPrintStabs" type="button" class="btn btn-primary" @click="printMealStab">
                <span><i class="fa fa-print"></i> Print Meal Stabs</span>
              </button>
              &nbsp;
              <button type="button" class="btn btn-danger" data-bs-dismiss="modal">
                <span><i class="fa fa-times"></i> Close</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="dayMenuModal" tabindex="-1" aria-labelledby="dayMenuModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="dayMenuModalLabel">
            Room Reservation
            {{
              this.selectionStart.toLocaleDateString("en-GB") ===
              this.selectionEnd.toLocaleDateString("en-GB")
              ? " for" + this.selectionStart.toLocaleDateString("en-GB")
              : " from" +
              this.selectionStart.toLocaleDateString("en-GB") +
              " to " +
              this.selectionEnd.toLocaleDateString("en-GB")
            }}
            <p class="text-muted" style="font-size: smaller">
              <i class="fa fa-info-circle"></i> Check-out date is day +1 from
              {{
                this.selectionStart.toLocaleDateString("en-GB") ===
                this.selectionEnd.toLocaleDateString("en-GB")
                ? this.selectionStart.toLocaleDateString("en-GB")
                : this.selectionEnd.toLocaleDateString("en-GB")
              }}.
            </p>
          </h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-4">
              <a href="#" @click="clickDay" class="d-flex flex-column align-items-center">
                <i class="fa fa-calendar-plus"></i>
                <span>Create</span>
              </a>
            </div>
            <div class="col-md-4">
              <a href="#" @click="viewAllReservation" class="d-flex flex-column align-items-center">
                <i class="fa fa-calendar-check"></i>
                <span>View All</span>
              </a>
            </div>
            <div class="col-md-4">
              <a href="#" @click="
                toggleRoomsModal();
              toggledayMenuModal();
              " class="d-flex flex-column align-items-center">
                <i class="fa fa-check"></i>
                <span>Available</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade show" id="BookDayModal" tabindex="-1" role="dialog" aria-labelledby="BookDayModalLabel"
    style="display: none; padding-right: 17px" aria-modal="true" ref="modal">
    <div class="modal-dialog" :class="filteredhistlogs.length > 0 ? 'modal-xl' : 'modal-lg'" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 id="BookDayModalLabel" class="text-primary">Reservation Info</h4>
          <span>
            <button v-if="reservation.status !== 'cancelled' &&
              reservation.status !== 'checkedout'
              " type="button" class="close" @click="saveBookingInfo">
              <span aria-hidden="true"><i class="fa fa-save"></i></span>
            </button>
            &nbsp;
            <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
              <span aria-hidden="true"><i class="fa fa-close"></i></span>
            </button>
          </span>
        </div>
        <div class="modal-body">
          <div v-if="!movetocartFlag || !bookNowFlag" class="loading-spinner">
            <div class="spinner-border text-primary" role="status">
              <span class="visually-hidden"></span>
            </div>
            <p class="loading-text h5">Loading...(Do not click anywhere!)</p>
          </div>
          <div class="row" v-else>
            <div :class="filteredhistlogs.length > 0 ? 'col-md-8' : 'col-md-12'">
              <h5>
                Booking Details<span class="text-muted" style="font-size: 12px">*Field required</span>
              </h5>
              <div class="form-group row">
                <label for="name" class="col-sm-2 col-form-label">Name:*</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control book-form" id="name" v-model="reservation.clientName" required
                    autocomplete="off" />
                </div>
                <label for="email" class="col-sm-2 col-form-label">Email:</label>
                <div class="col-sm-4">
                  <input type="email" class="form-control book-form" id="email" v-model="reservation.clientEmail"
                    autocomplete="off" />
                </div>
              </div>
              <div class="form-group row mt-2">
                <label for="address" class="col-sm-2 col-form-label">Address:</label>
                <div class="col-sm-4">
                  <input type="text" class="form-control book-form"  id="address" v-model="reservation.clientAddress"
                    autocomplete="off" />
                  <!--
                  <form
                    id="address-form"
                    action=""
                    method="get"
                    autocomplete="off"
                  >
                    <input
                      id="loc-address"
                      name="loc-address"
                      ref="address1Field"
                      v-on:focus="initAutocomplete"
                      class="address"
                      autocomplete="off"
                      required
                    />
                  </form>
                  -->
                </div>
                <label for="phone" class="col-sm-2 col-form-label">Phone:</label>
                <div class="col-sm-4">
                  <input type="tel" class="form-control book-form" id="phone" v-model="reservation.clientPhone"
                    autocomplete="off" />
                </div>
              </div>
              <div class="form-group row mt-2">
                <label for="nationality" class="col-sm-2 col-form-label">Nationality:*</label>
                <div class="col-sm-4">
                  <select class="form-control book-form" id="nationality" v-model="reservation.clientNationality"
                    required>
                    <option value="">-- Please select --</option>
                    <option value="Filipino">Filipino</option>
                    <option value="American">American</option>
                    <option value="South Korean">South Korean</option>
                    <option value="Indian">Indian</option>
                    <option value="Afghan">Afghan</option>
                    <option value="Albanian">Albanian</option>
                    <option value="Algerian">Algerian</option>
                    <option value="Andorran">Andorran</option>
                    <option value="Angolan">Angolan</option>
                    <option value="Antiguan/Barbudan">Antiguan/Barbudan</option>
                    <option value="Argentine">Argentine</option>
                    <option value="Armenian">Armenian</option>
                    <option value="Australian">Australian</option>
                    <option value="Austrian">Austrian</option>
                    <option value="Azerbaijani">Azerbaijani</option>
                    <option value="Bahamian">Bahamian</option>
                    <option value="Bahraini">Bahraini</option>
                    <option value="Bangladeshi">Bangladeshi</option>
                    <option value="Barbadian">Barbadian</option>
                    <option value="Belarusian">Belarusian</option>
                    <option value="Belgian">Belgian</option>
                    <option value="Belizean">Belizean</option>
                    <option value="Beninese">Beninese</option>
                    <option value="Bhutanese">Bhutanese</option>
                    <option value="Bolivian">Bolivian</option>
                    <option value="Bosnian and Herzegovinian">
                      Bosnian and Herzegovinian
                    </option>
                    <option value="Botswanan">Botswanan</option>
                    <option value="Brazilian">Brazilian</option>
                    <option value="British">British</option>
                    <option value="Bruneian">Bruneian</option>
                    <option value="Bulgarian">Bulgarian</option>
                    <option value="Burkinabe">Burkinabe</option>
                    <option value="Burmese">Burmese</option>
                    <option value="Burundian">Burundian</option>
                    <option value="Cambodian">Cambodian</option>
                    <option value="Cameroonian">Cameroonian</option>
                    <option value="Canadian">Canadian</option>
                    <option value="Cape Verdean">Cape Verdean</option>
                    <option value="Central African">Central African</option>
                    <option value="Chadian">Chadian</option>
                    <option value="Chilean">Chilean</option>
                    <option value="Chinese">Chinese</option>
                    <option value="Colombian">Colombian</option>
                    <option value="Comorian">Comorian</option>
                    <option value="Congolese">Congolese</option>
                    <option value="Costa Rican">Costa Rican</option>
                    <option value="Croatian">Croatian</option>
                    <option value="Cuban">Cuban</option>
                    <option value="Cypriot">Cypriot</option>
                    <option value="Czech">Czech</option>
                    <option value="Danish">Danish</option>
                    <option value="Djiboutian">Djiboutian</option>
                    <option value="Dominican">Dominican</option>
                    <option value="Ecuadorian">Ecuadorian</option>
                    <option value="Egyptian">Egyptian</option>
                    <option value="Salvadoran">Salvadoran</option>
                    <option value="Equatorial Guinean">
                      Equatorial Guinean
                    </option>
                    <option value="Eritrean">Eritrean</option>
                    <option value="Estonian">Estonian</option>
                    <option value="Eswatini">Eswatini</option>
                    <option value="Ethiopian">Ethiopian</option>
                    <option value="Fijian">Fijian</option>
                    <option value="Finnish">Finnish</option>
                    <option value="French">French</option>
                    <option value="Gabonese">Gabonese</option>
                    <option value="Gambian">Gambian</option>
                    <option value="Georgian">Georgian</option>
                    <option value="German">German</option>
                    <option value="Ghanaian">Ghanaian</option>
                    <option value="Greek">Greek</option>
                    <option value="Grenadian">Grenadian</option>
                    <option value="Guatemalan">Guatemalan</option>
                    <option value="Guinea-Bissauan">Guinea-Bissauan</option>
                    <option value="Guinean">Guinean</option>
                    <option value="Guyanese">Guyanese</option>
                    <option value="Haitian">Haitian</option>
                    <option value="Honduran">Honduran</option>
                    <option value="Hungarian">Hungarian</option>
                    <option value="Icelandic">Icelandic</option>
                    <option value="Indonesian">Indonesian</option>
                    <option value="Iranian">Iranian</option>
                    <option value="Iraqi">Iraqi</option>
                    <option value="Irish">Irish</option>
                    <option value="Israeli">Israeli</option>
                    <option value="Italian">Italian</option>
                    <option value="Ivorian">Ivorian</option>
                    <option value="Jamaican">Jamaican</option>
                    <option value="Japanese">Japanese</option>
                    <option value="Jordanian">Jordanian</option>
                    <option value="Kazakhstani">Kazakhstani</option>
                    <option value="Kenyan">Kenyan</option>
                    <option value="Kittitian and Nevisian">
                      Kittitian and Nevisian
                    </option>
                    <option value="Kuwaiti">Kuwaiti</option>
                    <option value="Kyrgyz">Kyrgyz</option>
                    <option value="Laotian">Laotian</option>
                    <option value="Latvian">Latvian</option>
                    <option value="Lebanese">Lebanese</option>
                    <option value="Liberian">Liberian</option>
                    <option value="Libyan">Libyan</option>
                    <option value="Liechtensteiner">Liechtensteiner</option>
                    <option value="Lithuanian">Lithuanian</option>
                    <option value="Luxembourgish">Luxembourgish</option>
                    <option value="Macedonian">Macedonian</option>
                    <option value="Malagasy">Malagasy</option>
                    <option value="Malawian">Malawian</option>
                    <option value="Malaysian">Malaysian</option>
                    <option value="Maldivian">Maldivian</option>
                    <option value="Malian">Malian</option>
                    <option value="Maltese">Maltese</option>
                    <option value="Marshallese">Marshallese</option>
                    <option value="Mauritanian">Mauritanian</option>
                    <option value="Mauritian">Mauritian</option>
                    <option value="Mexican">Mexican</option>
                    <option value="Micronesian">Micronesian</option>
                    <option value="Moldovan">Moldovan</option>
                    <option value="Monacan">Monacan</option>
                    <option value="Mongolian">Mongolian</option>
                    <option value="Montenegrin">Montenegrin</option>
                    <option value="Moroccan">Moroccan</option>
                    <option value="Mozambican">Mozambican</option>
                    <option value="Namibian">Namibian</option>
                    <option value="Nauruan">Nauruan</option>
                    <option value="Nepalese">Nepalese</option>
                    <option value="New Zealander">New Zealander</option>
                    <option value="Nicaraguan">Nicaraguan</option>
                    <option value="Nigerien">Nigerien</option>
                    <option value="Nigerian">Nigerian</option>
                    <option value="North Korean">North Korean</option>
                    <option value="Norwegian">Norwegian</option>
                    <option value="Omani">Omani</option>
                    <option value="Pakistani">Pakistani</option>
                    <option value="Palauan">Palauan</option>
                    <option value="Palestinian">Palestinian</option>
                    <option value="Panamanian">Panamanian</option>
                    <option value="Papua New Guinean">Papua New Guinean</option>
                    <option value="Paraguayan">Paraguayan</option>
                    <option value="Peruvian">Peruvian</option>
                    <option value="Polish">Polish</option>
                    <option value="Portuguese">Portuguese</option>
                    <option value="Qatari">Qatari</option>
                    <option value="Romanian">Romanian</option>
                    <option value="Russian">Russian</option>
                    <option value="Rwandan">Rwandan</option>
                    <option value="Saint Lucian">Saint Lucian</option>
                    <option value="Salvadoran">Salvadoran</option>
                    <option value="Samoan">Samoan</option>
                    <option value="San Marinese">San Marinese</option>
                    <option value="Sao Tomean">Sao Tomean</option>
                    <option value="Saudi">Saudi</option>
                    <option value="Senegalese">Senegalese</option>
                    <option value="Serbian">Serbian</option>
                    <option value="Seychellois">Seychellois</option>
                    <option value="Sierra Leonean">Sierra Leonean</option>
                    <option value="Singaporean">Singaporean</option>
                    <option value="Slovakian">Slovakian</option>
                    <option value="Slovenian">Slovenian</option>
                    <option value="Solomon Islander">Solomon Islander</option>
                    <option value="Somali">Somali</option>
                    <option value="South African">South African</option>
                    <option value="Spanish">Spanish</option>
                    <option value="Sri Lankan">Sri Lankan</option>
                    <option value="Sudanese">Sudanese</option>
                    <option value="Surinamese">Surinamese</option>
                    <option value="Swazi">Swazi</option>
                    <option value="Swedish">Swedish</option>
                    <option value="Swiss">Swiss</option>
                    <option value="Syrian">Syrian</option>
                    <option value="Taiwanese">Taiwanese</option>
                    <option value="Tajik">Tajik</option>
                    <option value="Tanzanian">Tanzanian</option>
                    <option value="Thai">Thai</option>
                    <option value="Togolese">Togolese</option>
                    <option value="Tongan">Tongan</option>
                    <option value="Trinidadian or Tobagonian">
                      Trinidadian or Tobagonian
                    </option>
                    <option value="Tunisian">Tunisian</option>
                    <option value="Turkish">Turkish</option>
                    <option value="Tuvaluan">Tuvaluan</option>
                    <option value="Ugandan">Ugandan</option>
                    <option value="Ukrainian">Ukrainian</option>
                    <option value="Uruguayan">Uruguayan</option>
                    <option value="Uzbekistani">Uzbekistani</option>
                    <option value="Vanuatuan">Vanuatuan</option>
                    <option value="Venezuelan">Venezuelan</option>
                    <option value="Vietnamese">Vietnamese</option>
                    <option value="Vincentian">Vincentian</option>
                    <option value="Yemenite">Yemenite</option>
                    <option value="Zambian">Zambian</option>
                    <option value="Zimbabwean">Zimbabwean</option>
                    <option value="Other">Other</option>
                  </select>
                </div>
                <label for="clientType" class="col-sm-2 col-form-label">Type:*</label>
                <div class="col-sm-4">
                  <select class="form-control book-form" id="clientType" v-model="reservation.clientType" required>
                    <option value="">-- Please select --</option>
                    <option value="in-house">In-house</option>
                  </select>
                </div>
              </div>
              <div class="form-group row mt-2">
                <label for="checkin" class="col-sm-2 col-form-label">Check-in Date:*</label>
                <div class="col-sm-4">
                  <div class="row d-flex justify-content-between">
                    <div class="col-sm-10">
                      <input v-if="!isCheckinToggle" type="text" aria-describedby="inputhelp1"
                        class="form-control mb-0 book-form" v-model="reservation.checkinDate" required readonly />
                      <input v-else type="date" aria-describedby="inputhelp1" class="form-control mb-0 book-form"
                        v-model="reservation.checkinDate" required />
                    </div>
                    <div class="col-sm-2">
                      <button v-if="!toggleselect &&
                        !toggleselect2 &&
                        !notoggle &&
                        !bookalltoggle &&
                        !newtoggle &&
                        reservation.status !== 'checkedout' &&
                        reservation.status !== 'cancelled' &&
                        booksearchtext === ''
                        " type="button" @click="toggleCheckin"
                        class="btn btn-lg badge rounded-pill d-inline btn-primary">
                        <i v-if="!isCheckinToggle" class="fas fa-pencil-alt text-white"></i>
                        <i v-else class="fas fa-save text-white"></i>
                      </button>
                    </div>
                  </div>
                </div>
                <label for="checkout" class="col-sm-2 col-form-label">Check-out Date:*</label>
                <div class="col-sm-4">
                  <div class="row d-flex justify-content-between">
                    <div class="col-sm-10">
                      <input v-if="reservation.status !== 'vacant' &&
                        reservation.status !== 'reserved' &&
                        reservation.status !== 'checkedin' &&
                        reservation.status !== 'checkedout' &&
                        reservation.status !== 'cancelled'
                        " type="text" aria-describedby="inputhelp0" class="form-control mb-0 book-form"
                        v-model="reservation.checkoutDate" required readonly />
                      <template v-else>
                        <input v-if="!isCheckoutToggle" type="text" aria-describedby="inputhelp0"
                          class="form-control mb-0 book-form" :value="setCheckoutDate()" required readonly />
                        <input v-else type="date" aria-describedby="inputhelp0" class="form-control mb-0 book-form"
                          v-model="reservation.checkoutDate" required />
                      </template>
                      <small v-if="isCheckoutToggle" id="inputhelp0" class="form-text text-muted mt-0">Check-out date is
                        day +1.</small>
                    </div>
                    <div class="col-sm-2">
                      <button v-if="!toggleselect &&
                        !toggleselect2 &&
                        !notoggle &&
                        !bookalltoggle &&
                        !newtoggle &&
                        reservation.status !== 'checkedout' &&
                        reservation.status !== 'cancelled' &&
                        booksearchtext === ''
                        " type="button" @click="toggleCheckout"
                        class="btn btn-lg badge rounded-pill d-inline btn-primary">
                        <i v-if="!isCheckoutToggle" class="fas fa-pencil-alt text-white"></i>
                        <i v-else class="fas fa-save text-white"></i>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <div class="form-group row mt-2">
                <label for="room" class="col-sm-2 col-form-label">Room:*</label>
                <div v-if="reservation.status === 'vacant' || toggleselect" class="col-sm-4">
                  <v-select :disabled="roomSelect !== 'ok'" aria-describedby="inputhelp3" :multiple="!toggleselect"
                    :options="updatedRooms" label="name" v-model="reservation.roomName" required>
                    <template #option="{ name, type, price, pax }">
                      <h6 style="margin: 0">{{ name }} &nbsp; pax:{{ pax }}</h6>
                      <em><small>{{ type }}</small></em>
                      <em><small> ({{ price }} units)</small></em>
                    </template>
                  </v-select>
                  <small v-if="toggleselect" id="inputhelp3" class="form-text text-muted mt-0">Please select a new
                    room.</small>
                </div>
                <div v-else class="col-sm-4">
                  <input type="text" class="form-control book-form" v-model="reservation.roomName" readonly />
                </div>
                <label for="remarks" class="col-sm-2 col-form-label">Remarks:</label>
                <div class="col-sm-4">
                  <textarea class="form-control book-form" v-model="reservation.remarks" autocomplete="off"
                    rows="4"></textarea>
                </div>
              </div>
            </div>
            <div v-if="filteredhistlogs.length > 0" class="col-md-4">
              <h5>History Logs</h5>
              <div class="row" style="
                  max-height: 300px !important;
                  overflow-y: auto;
                  overflow-x: auto;
                ">
                <table class="table table-hover table-sm" style="font-family: Roboto; font-size: 12px">
                  <thead>
                    <tr>
                      <th>type</th>
                      <th>actor</th>
                      <th>details</th>
                      <th>date</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in filteredhistlogs" style="height:">
                      <td>{{ item.type }}</td>
                      <td>{{ item.actor }}</td>
                      <td>{{ item.details }}</td>
                      <td>{{ item.date }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer p-2">
          <div class="form-group row">
            <div class="d-flex justify-content-end">
              <div v-if="reservation.status == 'reserved'">
                <button v-if="reservation.isPaid === 'no'" v-show="!toggleselect" type="button"
                  class="btn btn-primary btn-sm btn-margin rounded" @click="cancelReservation()">
                  <i class="fas fa-times"></i> Cancel Reservation
                </button>
                <span v-if="userdata.role !== 'reservationist'">
                  <button :disabled="disablebutton" v-show="!toggleselect" v-if="reservation.isPaid === '' || reservation.isPaid === 'no'
                    " @click="
    moveToCart();
  disablebutton = true;
  " type="button" class="btn btn-success btn-sm btn-margin rounded">
                    <i class="fas fa-check"></i> Down Payment
                  </button>
                  <button :disabled="disablebutton" v-show="!toggleselect" v-else-if="reservation.isPaid === 'partial'"
                    @click="
                      moveToCart();
                    disablebutton = true;
                    " type="button" class="btn btn-warning btn-sm btn-margin rounded">
                    <i class="fas fa-check"></i> Partial Payment
                  </button>
                  <button :disabled="disablebutton" v-show="!toggleselect" v-else-if="reservation.isPaid === 'yes'"
                    @click="
                      moveToCart();
                    disablebutton = true;
                    " type="button" class="btn btn-primary btn-sm btn-margin rounded">
                    <i class="fas fa-eye"></i> View Summary
                  </button>
                  <button :disabled="disablebutton" v-show="!toggleselect" v-if="new Date().setHours(0, 0, 0, 0) ===
                    parseDate2(reservation.checkinDate)
                    " type="button" class="btn btn-success btn-sm btn-margin rounded" @click="
    checkinGuest();
  disablebutton = true;
  ">
                    <i class="fas fa-sign-in-alt"></i> Check-in
                  </button>
                </span>
              </div>
              <div v-else-if="reservation.status == 'checkedin'">
                <span v-if="userdata.role !== 'reservationist'">
                  <div v-if="reservation.isPaid === '' || reservation.isPaid === 'no'
                    ">
                    <button :disabled="disablebutton" v-show="!toggleselect" @click="
                      moveToCart();
                    disablebutton = true;
                    " type="button" class="btn btn-success btn-sm btn-margin rounded">
                      <i class="fas fa-credit-card"></i> Pay Now
                    </button>
                  </div>
                  <div v-else-if="reservation.isPaid === 'partial'">
                    <button :disabled="disablebutton" v-show="!toggleselect" @click="
                      moveToCart();
                    disablebutton = true;
                    " type="button" class="btn btn-success btn-sm btn-margin rounded">
                      <i class="fas fa-credit-card"></i> Pay Now
                    </button>
                  </div>
                  <div v-else>
                    <button :disabled="disablebutton" v-show="!toggleselect" type="button"
                      class="btn btn-primary btn-sm btn-margin rounded" @click="
                        moveToCart();
                      disablebutton = true;
                      ">
                      <i class="fas fa-eye"></i> View Summary
                    </button>
                    <button :disabled="disablebutton" v-show="!toggleselect" type="button"
                      class="btn btn-danger btn-sm btn-margin rounded" @click="
                        earlycheckOutGuest();
                      disablebutton = true;
                      ">
                      <i class="fas fa-sign-out-alt"></i> Early Check-out
                    </button>
                    <button :disabled="disablebutton" v-show="!toggleselect" type="button"
                      class="btn btn-success btn-sm btn-margin rounded" @click="
                        checkOutGuest();
                      disablebutton = true;
                      ">
                      <i class="fas fa-sign-out-alt"></i> Check-out
                    </button>
                  </div>
                </span>
              </div>
              <div v-else-if="reservation.status == 'checkedout'">
                <button :disabled="disablebutton" v-show="!toggleselect" v-if="reservation.isPaid === 'yes'" @click="
                  moveToCart();
                disablebutton = true;
                " type="button" class="btn btn-primary btn-sm btn-margin rounded">
                  <i class="fas fa-eye"></i> View Summary
                </button>
              </div>
              <button :disabled="disablebutton" v-else-if="reservation.status == 'vacant' &&
                reservation.clientName !== ''
                " @click="clickTestAddItem" type="button" class="btn btn-primary btn-sm btn-margin rounded">
                <i class="fas fa-book"></i> Book Now
              </button>
              <button :disabled="disablebutton" v-if="userdata.role !== 'reservationist' &&
                reservation.status !== 'vacant' &&
                reservation.status !== 'checkedout' &&
                reservation.status !== 'cancelled'
                " v-show="!toggleselect" type="button" class="btn btn-primary btn-sm btn-margin rounded" @click="
    extendBooking();
  disablebutton = true;
  ">
                <i class="fas fa-calendar-plus"></i> Extend (1 day)
              </button>
              <button v-if="userdata.role !== 'reservationist' &&
                reservation.status !== 'vacant' &&
                reservation.status !== 'checkedout' &&
                reservation.status !== 'cancelled' &&
                (!toggleselect || toggleselect2)
                " @click="addRoom()" type="button" class="btn btn-success btn-sm btn-margin rounded">
                <i class="fas fa-square-plus"></i>
                {{ toggleselect2 ? "Save New Room" : "Add New Room" }}
              </button>
              <button v-if="userdata.role !== 'reservationist' &&
                reservation.status !== 'vacant' &&
                reservation.status !== 'checkedout' &&
                reservation.status !== 'cancelled' &&
                !toggleselect2
                " @click="transferRoom()" type="button" class="btn btn-success btn-sm btn-margin rounded">
                <i class="fas fa-exchange-alt"></i>
                {{ toggleselect ? "Save" : "Transfer" }}
              </button>
              <button :disabled="disablebutton" v-if="userdata.role !== 'reservationist' &&
                reservation.status !== 'vacant' &&
                reservation.status !== 'checkedout'
                " type="button" @click="
    voidBook();
  disablebutton = true;
  " class="btn btn-danger btn-sm btn-margin rounded" v-show="!toggleselect">
                <i class="fas fa-trash"></i> Void
              </button>
              <button :disabled="disablebutton" @click="disablebutton = true" type="button"
                class="btn btn-danger btn-sm btn-margin rounded" data-bs-dismiss="modal">
                <i class="fas fa-times"></i> Close
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="container-fluid" style="display: none"></div>
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
import CardBookings2Vue from "../common/CardBookings2.vue";
import ReceptionHotel from "../common/ReceptionHotel.vue";
import "/node_modules/vue-simple-calendar/dist/style.css";
import "/node_modules/vue-simple-calendar/dist/css/default.css";
import "/node_modules/vue-simple-calendar/dist/css/holidays-us.css";
import "/node_modules/vue-final-modal/dist/style.css";
import moment from "moment";
import jsPDF from "jspdf";
import axios from "axios";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "vue-chartjs";
import {
  CalendarView,
  CalendarViewHeader,
  CalendarMath,
} from "vue-simple-calendar"; // published version
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);
//helper functions
function parseDateOrig(dateString) {
  const [day, month, year] = dateString.split("/");
  return `${year}-${month}-${day}`;
}
function parseDateOrig2(dateString) {
  const [month, day, year] = dateString.split("/");
  return `${padTo2Digits(day)}/${padTo2Digits(month)}/${year}`;
}
function parseDate(dateString) {
  const [day, month, year] = dateString.split("/");
  return new Date(`${year}-${month}-${day}`).setHours(0, 0, 0, 0);
}
function parseDate2(dateString) {
  const index = dateString.indexOf("T");
  const result = dateString.substring(0, index);
  const [year, month, day] = result.split("-");
  return new Date(`${year}-${month}-${day}`).setHours(0, 0, 0, 0);
}
function padTo2Digits(num) {
  return num.toString().padStart(2, "0");
}
function formatDate(date = new Date()) {
  return [
    date.getFullYear(),
    padTo2Digits(date.getMonth() + 1),
    padTo2Digits(date.getDate()),
  ].join("-");
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
function formatDate3(date) {
  const options = {
    month: "2-digit",
    day: "2-digit",
    year: "numeric",
    hour: "numeric",
    minute: "numeric",
    second: "numeric",
  };
  return new Intl.DateTimeFormat("en-US", options).format(date);
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
    CardBookings2Vue,
    ReceptionHotel,
  },
  data() {
    return {
      filteredhistlogs: [],
      histlogs: [],
      autocomplete: null,
      filter: {
        bedtype: "",
        roompax: "",
        nearat: "",
        desc: "",
      },
      searchPackage: "",
      notoggle: false,
      isCheckinToggle: false,
      isCheckoutToggle: false,
      simulCtrl: false,
      isExtended: false,
      reportview: 1,
      agentPayment: 0,
      packages: [],
      isReadyToPrintStabs: false,
      currentGuestsInfo: null,
      currentMealStabs: [],
      currentTotalGuest: 0,
      cartItems: [],
      periodStart: "",
      periodEnd: "",
      allowOverPayment: false,
      newbillingbalance: 0,
      dragDayIsSelected: false,
      draggedItem: null,
      draggedRoom: null,
      justDiscounted: false,
      gbookingscount: 0,
      activeAccountFlag: false,
      movetocartFlag: true,
      bookNowFlag: true,
      socket: null,
      test: "",
      dashboardStatus: false,
      bookingComponentStatus: true,
      componentKey: 0,
      activeMainTab: "all",
      roomSelect: "ok",
      toggleselect: false,
      toggleselect2: false,
      bookalltoggle: false,
      isItNew: false,
      disablebutton: false,
      bookingsOptions: [
        {
          label: "Room Name",
          field: "room_name",
          sortable: true,
        },
        {
          label: "Checkin Date",
          field: "checkinDate",
          sortable: true,
        },
        {
          label: "Checkout Date",
          field: "checkoutDate",
          sortable: true,
        },
        {
          label: "Guest",
          field: "name",
          sortable: true,
        },
        {
          label: "Contact Number",
          field: "contactNumber",
          sortable: true,
        },
        {
          label: "Email",
          field: "clientemail",
          sortable: true,
        },
      ],
      bookingsAllOptions: [
        {
          label: "Room Name",
          field: "room_name",
          sortable: true,
        },
        {
          label: "Checkin Date",
          field: "checkinDate",
          sortable: true,
        },
        {
          label: "Checkout Date",
          field: "checkoutDate",
          sortable: true,
        },
        {
          label: "Guest",
          field: "name",
          sortable: true,
        },
        {
          label: "Contact Number",
          field: "contactNumber",
          sortable: true,
        },
        {
          label: "Email",
          field: "clientemail",
          sortable: true,
        },
        {
          label: "Status",
          field: "status",
          sortable: true,
        },
        {
          label: "Total Price (room+addons)",
          field: "totalPrice",
          sortable: true,
          reducible: true,
        },
        {
          label: "Partial Payment",
          field: "partialPayment",
          sortable: true,
          reducible: true,
        },
        {
          label: "Balance",
          field: "balance",
          sortable: true,
          reducible: true,
        },
        {
          label: "Action",
          field: "action",
        },
      ],
      reservationsOptions: [
        {
          label: "",
          field: "toggle",
          sortable: false,
        },
        {
          label: "No.",
          field: "id",
          sortable: true,
        },
        {
          label: "Name",
          field: "name",
          sortable: true,
        },
        {
          label: "Contact",
          field: "contactNumber",
          sortable: true,
        },
        {
          label: "Address",
          field: "clientaddress",
          sortable: true,
        },
        {
          label: "Checkin Date",
          field: "checkinDate",
          sortable: true,
        },
        {
          label: "Checkout Date",
          field: "checkoutDate",
          sortable: true,
        },
        {
          label: "Room",
          field: "room_name",
          sortable: true,
        },
        {
          label: "Cost (Room+addon)",
          field: "totalPrice",
          sortable: true,
          reducible: true,
        },
        {
          label: "Status",
          field: "status",
          sortable: true,
        },
        {
          label: "Payment",
          field: "isPaid",
          sortable: true,
        },
      ],
      transactionsOptions: [
        {
          label: "",
          field: "toggle",
          sortable: false,
        },
        {
          label: "#",
          field: "id",
          sortable: true,
        },
        {
          label: "Name",
          field: "clientname",
          sortable: true,
        },
        {
          label: "Contact",
          field: "clientcontact",
          sortable: true,
        },
        {
          label: "Total Amount",
          field: "totalAmountToPay",
          sortable: true,
          reducible: true,
        },
        {
          label: "Actual Income",
          field: "actualIncomeOfThisDay",
          sortable: true,
          reducible: true,
        },
        {
          label: "Total Cash",
          field: "cashAmountPay",
          sortable: true,
          reducible: true,
        },
        {
          label: "New Balance",
          field: "balance",
          sortable: true,
          reducible: true,
        },
        {
          label: "Latest Status",
          field: "payStatus",
          sortable: true,
        },
        {
          label: "Remarks",
          field: "cashRemarks",
          sortable: true,
        },
        {
          label: "Latest Transaction Date",
          field: "transaction_date",
          sortable: true,
        },
        {
          label: "Action",
          field: "action",
          sortable: false,
          slot: true,
        },
      ],
      transactionhistory: [
        {
          label: "Method",
          field: "paymentMethod",
        },
        {
          label: "Ref. No.",
          field: "nonCashReference",
        },
        {
          label: "Total",
          field: "totalAmountToPay",
        },
        {
          label: "Agent Payment",
          field: "agentPayment",
        },
        {
          label: "Amount Paid",
          field: "cashAmountPay",
        },
        {
          label: "Balance",
          field: "balance",
        },
        {
          label: "Discount Mode",
          field: "discountMode",
        },
        {
          label: "Discount Value",
          field: "discountValue",
        },
        {
          label: "Processed by",
          field: "processedBy",
        },
        {
          label: "Status",
          field: "payStatus",
        },
        {
          label: "Date",
          field: "transaction_date",
        },
      ],
      transactionitem: [
        {
          label: "Name",
          field: "itemName",
        },
        {
          label: "Category",
          field: "itemOption",
        },
        {
          label: "Type",
          field: "itemType",
        },
        {
          label: "Rate",
          field: "itemPriceRate",
        },
        {
          label: "Qty",
          field: "purchaseQty",
        },
        {
          label: "Total",
          field: "totalCost",
        },
        {
          label: "Date",
          field: "dateCreated",
        },
      ],
      walkinview: false,
      hoveredDay: null,
      dayreserve: new Date(),
      showTable: {},
      toggleAll: true,
      resdateFilter: "any",
      resfromDate: null,
      restoDate: null,
      respaymentStatusFilter: "",
      resstatusFilter: "",
      dateFilter: "any",
      fromDate: null,
      toDate: null,
      paymentMethodFilter: "",
      statusFilter: "",
      convDate: "",
      optionsArray1: [
        {
          name: "Show Account",
          slug: "show",
        },
        {
          type: "divider",
        },
        {
          name: "Edit",
          slug: "edit",
        },
        {
          name: "<em>Delete</em>",
          slug: "delete",
        },
      ],
      itemIndex: -1,
      walkinreservation: {
        clientName: "",
        clientEmail: "",
        clientPhone: "",
        clientAddress: "",
        clientNationality: "Filipino",
        clientType: "",
      },
      reservation: {
        clientName: "",
        clientEmail: "",
        clientPhone: "",
        clientAddress: "",
        clientNationality: "",
        clientType: "",
        checkinDate: "",
        checkoutDate: "",
        roomName: "",
        roomPrice: "",
        roomType: "",
        remarks: "",
        status: "vacant",
        isPaid: "no",
        numguests: "",
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
      selectionStart: new Date(),
      selectionEnd: new Date(),
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
      walkinID: "",
      calendarItems: [],
      linedata: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "Cancelled",
            backgroundColor: "gray",
            data: [50, 29, 1, 4, 37, 80, 40],
          },
          {
            label: "Reserved",
            backgroundColor: "red",
            data: [40, 39, 10, 40, 39, 80, 40],
          },
          {
            label: "Check-in",
            backgroundColor: "green",
            data: [40, 39, 10, 40, 39, 80, 40],
          },
          {
            label: "Check-out",
            backgroundColor: "yellow",
            data: [40, 39, 10, 40, 39, 80, 40],
          },
        ],
      },
      lineoptions: {
        responsive: true,
        maintainAspectRatio: false,
      },
      paymentMethod: "cash",
      cashAmount: 0,
      nonCashPayPlatform: "",
      nonCashReference: "",
      discountMode: "percentage",
      discountValue: 0,
      taxValue: 0,
      partialPayment: 0,
      cashOR: "",
      cashOS: "",
      cashHistory: [],
      cashRemarks: "",
      activeTab: "all",
      clientName: "",
      clientEmail: "",
      clientPhone: "",
      clientAddress: "",
      clientNationality: "",
      clientType: "",
      transactions: [],
      roomcategories: [],
      agents: [],
      rooms: [],
      howMany: [],
      guestdetails: {
        names: [],
        genders: [],
        types: [],
        addresses: [],
        contactnos: [],
        emails: [],
      },
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
        bookingID: "",
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
      cashDenominations: [
        {
          label: "+1.00",
          value: 1,
        },
        {
          label: "+5.00",
          value: 5,
        },
        {
          label: "+10.00",
          value: 10,
        },
        {
          label: "+20.00",
          value: 20,
        },
        {
          label: "+50.00",
          value: 50,
        },
        {
          label: "+100.00",
          value: 100,
        },
        {
          label: "+500.00",
          value: 500,
        },
        {
          label: "+1000.00",
          value: 1000,
        },
      ],
    };
  },
  async created() {
    if (this.EVALUATION_STAGE) {
      const countdownMessage = `This app is for evaluation and not the full version. Please wait for <span id="countdowntimer">${this.EVALUATION_TIME}</span> seconds to load.`;
      let countdownResult;
      let timeoutExpired = false; // New variable for tracking timeout
      countdownResult = await this.$swal.fire({
        title: "Please wait",
        html: countdownMessage,
        icon: "info",
        showCancelButton: false,
        showConfirmButton: false,
        allowOutsideClick: false,
        didOpen: () => {
          const countdownEl = document.querySelector("#countdowntimer");
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
        },
      });
      if (!countdownResult.isConfirmed && timeoutExpired) {
        countdownResult.isConfirmed = true; // Set isConfirmed to true if timeout expired
      }
      if (!countdownResult.isConfirmed) {
        return;
      }
    }
    this.loadAlldata();
  },
  watch: {
    "reservation.checkinDate": function (newPrice, oldPrice) {
      if (!this.toggleCheckin) {
        this.reservation.roomName = "";
      }
    },
    "reservation.checkoutDate": function (newPrice, oldPrice) {
      if (!this.toggleCheckout) {
        this.reservation.roomName = "";
      }
    },
  },
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
        height1: parseFloat(window.innerHeight) - 300 + "px",
        height2: parseFloat(window.innerHeight) - 230 + "px",
        height3: parseFloat(window.innerHeight) - 240 + "px",
        height4: parseFloat(window.innerHeight) - 150 + "px",
      };
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
      return this.cart.filter((item) => item.category === "main");
    },
    filteredInclusionCart() {
      return this.cart
        .map((o) => {
          return {
            ...o,
          };
        })
        .filter((item) => item.category === "inclusion");
    },
    filteredReservationsHistory() {
      let filtered = this.bookings
        .filter((reservation) => {
          // Filter by date range
          if (
            this.resdateFilter === "range" &&
            this.resfromDate &&
            this.restoDate
          ) {
            const checkinDate = parseDate(reservation.checkinDate);
            const checkoutDate = parseDate(reservation.checkoutDate);
            const fromDate = parseDate(this.resfromDate);
            const toDate = parseDate(this.restoDate);
            return fromDate <= checkoutDate && toDate >= checkinDate;
          }
          return true;
        })
        .filter((reservation) => {
          // Filter by payment method
          if (this.respaymentStatusFilter) {
            return reservation.isPaid === this.respaymentStatusFilter;
          }
          return true;
        })
        .filter((reservation) => {
          // Filter by status
          if (this.resstatusFilter) {
            return reservation.status === this.resstatusFilter;
          }
          return true;
        });
      return filtered
        .map((item) => {
          const searchCode = Object.values(item).join("~");
          return {
            ...item,
            searchCode,
          };
        })
        .filter((item) =>
          item.searchCode
            .toString()
            .toLowerCase()
            .includes(this.searchTerm2.toLowerCase())
        );
    },
    filteredTransactionsTotal() {
      return this.filteredTransactions.reduce(
        (acc, item) => acc + parseFloat(item.cashAmountPay),
        0
      );
    },
    filteredTransactionsBalance() {
      return this.filteredTransactions.reduce(
        (acc, item) => acc + parseFloat(item.balance),
        0
      );
    },
    filteredTransactions() {
      let filtered = this.transactions;
      // Filter by date
      if (this.dateFilter === "range" && this.fromDate && this.toDate) {
        filtered = filtered.filter((transaction) => {
          return (
            parseDate2(transaction.transaction_date) >=
            parseDate(this.fromDate) &&
            parseDate2(transaction.transaction_date) <= parseDate(this.toDate)
          );
        });
      }
      // Filter by payment method
      if (this.paymentMethodFilter) {
        filtered = filtered.filter((transaction) => {
          return transaction.paymentMethod === this.paymentMethodFilter;
        });
      }
      // Filter by status
      if (this.statusFilter) {
        filtered = filtered.filter((transaction) => {
          return transaction.payStatus === this.statusFilter;
        });
      }
      return filtered
        .map((item) => {
          const searchCode =
            Object.values(item).join("~") +
            (item.items ? JSON.stringify(item.items) : []) +
            (item.props ? JSON.stringify(item.props) : []);
          return {
            ...item,
            searchCode,
          };
        })
        .filter((item) =>
          item.searchCode
            .toString()
            .toLowerCase()
            .includes(this.searchTerm.toLowerCase())
        );
    },
    roomsjoinbookingsfordeparting() {
      let filtered =
        this.activeMainTab === "all"
          ? this.rooms
          : this.rooms.filter(
            (item) => item.type === this.activeMainTab.toString()
          );
      return filtered.map((room) => {
        const booking = this.bookings
          .filter((item) => item.status !== "checkedout")
          .filter((item) => item.status !== "cancelled")
          .filter((item) => {
            const isCheckedin = item.status === "checkedin";
            const today = new Date().setHours(0, 0, 0, 0);
            let checkoutDate = new Date(parseDate(item.checkoutDate));
            checkoutDate.setDate(checkoutDate.getDate() + 1);
            checkoutDate = checkoutDate.setHours(0, 0, 0, 0);
            const isStaying = checkoutDate === today;
            return isCheckedin && isStaying;
          })
          .find((booking) => booking.room_name === room.name);
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
    roomsjoinbookings() {
      let filtered =
        this.activeMainTab === "all"
          ? this.rooms
          : this.rooms.filter(
            (item) => item.type === this.activeMainTab.toString()
          );
      return filtered.map((room) => {
        const booking = this.bookings
          .filter((item) => item.status !== "checkedout")
          .filter(
            (item) =>
              item.status !== "cancelled" &&
              parseDate(new Date().toLocaleDateString("en-GB")) >=
              parseDate(item.checkinDate) &&
              parseDate(item.checkoutDate) >=
              parseDate(new Date().toLocaleDateString("en-GB"))
          )
          .find((booking) => booking.room_name === room.name);
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
      const isCancelled = this.activeTab === "cancelled";
      const isReserved = this.activeTab === "reserved";
      const isOccupied = this.activeTab === "occupied";
      const isCheckedout = this.activeTab === "checkedout";
      const selectedDate = parseDate(this.convDate);
      const startDate = this.selectionStart.setHours(0, 0, 0, 0);
      const endDate = this.selectionEnd.setHours(0, 0, 0, 0);
      return this.bookings
        .filter((booking) => {
          const bookingCheckinDate = parseDate(booking.checkinDate);
          const bookingCheckoutDate = parseDate(booking.checkoutDate);
          const dateInRange =
            endDate >= bookingCheckinDate && startDate <= bookingCheckoutDate;
          const isReservedMatch = !isReserved || booking.status === "reserved";
          const isOccupiedMatch = !isOccupied || booking.status === "checkedin";
          const isCancelledMatch =
            !isCancelled || booking.status === "cancelled";
          const isCheckedoutMatch =
            !isCheckedout || booking.status === "checkedout";
          return (
            dateInRange &&
            isCancelledMatch &&
            isReservedMatch &&
            isOccupiedMatch &&
            isCheckedoutMatch
          );
        })
        .map((o) => {
          const balance =
            parseFloat(o.totalPrice) - parseFloat(o.partialPayment);
          return {
            ...o,
            balance,
          };
        });
    },
    filteredupdatedRooms() {
      return this.updatedRooms
        .filter((room) => {
          if (this.filter.roompax) {
            return room.pax === parseFloat(this.filter.roompax);
          }
          return true;
        })
        .filter((room) => {
          if (this.filter.bedtype) {
            const category = room.type;
            const item = this.roomcategories.filter(
              (o) => o.name === category
            )[0];
            return item.bedtypes === this.filter.bedtype;
          }
          return true;
        })
        .filter((room) => {
          if (this.filter.nearat) {
            const category = room.type;
            const item = this.roomcategories.filter(
              (o) => o.name === category
            )[0];
            return item.nearat === this.filter.nearat;
          }
          return true;
        })
        .filter((room) => {
          if (this.filter.desc) {
            const category = room.type;
            const item = this.roomcategories.filter(
              (o) => o.name === category
            )[0];
            if (item.desc !== null) {
              return item.desc
                .toLowerCase()
                .includes(this.filter.desc.toLowerCase());
            } else {
              return false;
            }
          }
          return true;
        });
    },
    updatedRooms() {
      return this.rooms.filter((room) => {
        // Check if there are any bookings for this room that overlap with the specified date range
        const overlappingBookings = this.bookings.filter((booking) => {
          // Check if the booking is not cancelled and not checked out
          if (
            booking.status === "cancelled" ||
            booking.status === "checkedout"
          ) {
            return false;
          }

          // Check if the booking's room_name matches the current room and the date range overlaps with the reservation
          const checkInDate = parseDate(booking.checkinDate);
          let checkOutDate = parseDate(booking.checkoutDate);
          const startDate = parseDate(this.reservation.checkinDate);
          const endDate = parseDate(this.reservation.checkoutDate);
          const numdays = checkOutDate - checkInDate;
          //   if (numdays > 0) {
          //     checkOutDate.setDate(checkOutDate.getDate() - 1);
          //     checkOutDate = checkOutDate.setHours(0, 0, 0, 0);
          //   }
          const isOverlap =
            booking.room_name === room.name &&
            startDate <= checkOutDate &&
            endDate >= checkInDate;

          return isOverlap;
        });

        // Check if there exists a booking with the same room_name in yesterday that has not been checked out
        // const yesterday = new Date();
        // yesterday.setDate(yesterday.getDate() - 1);
        // const yesterdayBooking = this.bookings.find((prevBooking) => {
        //   const prevCheckOutDate = parseDate(prevBooking.checkoutDate);
        //   return (
        //     prevBooking.room_name === room.name &&
        //     new Date(prevCheckOutDate).toDateString() ===
        //       new Date(yesterday).toDateString() &&
        //     prevBooking.status === "checkedin"
        //   );
        // });

        // Return true if there are no overlapping bookings and no booking in yesterday that has not been checked out
        // return overlappingBookings.length === 0 && !yesterdayBooking;
        return overlappingBookings.length === 0;
      });
    },
    userLocale() {
      return CalendarMath.getDefaultBrowserLocale;
    },
    dayNames() {
      return CalendarMath.getFormattedWeekdayNames(this.userLocale, "long", 0);
    },
    themeClasses() {
      return {
        "theme-default": this.useDefaultTheme,
        "holiday-us-traditional": this.useHolidayTheme,
        "holiday-us-official": this.useHolidayTheme,
      };
    },
    myDateClasses() {
      // This was added to demonstrate the dateClasses prop. Note in particular that the
      // keys of the object are `yyyy-mm-dd` ISO date strings (not dates), and the values
      // for those keys are strings or string arrays. Keep in mind that your CSS to style these
      // may need to be fairly specific to make it override your theme's styles. See the
      // CSS at the bottom of this component to see how these are styled.
      const o = {};
      const theFirst = this.thisMonth(1);
      const ides = [2, 4, 6, 9].includes(theFirst.getMonth()) ? 15 : 13;
      const idesDate = this.thisMonth(ides);
      o[CalendarMath.isoYearMonthDay(idesDate)] = "ides";
      o[CalendarMath.isoYearMonthDay(this.thisMonth(21))] = [
        "do-you-remember",
        "the-21st",
      ];
      return o;
    },
    currentDate() {
      const options = {
        month: "2-digit",
        day: "2-digit",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: true,
      };
      return new Date().toLocaleString("en-US", options);
    },
    subroom() {
      const mainRoomItems = this.cart.filter(
        (item) => item.category === "main" && item.itemOption === "room"
      );
      const originalPrice = mainRoomItems.reduce(
        (acc, item) => acc + parseFloat(item.totalCartPrice),
        0
      );
      if (this.discount === 0) {
        return { original: originalPrice, discounted: "" };
      }
      const discountedPrice = originalPrice - this.discount;
      const discountAmount =
        this.discountMode === "percentage"
          ? `${this.discountValue}%`
          : `₱${this.discountValue}`;
      const formattedOriginalPrice = `<del class="text-danger">${originalPrice}</del>`;
      const formattedDiscountedPrice = `<sup class="text-danger font-weight-bold">${discountAmount} off</sup> <span class="text-success font-weight-bold">${discountedPrice}</span>`;
      return {
        original: formattedOriginalPrice,
        discounted: formattedDiscountedPrice,
        discountMode: this.discountMode,
        discountValue: this.discountValue,
      };
    },
    subaddons() {
      return this.cart
        .filter(
          (item) => item.category === "main" && item.itemOption === "addons"
        )
        .reduce((acc, item) => acc + parseFloat(item.totalCartPrice), 0);
    },
    subtotal() {
      return (
        this.cart
          .filter((item) => item.category === "main")
          .reduce((acc, item) => acc + parseFloat(item.totalCartPrice), 0) -
        this.discount
      );
    },
    sumInclusion() {
      return this.cart
        .filter((item) => item.category === "inclusion")
        .reduce((acc, item) => acc + parseFloat(item.totalCartPrice), 0);
    },
    discount() {
      if (this.discountMode === "percentage") {
        return (
          ((this.cart
            .filter((item) => item.category === "main")
            .reduce((acc, item) => acc + parseFloat(item.totalCartPrice), 0) -
            this.subaddons) *
            this.discountValue) /
          100
        );
      } else {
        return this.discountValue;
      }
    },
    total() {
      return this.subtotal - this.partialPayment;
    },
    change() {
      return this.cashAmount > this.total && this.total > 0
        ? this.cashAmount - this.total
        : 0;
    },
    isThereLeisures() {
      return this.cart.filter((item) => item.type === "LEISURES").length > 0;
    },
    countInclusion() {
      return this.cart.filter((item) => item.category === "inclusion").length;
    },
    numItemCart() {
      return this.cart.filter((item) => item.category === "main").length;
    },
    filteredCart() {
      return this.cart
        .map((o) => {
          const searchCode = o.name;
          return {
            ...o,
            searchCode,
          };
        })
        .filter((item) => item.category === "main");
    },
    bookings() {
      return this.origbookings
        .map((book) => {
          const { name, room_name, status, isPaid } = book;
          const paymentStatus =
            isPaid === "yes"
              ? "fully-paid"
              : isPaid === "no"
                ? "not paid"
                : "partial";
          const searchCode = `${name}~${room_name}~${status}~${paymentStatus}`;
          return {
            ...book,
            searchCode,
          };
        })
        .filter((book) =>
          book.searchCode
            .toLowerCase()
            .includes(this.booksearchtext.toLowerCase())
        );
    },
    roomStatus() {
      return this.rooms
        .map((room) => {
          const isVacant = this.vacantRoom(room.name);
          const searchCode = room.name + "~" + room.type + "~" + room.price;
          return {
            ...room,
            isVacant,
            searchCode,
          };
        })
        .filter((rooms) =>
          rooms.searchCode
            .toString()
            .toLowerCase()
            .includes(this.searchText2.toLowerCase())
        );
    },
    filteredReservations() {
      return this.reservations
        .map((book) => {
          const searchCode =
            book.name +
            "~" +
            book.checkinDate +
            "~" +
            book.checkoutDate +
            "~" +
            book.room_name;
          return {
            ...book,
            searchCode,
          };
        })
        .filter((reservation) =>
          reservation.searchCode
            .toString()
            .toLowerCase()
            .includes(this.searchText1.toLowerCase())
        );
    },
    filteredItems() {
      return this.items
        .map((item) => {
          const searchCode = item.item + "~" + item.type;
          return {
            ...item,
            searchCode,
          };
        })
        .filter((item) =>
          item.searchCode
            .toString()
            .toLowerCase()
            .includes(this.searchText3.toLowerCase())
        );
    },
  },
  methods: {
    insertNewBooking() {
      const today = new Date();
      this.toggleselect = false;
      this.toggleselect2 = false;
      this.roomSelect = "ok";
      this.bookalltoggle = false;
      this.reservation.clientName = "";
      this.reservation.clientEmail = "";
      this.reservation.clientAddress = "";
      // this.$refs.address1Field.value = "";
      this.isCheckinToggle = false;
      this.isCheckoutToggle = false;
      this.simulCtrl = false;
      this.reservation.clientNationality = "Filipino";
      this.reservation.clientType = "in-house";
      this.reservation.roomName = "";
      this.reservation.remarks = "";
      this.filteredhistlogs = [];
      this.reservation.clientPhone = "";
      this.reservation.status = "vacant";
      this.reservation.checkinDate = formatDate(today);
      this.reservation.checkoutDate = formatDate(today);
      this.newtoggle = true;
      this.isCheckinToggle = true;
      this.isCheckoutToggle = true;
      this.toggleItemModal();
    },
    async toggleCheckin() {
      this.isCheckinToggle = !this.isCheckinToggle;
      if (this.isCheckinToggle) {
        this.reservation.checkinDate = formatDate(
          new Date(parseDateOrig(this.reservation.checkinDate))
        );
      } else {
        const newstartdate = new Date(
          parseDateOrig(this.reservation.checkinDate)
        );
        const item = {
          originalItem: {
            startDate: parseDateOrig(this.bookings[this.itemIndex].checkinDate),
            endDate: parseDateOrig(this.bookings[this.itemIndex].checkoutDate),
          },
          id: this.bookings[this.itemIndex].itemID,
          startDate: new Date(
            parseDateOrig(this.bookings[this.itemIndex].checkinDate)
          ),
          endDate: new Date(
            parseDateOrig(this.bookings[this.itemIndex].checkoutDate)
          ),
        };
        const dateselection = newstartdate;

        let filteredBookings = this.bookings.filter(
          (booking) =>
            (booking.status === "reserved" || booking.status === "checkedin") &&
            booking.itemID !== this.bookings[this.itemIndex].itemID &&
            booking.room_name === this.bookings[this.itemIndex].room_name &&
            new Date(parseDateOrig(booking.checkinDate)).setHours(0, 0, 0, 0) <=
            item.endDate.setHours(0, 0, 0, 0) &&
            new Date(parseDateOrig(booking.checkoutDate)).setHours(
              0,
              0,
              0,
              0
            ) >= newstartdate.setHours(0, 0, 0, 0)
        );

        if (
          newstartdate.setHours(0, 0, 0, 0) > item.endDate.setHours(0, 0, 0, 0)
        ) {
          this.isCheckinToggle = !this.isCheckinToggle;
          return false;
        }

        if (filteredBookings.length === 0) {
          this.bookings[this.itemIndex].checkinDate = formatDate2(
            this.reservation.checkinDate
          );
          this.populateCalendarItems();

          const numdays =
            (parseDate(this.bookings[this.itemIndex].checkoutDate) -
              parseDate(this.reservation.checkinDate)) /
            (1000 * 60 * 60 * 24);

          const response = await axios.post(
            this.API_URL + "transaction/item/filter/",
            {
              columnName: "bookingID",
              columnKey: this.bookings[this.itemIndex].itemID,
            }
          );

          for (const item of response.data.filter(
            (o) =>
              o.bookingID === this.bookings[this.itemIndex].itemID &&
              (o.itemOption === "room" ||
                o.itemType.toLowerCase() === "entrance")
          )) {
            const data = {
              bookingID: item.bookingID,
              itemName: item.itemName,
              itemType: item.itemType,
              itemPriceRate: item.itemPriceRate,
              purchaseQty:
                item.itemOption === "room" ? numdays + 1 : item.purchaseQty,
              totalCost:
                item.itemOption === "room"
                  ? (numdays + 1) * parseFloat(item.itemPriceRate.split("/")[0])
                  : (numdays + 1) *
                  (item.totalguest - item.totalpax) *
                  parseFloat(item.itemPriceRate.split("/")[0]),
              category: item.category,
              itemOption: item.itemOption,
              dateCreated: new Date(), // Set the dateCreated field to the current date and time
              numdays: numdays + 1,
              totalguest: item.totalguest,
              totalpax: item.totalpax,
              currentroom: item.currentroom,
            };
            await axios.put(
              this.API_URL + `transaction/item/${item.id}/`,
              data
            );
          }

          this.updateBookings(this.bookings[this.itemIndex].id);

          const originalStart = item.startDate.toLocaleDateString("en-GB");
          const originalEnd = item.endDate.toLocaleDateString("en-GB");

          let newcheckoutdate = new Date(
            parseDate(this.bookings[this.itemIndex].checkoutDate)
          );
          newcheckoutdate.setDate(newcheckoutdate.getDate() + 1);
          newcheckoutdate = formatDate2(newcheckoutdate);

          let newcheckoutdate2 = new Date(parseDate(originalEnd));
          newcheckoutdate2.setDate(newcheckoutdate2.getDate() + 1);
          newcheckoutdate2 = formatDate2(newcheckoutdate2);

          this.actionRecorder(
            `record?type=changedate&bookingID=${this.bookings[this.itemIndex].itemID
            }&groupkey=${this.bookings[this.itemIndex].groupkey}&remarks=${originalStart === this.bookings[this.itemIndex].checkinDate
              ? ""
              : `Checkin date: from ${originalStart} to ${this.bookings[this.itemIndex].checkinDate
              }; `
            }${originalEnd === this.bookings[this.itemIndex].checkoutDate
              ? ""
              : `Checkout date: from ${newcheckoutdate2} to ${newcheckoutdate}`
            }`
          );

          this.taskRecord(
            `action:/adjust date reservation/client:/${this.bookings[this.itemIndex].name
            }`
          );
        } else {
          this.$swal.fire({
            icon: "error",
            title: "Cannot Adjust Reservation",
            text: "Dates conflict with an existing room reservation.",
            confirmButtonText: "OK",
          });
          return false;
        }

        // this.onDrop(item, dateselection);
        this.toggleItemModal();
        this.isCheckinToggle = !this.isCheckinToggle;
      }
    },
    async toggleCheckout() {
      this.isCheckoutToggle = !this.isCheckoutToggle;
      this.simulCtrl = true;
      if (this.isCheckoutToggle) {
        this.reservation.checkoutDate = formatDate(
          new Date(parseDateOrig(this.reservation.checkoutDate))
        );
      } else {
        const newenddate = new Date(
          parseDateOrig(this.reservation.checkoutDate)
        );
        const item = {
          originalItem: {
            startDate: parseDateOrig(this.bookings[this.itemIndex].checkinDate),
            endDate: parseDateOrig(this.bookings[this.itemIndex].checkoutDate),
          },
          id: this.bookings[this.itemIndex].itemID,
          startDate: new Date(
            parseDateOrig(this.bookings[this.itemIndex].checkinDate)
          ),
          endDate: new Date(
            parseDateOrig(this.bookings[this.itemIndex].checkoutDate)
          ),
        };
        const dateselection = newenddate;

        let filteredBookings = this.bookings.filter(
          (booking) =>
            (booking.status === "reserved" || booking.status === "checkedin") &&
            booking.itemID !== this.bookings[this.itemIndex].itemID &&
            booking.room_name === this.bookings[this.itemIndex].room_name &&
            new Date(parseDateOrig(booking.checkinDate)).setHours(0, 0, 0, 0) <=
            newenddate.setHours(0, 0, 0, 0) &&
            new Date(parseDateOrig(booking.checkoutDate)).setHours(
              0,
              0,
              0,
              0
            ) >= item.startDate.setHours(0, 0, 0, 0)
        );

        if (
          newenddate.setHours(0, 0, 0, 0) < item.startDate.setHours(0, 0, 0, 0)
        ) {
          this.isCheckoutToggle = !this.isCheckoutToggle;
          this.simulCtrl = false;
          return false;
        }

        if (filteredBookings.length === 0) {
          this.bookings[this.itemIndex].checkoutDate = formatDate2(
            this.reservation.checkoutDate
          );
          this.populateCalendarItems();

          const numdays =
            (parseDate(this.reservation.checkoutDate) -
              parseDate(this.bookings[this.itemIndex].checkinDate)) /
            (1000 * 60 * 60 * 24);

          const response = await axios.post(
            this.API_URL + "transaction/item/filter/",
            {
              columnName: "bookingID",
              columnKey: this.bookings[this.itemIndex].itemID,
            }
          );

          for (const item of response.data.filter(
            (o) =>
              o.bookingID === this.bookings[this.itemIndex].itemID &&
              (o.itemOption === "room" ||
                o.itemType.toLowerCase() === "entrance")
          )) {
            const data = {
              bookingID: item.bookingID,
              itemName: item.itemName,
              itemType: item.itemType,
              itemPriceRate: item.itemPriceRate,
              purchaseQty:
                item.itemOption === "room" ? numdays + 1 : item.purchaseQty,
              totalCost:
                item.itemOption === "room"
                  ? (numdays + 1) * parseFloat(item.itemPriceRate.split("/")[0])
                  : (numdays + 1) *
                  (item.totalguest - item.totalpax) *
                  parseFloat(item.itemPriceRate.split("/")[0]),
              category: item.category,
              itemOption: item.itemOption,
              dateCreated: new Date(), // Set the dateCreated field to the current date and time
              numdays: numdays + 1,
              totalguest: item.totalguest,
              totalpax: item.totalpax,
              currentroom: item.currentroom,
            };
            await axios.put(
              this.API_URL + `transaction/item/${item.id}/`,
              data
            );
          }

          this.updateBookings(this.bookings[this.itemIndex].id);

          const originalStart = item.startDate.toLocaleDateString("en-GB");
          const originalEnd = item.endDate.toLocaleDateString("en-GB");

          let newcheckoutdate = new Date(
            parseDate(this.bookings[this.itemIndex].checkoutDate)
          );
          newcheckoutdate.setDate(newcheckoutdate.getDate() + 1);
          newcheckoutdate = formatDate2(newcheckoutdate);

          let newcheckoutdate2 = new Date(parseDate(originalEnd));
          newcheckoutdate2.setDate(newcheckoutdate2.getDate() + 1);
          newcheckoutdate2 = formatDate2(newcheckoutdate2);

          this.actionRecorder(
            `record?type=changedate&bookingID=${this.bookings[this.itemIndex].itemID
            }&groupkey=${this.bookings[this.itemIndex].groupkey}&remarks=${originalStart === this.bookings[this.itemIndex].checkinDate
              ? ""
              : `Checkin date: from ${originalStart} to ${this.bookings[this.itemIndex].checkinDate
              }; `
            }${originalEnd === this.bookings[this.itemIndex].checkoutDate
              ? ""
              : `Checkout date: from ${newcheckoutdate2} to ${newcheckoutdate}`
            }`
          );

          this.taskRecord(
            `action:/adjust date reservation/client:/${this.bookings[this.itemIndex].name
            }`
          );
        } else {
          this.$swal.fire({
            icon: "error",
            title: "Cannot Adjust Reservation",
            text: "Dates conflict with an existing room reservation.",
            confirmButtonText: "OK",
          });
          return false;
        }

        // this.onDrop(item, dateselection);
        this.toggleItemModal();
        this.isCheckoutToggle = !this.isCheckoutToggle;
        this.simulCtrl = false;
      }
    },
    initAutocomplete() {
      const address1Field = this.$refs.address1Field;

      // Create the autocomplete object, restricting the search predictions to
      // addresses in the Philippines (PH).
      this.autocomplete = new google.maps.places.Autocomplete(address1Field, {
        componentRestrictions: { country: ["ph"] },
        fields: ["address_components", "geometry"],
        types: ["geocode"],
      });

      address1Field.focus();

      this.autocomplete.addListener("place_changed", () => {
        this.reservation.clientAddress = this.$refs.address1Field.value;
      });
    },
    extendView() {
      this.isExtended = !this.isExtended;
      if (!this.isExtended) {
        $(".printform").removeClass("col-md-9").addClass("col-md-6");
        $(".paymentmodal").show(1000);
      } else {
        $(".printform").removeClass("col-md-6").addClass("col-md-9");
        $(".paymentmodal").hide(1000);
      }
    },
    async generateAllStabs() {
      let reservations = this.roomsjoinbookings;
      this.currentMealStabs = [];
      for (const item of reservations) {
        if ("itemID" in item) {
          const itemCheckinDate = item.checkinDate;
          await axios
            .post(`${this.API_URL}transaction/item/filter/`, [
              { columnName: "bookingID", columnKey: item.itemID },
              { columnName: "itemName", columnKey: "Room Guest" },
            ])
            .then(async (response) => {
              try {
                for (const o of response.data) {
                  const numdays = o.numdays;
                  const total = o.purchaseQty;
                  const guestarr = JSON.parse(o.guestinfo);
                  for (let i = 0; i < total; i++) {
                    for (let j = 0; j < numdays; j++) {
                      let checkinDate = new Date(parseDate(itemCheckinDate));
                      checkinDate.setDate(checkinDate.getDate() + 1 + j);
                      this.currentMealStabs.push({
                        person: guestarr[i].name,
                        validdate: checkinDate.toDateString(),
                        ticketno: i + "" + j + "" + guestarr[i].id,
                      });
                    }
                  }
                }
              } catch (error) { }
            });
        }
      }
      // console.log(this.currentMealStabs);
      setTimeout(() => {
        this.printSection("printstab", 425, 1300, false, 1);
      }, 1000);
    },
    howmanyPax(name) {
      return this.rooms.filter((o) => o.name === name)[0].pax;
    },
    passwordProtectTab(n) {
      document.getElementById(`rview${n}`).style.display = "none";
      this.$swal
        .fire({
          title: "Authorization Required",
          input: "text",
          showCancelButton: true,
          allowOutsideClick: false,
          inputAttributes: {
            minlength: 6, // Minimum length of 3 characters
            maxlength: 24, // Maximum length of 24 characters
            autocomplete: "off",
            style: "text-security:disc; -webkit-text-security:disc;",
          },
          confirmButtonText: "Submit",
          cancelButtonText: "Cancel",
          inputPlaceholder: "Enter authorization code",
        })
        .then((result) => {
          if (result.isConfirmed) {
            const authorizationCode = result.value;
            // Validate the authorization code and perform necessary actions
            if (
              authorizationCode.toLowerCase() ===
              this.AUTHORIZATION_KEY2.toLowerCase()
            ) {
              // Code is correct, proceed with the desired action
              document.getElementById(`rview${n}`).style.display = "block";
            } else {
              // Code is incorrect, show an error message or take appropriate action
              this.$swal
                .fire({
                  icon: "error",
                  title: "Incorrect Passcode",
                  text: "The entered passcode is incorrect. Please try again.",
                  allowOutsideClick: false,
                })
                .then((result) => {
                  this.reportview = 1;
                  $("#linkview1").tab("show");
                });
            }
          } else {
            this.reportview = 1;
            $("#linkview1").tab("show");
          }
        });
    },
    loadPackageItems(item) {
      const packItems = this.items.filter((o) => o.package_name == item.id);
      for (const o of packItems) {
        this.howMany[0] = 1;
        this.addToCart(o, 0);
      }
      this.howMany[0] = null;
    },
    async addNewGuest(item) {
      let guestinfos = [];
      this.currentMealStabs = [];
      this.guestdetails.names = [];
      this.guestdetails.genders = [];
      this.guestdetails.types = [];
      this.guestdetails.addresses = [];
      this.guestdetails.contactnos = [];
      this.guestdetails.emails = [];
      this.isReadyToPrintStabs = false;

      await axios
        .get(`${this.API_URL}transaction/item/${item.id}/`)
        .then((response) => {
          this.currentGuestsInfo = response.data;
          this.currentTotalGuest = response.data.purchaseQty;

          if (
            this.currentGuestsInfo.guestinfo !== null &&
            this.currentGuestsInfo.guestinfo !== ""
          ) {
            guestinfos = JSON.parse(this.currentGuestsInfo.guestinfo);
            this.isReadyToPrintStabs = guestinfos.length > 0;
            for (let i = 0; i < this.currentTotalGuest; i++) {
              this.guestdetails.names.push(guestinfos[i].name);
              this.guestdetails.genders.push(guestinfos[i].gender);
              this.guestdetails.types.push(guestinfos[i].type);
              this.guestdetails.addresses.push(guestinfos[i].address);
              this.guestdetails.contactnos.push(guestinfos[i].contactno);
              this.guestdetails.emails.push(guestinfos[i].email);
            }
          }

          this.toggleGuestListModal();
        });
    },
    generateRandomNString() {
      const length = 6;
      let result = "";
      const characters = "0123456789";

      for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        result += characters.charAt(randomIndex);
      }

      return result;
    },
    async printMealStab() {
      const numdays = this.currentGuestsInfo.numdays;
      const total = this.currentGuestsInfo.purchaseQty;
      const guestarr = JSON.parse(this.currentGuestsInfo.guestinfo);
      this.currentMealStabs = [];
      for (let i = 0; i < total; i++) {
        for (let j = 0; j < numdays; j++) {
          let checkinDate = new Date(parseDate(this.reservation.checkinDate));
          checkinDate.setDate(checkinDate.getDate() + 1 + j);
          this.currentMealStabs.push({
            person: guestarr[i].name,
            validdate: checkinDate.toDateString(),
            ticketno: i + "" + j + "" + guestarr[i].id,
          });
        }
      }

      setTimeout(() => {
        this.printSection("printstab", 425, 1300, false, 1);
      }, 1000);
      this.toggleGuestListModal();
    },
    async postGuest(n) {
      const guestinfo = [];
      const existingArr = JSON.parse(this.currentGuestsInfo.guestinfo);

      for (let i = 0; i < this.currentTotalGuest; i++) {
        guestinfo.push({
          name: this.guestdetails.names[i],
          gender: this.guestdetails.genders[i],
          type: this.guestdetails.types[i],
          address: this.guestdetails.addresses[i],
          contactno: this.guestdetails.contactnos[i],
          email: this.guestdetails.emails[i],
          id:
            i +
            "-" +
            this.currentGuestsInfo.id +
            "-" +
            this.generateRandomNString(),
        });
      }

      const data = {
        bookingID: this.currentGuestsInfo.bookingID,
        itemName: this.currentGuestsInfo.itemName,
        itemType: this.currentGuestsInfo.itemType,
        itemPriceRate: this.currentGuestsInfo.itemPriceRate,
        purchaseQty: this.currentGuestsInfo.purchaseQty,
        totalCost: this.currentGuestsInfo.totalCost,
        category: this.currentGuestsInfo.category,
        itemOption: this.currentGuestsInfo.itemOption,
        groupkey: this.currentGuestsInfo.groupkey,
        totalguest: this.currentGuestsInfo.totalguest,
        totalpax: this.currentGuestsInfo.totalpax,
        currentroom: this.currentGuestsInfo.currentroom,
        numdays: this.currentGuestsInfo.numdays,
        guestinfo: JSON.stringify(guestinfo),
      };
      await axios
        .put(
          `${this.API_URL}transaction/item/${this.currentGuestsInfo.id}/`,
          data
        )
        .then((response) => {
          this.currentGuestsInfo = response.data;
          this.toggleGuestListModal();
        });
    },
    saveBookingInfo() {
      if (this.bookings[this.itemIndex].status === "checkedout") {
        return;
      }
      if (
        (this.reservation.clientName === "" ||
          this.reservation.clientName === this.bookings[this.itemIndex].name) &&
        this.reservation.clientEmail ===
        this.bookings[this.itemIndex].clientemail &&
        this.reservation.clientAddress ===
        this.bookings[this.itemIndex].clientaddress &&
        this.reservation.clientPhone ===
        this.bookings[this.itemIndex].contactNumber &&
        this.reservation.remarks === this.bookings[this.itemIndex].remarks
      ) {
        return;
      }
      this.$swal
        .fire({
          icon: "warning",
          title: "Update Info",
          text: "Are you certain so save this updates?",
          confirmButtonText: "Yes",
          cancelButtonText: "No",
          showCancelButton: true,
        })
        .then(async (result) => {
          if (result.isConfirmed) {
            this.actionRecorder(
              `record?type=updateinfo&bookingID=${this.bookings[this.itemIndex].itemID
              }&groupkey=${this.bookings[this.itemIndex].groupkey}&remarks=${this.reservation.clientName ===
                this.bookings[this.itemIndex].name
                ? ""
                : `name: from ${this.bookings[this.itemIndex].name} to ${this.reservation.clientName
                }; `
              }${this.reservation.clientEmail ===
                this.bookings[this.itemIndex].clientemail
                ? ""
                : `email: from ${this.bookings[this.itemIndex].clientemail
                } to ${this.reservation.clientEmail};`
              }${this.reservation.clientAddress ===
                this.bookings[this.itemIndex].clientaddress
                ? ""
                : `address: from ${this.bookings[this.itemIndex].clientaddress
                } to ${this.reservation.clientAddress};`
              }${this.reservation.clientPhone ===
                this.bookings[this.itemIndex].contactNumber
                ? ""
                : `contact: from ${this.bookings[this.itemIndex].contactNumber
                } to ${this.reservation.clientPhone};`
              }`
            );

            const response = await axios.put(
              this.API_URL + `bookings/${this.bookings[this.itemIndex].id}/`,
              {
                itemID: this.bookings[this.itemIndex].itemID,
                status: this.bookings[this.itemIndex].status,
                name: this.reservation.clientName,
                clientemail: this.reservation.clientEmail,
                clientaddress: this.reservation.clientAddress,
                clientnationality: this.reservation.clientNationality,
                clientType: this.reservation.clientType,
                checkinDate: this.bookings[this.itemIndex].checkinDate,
                checkoutDate: this.bookings[this.itemIndex].checkoutDate,
                room_name: this.bookings[this.itemIndex].room_name,
                room_price: this.bookings[this.itemIndex].room_price,
                room_type: this.bookings[this.itemIndex].room_type,
                remarks:
                  this.reservation.remarks +
                  "\n" +
                  this.bookings[this.itemIndex].remarks,
                contactNumber: this.reservation.clientPhone,
                isPaid: this.bookings[this.itemIndex].isPaid,
                totalPrice: this.bookings[this.itemIndex].totalPrice,
                partialPayment: this.bookings[this.itemIndex].partialPayment,
                processedBy: this.userdata.fName + " " + this.userdata.lName,
                groupkey: this.bookings[this.itemIndex].groupkey,
              }
            );
            this.taskRecord(
              `action:/modified guest info/client:/${this.bookings[this.itemIndex].name
              }`
            );
            this.populateCalendarItems();
            this.toggleItemModal();
          }
        });
    },
    handledragstart(e, room, book) {
      this.draggedItem = this.origbookings.filter(
        (o) => o.itemID === book.itemID
      );
      // this.itemIndex = this.bookings.findIndex((o) => o.itemID === book.itemID);

      // const checkindate = new Date(
      //   parseDate(this.origbookings[this.itemIndex].checkinDate)
      // );
      // checkindate.setDate(checkindate.getDate() + 1);

      // const checkoutdate = new Date(
      //   parseDate(this.origbookings[this.itemIndex].checkoutDate)
      // );
      // checkoutdate.setDate(checkoutdate.getDate() + 1);

      // this.origbookings[this.itemIndex].checkinDate = formatDate2(checkindate);
      // this.origbookings[this.itemIndex].checkoutDate =
      //   formatDate2(checkoutdate);
      this.draggedRoom = room;
    },
    handledragstartday(e, d, r) {
      this.selectionStart = d;
      this.dragDayIsSelected = true;
    },
    handleDragOver(e) { },
    handledragend(e) { },
    handleDragDrop(e, d, r) {
      if (this.dragDayIsSelected) {
        this.selectionEnd = d;
        this.finishSelection([this.selectionStart, this.selectionEnd]);
        this.dragDayIsSelected = false;
        this.toggleselect = false;
        this.toggleselect2 = false;
        this.notoggle = false;
        this.roomSelect = "no";
        this.reservation.roomName = [r];
      } else {
        const id = this.draggedItem[0].itemID;
        const startDate = parseDateOrig(this.draggedItem[0].checkinDate);
        const endDate = parseDateOrig(this.draggedItem[0].checkoutDate);
        const roomOrig = this.draggedRoom.name;
        const roomNew = r.name;
        let item = {
          originalItem: {
            startDate: startDate,
            endDate: endDate,
          },
          id: id,
          startDate: new Date(startDate),
          endDate: new Date(endDate),
        };
        if (roomOrig !== roomNew) {
          this.moveRoom(this.draggedItem[0], r, d, item);
        } else {
          this.onDrop(item, d);
          this.draggedItem = null;
          this.draggedRoom = null;
        }
      }
    },
    async moveRoom(book, r, d, o) {
      const item = book;
      const room = r;
      const day = d;
      this.itemIndex = this.bookings.findIndex((o) => o.itemID === item.itemID);
      const oldroom = {
        name: this.bookings[this.itemIndex].room_name,
        type: this.bookings[this.itemIndex].room_type,
        price: this.bookings[this.itemIndex].room_price,
      };
      const newroom = {
        name: room.name,
        type: room.type,
        price: room.price,
      };
      const pax = this.rooms.filter((o) => o.name === newroom.name)[0].pax;
      const roomprice = this.items.filter(
        (o) => o.item === "Room Guest" && o.type.toLowerCase() === "entrance"
      )[0].priceRate;
      const itemStatus = this.bookings[this.itemIndex].status;
      if (itemStatus === "reserved") {
        const eLength = CalendarMath.dayDiff(o.startDate, d);
        let landingDateCheckin = CalendarMath.addDays(o.startDate, eLength);
        let landingDateCheckout = CalendarMath.addDays(o.endDate, eLength);
        let filteredBookings = this.bookings.filter(
          (booking) =>
            booking.status === "reserved" &&
            booking.itemID !== o.id &&
            booking.room_name === r.name &&
            new Date(
              booking.checkinDate.split("/")[2] +
              "-" +
              booking.checkinDate.split("/")[1] +
              "-" +
              booking.checkinDate.split("/")[0]
            ).setHours(0, 0, 0, 0) <=
            landingDateCheckout.setHours(0, 0, 0, 0) &&
            new Date(
              booking.checkoutDate.split("/")[2] +
              "-" +
              booking.checkoutDate.split("/")[1] +
              "-" +
              booking.checkoutDate.split("/")[0]
            ).setHours(0, 0, 0, 0) >= landingDateCheckin.setHours(0, 0, 0, 0)
        );
        if (filteredBookings.length > 0) {
          this.$swal.fire({
            icon: "error",
            title: "Cannot Adjust Reservation",
            text: "Dates conflict with an existing room reservation.",
            confirmButtonText: "OK",
          });
          return false;
        }
      }

      axios
        .post(`${this.API_URL}transaction/item/filter/`, {
          columnName: "bookingID",
          columnKey: item.itemID,
        })
        .then(async (response) => {
          try {
            for (const o of response.data) {
              await axios.put(`${this.API_URL}transaction/item/${o.id}/`, {
                bookingID: o.bookingID,
                itemName: o.itemOption === "room" ? newroom.name : o.itemName,
                itemType: o.itemOption === "room" ? newroom.type : o.itemType,
                itemPriceRate:
                  o.itemOption === "room"
                    ? newroom.price + "/" + o.itemPriceRate.split("/")[1].trim()
                    : o.itemPriceRate,
                purchaseQty: o.purchaseQty,
                totalCost:
                  o.itemOption === "room"
                    ? parseFloat(newroom.price) * parseFloat(o.purchaseQty)
                    : o.itemType.toLowerCase() === "entrance"
                      ? roomprice * o.numdays * o.purchaseQty
                      : o.totalCost,
                category:
                  o.itemType.toLowerCase() === "entrance"
                    ? "inclusion"
                    : o.category,
                itemOption: o.itemOption,
                totalguest: o.totalguest,
                totalpax:
                  o.itemOption === "room" ||
                    o.itemType.toLowerCase() === "entrance"
                    ? pax
                    : o.totalpax,
                currentroom: newroom.name,
                numdays: o.numdays,
                guestinfo: o.guestinfo,
              });
            }
          } catch (error) {
            console.error(error);
          }

          //this.onDrop(o, d);
          item.room_name = newroom.name;
          item.room_price = newroom.price;
          item.room_type = newroom.type;
          item.remarks =
            item.remarks +
            "\n" +
            "transferred from: " +
            oldroom.name +
            " on " +
            formatDate();

          this.updateBookings(item.id);
          this.actionRecorder(
            `record?type=transfer&bookingID=${item.itemID}&groupkey=${item.groupkey}&remarks=from ${oldroom.name} to ${newroom.name}`
          );
          this.taskRecord(`action:/transfer guest/client:/${item.name}`);
          this.draggedItem = null;
          this.draggedRoom = null;
        });
    },
    handleReceptionRoomAction(room) {
      this.$swal
        .fire({
          icon: "warning",
          title: "Room Housekeeping",
          text: "Are you certain that this room has already been inspected?",
          confirmButtonText: "Yes",
          cancelButtonText: "No",
          showCancelButton: true,
        })
        .then((result) => {
          if (result.isConfirmed) {
            axios
              .post(`${this.API_URL}rooms/filter/`, [
                { columnName: "name", columnKey: room.name },
              ])
              .then((response) => {
                axios
                  .put(`${this.API_URL}rooms/${room.id}/`, {
                    name: response.data[0].name,
                    type: response.data[0].type,
                    price: response.data[0].price,
                    isAvailable: response.data[0].isAvailable,
                    status:
                      response.data[0].status === "clean" ? "dirty" : "clean",
                  })
                  .then((response) => {
                    document.location.reload();
                  });
              });
          }
        });
    },
    handleReceptionDayAction(d, room) {
      if (this.booksearchtext !== "") {
        this.$swal.fire({
          icon: "error",
          title: "Calendar Day Selection Restricted",
          text: "Unable to select a day on the calendar when the search query is not empty.",
          confirmButtonText: "OK",
        });
        return;
      }
      this.reservation.status = "vacant";
      this.reservation.clientName = "";
      this.reservation.clientEmail = "";
      this.reservation.clientAddress = "";
      this.reservation.clientNationality = "Filipino";
      this.reservation.clientType = "in-house";
      this.reservation.remarks = "";
      this.reservation.clientPhone = "";
      this.reservation.roomName = [
        { name: room.name, type: room.type, price: room.price },
      ];
      this.roomSelect = "no";
      this.reservation.checkinDate = d.toLocaleDateString("en-GB");
      this.reservation.checkoutDate = d.toLocaleDateString("en-GB");
      this.toggleItemModal();
    },
    handleReceptionItemAction(book, room) {
      this.itemIndex = this.bookings.findIndex((o) => o.itemID === book.itemID);
      if (this.itemIndex !== -1) {
        this.showReservation();
      } else {
        this.reservation.status = "vacant";
        this.reservation.clientName = "";
        this.reservation.clientEmail = "";
        this.reservation.clientAddress = "";
        this.reservation.clientNationality = "Filipino";
        this.reservation.clientType = "in-house";
        this.reservation.remarks = "";
        // this.reservation.numguests = "";
        this.reservation.clientPhone = "";
        this.reservation.roomName = [
          { name: room.name, type: room.type, price: room.price },
        ];
        this.roomSelect = "no";
        this.reservation.checkinDate = new Date().toLocaleDateString("en-GB");
        this.reservation.checkoutDate = new Date().toLocaleDateString("en-GB");
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
      if (this.reservation.status === "checkedout") {
        return;
      }
      switch (event.key) {
        case "Enter":
          event.preventDefault();
          if (this.total > 0) {
            this.initializePlaceOrder();
          }
          break;
        case "F1":
          event.preventDefault();
          this.showShoppingModal();
          break;
        case "F2":
          event.preventDefault();
          this.moveInclusionCartToMain();
          break;
        case "F10":
          event.preventDefault();
          this.generateBillingStatement();
          break;
      }
    },
    addToCash(d) {
      this.cashAmount = isNaN(parseFloat(this.cashAmount))
        ? 0
        : parseFloat(this.cashAmount) + d;
    },
    updateTotalCash() {
      if (
        this.cashAmount === 0 ||
        this.cashAmount.toString() === "" ||
        this.cashAmount === NaN
      ) {
        this.cashAmount = 0;
      } else {
        this.cashAmount = this.cashAmount.toString();
      }
      //alert(this.totalCash)
    },
    setDiscount() {
      this.$swal
        .fire({
          title: "Set discount value",
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
          confirmButtonText: "Submit",
          cancelButtonText: "Cancel",
          allowOutsideClick: false,
          preConfirm: () => {
            const discountType = document.querySelector(
              'input[name="discountType"]:checked'
            ).value;
            const discountValue =
              document.getElementById("discountValue").value;
            return { discountType, discountValue };
          },
        })
        .then((result) => {
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
      if (this.paymentMethod === "non-cash") {
        this.$swal
          .fire({
            title: "Choose non-cash type",
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
            confirmButtonText: "Submit",
            cancelButtonText: "Cancel",
            allowOutsideClick: false,
            preConfirm: () => {
              const noncashType = document.querySelector(
                'input[name="noncashType"]:checked'
              ).value;
              const referenceno = document.getElementById("referenceno").value;
              return { noncashType, referenceno };
            },
          })
          .then((result) => {
            if (result.isConfirmed) {
              const { noncashType, referenceno } = result.value;
              if (noncashType !== "" || referenceno !== "") {
                this.nonCashPayPlatform = noncashType;
                this.nonCashReference = referenceno;
              } else {
                this.$swal({
                  title: "Warning",
                  text: "Please provide both the non-cash type and the reference number.",
                  icon: "warning",
                });
                return;
              }
            }
          });
      } else {
        this.nonCashPayPlatform = "";
        this.nonCashReference = "";
        this.setAgent();
      }
    },
    setAgentNoCredit() {
      if (this.paymentMethod === "agentnocredit") {
        let divinputs = "";
        let currentIndex = 0;

        for (const agent of this.agents.filter((o) => o.type === "nocredit")) {
          divinputs += `<input type="radio" class="form-check-input" id="cat${currentIndex}" name="agentType" value="${agent.name
            }" ${currentIndex === 0 ? "checked" : ""
            }><label for="cat${currentIndex}" class="form-check-label">${agent.name
            }</label> &nbsp;`;
          currentIndex += 1;
        }
        this.$swal
          .fire({
            title: "Choose agent",
            html: `
        <div>
          ${divinputs}
          <br><br>
          <input type="text" class="form-control" maxlength=32 id="referenceno" placeholder="Enter reference/transaction no. here after agent payment."><br>
          <input type="number" min=1 step=0.1 class="form-control" maxlength=32 id="actualpay" placeholder="Enter actual item price as credited by the agent.">
        </div>
      `,
            showCancelButton: true,
            confirmButtonText: "Submit",
            cancelButtonText: "Cancel",
            allowOutsideClick: false,
            preConfirm: () => {
              const agentType = document.querySelector(
                'input[name="agentType"]:checked'
              ).value;
              const referenceno = document.getElementById("referenceno").value;
              const actualpay = document.getElementById("actualpay").value;
              return { agentType, referenceno, actualpay };
            },
          })
          .then((result) => {
            if (result.isConfirmed) {
              const { agentType, referenceno, actualpay } = result.value;
              if (agentType !== "" || referenceno !== "") {
                this.agentPayPlatform = agentType;
                this.nonCashReference = referenceno;
                this.agentPayment = parseFloat(actualpay);
              } else {
                this.$swal({
                  title: "Warning",
                  text: "Please provide both the agent type and the reference number.",
                  icon: "warning",
                });
                return;
              }
            }
          });
      } else {
        this.agentPayPlatform = "";
        this.nonCashReference = "";
        this.setAgent();
      }
    },
    setAgent() {
      if (this.paymentMethod === "agentcredit") {
        let divinputs = "";
        let currentIndex = 0;

        for (const agent of this.agents.filter((o) => o.type === "credit")) {
          divinputs += `<input type="radio" class="form-check-input" id="cat${currentIndex}" name="agentType" value="${agent.name
            }" ${currentIndex === 0 ? "checked" : ""
            }><label for="cat${currentIndex}" class="form-check-label">${agent.name
            }</label> &nbsp;`;
          currentIndex += 1;
        }

        this.$swal
          .fire({
            title: "Choose agent",
            html: `
        <div>
          ${divinputs}
          <br><br>
          <input type="text" class="form-control" maxlength=32 id="referenceno" placeholder="Enter reference/transaction no. here after agent payment."><br>
          <input type="number" min=1 step=0.1 class="form-control" maxlength=32 id="actualpay" placeholder="Enter actual item price as credited by the agent.">
        </div>
      `,
            showCancelButton: true,
            confirmButtonText: "Submit",
            cancelButtonText: "Cancel",
            allowOutsideClick: false,
            preConfirm: () => {
              const agentType = document.querySelector(
                'input[name="agentType"]:checked'
              ).value;
              const referenceno = document.getElementById("referenceno").value;
              const actualpay = document.getElementById("actualpay").value;
              return { agentType, referenceno, actualpay };
            },
          })
          .then((result) => {
            if (result.isConfirmed) {
              const { agentType, referenceno, actualpay } = result.value;
              if (agentType !== "" || referenceno !== "") {
                this.agentPayPlatform = agentType;
                this.nonCashReference = referenceno;
                this.agentPayment = parseFloat(actualpay);
              } else {
                this.$swal({
                  title: "Warning",
                  text: "Please provide both the agent type and the reference number.",
                  icon: "warning",
                });
                return;
              }
            }
          });
      } else {
        this.agentPayPlatform = "";
        this.nonCashReference = "";
        this.setAgentNoCredit();
      }
    },
    async deleteTransaction(id) {
      axios
        .get(this.API_URL + `transaction/${id}/`)
        .then(async (response) => {
          const data = response.data;
          const itemID = data.bookingID;
          const gkey = data.groupkey || "";
          const cname = data.clientname;
          const type = itemID.charAt(0);
          this.$swal
            .fire({
              title: "Authorization Required",
              input: "text",
              showCancelButton: true,
              allowOutsideClick: false,
              inputAttributes: {
                minlength: 6, // Minimum length of 3 characters
                maxlength: 24, // Maximum length of 24 characters
                autocomplete: "off",
                style: "text-security:disc; -webkit-text-security:disc;",
              },
              confirmButtonText: "Submit",
              cancelButtonText: "Cancel",
              inputPlaceholder: "Enter authorization code",
            })
            .then(async (result) => {
              if (result.isConfirmed) {
                const authorizationCode = result.value;
                // Validate the authorization code and perform necessary actions
                if (
                  authorizationCode.toLowerCase() ===
                  this.AUTHORIZATION_KEY.toLowerCase()
                ) {
                  // Code is correct, proceed with the desired action
                  const confirmMessage =
                    " If you proceed with voiding, all associated items and booking and transaction records will be permanently deleted, and this action cannot be reversed.";
                  const result = await this.$swal.fire({
                    title: "Are you sure you want to void this?",
                    text: confirmMessage,
                    icon: "warning",
                    showCancelButton: true,
                    confirmButtonColor: "#3085d6",
                    cancelButtonColor: "#d33",
                    confirmButtonText: "Yes, void it!",
                    cancelButtonText: "Cancel",
                  });
                  if (result.isConfirmed) {
                    const countdownMessage =
                      'Item will be voided in <span id="countdown">5</span> seconds. Do you want to cancel?';
                    let countdownResult;
                    countdownResult = await this.$swal.fire({
                      title: "Please wait",
                      html: countdownMessage,
                      icon: "info",
                      showCancelButton: true,
                      confirmButtonColor: "#3085d6",
                      cancelButtonColor: "#d33",
                      confirmButtonText: "Confirm now",
                      cancelButtonText: "Cancel",
                      didOpen: () => {
                        const countdownEl =
                          document.querySelector("#countdown");
                        let count = 5;
                        const timerId = setInterval(() => {
                          countdownEl.textContent = count;
                          count--;
                          if (count < 0) {
                            clearInterval(timerId);
                            this.$swal.close();
                          }
                        }, 1000);
                      },
                    });
                    if (!countdownResult.isConfirmed) {
                      return;
                    }
                    if (type === "f") {
                      this.voidAction(null, null, itemID, gkey, cname, false);
                    } else if (type === "e") {
                      const bID = this.bookings.findIndex(
                        (o) => o.itemID === itemID
                      );
                      const request = await axios.post(
                        `${this.API_URL}bookings/filter/`,
                        [{ columnName: "itemID", columnKey: itemID }]
                      );
                      const keyID = request.data[0].id;
                      this.voidAction(bID, keyID, itemID, gkey, cname, true);
                    }
                  }
                } else {
                  // Code is incorrect, show an error message or take appropriate action
                  this.$swal.fire({
                    icon: "error",
                    title: "Incorrect Passcode",
                    text: "The entered passcode is incorrect. Please try again.",
                    allowOutsideClick: false,
                  });
                }
              }
            });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getTime(d) {
      const date = d;
      const hours = date.getHours().toString().padStart(2, "0");
      const minutes = date.getMinutes().toString().padStart(2, "0");
      return `${hours}:${minutes}`;
    },
    async voidBook() {
      this.toggleItemModal();
      this.$swal
        .fire({
          title: "Authorization Required",
          input: "text",
          showCancelButton: true,
          allowOutsideClick: false,
          inputAttributes: {
            minlength: 6, // Minimum length of 3 characters
            maxlength: 24, // Maximum length of 24 characters
            autocomplete: "off",
            style: "text-security:disc; -webkit-text-security:disc;",
          },
          confirmButtonText: "Submit",
          cancelButtonText: "Cancel",
          inputPlaceholder: "Enter authorization code",
        })
        .then(async (result) => {
          if (result.isConfirmed) {
            const authorizationCode = result.value;
            // Validate the authorization code and perform necessary actions
            if (
              authorizationCode.toLowerCase() ===
              this.AUTHORIZATION_KEY.toLowerCase()
            ) {
              // Code is correct, proceed with the desired action
              const confirmMessage =
                " If you proceed with voiding, all associated items and transaction records will be permanently deleted, and this action cannot be reversed.";
              const result = await this.$swal.fire({
                title: "Are you sure you want to void this?",
                text: confirmMessage,
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Yes, void it!",
                cancelButtonText: "Cancel",
              });
              if (result.isConfirmed) {
                const countdownMessage =
                  'Item will be voided in <span id="countdown">5</span> seconds. Do you want to cancel?';
                let countdownResult;
                countdownResult = await this.$swal.fire({
                  title: "Please wait",
                  html: countdownMessage,
                  icon: "info",
                  showCancelButton: true,
                  confirmButtonColor: "#3085d6",
                  cancelButtonColor: "#d33",
                  confirmButtonText: "Confirm now",
                  cancelButtonText: "Cancel",
                  didOpen: () => {
                    const countdownEl = document.querySelector("#countdown");
                    let count = 5;
                    const timerId = setInterval(() => {
                      countdownEl.textContent = count;
                      count--;
                      if (count < 0) {
                        clearInterval(timerId);
                        this.$swal.close();
                      }
                    }, 1000);
                  },
                });
                if (!countdownResult.isConfirmed) {
                  return;
                }
                this.voidAction(this.itemIndex, null, null, null, null, true);
              }
            } else {
              // Code is incorrect, show an error message or take appropriate action
              this.$swal.fire({
                icon: "error",
                title: "Incorrect Passcode",
                text: "The entered passcode is incorrect. Please try again.",
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
          const existingTransaction = await axios.post(
            `${this.API_URL}transaction/filter/`,
            {
              columnName: "groupkey",
              columnKey: groupkey,
            }
          );
          transdata_ID = existingTransaction.data[0].id;
        } catch (error) { }
        try {
          const existingTransaction_ITEM = await axios.post(
            `${this.API_URL}transaction/item/filter/`,
            {
              columnName: "groupkey",
              columnKey: groupkey,
            }
          );
          for (const item of existingTransaction_ITEM.data) {
            axios.get(this.API_URL + `transaction/item/delete/${item.id}/`);
          }
        } catch (error) { }
        try {
          if (transdata_ID) {
            const existingTransaction_RECORD = await axios.post(
              `${this.API_URL}transaction/record/filter/`,
              {
                columnName: "transaction",
                columnKey: transdata_ID,
              }
            );
            for (const item of existingTransaction_RECORD.data) {
              axios.get(this.API_URL + `transaction/record/delete/${item.id}/`);
            }
          }
        } catch (error) { }
        try {
          if (transdata_ID) {
            axios.get(this.API_URL + `transaction/delete/${transdata_ID}/`);
          }
        } catch (error) { }
        if (brute) {
          try {
            const existingBooking = await axios.post(
              `${this.API_URL}bookings/filter/`,
              {
                columnName: "groupkey",
                columnKey: groupkey,
              }
            );
            for (const item of existingBooking.data) {
              axios.get(this.API_URL + `bookings/delete/${item.id}/`);
            }
          } catch (error) { }
        }
      } else {
        try {
          const existingTransaction = await axios.post(
            `${this.API_URL}transaction/filter/`,
            {
              columnName: "bookingID",
              columnKey: bookKey,
            }
          );
          transdata_ID = existingTransaction.data[0].id;
        } catch (error) { }
        try {
          const existingTransaction_ITEM = await axios.post(
            `${this.API_URL}transaction/item/filter/`,
            {
              columnName: "bookingID",
              columnKey: bookKey,
            }
          );
          for (const item of existingTransaction_ITEM.data) {
            axios.get(this.API_URL + `transaction/item/delete/${item.id}/`);
          }
        } catch (error) { }
        try {
          if (transdata_ID) {
            const existingTransaction_RECORD = await axios.post(
              `${this.API_URL}transaction/record/filter/`,
              {
                columnName: "transaction",
                columnKey: transdata_ID,
              }
            );
            for (const item of existingTransaction_RECORD.data) {
              axios.get(this.API_URL + `transaction/record/delete/${item.id}/`);
            }
          }
        } catch (error) { }
        try {
          if (transdata_ID) {
            axios.get(this.API_URL + `transaction/delete/${transdata_ID}/`);
          }
        } catch (error) { }
        if (brute) {
          try {
            await axios.get(this.API_URL + `bookings/delete/${kid}/`);
          } catch (error) { }
        }
      }
      this.taskRecord(`action:/void/client:/${cname}`);
      await this.$swal
        .fire({
          title: "Success",
          text: "Item was voided successfully!",
          icon: "success",
        })
        .then((response) => {
          //document.location.reload();
        });
    },
    taskRecord(msg) {
      this.socket.send(
        JSON.stringify({
          message: msg,
        })
      );
      this.actionRecorder(msg);
    },
    async actionRecorder(msg) {
      try {
        await axios.post(`${this.API_URL}task/record/`, {
          actor: this.userdata.fName + " " + this.userdata.lName,
          task: msg,
        });
      } catch (error) { }
    },
    handleChange() {
      alert();
    },
    addToCartItem(item) {
      const isItemExist = !(
        this.cartItems.findIndex((o) => o.id === item.id) === -1
      );
      if (isItemExist) return;
      this.cartItems.push(item);
    },
    clearAll() {
      this.cartItems = [];
    },
    bookAll() {
      this.bookalltoggle = true;
      this.newtoggle = false;
      this.isCheckinToggle = false;
      this.isCheckoutToggle = false;
      this.reservation.clientNationality = "Filipino";
      this.reservation.clientType = "in-house";
      this.reservation.roomName = this.cartItems;
      this.clearAll();
      this.toggleRoomsModal();
      this.toggleItemModal();
    },
    removeFromCart(item) {
      this.cartItems = this.cartItems.filter((o) => o.id !== item.id);
    },
    cardAction(id, room_name, room_type, room_price) {
      this.itemIndex = this.bookings.findIndex((o) => o.itemID === id);
      if (this.itemIndex !== -1) {
        this.showReservation();
      } else {
        this.reservation.status = "vacant";
        this.reservation.clientName = "";
        this.reservation.clientEmail = "";
        this.reservation.clientAddress = "";
        this.reservation.clientNationality = "Filipino";
        this.reservation.clientType = "in-house";
        this.reservation.remarks = "";
        // this.reservation.numguests = "";
        this.reservation.clientPhone = "";
        this.reservation.roomName = [
          { name: room_name, type: room_type, price: room_price },
        ];
        this.roomSelect = "no";
        this.reservation.checkinDate = new Date().toLocaleDateString("en-GB");
        this.reservation.checkoutDate = new Date().toLocaleDateString("en-GB");
        this.toggleItemModal();
      }
    },
    sendMessage() {
      console.log("Hello");
      console.log(this.socket);
      this.socket.send('{"message":"hello"}');
    },
    async loadAlldata() {
      this.reloadData();
      this.reloadItemsData();
      this.loadTransactionData();
    },
    parseDate2(dateString) {
      const [day, month, year] = dateString.split("/");
      return new Date(`${month}/${day}/${year}`).setHours(0, 0, 0, 0);
    },
    async logout() {
      const authStore = useAuthStore();
      const user = {
        username: authStore.user.username,
        FirstName: authStore.user.fName,
        LastName: authStore.user.lName,
        role: authStore.user.role,
      };
      const response = await axios.put(
        `${this.API_URL}users/${authStore.user.id}/`,
        { ...user, isActive: false }
      );
      if (response.data !== undefined) {
        authStore.logout();
        this.$router.push("/");
      } else {
        this.$swal({
          icon: "error",
          title: "Logout error. Please contact your admin for assistance!",
        });
      }
    },
    toggleAllTD() {
      this.toggleAll = !this.toggleAll;
      Object.keys(this.showTable).forEach((prop) => {
        this.showTable[prop] = this.toggleAll;
      });
      $(".togglebuttons").trigger("click");
    },
    async toggleTable(transactionID, bookingID) {
      // method to toggle the visibility of the related table for the given transactionID
      this.showTable[transactionID] = !this.showTable[transactionID];
      if (this.showTable[transactionID]) {
        try {
          const response = await axios.post(
            `${this.API_URL}transaction/record/filter/`,
            [{ columnName: "transaction", columnKey: transactionID }]
          );
          const response2 = await axios.post(
            `${this.API_URL}transaction/item/filter/`,
            [{ columnName: "bookingID", columnKey: bookingID }]
          );
          //     return filtered.map(item => {
          //   const searchCode = Object.values(item).join("~");
          //   return {
          //     ...item,
          //     searchCode
          //   };
          // }).filter(item => item.searchCode.toString().toLowerCase().includes(this.searchTerm.toLowerCase()));
          const history = response.data;
          const itemprops = response2.data;
          this.transactions = this.transactions.map((t) => {
            if (t.id === transactionID) {
              t.items = history;
              t.props = itemprops;
            }
            return t;
          });
        } catch (error) { }
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
        const response = await axios.get(this.API_URL + "transaction/");
        this.billing.bookingID = response.data[response.data.length - 1].id + 1;
      } catch { }
      this.toggleAddAccountModal();
    },
    showShoppingModal() {
      $("#shopModal").modal("toggle");
    },
    sumtotalPax() {
      const roomsBooked = this.cart.filter(
        (item) =>
          item.category === "main" && item.type.toLowerCase().includes("room")
      );

      let sumAllowedGuest = 0;
      try {
        for (const r of roomsBooked) {
          const roompax = parseFloat(
            this.rooms.filter((o) => o.name === r.name)[0].pax
          );
          sumAllowedGuest += roompax;
        }
      } catch (e) { }
      return sumAllowedGuest;
    },
    sumTotalGuests() {
      const totalGuests = this.cart
        .filter(
          (o) => o.name.toLowerCase() === "room guest" && o.category === "main"
        )
        .reduce((acc, item) => acc + parseFloat(item.purqty), 0);
      return totalGuests;
    },
    howManyDays() {
      const checkInDate = parseDate(this.bookings[this.itemIndex].checkinDate);
      const checkOutDate = parseDate(
        this.bookings[this.itemIndex].checkoutDate
      );
      const numdays = (checkOutDate - checkInDate) / (1000 * 60 * 60 * 24);
      return numdays + 1;
    },
    async moveInclusionCartToMain() {
      let bId = null;
      let gkey = null;
      const n = this.filteredInclusionCart.length;
      if (n > 0) {
        const result = await this.$swal.fire({
          title: "Confirmation",
          text: "This action will update your cart. Do you want to proceed?",
          icon: "warning",
          showCancelButton: true,
          confirmButtonColor: "#3085d6",
          cancelButtonColor: "#d33",
          confirmButtonText: "Yes, do it!",
          cancelButtonText: "Cancel",
        });
        if (result.isConfirmed) {
          try {
            bId = this.bookings[this.itemIndex].itemID;
          } catch {
            bId = "walkin";
            if (this.walkinID === "") {
              this.walkinID =
                "f" +
                new Date().getTime().toString() +
                this.generateUniqueString();
            }
          }
          try {
            gkey = this.bookings[this.itemIndex].groupkey;
          } catch { }
          try {
            const updatedItems = [];
            let isFind = false;
            // Loop through inclusion items in the cart

            const roomsBooked = this.cart.filter(
              (item) =>
                item.category === "main" &&
                item.type.toLowerCase().includes("room")
            );

            let sumAllowedGuest = 0;
            try {
              for (const r of roomsBooked) {
                const roompax = parseFloat(
                  this.rooms.filter((o) => o.name === r.name)[0].pax
                );
                sumAllowedGuest += roompax;
              }
            } catch (e) { }

            let inclusionprice = 0;

            for (const item of this.cart.filter(
              (item) => item.category === "inclusion"
            )) {
              // Define the API endpoint and data for the PUT request
              const api = `${this.API_URL}transaction/item/${item.id}/`;
              const data = {
                itemName: item.name,
                itemType: item.type,
                itemPriceRate: item.priceRate,
                purchaseQty: item.purqty,
                totalCost: item.totalCartPrice,
                category: "main",
                itemOption: "addons",
                numdays: item.numdays,
                totalguest: item.totalguest,
                totalpax: item.totalpax,
                currentroom: item.currentroom,
              };

              if (!this.walkinStatus) {
                const numBookedRooms = this.cart.filter(
                  (o) =>
                    (o.type.toLowerCase().includes("room") ||
                      o.type.toLowerCase() === "leisures") &&
                    o.category === "main"
                ).length;
                const numGuestsCard = this.cart
                  .filter((o) => o.name.toLowerCase() === "room guest")
                  .reduce((acc, item) => acc + parseFloat(item.purqty), 0);
                const entranceFee = parseFloat(
                  this.items.filter(
                    (o) => o.item.toLowerCase() === "room guest"
                  )[0].priceRate
                );

                const response = await axios.post(
                  this.API_URL + "transaction/item/filter/",
                  {
                    columnName: "bookingID",
                    columnKey: this.bookings[this.itemIndex].itemID,
                  }
                );

                const totalGuestsMain = response.data
                  .filter(
                    (o) =>
                      o.itemName.toLowerCase() === "room guest" &&
                      o.category === "main"
                  )
                  .reduce((acc, item) => acc + parseFloat(item.purchaseQty), 0);

                const checkInDate = parseDate(
                  this.bookings[this.itemIndex].checkinDate
                );
                const checkOutDate = parseDate(
                  this.bookings[this.itemIndex].checkoutDate
                );
                const numdays =
                  (checkOutDate - checkInDate) / (1000 * 60 * 60 * 24);

                if (totalGuestsMain <= data.totalpax) {
                  // if (totalGuestsMain <= totalGuests) {

                  data.totalCost =
                    parseFloat(data.totalCost) -
                      (parseFloat(data.purchaseQty) >
                        parseFloat(data.totalpax) - totalGuestsMain
                        ? parseFloat(data.totalpax) - totalGuestsMain
                        : parseFloat(data.purchaseQty)) *
                      entranceFee <
                      0
                      ? 0
                      : parseFloat(data.totalCost) -
                      (parseFloat(data.purchaseQty) >
                        parseFloat(data.totalpax) - totalGuestsMain
                        ? parseFloat(data.totalpax) - totalGuestsMain
                        : parseFloat(data.purchaseQty)) *
                      entranceFee;
                }

                if (data.itemName.toLowerCase() === "room guest") {
                  data.totalCost = (numdays + 1) * data.totalCost;
                  data.totalguest = totalGuestsMain + data.purchaseQty;
                }
              }

              item.totalCartPrice = data.totalCost;
              item.totalguest = data.totalguest;
              item.totalpax = data.totalpax;
              item.numdays = data.numdays;
              item.currentroom = data.currentroom;

              inclusionprice += item.totalCartPrice;

              try {
                if (!this.walkinStatus) {
                  data.bookingID = bId;
                  data.groupkey = gkey;
                  // Send PUT request to update the item
                  const response = await axios.put(api, data);
                  updatedItems.push(response.data);
                } else {
                  data.bookingID = this.walkinID;
                  data.currentroom = "walkin";
                  bId = data.bookingID;
                  const response = await axios.post(api, data);
                  updatedItems.push(response.data);
                }
              } catch (error) { }

              if (bId.charAt(0) !== "f") {
                this.actionRecorder(
                  `record?type=additem&bookingID=${this.bookings[this.itemIndex].itemID
                  }&groupkey=${this.bookings[this.itemIndex].groupkey
                  }&remarks=added ${data.itemName}`
                );
              }
            }

            // this.cart
            //   .filter((item) => item.category === "inclusion")
            //   .forEach(async (item, index) => {
            //     // Define the API endpoint and data for the PUT request
            //     const api = `${this.API_URL}transaction/item/${item.id}/`;
            //     const data = {
            //       itemName: item.name,
            //       itemType: item.type,
            //       itemPriceRate: item.priceRate,
            //       purchaseQty: item.purqty,
            //       totalCost: item.totalCartPrice,
            //       category: "main",
            //       itemOption: "addons",
            //       numdays: item.numdays,
            //       totalguest: item.totalguest,
            //       totalpax: item.totalpax,
            //       currentroom: item.currentroom,
            //     };
            //     if (!this.walkinStatus) {
            //       const numBookedRooms = this.cart.filter(
            //         (o) =>
            //           (o.type.toLowerCase().includes("room") ||
            //             o.type.toLowerCase() === "leisures") &&
            //           o.category === "main"
            //       ).length;
            //       const numGuestsCard = this.cart
            //         .filter((o) => o.name.toLowerCase() === "room guest")
            //         .reduce((acc, item) => acc + parseFloat(item.purqty), 0);
            //       const entranceFee = parseFloat(
            //         this.items.filter(
            //           (o) => o.item.toLowerCase() === "room guest"
            //         )[0].priceRate
            //       );
            //       const response = await axios.post(
            //         this.API_URL + "transaction/item/filter/",
            //         {
            //           columnName: "bookingID",
            //           columnKey: this.bookings[this.itemIndex].itemID,
            //         }
            //       );
            //       const totalGuestsMain = response.data
            //         .filter(
            //           (o) =>
            //             o.itemName.toLowerCase() === "room guest" &&
            //             o.category === "main"
            //         )
            //         .reduce(
            //           (acc, item) => acc + parseFloat(item.purchaseQty),
            //           0
            //         );
            //       const checkInDate = parseDate(
            //         this.bookings[this.itemIndex].checkinDate
            //       );
            //       const checkOutDate = parseDate(
            //         this.bookings[this.itemIndex].checkoutDate
            //       );
            //       const numdays =
            //         (checkOutDate - checkInDate) / (1000 * 60 * 60 * 24);
            //       if (totalGuestsMain <= data.totalpax) {
            //         // if (totalGuestsMain <= totalGuests) {
            //         data.totalCost =
            //           parseFloat(data.totalCost) -
            //             (parseFloat(data.purchaseQty) >
            //             parseFloat(data.totalpax) - totalGuestsMain
            //               ? parseFloat(data.totalpax) - totalGuestsMain
            //               : parseFloat(data.purchaseQty)) *
            //               entranceFee <
            //           0
            //             ? 0
            //             : parseFloat(data.totalCost) -
            //               (parseFloat(data.purchaseQty) >
            //               parseFloat(data.totalpax) - totalGuestsMain
            //                 ? parseFloat(data.totalpax) - totalGuestsMain
            //                 : parseFloat(data.purchaseQty)) *
            //                 entranceFee;
            //       }
            //       if (data.itemName.toLowerCase() === "room guest") {
            //         data.totalCost = (numdays + 1) * data.totalCost;
            //         data.totalguest = totalGuestsMain + data.purchaseQty;
            //       }
            //     }
            //     item.totalCartPrice = data.totalCost;
            //     item.totalguest = data.totalguest;
            //     item.totalpax = data.totalpax;
            //     item.numdays = data.numdays;
            //     item.currentroom = data.currentroom;
            //     try {
            //       if (!this.walkinStatus) {
            //         data.bookingID = bId;
            //         data.groupkey = gkey;
            //         // Send PUT request to update the item
            //         const response = await axios.put(api, data);
            //         updatedItems.push(response.data);
            //       } else {
            //         data.bookingID = this.walkinID;
            //         data.currentroom = "walkin";
            //         bId = data.bookingID;
            //         const response = await axios.post(api, data);
            //         updatedItems.push(response.data);
            //       }
            //     } catch (error) {}
            //   });
            // Wait for all PUT requests to finish before updating the local cart

            await Promise.all(
              this.cart
                .filter((item) => item.category === "inclusion")
                .map(async (item) => {
                  // Update the category of each inclusion item to 'main'
                  item.category = "main";
                  // Find the updated version of the item in the list of updated items
                  const updatedItem = updatedItems.find(
                    (updatedItem) => updatedItem.id === item.id
                  );
                  // If the item was successfully updated, update the local cart with the new data
                  if (updatedItem) {
                    Object.assign(item, updatedItem);
                  }
                })
            );

            if (bId !== "walkin") {
              const resId = this.bookings[this.itemIndex].id;
              if (inclusionprice > 0) {
                this.bookings[this.itemIndex].isPaid = "partial";
              }

              this.updateBookings(resId);
              this.populateCalendarItems();
            }
          } catch (error) {
            console.error(error);
          }
        }
      }
    },
    setCheckoutDate() {
      const checkoutdate = new Date(parseDate(this.reservation.checkoutDate));
      checkoutdate.setDate(checkoutdate.getDate() + 1);
      return formatDate2(checkoutdate);
    },
    async resetSummary(no) {
      this.cart = [];
      this.billing = {
        clientName: "",
        clientEmail: "",
        clientPhone: "",
        clientAddress: "",
        clientNationality: "Filipino",
        clientType: "walkin",
        bookingID: "",
      };
      this.walkinID = "";
      this.cashHistory = [];
      this.walkinreservation = {
        clientName: "",
        clientEmail: "",
        clientPhone: "",
        clientAddress: "",
        clientNationality: "Filipino",
        clientType: "walkin",
      };
      this.subtotal = 0;
      this.partialPayment = 0;
      this.total = 0;
      this.discountValue = 0;
      this.change = 0;
      this.paymentMethod = "cash";
      this.nonCashPayPlatform = "";
      this.agentPayPlatform = "";
      this.nonCashReference = "";
      this.isCheckinToggle = false;
      this.isCheckoutToggle = false;
      this.simulCtrl = false;
      this.isExtended = false;
      this.extendView();
      this.itemCart = {
        id: 0,
        name: "",
        type: "",
        priceRate: "",
        rate: "",
        counter: "",
        purqty: "",
        totalCartPrice: "",
        category: "",
      };
      this.justDiscounted = false;
      this.alreadyDiscounted = false;
      this.itemIndex = -1;
      this.walkinStatus = false;
      this.walkinview = false;
      this.isItNew = false;
      if (no === 0) {
        this.dashboardStatus = true;
      }
      if (no === 1) {
        this.$refs.searchQuery.focus();
        this.$refs.searchQuery.blur();
      }
      if (no === 2 && this.billing.clientName === "") {
        this.activeAccountFlag = true;
        this.walkinStatus = true;
        // this.toggleAddAccountModal();
      }
      if (no === 3) {
        const response = await axios.get(
          this.API_URL + "transactions_itemizer/0/?N=1000"
        );
        this.transactions = response.data;
      }
      if (no !== 2) {
        this.activeAccountFlag = false;
      }
    },
    changeTab(tab) {
      this.activeTab = tab;
    },
    //generic methods
    optionClicked1(event) {
      const item = event.item;
      const uniqID = item.substring(
        item.toString().indexOf("~") + 1,
        item.toString().lastIndexOf("~")
      );
      const action = event.option.slug;
      window.alert(action);
    },
    toggleGuestListModal() {
      $("#guestListModal").modal("toggle");
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
    toggleRoomsModal() {
      const currentDate = new Date(); // get current date
      if (
        this.selectionStart.setHours(0, 0, 0, 0) <
        currentDate.setHours(0, 0, 0, 0)
      ) {
        // check if start date is before current date
        // prompt user to select a valid start date
        return;
      }
      this.disablebutton = false;
      $("#availableRoomsModal").modal("toggle");
    },
    toggleSettingsModal() {
      $("#settings-modal").modal("toggle");
    },
    toggleShowAllModal() {
      $("#showall-modal").modal("toggle");
    },
    changeItemColor(status) {
      let item =
        this.calendarItems[
        this.calendarItems.findIndex(
          (o) => o.id === this.bookings[this.itemIndex].itemID
        )
        ];
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
      this.updateBookings(item.id);
      try {
        gkey = this.bookings[this.itemIndex].groupkey || "x";
        try {
          const o = await axios.post(`${this.API_URL}bookings/filter/`, [
            { columnName: "groupkey", columnKey: gkey },
          ]);
          groupbookings = o.data;
        } catch (error) { }
      } catch (error) { }
      if (groupbookings.length > 0) {
        existingTransaction = await axios.post(
          `${this.API_URL}transaction/filter/`,
          {
            columnName: "groupkey",
            columnKey: gkey,
          }
        );
      } else {
        existingTransaction = await axios.post(
          `${this.API_URL}transaction/filter/`,
          {
            columnName: "bookingID",
            columnKey: bookingID,
          }
        );
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
      } catch (error) { }
      const response = await axios.post(
        `${this.API_URL}transaction/item/filter/`,
        [
          { columnName: "bookingID", columnKey: bookingID },
          { columnName: "itemName", columnKey: item.room_name },
        ]
      );
      if (response.data.length > 0) {
        //show instead
        //update this.cart
        this.cart = [];
        if (groupbookings.length > 0) {
          const response = await axios.post(
            `${this.API_URL}transaction/item/filter/`,
            [{ columnName: "groupkey", columnKey: gkey }]
          );
          response.data.forEach((item) => {
            let newItem = {
              id: item.id,
              bookingID: item.bookingID,
              groupkey: item.groupkey,
              name: item.itemName,
              type: item.itemType,
              priceRate: item.itemPriceRate,
              purqty: item.purchaseQty,
              totalCartPrice: item.totalCost,
              category: item.category,
              itemOption: item.itemOption,
            };
            this.cart.push(newItem);
          });
        } else {
          const response = await axios.post(
            `${this.API_URL}transaction/item/filter/`,
            [{ columnName: "bookingID", columnKey: bookingID }]
          );
          if (response.data.length > 0) {
            try {
              response.data.forEach((item) => {
                let newItem = {
                  id: item.id,
                  bookingID: item.bookingID,
                  groupkey: item.groupkey,
                  name: item.itemName,
                  type: item.itemType,
                  priceRate: item.itemPriceRate,
                  purqty: item.purchaseQty,
                  totalCartPrice: item.totalCost,
                  category: item.category,
                  itemOption: item.itemOption,
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
        this.newbillingbalance = existingTransaction.data[0].balance;
        this.isItNew = true;
      } else {
        this.billing.bookingID = "";
      }
      try {
        this.partialPayment =
          groupbookings.length === 0
            ? item.partialPayment
            : transaction.cashAmountPay;
        const response = await axios.post(
          `${this.API_URL}transaction/record/filter/`,
          [{ columnName: "transaction", columnKey: transaction.id }]
        );
        this.cashHistory = response.data;
        this.gbookingscount =
          groupbookings.length === 0 ? 1 : groupbookings.length;
      } catch (error) { }
      if (!$("#BookDayModal").hasClass("show")) {
        this.toggleItemModal();
      }
      $("#others-tab").tab("show");
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
      };
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
    async openToCart(trans_id) {
      try {
        const response = await axios.get(
          this.API_URL + `transaction/${trans_id}/`
        );
        const transaction = response.data;
        const bookingID = transaction.bookingID;
        if (bookingID.charAt(0) === "e") {
          this.itemIndex = this.bookings.findIndex(
            (o) => o.itemID === bookingID
          );
          this.reservation.checkinDate =
            this.bookings[this.itemIndex].checkinDate;
          this.reservation.checkoutDate =
            this.bookings[this.itemIndex].checkoutDate;
          this.reservation.status = this.bookings[this.itemIndex].status;
          this.movecartAction();
        } else if (bookingID.charAt(0) === "f") {
          this.walkinStatus = true;
          this.walkinview = true;
          let existingTransaction = null;
          existingTransaction = await axios.post(
            `${this.API_URL}transaction/filter/`,
            {
              columnName: "bookingID",
              columnKey: bookingID,
            }
          );
          try {
            if (existingTransaction.length !== 0) {
              const trans = existingTransaction.data[0];
              this.discountMode = trans.discountMode;
              this.discountValue = trans.discountValue;
              this.cashRemarks = trans.cashRemarks;
              if (trans.discountValue > 0) {
                this.alreadyDiscounted = true;
              }
            }
            const response = await axios.post(
              `${this.API_URL}transaction/item/filter/`,
              [{ columnName: "bookingID", columnKey: bookingID }]
            );
            if (response.data.length > 0) {
              try {
                response.data.forEach((item) => {
                  let newItem = {
                    id: item.id,
                    bookingID: item.bookingID,
                    groupkey: item.groupkey,
                    name: item.itemName,
                    type: item.itemType,
                    priceRate: item.itemPriceRate,
                    purqty: item.purchaseQty,
                    totalCartPrice: item.totalCost,
                    category: item.category,
                    itemOption: item.itemOption,
                    numdays: item.numdays,
                    totalguest: item.totalguest,
                    totalpax: item.totalpax,
                    currentroom: item.currentroom,
                    guestinfo: item.guestinfo,
                  };
                  this.cart.push(newItem);
                });
              } catch (error) {
                console.log(error);
              }
            }
            this.billing.clientName = transaction.clientname;
            this.billing.clientAddress = transaction.clientaddress;
            this.billing.clientPhone = transaction.clientcontact;
            this.billing.clientEmail = transaction.clientemail;
            this.billing.clientNationality = transaction.clientnationality;
            this.billing.clientType = transaction.clientType;
            if (existingTransaction.data[0] !== undefined) {
              this.billing.bookingID = existingTransaction.data[0].id;
              this.newbillingbalance = existingTransaction.data[0].balance;
              this.isItNew = true;
            } else {
              this.billing.bookingID = "";
            }
            try {
              this.partialPayment = transaction.cashAmountPay;
              const response = await axios.post(
                `${this.API_URL}transaction/record/filter/`,
                [{ columnName: "transaction", columnKey: transaction.id }]
              );
              this.cashHistory = response.data;
            } catch (error) {
              console.error(error);
            }
            $("#others-tab").tab("show");
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
            };
          } catch (error) {
            console.error(error);
          }
        } else {
        }
      } catch (error) {
        console.error(error);
      }
    },
    moveToCart() {
      this.movetocartFlag = false;
      this.movecartAction();
    },
    async movecartAction() {
      const item = this.bookings[this.itemIndex];
      const bookingID = item.itemID;
      let existingTransaction = null;
      let transaction = null;
      let gkey = "";
      let groupbookings = [];
      item.remarks = this.reservation.remarks;
      this.updateBookings(item.id);
      try {
        gkey = this.bookings[this.itemIndex].groupkey || "x";
        try {
          const o = await axios.post(`${this.API_URL}bookings/filter/`, [
            { columnName: "groupkey", columnKey: gkey },
          ]);
          groupbookings = o.data;
        } catch (error) { }
      } catch (error) { }
      if (groupbookings.length > 0) {
        existingTransaction = await axios.post(
          `${this.API_URL}transaction/filter/`,
          {
            columnName: "groupkey",
            columnKey: gkey,
          }
        );
      } else {
        existingTransaction = await axios.post(
          `${this.API_URL}transaction/filter/`,
          {
            columnName: "bookingID",
            columnKey: bookingID,
          }
        );
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
      } catch (error) { }
      const response = await axios.post(
        `${this.API_URL}transaction/item/filter/`,
        [
          { columnName: "bookingID", columnKey: bookingID },
          { columnName: "itemName", columnKey: item.room_name },
        ]
      );
      if (response.data.length === 0) {
        if (groupbookings.length > 0) {
          groupbookings.forEach(async (res) => {
            const numDays = Math.ceil(
              (new Date(
                res.checkoutDate.split("/")[2] +
                "-" +
                res.checkoutDate.split("/")[1] +
                "-" +
                res.checkoutDate.split("/")[0]
              ).setHours(0, 0, 0, 0) -
                new Date(
                  res.checkinDate.split("/")[2] +
                  "-" +
                  res.checkinDate.split("/")[1] +
                  "-" +
                  res.checkinDate.split("/")[0]
                ).setHours(0, 0, 0, 0)) /
              (1000 * 60 * 60 * 24)
            );
            this.itemCart.id = this.cart.length + 1;
            this.itemCart.name = res.room_name;
            this.itemCart.type = res.room_type;
            this.itemCart.priceRate = res.room_price + "/check-in";
            this.itemCart.purqty = numDays + 1;
            this.itemCart.totalCartPrice =
              parseFloat(res.room_price) * (numDays + 1);
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
              numdays: 0,
              totalguest: 0,
              totalpax: 0,
              currentroom: this.itemCart.name,
            };
            // Make a POST request to the API to save the data
            await axios
              .post(this.API_URL + "transaction/item/", data)
              .then((response) => {
                // Log a success message to the console
                this.itemCart = {};
                this.itemCart.id = response.data.id;
                this.itemCart.name = response.data.itemName;
                this.itemCart.type = response.data.itemType;
                this.itemCart.priceRate = response.data.itemPriceRate;
                this.itemCart.purqty = response.data.purchaseQty;
                this.itemCart.totalCartPrice = response.data.totalCost;
                this.itemCart.category = response.data.category;
                this.itemCart.itemOption = response.data.itemOption;
                this.itemCart.groupkey = response.data.groupkey;
                this.itemCart.guestinfo = response.data.guestinfo;
                this.cart.push(this.itemCart);
              })
              .catch((error) => {
                // Log an error message to the console
                console.error("Error saving data:", error);
              });
          });
        } else {
          const numDays = Math.ceil(
            (new Date(
              item.checkoutDate.split("/")[2] +
              "-" +
              item.checkoutDate.split("/")[1] +
              "-" +
              item.checkoutDate.split("/")[0]
            ).setHours(0, 0, 0, 0) -
              new Date(
                item.checkinDate.split("/")[2] +
                "-" +
                item.checkinDate.split("/")[1] +
                "-" +
                item.checkinDate.split("/")[0]
              ).setHours(0, 0, 0, 0)) /
            (1000 * 60 * 60 * 24)
          );
          this.itemCart.id = this.cart.length + 1;
          this.itemCart.name = item.room_name;
          this.itemCart.type = item.room_type;
          this.itemCart.priceRate = item.room_price + "/check-in";
          this.itemCart.purqty = numDays + 1;
          this.itemCart.totalCartPrice =
            parseFloat(item.room_price) * (numDays + 1);
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
            numdays: 0,
            totalguest: 0,
            totalpax: 0,
            currentroom: this.itemCart.name,
            dateCreated: new Date(), // Set the dateCreated field to the current date and time
          };
          // Make a POST request to the API to save the data
          await axios
            .post(this.API_URL + "transaction/item/", data)
            .then((response) => {
              // Log a success message to the console
              console.log("Data saved:", response.data);
            })
            .catch((error) => {
              // Log an error message to the console
              console.error("Error saving data:", error);
            });
          this.cart.push(this.itemCart);
        }
      } else {
        //show instead
        //update this.cart
        this.cart = [];
        if (groupbookings.length > 0) {
          const response = await axios.post(
            `${this.API_URL}transaction/item/filter/`,
            [{ columnName: "groupkey", columnKey: gkey }]
          );
          response.data.forEach((item) => {
            let newItem = {
              id: item.id,
              bookingID: item.bookingID,
              groupkey: item.groupkey,
              name: item.itemName,
              type: item.itemType,
              priceRate: item.itemPriceRate,
              purqty: item.purchaseQty,
              totalCartPrice: item.totalCost,
              category: item.category,
              itemOption: item.itemOption,
              numdays: item.numdays,
              totalguest: item.totalguest,
              totalpax: item.totalpax,
              currentroom: item.currentroom,
            };
            this.cart.push(newItem);
          });
        } else {
          //starthere
          const response = await axios.post(
            `${this.API_URL}transaction/item/filter/`,
            [{ columnName: "bookingID", columnKey: bookingID }]
          );
          if (response.data.length > 0) {
            try {
              response.data.forEach((item) => {
                let newItem = {
                  id: item.id,
                  bookingID: item.bookingID,
                  groupkey: item.groupkey,
                  name: item.itemName,
                  type: item.itemType,
                  priceRate: item.itemPriceRate,
                  purqty: item.purchaseQty,
                  totalCartPrice: item.totalCost,
                  category: item.category,
                  itemOption: item.itemOption,
                  numdays: item.numdays,
                  totalguest: item.totalguest,
                  totalpax: item.totalpax,
                  currentroom: item.currentroom,
                  guestinfo: item.guestinfo,
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
        this.newbillingbalance = existingTransaction.data[0].balance;
        this.isItNew = true;
        if (
          (existingTransaction.data[0].payStatus === "full" ||
            parseFloat(existingTransaction.data[0].balance) === 0) &&
          this.bookings[this.itemIndex].status !== "checkedin" &&
          this.bookings[this.itemIndex].status !== "checkedout" &&
          this.bookings[this.itemIndex].isPaid !== "yes"
        ) {
          this.bookings[this.itemIndex].isPaid = "yes";
          this.updateBookings(this.bookings[this.itemIndex].id);
          this.populateCalendarItems();
          this.toggleItemModal();
          this.movetocartFlag = true;
          this.activeAccountFlag = true;
          this.$swal
            .fire({
              icon: "info",
              title: "Payment status for the reservation has been modified!",
              message: "A change in the transaction was noticed by the system.",
              confirmButtonText: "Understood",
            })
            .then((result) => {
              return false;
            });
          return false;
        }
      } else {
        this.billing.bookingID = "";
      }
      try {
        this.partialPayment =
          groupbookings.length === 0
            ? item.partialPayment
            : transaction.cashAmountPay;
        const response = await axios.post(
          `${this.API_URL}transaction/record/filter/`,
          [{ columnName: "transaction", columnKey: transaction.id }]
        );
        this.cashHistory = response.data;
        this.gbookingscount =
          groupbookings.length === 0 ? 1 : groupbookings.length;
      } catch (error) { }
      if (!this.movetocartFlag) {
        this.toggleItemModal();
      }
      $("#others-tab").tab("show");
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
      };
    },
    async cancelReservation() {
      this.$swal
        .fire({
          icon: "warning",
          title: "Are you sure?",
          text: "Are you sure you want to cancel this reservation?",
          confirmButtonText: "Yes",
          cancelButtonText: "No",
          showCancelButton: true,
        })
        .then(async (result) => {
          // Check if user confirmed the cancellation
          if (result.isConfirmed) {
            // Perform reservation cancellation logic here
            this.bookings[this.itemIndex].status = "cancelled";
            this.bookings[this.itemIndex].groupkey = null;
            this.bookings[this.itemIndex].cancellationDate = new Date();
            this.updateBookings(this.bookings[this.itemIndex].id);
            const existingTransactionItems = await axios.post(
              `${this.API_URL}transaction/item/filter/`,

              {
                columnName: "bookingID",
                columnKey: this.bookings[this.itemIndex].itemID,
              }
            );
            await axios.put(
              `${this.API_URL}transaction/item/${existingTransactionItems.data[0].id}/`,
              {
                bookingID: existingTransactionItems.data[0].bookingID,
                itemName: existingTransactionItems.data[0].itemName,
                itemType: existingTransactionItems.data[0].itemType,
                itemPriceRate: existingTransactionItems.data[0].itemPriceRate,
                purchaseQty: existingTransactionItems.data[0].purchaseQty,
                totalCost: existingTransactionItems.data[0].totalCost,
                category: existingTransactionItems.data[0].category,
                itemOption: existingTransactionItems.data[0].itemOption,
                totalguest: existingTransactionItems.data[0].totalguest,
                totalpax: existingTransactionItems.data[0].totalpax,
                currentroom: existingTransactionItems.data[0].currentroom,
                numdays: existingTransactionItems.data[0].numdays,
                guestinfo: existingTransactionItems.data[0].guestinfo,
                groupkey: null,
              }
            );
            this.changeItemColor("cancelled");
            this.actionRecorder(
              `record?type=cancel&bookingID=${this.bookings[this.itemIndex].itemID
              }&groupkey=${this.bookings[this.itemIndex].groupkey}`
            );
            this.taskRecord(
              `action:/cancel reservation/client:/${this.bookings[this.itemIndex].name
              }`
            );
            this.toggleItemModal();
            // Display success message using SweetAlert
            this.$swal
              .fire({
                icon: "success",
                title: "Reservation Canceled!",
                text: "The reservation has been canceled.",
                confirmButtonText: "OK",
              })
              .then((response) => {
                //document.location.reload();
              });
          }
        });
    },
    async refundPayment() {
      this.$swal
        .fire({
          title: "Authorization Required",
          input: "text",
          showCancelButton: true,
          allowOutsideClick: false,
          inputAttributes: {
            minlength: 6, // Minimum length of 3 characters
            maxlength: 24, // Maximum length of 24 characters
            autocomplete: "off",
            style: "text-security:disc; -webkit-text-security:disc;",
          },
          confirmButtonText: "Submit",
          cancelButtonText: "Cancel",
          inputPlaceholder: "Enter authorization code",
        })
        .then(async (result) => {
          if (result.isConfirmed) {
            const authorizationCode = result.value;
            // Validate the authorization code and perform necessary actions
            if (
              authorizationCode.toLowerCase() ===
              this.AUTHORIZATION_KEY.toLowerCase()
            ) {
              // Code is correct, proceed with the desired action
              const confirmMessage = "This action cannot be undone.";
              const result = await this.$swal.fire({
                title: "Are you sure to proceed for refund?",
                text: confirmMessage,
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Yes",
                cancelButtonText: "Cancel",
              });
              if (result.isConfirmed) {
                const countdownMessage =
                  'Refund will be processed in <span id="countdown">5</span> seconds. Do you want to cancel?';
                let countdownResult;
                countdownResult = await this.$swal.fire({
                  title: "Please wait",
                  html: countdownMessage,
                  icon: "info",
                  showCancelButton: true,
                  confirmButtonColor: "#3085d6",
                  cancelButtonColor: "#d33",
                  confirmButtonText: "Confirm now",
                  cancelButtonText: "Cancel",
                  didOpen: () => {
                    const countdownEl = document.querySelector("#countdown");
                    let count = 5;
                    const timerId = setInterval(() => {
                      countdownEl.textContent = count;
                      count--;
                      if (count < 0) {
                        clearInterval(timerId);
                        this.$swal.close();
                      }
                    }, 1000);
                  },
                });
                if (!countdownResult.isConfirmed) {
                  return;
                }
                this.processRefundPayment();
              }
            } else {
              // Code is incorrect, show an error message or take appropriate action
              this.$swal.fire({
                icon: "error",
                title: "Incorrect Passcode",
                text: "The entered passcode is incorrect. Please try again.",
                allowOutsideClick: false,
              });
            }
          }
        });
    },
    async processRefundPayment() {
      const trans_id = this.billing.bookingID;
      this.bookings[this.itemIndex].partialPayment =
        parseFloat(this.bookings[this.itemIndex].partialPayment) +
        parseFloat(this.newbillingbalance);
      this.updateBookings(this.bookings[this.itemIndex].id);

      await axios
        .get(this.API_URL + `transaction/${trans_id}/`)
        .then(async (response) => {
          const transactionData = {
            clientname: response.data.clientname,
            clientemail: response.data.clientemail,
            clientcontact: response.data.clientcontact,
            clientaddress: response.data.clientaddress,
            clientnationality: response.data.clientnationality,
            clientType: response.data.clientType,
            nonCashReference: response.data.nonCashReference,
            totalAmountToPay: response.data.totalAmountToPay,
            paymentMethod: response.data.paymentMethod,
            cashAmountPay: response.data.cashAmountPay,
            balance: 0,
            payStatus: response.data.payStatus,
            discountMode: response.data.discountMode,
            discountValue: response.data.discountValue,
            bookingID: response.data.bookingID,
            processedBy: this.userdata.fName + " " + this.userdata.lName,
            groupkey: response.data.groupkey,
            cashRemarks: response.data.cashRemarks,
          };

          let doneTransaction = await axios.put(
            this.API_URL + `transaction/${trans_id}/`,
            transactionData
          );

          let transactionRecordData = {
            transaction: doneTransaction.data.id,
            transaction_date: doneTransaction.data.transaction_date,
            paymentMethod: doneTransaction.data.paymentMethod,
            nonCashReference: doneTransaction.data.nonCashReference,
            totalAmountToPay: doneTransaction.data.totalAmountToPay,
            cashAmountPay: parseFloat(this.newbillingbalance),
            balance: doneTransaction.data.balance,
            discountMode: doneTransaction.data.discountMode,
            discountValue: doneTransaction.data.discountValue,
            processedBy: this.userdata.fName + " " + this.userdata.lName,
            payStatus: doneTransaction.data.payStatus,
          };
          await axios.post(
            `${this.API_URL}transaction/record/`,
            transactionRecordData
          );

          this.$swal
            .fire({
              icon: "success",
              title: "Success!",
              text: "Refund has been processed successfully.",
              confirmButtonText: "OK",
            })
            .then((response) => {
              this.taskRecord(
                `action:/refunded guest/client:/${transactionData.clientname}`
              );
              document.location.reload();
            });
        });
    },
    async addRoom() {
      if (this.booksearchtext !== "") {
        this.$swal.fire({
          icon: "error",
          title: "Add room Restricted",
          text: "Unable to transfer when the search query is not empty.",
          confirmButtonText: "OK",
        });
        this.toggleItemModal();
        return;
      }
      if (this.toggleselect2 === false) {
        this.reservation.roomName = "";
        this.toggleselect2 = true;
        this.toggleselect = true;
        this.notoggle = false;
        this.roomSelect = "ok";
        this.isCheckinToggle = true;
        this.isCheckoutToggle = true;
        this.reservation.checkinDate = parseDateOrig(
          this.bookings[this.itemIndex].checkinDate
        );
        this.reservation.checkoutDate = parseDateOrig(
          this.bookings[this.itemIndex].checkoutDate
        );
      } else {
        const checkin = parseDate(this.reservation.checkinDate);
        const checkout = parseDate(this.reservation.checkoutDate);
        if (checkout < checkin) {
          this.$swal.fire({
            title: "error",
            text: "Check-out date ≥ Check-in date.",
            icon: "error",
          });
          return false;
        }
        this.bookNowFlag = false;
        const room = this.reservation.roomName;
        if (room.name === undefined) {
          return;
        }
        const newroom = {
          name: room.name,
          type: room.type,
          price: room.price,
        };
        const item = this.bookings[this.itemIndex];
        const pax = this.rooms.filter((o) => o.name === newroom.name)[0].pax;
        const result = await this.$swal.fire({
          icon: "warning",
          title: "Are you sure?",
          text: "Are you sure you want to add " + newroom.name + "?",
          confirmButtonText: "Yes",
          cancelButtonText: "No",
          showCancelButton: true,
        });
        if (!result.isConfirmed) {
          return;
        }
        const existingTransactionItems = await axios.post(
          `${this.API_URL}transaction/item/filter/`,
          [
            {
              columnName: "bookingID",
              columnKey: item.itemID,
            },
            {
              columnName: "itemOption",
              columnKey: "room",
            },
          ]
        );
        let id =
          "e" + new Date().getTime().toString() + this.generateUniqueString();
        let title = newroom.name + "-" + this.reservation.clientName;

        const numDays = Math.ceil(
          (new Date(
            formatDate2(this.reservation.checkoutDate).split("/")[2] +
            "-" +
            formatDate2(this.reservation.checkoutDate).split("/")[1] +
            "-" +
            formatDate2(this.reservation.checkoutDate).split("/")[0]
          ).setHours(0, 0, 0, 0) -
            new Date(
              formatDate2(this.reservation.checkinDate).split("/")[2] +
              "-" +
              formatDate2(this.reservation.checkinDate).split("/")[1] +
              "-" +
              formatDate2(this.reservation.checkinDate).split("/")[0]
            ).setHours(0, 0, 0, 0)) /
          (1000 * 60 * 60 * 24)
        );
        let gkey = existingTransactionItems.data[0].groupkey;
        if (
          existingTransactionItems.data[0].groupkey === null ||
          existingTransactionItems.data[0].groupkey === ""
        ) {
          gkey = "group-" + this.generateUniqueString();
          item.groupkey = gkey;
          this.updateBookings(item.id);

          await axios.put(
            `${this.API_URL}transaction/item/${existingTransactionItems.data[0].id}/`,
            {
              bookingID: existingTransactionItems.data[0].bookingID,
              itemName: existingTransactionItems.data[0].itemName,
              itemType: existingTransactionItems.data[0].itemType,
              itemPriceRate: existingTransactionItems.data[0].itemPriceRate,
              purchaseQty: existingTransactionItems.data[0].purchaseQty,
              totalCost: existingTransactionItems.data[0].totalCost,
              category: existingTransactionItems.data[0].category,
              itemOption: existingTransactionItems.data[0].itemOption,
              totalguest: existingTransactionItems.data[0].totalguest,
              totalpax: existingTransactionItems.data[0].totalpax,
              currentroom: existingTransactionItems.data[0].currentroom,
              numdays: existingTransactionItems.data[0].numdays,
              guestinfo: existingTransactionItems.data[0].guestinfo,
              groupkey: gkey,
            }
          );
        }
        await axios
          .post(this.API_URL + "bookings/", {
            itemID: id,
            status: "reserved",
            name: this.reservation.clientName,
            clientemail: this.reservation.clientEmail,
            clientaddress: this.reservation.clientAddress,
            clientnationality: this.reservation.clientNationality,
            clientType: this.reservation.clientType,
            checkinDate: formatDate2(this.reservation.checkinDate),
            checkoutDate: formatDate2(this.reservation.checkoutDate),
            room_name: newroom.name,
            room_price: newroom.price,
            room_type: newroom.type,
            remarks: "",
            contactNumber: this.reservation.clientPhone,
            isPaid: this.reservation.isPaid,
            created_at: moment().format("YYYY-MM-DD hh:mm:ss"),
            totalPrice: (numDays + 1) * parseFloat(newroom.price),
            partialPayment: 0,
            processedBy: this.userdata.fName + " " + this.userdata.lName,
            groupkey: gkey,
          })
          .then(async (response) => {
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
              room_name: newroom.name,
              room_price: newroom.price,
              room_type: newroom.type,
              remarks: "",
              contactNumber: this.reservation.clientPhone,
              isPaid: "no",
              created_at: moment().format("YYYY-MM-DD hh:mm:ss"),
              totalPrice: (numDays + 1) * parseFloat(newroom.price),
              partialPayment: 0,
              // numguests: this.reservation.numguests,
              processedBy: this.userdata.fName + " " + this.userdata.lName,
              groupkey: gkey,
            });
            await axios
              .post(`${this.API_URL}transaction/item/`, {
                bookingID: id,
                itemName: newroom.name,
                itemType: newroom.type,
                itemPriceRate: newroom.price + "/check-in",
                purchaseQty: numDays + 1,
                totalCost: parseFloat(newroom.price) * (numDays + 1),
                category: "main",
                itemOption: "room",
                totalguest: 0,
                totalpax: pax,
                currentroom: newroom.name,
                numdays: numDays + 1,
                guestinfo: "",
                groupkey: gkey,
                dateCreated: new Date(),
              })
              .then(async (response) => {
                this.actionRecorder(
                  `record?type=book&bookingID=${id}&groupkey=${gkey}`
                );
                this.taskRecord(
                  `action:/added reservation/client:/${this.reservation.clientName}/`
                );
                this.toggleItemModal();
                this.bookNowFlag = true;
                this.toggleselect = false;
                this.toggleselect2 = false;
                this.notoggle = false;
                this.roomSelect = "no";
                this.$swal.fire({
                  title: "Success!",
                  text: "Successfully added a room!",
                  icon: "success",
                });
              });
          });
      }
    },
    async transferRoom() {
      if (this.booksearchtext !== "") {
        this.$swal.fire({
          icon: "error",
          title: "Transfer Restricted",
          text: "Unable to transfer when the search query is not empty.",
          confirmButtonText: "OK",
        });
        this.toggleItemModal();
        return;
      }
      if (this.toggleselect === false) {
        this.reservation.roomName = "";
        this.toggleselect = true;
        this.roomSelect = "ok";
      } else {
        this.bookNowFlag = false;
        const item = this.bookings[this.itemIndex];
        const room = this.reservation.roomName;
        if (room.name === undefined) {
          return;
        }
        const oldroom = {
          name: this.bookings[this.itemIndex].room_name,
          type: this.bookings[this.itemIndex].room_type,
          price: this.bookings[this.itemIndex].room_price,
        };
        const newroom = {
          name: room.name,
          type: room.type,
          price: room.price,
        };
        const pax = this.rooms.filter((o) => o.name === newroom.name)[0].pax;
        const roomprice = this.items.filter(
          (o) => o.item === "Room Guest" && o.type.toLowerCase() === "entrance"
        )[0].priceRate;
        const result = await this.$swal.fire({
          icon: "warning",
          title: "Are you sure?",
          text:
            "Are you sure you want to transfer from " +
            oldroom.name +
            " to " +
            newroom.name +
            "?",
          confirmButtonText: "Yes",
          cancelButtonText: "No",
          showCancelButton: true,
        });
        if (!result.isConfirmed) {
          return;
        }
        item.room_name = newroom.name;
        item.room_price = newroom.price;
        item.room_type = newroom.type;
        item.remarks =
          item.remarks +
          "\n" +
          "transferred from: " +
          oldroom.name +
          " on " +
          formatDate();
        this.updateBookings(item.id);
        const existingTransactionItems = await axios.post(
          `${this.API_URL}transaction/item/filter/`,
          {
            columnName: "bookingID",
            columnKey: item.itemID,
          }
        );
        try {
          for (const o of existingTransactionItems.data) {
            await axios.put(`${this.API_URL}transaction/item/${o.id}/`, {
              bookingID: o.bookingID,
              itemName: o.itemOption === "room" ? newroom.name : o.itemName,
              itemType: o.itemOption === "room" ? newroom.type : o.itemType,
              itemPriceRate:
                o.itemOption === "room"
                  ? newroom.price + "/" + o.itemPriceRate.split("/")[1].trim()
                  : o.itemPriceRate,
              purchaseQty: o.purchaseQty,
              totalCost:
                o.itemOption === "room"
                  ? parseFloat(newroom.price) * parseFloat(o.purchaseQty)
                  : o.itemType.toLowerCase() === "entrance"
                    ? roomprice * o.numdays * o.purchaseQty
                    : o.totalCost,
              category:
                o.itemType.toLowerCase() === "entrance"
                  ? "inclusion"
                  : o.category,
              itemOption: o.itemOption,
              totalguest: o.totalguest,
              totalpax:
                o.itemOption === "room" ||
                  o.itemType.toLowerCase() === "entrance"
                  ? pax
                  : o.totalpax,
              currentroom: newroom.name,
              numdays: o.numdays,
              guestinfo: o.guestinfo,
            });
          }
        } catch (error) {
          console.error(error);
        }
        this.toggleItemModal();
        this.actionRecorder(
          `record?type=transfer&bookingID=${item.itemID}&groupkey=${item.groupkey}&remarks=from ${oldroom.name} to ${newroom.name}`
        );
        this.taskRecord(`action:/transfer guest/client:/${item.name}`);
        this.bookNowFlag = true;
        this.$swal
          .fire({
            icon: "success",
            title: "Room Transfer",
            text: "Room transferred successfully.",
            confirmButtonText: "OK",
          })
          .then((response) => { });
      }
    },
    async extendBooking() {
      if (this.booksearchtext !== "") {
        this.$swal.fire({
          icon: "error",
          title: "Extend booking Restricted",
          text: "Unable to extend when the search query is not empty.",
          confirmButtonText: "OK",
        });
        this.toggleItemModal();
        return;
      }
      const result = await this.$swal.fire({
        icon: "warning",
        title: "Are you sure?",
        text: "Are you sure you want to extend this guest?",
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        showCancelButton: true,
      });
      if (!result.isConfirmed) {
        this.toggleItemModal();
        return;
      }
      const item = this.bookings[this.itemIndex];
      const bId = item.id;
      const bookingID = item.itemID;
      const groupkey = item.groupkey || "";
      const roomPrice = parseFloat(item.room_price);
      let groupbookings = [];
      let existingTransactionItems = [];

      existingTransactionItems = await axios.post(
        `${this.API_URL}transaction/item/filter/`,
        {
          columnName: "bookingID",
          columnKey: bookingID,
        }
      );
      const itemCheckout = new Date(
        parseDate(this.bookings[this.itemIndex].checkoutDate)
      );
      const extendItemCheckout = new Date(
        itemCheckout.setDate(itemCheckout.getDate() + 1)
      );
      const newCheckoutString = extendItemCheckout.toLocaleDateString("en-GB");
      const newTotalPrice =
        parseFloat(this.bookings[this.itemIndex].totalPrice) +
        parseFloat(this.bookings[this.itemIndex].room_price);
      this.bookings[this.itemIndex].checkoutDate = newCheckoutString;
      this.bookings[this.itemIndex].isPaid = "partial";
      this.bookings[this.itemIndex].totalPrice = newTotalPrice;
      this.updateBookings(bId);

      existingTransactionItems.data
        .filter(
          (o) =>
            o.bookingID === this.bookings[this.itemIndex].itemID &&
            (o.itemOption === "room" || o.itemType.toLowerCase() === "entrance")
        )
        .forEach(async (item) => {
          try {
            const numdays = item.purchaseQty;
            await axios.put(`${this.API_URL}transaction/item/${item.id}/`, {
              bookingID: item.bookingID,
              itemName: item.itemName,
              itemType: item.itemType,
              itemPriceRate: item.itemPriceRate,
              purchaseQty:
                item.itemOption === "room"
                  ? item.purchaseQty + 1
                  : item.purchaseQty,
              totalCost:
                item.itemOption === "room"
                  ? (item.purchaseQty + 1) *
                  parseFloat(item.itemPriceRate.split("/")[0])
                  : item.itemType.toLowerCase() === "entrance"
                    ? (item.numdays + 1) *
                    (item.totalguest - item.totalpax) *
                    parseFloat(item.itemPriceRate.split("/")[0])
                    : item.totalCost,
              category: item.category,
              itemOption: item.itemOption,
              dateCreated: new Date(), // Set the dateCreated field to the current date and time
              numdays:
                item.itemType.toLowerCase() === "entrance" ||
                  item.itemOption === "room"
                  ? item.numdays + 1
                  : item.numdays,
              totalguest: item.totalguest,
              totalpax: item.totalpax,
              currentroom: item.currentroom,
            });
          } catch (error) { }
        });
      this.actionRecorder(
        `record?type=extend&bookingID=${this.bookings[this.itemIndex].itemID
        }&groupkey=${this.bookings[this.itemIndex].groupkey}`
      );
      this.taskRecord(
        `action:/extend guest/client:/${this.bookings[this.itemIndex].name}`
      );
      // this.updateBookings(this.bookings[bId].id);
      this.toggleItemModal();
      this.$swal
        .fire({
          icon: "success",
          title: "Guest Extended!",
          text: "Thank you for extending the guest.",
          confirmButtonText: "OK",
        })
        .then((response) => { });
    },
    checkinGuest() {
      this.toggleItemModal();
      this.$swal
        .fire({
          icon: "warning",
          title: "Are you sure?",
          text: "Are you sure you want to check in this guest?",
          confirmButtonText: "Yes",
          cancelButtonText: "No",
          showCancelButton: true,
        })
        .then((result) => {
          if (result.isConfirmed) {
            axios
              .post(`${this.API_URL}rooms/filter/`, [
                {
                  columnName: "name",
                  columnKey: this.bookings[this.itemIndex].room_name,
                },
              ])
              .then((response) => {
                const status = response.data[0].status;
                const category = response.data[0].type;
                if (status === "dirty" && category.includes("room")) {
                  this.$swal({
                    title: "Error!",
                    text: "Uncleaned room, not ready for check-in. Contact housekeeping first.",
                    icon: "error",
                  }).then((result) => {
                    this.toggleItemModal();
                    return;
                  });
                } else {
                  const item = this.bookings[this.itemIndex];
                  item.remarks = this.reservation.remarks;
                  item.status = "checkedin";
                  this.updateBookings(item.id);
                  this.populateCalendarItems();
                  //this.changeItemColor("checkedin");
                  this.actionRecorder(
                    `record?type=checkin&bookingID=${item.itemID}&groupkey=${item.groupkey}`
                  );
                  this.taskRecord(
                    `action:/checked-in guest/client:/${item.name}`
                  );
                  this.$swal
                    .fire({
                      icon: "success",
                      title: "Guest Checked In!",
                      text: "Thank you for checking in the guest.",
                      confirmButtonText: "OK",
                    })
                    .then((response) => {
                      //document.location.reload();
                    });
                }
              });
          }
        });
    },
    earlycheckOutGuest() {
      this.toggleItemModal();
      this.$swal
        .fire({
          icon: "warning",
          title: "Are you sure?",
          text: "Are you sure you want to check out this guest earlier?",
          confirmButtonText: "Yes",
          cancelButtonText: "No",
          showCancelButton: true,
        })
        .then((result) => {
          // Check if user confirmed the cancellation
          if (result.isConfirmed) {
            // Perform reservation cancellation logic here
            axios
              .post(`${this.API_URL}restoorders/filter/`, [
                {
                  columnName: "customer_name",
                  columnKey: this.bookings[this.itemIndex].room_name,
                },
                { columnName: "status", columnKey: "progress" },
              ])
              .then((response) => {
                let checkTable = null;
                let restoStatus = null;
                try {
                  const tableID = response.data[0].table_id;
                  restoStatus = response.data[0].status;
                  checkTable = this.rooms.find(
                    (table) => table.id === tableID
                  ).name;
                } catch (error) {
                  checkTable = this.bookings[this.itemIndex].room_name;
                  restoStatus = "closed";
                }
                if (checkTable === this.bookings[this.itemIndex].room_name) {
                  if (restoStatus !== "closed") {
                    this.$swal.fire({
                      icon: "error",
                      title: "Customer Checkout Restricted",
                      text: "Customer has outstanding payables in the restaurant; cannot be checked out yet!",
                      confirmButtonText: "OK",
                    });
                    return;
                  } else {
                    let roomId = -1;
                    axios
                      .post(`${this.API_URL}rooms/filter/`, [
                        {
                          columnName: "name",
                          columnKey: this.bookings[this.itemIndex].room_name,
                        },
                      ])
                      .then((response) => {
                        roomId = response.data[0].id;
                        axios
                          .put(`${this.API_URL}rooms/${roomId}/`, {
                            name: response.data[0].name,
                            type: response.data[0].type,
                            price: response.data[0].price,
                            isAvailable: response.data[0].isAvailable,
                            status: "dirty",
                          })
                          .then((response) => {
                            let today = new Date();
                            this.bookings[this.itemIndex].checkoutDate =
                              formatDate2(today);
                            this.bookings[this.itemIndex].status = "checkedout";
                            this.bookings[this.itemIndex].actualCheckoutDate =
                              new Date();
                            this.reservation.status = "vacant";
                            this.updateBookings(
                              this.bookings[this.itemIndex].id
                            );
                            this.populateCalendarItems();
                            //this.changeItemColor("checkedout");
                            this.actionRecorder(
                              `record?type=earlycheckout&bookingID=${this.bookings[this.itemIndex].itemID
                              }&groupkey=${this.bookings[this.itemIndex].groupkey
                              }`
                            );
                            this.taskRecord(
                              `action:/earlychecked-out guest/client:/${this.bookings[this.itemIndex].name
                              }`
                            );
                            // Display success message using SweetAlert
                            this.$swal
                              .fire({
                                icon: "success",
                                title: "Guest Checked Out!",
                                text: "The guest has been checked out.",
                                confirmButtonText: "OK",
                              })
                              .then((response) => {
                                //document.location.reload();
                              });
                          });
                      });
                  }
                }
              });
          }
        });
    },
    checkOutGuest() {
      this.toggleItemModal();
      this.$swal
        .fire({
          icon: "warning",
          title: "Are you sure?",
          text: "Are you sure you want to check out this guest?",
          confirmButtonText: "Yes",
          cancelButtonText: "No",
          showCancelButton: true,
        })
        .then((result) => {
          // Check if user confirmed the cancellation
          if (result.isConfirmed) {
            // Perform reservation cancellation logic here
            axios
              .post(`${this.API_URL}restoorders/filter/`, [
                {
                  columnName: "customer_name",
                  columnKey: this.bookings[this.itemIndex].room_name,
                },
                { columnName: "status", columnKey: "progress" },
              ])
              .then((response) => {
                let checkTable = null;
                let restoStatus = null;
                try {
                  const tableID = response.data[0].table_id;
                  restoStatus = response.data[0].status;
                  checkTable = this.rooms.find(
                    (table) => table.id === tableID
                  ).name;
                } catch (error) {
                  checkTable = this.bookings[this.itemIndex].room_name;
                  restoStatus = "closed";
                }
                if (checkTable === this.bookings[this.itemIndex].room_name) {
                  if (restoStatus !== "closed") {
                    this.$swal.fire({
                      icon: "error",
                      title: "Customer Checkout Restricted",
                      text: "Customer has outstanding payables in the restaurant; cannot be checked out yet!",
                      confirmButtonText: "OK",
                    });
                    return;
                  } else {
                    let roomId = -1;
                    axios
                      .post(`${this.API_URL}rooms/filter/`, [
                        {
                          columnName: "name",
                          columnKey: this.bookings[this.itemIndex].room_name,
                        },
                      ])
                      .then((response) => {
                        roomId = response.data[0].id;
                        axios
                          .put(`${this.API_URL}rooms/${roomId}/`, {
                            name: response.data[0].name,
                            type: response.data[0].type,
                            price: response.data[0].price,
                            isAvailable: response.data[0].isAvailable,
                            status: "dirty",
                          })
                          .then((response) => {
                            this.bookings[this.itemIndex].status = "checkedout";
                            this.bookings[this.itemIndex].actualCheckoutDate =
                              new Date();
                            this.reservation.status = "vacant";
                            this.updateBookings(
                              this.bookings[this.itemIndex].id
                            );
                            this.populateCalendarItems();
                            //this.changeItemColor("checkedout");
                            this.actionRecorder(
                              `record?type=checkout&bookingID=${this.bookings[this.itemIndex].itemID
                              }&groupkey=${this.bookings[this.itemIndex].groupkey
                              }`
                            );
                            this.taskRecord(
                              `action:/checked-out guest/client:/${this.bookings[this.itemIndex].name
                              }`
                            );
                            // Display success message using SweetAlert
                            this.$swal
                              .fire({
                                icon: "success",
                                title: "Guest Checked Out!",
                                text: "The guest has been checked out.",
                                confirmButtonText: "OK",
                              })
                              .then((response) => {
                                //document.location.reload();
                              });
                          });
                      });
                  }
                }
              });
          }
        });
    },
    //methods for calendar items
    periodChanged(range) {
      this.periodStart = parseDateOrig2(
        range._value.displayFirstDate._value.toLocaleDateString()
      );
      this.periodEnd = parseDateOrig2(
        range._value.displayLastDate._value.toLocaleDateString()
      );
    },
    thisMonth(d, h, m) {
      const t = new Date();
      return new Date(t.getFullYear(), t.getMonth(), d, h || 0, m || 0);
    },
    clickDay() {
      let today = new Date();
      if (this.dayreserve.setHours(0, 0, 0, 0) >= today.setHours(0, 0, 0, 0)) {
        this.selectionStart = this.dayreserve;
        this.selectionEnd = this.dayreserve;
        this.toggledayMenuModal();
        this.toggleItemModal();
        this.toggleselect = false;
        this.toggleselect2 = false;
        this.notoggle = true;
        this.newtoggle = false;
        this.roomSelect = "ok";
        this.bookalltoggle = false;
        this.reservation.clientName = "";
        this.reservation.clientEmail = "";
        this.reservation.clientAddress = "";
        // this.$refs.address1Field.value = "";
        this.isCheckinToggle = false;
        this.isCheckoutToggle = false;
        this.simulCtrl = false;
        this.reservation.clientNationality = "Filipino";
        this.reservation.clientType = "in-house";
        this.reservation.roomName = "";
        this.reservation.remarks = "";
        this.filteredhistlogs = [];
        // this.reservation.numguests = "";
        this.reservation.clientPhone = "";
        // this.reservation.checkinDate =
        //   this.dayreserve.toLocaleDateString("en-GB");
        // this.reservation.checkoutDate =
        //   this.dayreserve.toLocaleDateString("en-GB");
        this.reservation.status = "vacant";
      }
    },
    viewAllReservation() {
      this.convDate = this.dayreserve.toLocaleDateString("en-GB");
      this.toggledayMenuModal();
      this.toggleShowAllModal();
    },
    onClickDay(d) {
      if (this.calendarItems.length === 0) {
        return false;
      }
      if (this.booksearchtext !== "") {
        this.$swal.fire({
          icon: "error",
          title: "Calendar Day Selection Restricted",
          text: "Unable to select a day on the calendar when the search query is not empty.",
          confirmButtonText: "OK",
        });
        return;
      }
      this.dayreserve = d;
      this.selectionStart = d;
      this.selectionEnd = d;
      this.reservation.checkinDate = d.toLocaleDateString("en-GB");
      this.reservation.checkoutDate = d.toLocaleDateString("en-GB");
      this.roomSelect = "ok";
      this.toggledayMenuModal();
    },
    onClickItem(e) {
      // if (this.booksearchtext !== "") {
      //   this.$swal.fire({
      //     icon: "error",
      //     title: "Calendar Item Selection Restricted",
      //     text: "Unable to select an item on the calendar when the search query is not empty.",
      //     confirmButtonText: "OK",
      //   });
      //   return;
      // }
      this.itemIndex = this.bookings.findIndex((o) => o.itemID === e.id);
      this.showReservation();
    },
    viewBooking(id) {
      this.itemIndex = this.bookings.findIndex((o) => o.id === id);
      this.showReservation();
    },
    showReservation() {
      this.isCheckinToggle = false;
      this.isCheckoutToggle = false;
      this.simulCtrl = false;
      this.toggleselect = false;
      this.toggleselect2 = false;
      this.bookalltoggle = false;
      this.notoggle = false;
      this.newtoggle = false;
      this.roomSelect = "ok";
      this.reservation.clientName = this.bookings[this.itemIndex].name;
      this.reservation.clientEmail = this.bookings[this.itemIndex].clientemail;
      this.reservation.clientAddress =
        this.bookings[this.itemIndex].clientaddress;
      // this.$refs.address1Field.value = this.reservation.clientAddress;
      this.reservation.clientNationality =
        this.bookings[this.itemIndex].clientnationality;
      this.reservation.clientType = this.bookings[this.itemIndex].clientType;
      this.reservation.checkinDate = this.bookings[this.itemIndex].checkinDate;
      //   const checkoutdate = new Date(
      //     parseDate(this.bookings[this.itemIndex].checkoutDate)
      //   );
      //   checkoutdate.setDate(checkoutdate.getDate() + 1);
      //   this.reservation.checkoutDate = formatDate2(checkoutdate);
      this.reservation.checkoutDate =
        this.bookings[this.itemIndex].checkoutDate;
      this.reservation.roomName = this.bookings[this.itemIndex].room_name;
      this.reservation.remarks = this.bookings[this.itemIndex].remarks;
      this.reservation.clientPhone =
        this.bookings[this.itemIndex].contactNumber;
      this.reservation.status = this.bookings[this.itemIndex].status;
      this.reservation.isPaid = this.bookings[this.itemIndex].isPaid;
      // this.reservation.numguests = this.bookings[this.itemIndex].numguests;

      this.filteredhistlogs = this.histlogs
        .filter(
          (o) =>
            o.task.includes("record?type=") &&
            o.task.includes(this.bookings[this.itemIndex].itemID)
        )
        .map((o) => {
          const comp = o.task.replace("record?", "").split("&");
          const result = {};
          for (const pair of comp) {
            const [key, value] = pair.split("=");
            result[key] = value;
          }
          const type = result.type;
          const actor = o.actor;
          const details = result.remarks;
          const date = formatDate3(new Date(o.date_created));
          return {
            type,
            actor,
            details,
            date,
          };
        });
      this.toggleItemModal();
    },
    setShowDate(d) {
      this.message = `Changing calendar view to ${d.toLocaleDateString()}`;
      this.showDate = d;
    },
    setSelection(dateRange) {
      this.selectionEnd = dateRange[1];
      this.selectionStart = dateRange[0];
    },
    finishSelection(dateRange) {
      const currentDate = new Date(); // get current date
      if (
        dateRange[0].setHours(0, 0, 0, 0) < currentDate.setHours(0, 0, 0, 0)
      ) {
        // check if start date is before current date
        // prompt user to select a valid start date
        return;
      }
      this.setSelection(dateRange);
      this.message = `You selected: ${this.selectionStart.toLocaleDateString()} -${this.selectionEnd.toLocaleDateString()}`;
      this.toggleselect = false;
      this.toggleselect2 = false;
      this.notoggle = false;
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
      this.reservation.checkinDate =
        this.selectionStart.toLocaleDateString("en-GB");
      this.reservation.checkoutDate =
        this.selectionEnd.toLocaleDateString("en-GB");
      //     const checkoutdate = new Date(
      //     parseDate(this.selectionEnd.toLocaleDateString("en-GB"))
      //   );
      //   checkoutdate.setDate(checkoutdate.getDate() + 1);
      //   this.reservation.checkoutDate = formatDate2(checkoutdate);
      this.toggledayMenuModal();
    },
    async onDrop(item, date) {
      if (this.booksearchtext !== "") {
        this.$swal.fire({
          icon: "error",
          title: "Calendar Item Selection Restricted",
          text: "Unable to select an item on the calendar when the search query is not empty.",
          confirmButtonText: "OK",
        });
        return;
      }
      const currentDate = new Date(); // get current date
      // if (date.setHours(0, 0, 0, 0) < currentDate.setHours(0, 0, 0, 0)) {
      //   // check if start date is before current date
      //   // prompt user to select a valid start date
      //   return;
      // }
      this.itemIndex = this.bookings.findIndex((o) => o.itemID === item.id);
      //issue in reloading
      const itemStatus = this.bookings[this.itemIndex].status;
      if (itemStatus === "reserved" || itemStatus === "checkedin") {
        const eLength = CalendarMath.dayDiff(item.startDate, date);
        let landingDateCheckin = CalendarMath.addDays(item.startDate, eLength);
        let landingDateCheckout = CalendarMath.addDays(item.endDate, eLength);
        const originalStart = item.startDate.toLocaleDateString("en-GB");
        const originalEnd = item.endDate.toLocaleDateString("en-GB");
        let filteredBookings = this.bookings.filter(
          (booking) =>
            (booking.status === "reserved" || booking.status === "checkedin") &&
            booking.itemID !== this.bookings[this.itemIndex].itemID &&
            booking.room_name === this.bookings[this.itemIndex].room_name &&
            new Date(
              booking.checkinDate.split("/")[2] +
              "-" +
              booking.checkinDate.split("/")[1] +
              "-" +
              booking.checkinDate.split("/")[0]
            ).setHours(0, 0, 0, 0) <=
            landingDateCheckout.setHours(0, 0, 0, 0) &&
            new Date(
              booking.checkoutDate.split("/")[2] +
              "-" +
              booking.checkoutDate.split("/")[1] +
              "-" +
              booking.checkoutDate.split("/")[0]
            ).setHours(0, 0, 0, 0) >= landingDateCheckin.setHours(0, 0, 0, 0)
        );
        if (filteredBookings.length === 0) {
          if (event.ctrlKey || this.simulCtrl) {
            let sd = CalendarMath.addDays(item.startDate, 0);
            let ed = CalendarMath.addDays(
              item.endDate,
              eLength - CalendarMath.dayDiff(item.startDate, item.endDate)
            );
            if (ed >= sd) {
              item.originalItem.startDate = sd;
              item.originalItem.endDate = ed;
            } else {
              item.originalItem.endDate = item.endDate;
              item.originalItem.startDate = ed;
            }
          } else {
            item.originalItem.startDate = CalendarMath.addDays(
              item.startDate,
              eLength
            );
            item.originalItem.endDate = CalendarMath.addDays(
              item.endDate,
              eLength
            );
          }
          if (this.draggedItem) {
            this.draggedItem[0].checkinDate =
              item.originalItem.startDate.toLocaleDateString("en-GB");
            this.draggedItem[0].checkoutDate =
              item.originalItem.endDate.toLocaleDateString("en-GB");
          } else {
            this.bookings[this.itemIndex].checkinDate =
              item.originalItem.startDate.toLocaleDateString("en-GB");
            this.bookings[this.itemIndex].checkoutDate =
              item.originalItem.endDate.toLocaleDateString("en-GB");
          }

          const numdays =
            (parseDate(this.bookings[this.itemIndex].checkoutDate) -
              parseDate(this.bookings[this.itemIndex].checkinDate)) /
            (1000 * 60 * 60 * 24);

          const response = await axios.post(
            this.API_URL + "transaction/item/filter/",
            {
              columnName: "bookingID",
              columnKey: this.bookings[this.itemIndex].itemID,
            }
          );

          for (const item of response.data.filter(
            (o) =>
              o.bookingID === this.bookings[this.itemIndex].itemID &&
              (o.itemOption === "room" ||
                o.itemType.toLowerCase() === "entrance")
          )) {
            const data = {
              bookingID: item.bookingID,
              itemName: item.itemName,
              itemType: item.itemType,
              itemPriceRate: item.itemPriceRate,
              purchaseQty:
                item.itemOption === "room" ? numdays + 1 : item.purchaseQty,
              totalCost:
                item.itemOption === "room"
                  ? (numdays + 1) * parseFloat(item.itemPriceRate.split("/")[0])
                  : (numdays + 1) *
                  (item.totalguest - item.totalpax) *
                  parseFloat(item.itemPriceRate.split("/")[0]),
              category: item.category,
              itemOption: item.itemOption,
              dateCreated: new Date(), // Set the dateCreated field to the current date and time
              numdays: numdays + 1,
              totalguest: item.totalguest,
              totalpax: item.totalpax,
              currentroom: item.currentroom,
            };
            await axios.put(
              this.API_URL + `transaction/item/${item.id}/`,
              data
            );
          }

          this.updateBookings(this.bookings[this.itemIndex].id);
          //this.reloadData();
          //this.populateCalendarItems();

          let newcheckoutdate = new Date(
            parseDate(this.bookings[this.itemIndex].checkoutDate)
          );
          newcheckoutdate.setDate(newcheckoutdate.getDate() + 1);
          newcheckoutdate = formatDate2(newcheckoutdate);

          let newcheckoutdate2 = new Date(parseDate(originalEnd));
          newcheckoutdate2.setDate(newcheckoutdate2.getDate() + 1);
          newcheckoutdate2 = formatDate2(newcheckoutdate2);

          this.actionRecorder(
            `record?type=changedate&bookingID=${this.bookings[this.itemIndex].itemID
            }&groupkey=${this.bookings[this.itemIndex].groupkey}&remarks=${originalStart === this.bookings[this.itemIndex].checkinDate
              ? ""
              : `Checkin date: from ${originalStart} to ${this.bookings[this.itemIndex].checkinDate
              }; `
            }${originalEnd === this.bookings[this.itemIndex].checkoutDate
              ? ""
              : `Checkout date: from ${newcheckoutdate2} to ${newcheckoutdate}`
            }`
          );

          this.taskRecord(
            `action:/adjust date reservation/client:/${this.bookings[this.itemIndex].name
            }`
          );
        } else {
          this.$swal.fire({
            icon: "error",
            title: "Cannot Adjust Reservation",
            text: "Dates conflict with an existing room reservation.",
            confirmButtonText: "OK",
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
      const STATUS_CLASSES = {
        reserved: {
          yes: "hotel-reserved",
          partial: "hotel-reserved",
          no: "hotel-reserved-unpaid",
          "": "hotel-reserved-unpaid",
        },
        checkedin: {
          yes: "hotel-checkedin-paid",
          partial: "hotel-checkedin-partial",
          no: "hotel-checkedin-unpaid",
          "": "hotel-checkedin-unpaid",
        },
        cancelled: {
          yes: "hotel-cancelled",
          partial: "hotel-cancelled",
          no: "hotel-cancelled",
          "": "hotel-cancelled",
        },
        checkedout: {
          yes: "hotel-checkedout",
          partial: "hotel-checkedout",
          no: "hotel-checkedout",
          "": "hotel-checkedout",
        },
      };

      this.calendarItems = this.bookings.map((booking) => {
        const {
          checkinDate,
          checkoutDate,
          room_name,
          groupkey,
          name,
          itemID,
          status,
          isPaid,
        } = booking;

        const startDate = parseDateOrig(checkinDate);
        const endDate = parseDateOrig(checkoutDate);
        const titlePrefix =
          groupkey === null ? "" : '<span class="text-white">group</span>-';
        const title = `${room_name}-${titlePrefix}${name}<span style="display:none">~${itemID}~</span>`;
        const tooltip = `${room_name}-${name}\n*${status}-${isPaidMapping(
          isPaid
        )}`;

        return {
          startDate,
          endDate,
          title,
          id: itemID,
          classes: [STATUS_CLASSES[status][isPaid]],
          tooltip,
        };
      });

      function isPaidMapping(paymentStatus) {
        switch (paymentStatus) {
          case "yes":
            return "fully paid";
          case "no":
            return "not paid";
          default:
            return "partial";
        }
      }
      setTimeout(function () {
        $(".currentPeriod").click();
      }, 2000);

      // let suggestionsArray = this.rooms.map((room) => room.name);
      // const roomStatus = ["cancelled", "reserved", "checkedin", "checkedout"];
      // suggestionsArray = roomStatus.concat(suggestionsArray);
      // // Filter the suggestions based on the search text
      // this.autosuggestions = suggestionsArray.filter((suggestion) =>
      //   suggestion.toLowerCase().includes(this.booksearchtext.toLowerCase())
      // );
      // this.autosuggestions = this.autosuggestions.slice(0, 15);
      // // this.showAutosuggestions = true;
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
      let randomString = "";
      while (randomString.length < 64) {
        randomString += Math.random().toString(36).substr(2, 36);
      }
      randomString = randomString.substr(0, 64);
      return randomString;
    },
    async clickTestAddItem() {
      // if (
      //   this.reservation.clientAddress === "" ||
      //   this.reservation.clientAddress === null
      // ) {
      //   this.$swal.fire({
      //     title: "error",
      //     text: "Please fill out the address field.",
      //     icon: "error",
      //   });
      //   this.$refs.address1Field.focus();
      //   return false;
      // }
      this.bookNowFlag = false;
      this.disablebutton = true;
      const checkin = parseDate(this.reservation.checkinDate);
      const checkout = parseDate(this.reservation.checkoutDate);
      if (checkout < checkin) {
        this.$swal.fire({
          title: "Booking Error",
          text: "The check-out date should be the same as or after the check-in date.",
          icon: "error",
        });
        this.newtoggle = false;
        this.bookNowFlag = true;
        this.toggleItemModal();
        return false;
      }
      if (checkin < new Date().setHours(0, 0, 0, 0)) {
        this.$swal.fire({
          title: "Booking Error",
          text: "Booking for past dates is not allowed.",
          icon: "error",
        });
        this.newtoggle = false;
        this.bookNowFlag = true;
        this.toggleItemModal();
        return false;
      }
      //   const initialResPax = this.reservation.roomName[0].pax;
      //   for (const res of this.reservation.roomName) {
      //     if (res.pax !== initialResPax) {
      //       await this.$swal.fire({
      //         icon: "error",
      //         title: "Booking Error",
      //         text: "It is not allowed to book multiple rooms with different pax.",
      //       });
      //       this.reservation.roomName = "";
      //       return;
      //     }
      //   }

      for (const res of this.reservation.roomName) {
        const hasExistingBooking = this.bookings
          .filter((item) => item.status !== "checkedout")
          .filter((item) => item.status !== "cancelled")
          .filter(
            (booking) =>
              booking.room_name === res.name &&
              booking.checkinDate === this.reservation.checkinDate
          );
        if (hasExistingBooking.length > 0) {
          await this.$swal.fire({
            icon: "error",
            title: "Booking Error",
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
        roomBooked.forEach(async (res) => {
          //change id format
          let id =
            "e" + new Date().getTime().toString() + this.generateUniqueString();
          let startDate = parseDateOrig(this.reservation.checkinDate);
          let endDate = parseDateOrig(this.reservation.checkoutDate);
          let title = res.name + "-" + this.reservation.clientName;
          let numDays = Math.ceil(
            (new Date(endDate).setHours(0, 0, 0, 0) -
              new Date(startDate).setHours(0, 0, 0, 0)) /
            (1000 * 60 * 60 * 24)
          );

          const roomPrice =
            this.rooms.findIndex((o) => o.name === res.name) !== -1
              ? this.rooms[this.rooms.findIndex((o) => o.name === res.name)]
                .price
              : 0;
          const roomType =
            this.rooms.findIndex((o) => o.name === res.name) !== -1
              ? this.rooms[this.rooms.findIndex((o) => o.name === res.name)]
                .type
              : "";
          const response = await axios.post(this.API_URL + "bookings/", {
            itemID: id,
            status: "reserved",
            name: this.reservation.clientName,
            clientemail: this.reservation.clientEmail,
            clientaddress: this.reservation.clientAddress,
            clientnationality: this.reservation.clientNationality,
            clientType: this.reservation.clientType,
            checkinDate: this.newtoggle
              ? formatDate2(this.reservation.checkinDate)
              : this.reservation.checkinDate,
            checkoutDate: this.newtoggle
              ? formatDate2(this.reservation.checkoutDate)
              : this.reservation.checkoutDate,
            room_name: res.name,
            room_price: roomPrice,
            room_type: roomType,
            remarks: this.reservation.remarks,
            // numguests: this.reservation.numguests,
            contactNumber: this.reservation.clientPhone,
            isPaid: "no",
            created_at: moment().format("YYYY-MM-DD hh:mm:ss"),
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
          });

          const data = {
            bookingID: id,
            itemName: res.name,
            itemType: roomType,
            itemPriceRate: roomPrice + "/check-in",
            purchaseQty: numDays + 1,
            totalCost: (numDays + 1) * parseFloat(roomPrice),
            category: "main",
            itemOption: "room",
            dateCreated: new Date(), // Set the dateCreated field to the current date and time
            groupkey: gkey,
            numdays: numDays + 1,
            totalguest: 0,
            totalpax: 0,
            currentroom: res.name,
          };

          try {
            await axios.post(this.API_URL + "transaction/item/", data);
          } catch (e) { }
          this.actionRecorder(
            `record?type=book&bookingID=${id}&groupkey=${gkey}`
          );
        });
        this.reloadData();
        this.populateCalendarItems();
        this.taskRecord(
          `action:/added reservation/client:/${this.reservation.clientName}/`
        );
        this.toggleItemModal();
        this.newtoggle = false;
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
        this.$swal
          .fire({
            title: "Success!",
            text: "Booking successful!",
            icon: "success",
          })
          .then((response) => {
            //document.location.reload();
          });
      } catch (error) {
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
        (o) => o.id !== this.bookings[this.itemIndex].itemID
      );
      this.bookings = this.bookings.filter(
        (o) => o.itemID !== this.bookings[this.itemIndex].itemID
      );
    },
    async loadTransactionData() {
      try {
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
    initializePlaceOrder() {
      if (
        (this.paymentMethod === "non-cash" ||
          this.paymentMethod.includes("agent")) &&
        (this.nonCashReference === "" || this.nonCashReference === null)
      ) {
        this.$swal.fire({
          icon: "error",
          title: "Please provide a reference number",
          text: "A reference number is required for non-cash and agent-type payments.",
          allowOutsideClick: false,
        });
        return;
      }
      if (
        this.paymentMethod.includes("agent") &&
        (isNaN(this.agentPayment) ||
          this.agentPayment === "" ||
          this.agentPayment <= 0 ||
          this.agentPayment === null)
      ) {
        this.$swal.fire({
          icon: "error",
          title: "Please enter a valid agent's actual price",
          text: "You need to provide a valid actual price credited by the agent for agent-type payments",
          allowOutsideClick: false,
        });

        return;
      }
      if (this.cashAmount > this.total && !this.walkinStatus) {
        this.$swal({
          title: "Over-Payment Detected!",
          text: "You are about to overpay. Do you want to push excess amount to this account?",
          icon: "warning",
          showCancelButton: true,
          confirmButtonText: "No!",
          cancelButtonText: "Yes, continue!",
          reverseButtons: true,
        }).then((result) => {
          if (!result.isConfirmed) {
            this.$swal
              .fire({
                title: "Authorization Required",
                input: "text",
                showCancelButton: true,
                allowOutsideClick: false,
                inputAttributes: {
                  minlength: 6, // Minimum length of 3 characters
                  maxlength: 24, // Maximum length of 24 characters
                  autocomplete: "off",
                  style: "text-security:disc; -webkit-text-security:disc;",
                },
                confirmButtonText: "Submit",
                cancelButtonText: "Cancel",
                inputPlaceholder: "Enter authorization code",
              })
              .then(async (result) => {
                if (result.isConfirmed) {
                  const authorizationCode = result.value;
                  // Validate the authorization code and perform necessary actions
                  if (
                    authorizationCode.toLowerCase() ===
                    this.AUTHORIZATION_KEY.toLowerCase()
                  ) {
                    // Code is correct, proceed with the desired action
                    const confirmMessage = "Action cannot be undone";
                    const result = await this.$swal.fire({
                      title: "Are you sure you want to continue?",
                      text: confirmMessage,
                      icon: "warning",
                      showCancelButton: true,
                      confirmButtonColor: "#3085d6",
                      cancelButtonColor: "#d33",
                      confirmButtonText: "Yes!",
                      cancelButtonText: "Cancel",
                    });
                    if (result.isConfirmed) {
                      const countdownMessage =
                        'Transaction will be posted in <span id="countdown">5</span> seconds. Do you want to cancel?';
                      let countdownResult;
                      countdownResult = await this.$swal.fire({
                        title: "Please wait",
                        html: countdownMessage,
                        icon: "info",
                        showCancelButton: true,
                        confirmButtonColor: "#3085d6",
                        cancelButtonColor: "#d33",
                        confirmButtonText: "Confirm now",
                        cancelButtonText: "Cancel",
                        didOpen: () => {
                          const countdownEl =
                            document.querySelector("#countdown");
                          let count = 5;
                          const timerId = setInterval(() => {
                            countdownEl.textContent = count;
                            count--;
                            if (count < 0) {
                              clearInterval(timerId);
                              this.$swal.close();
                            }
                          }, 1000);
                        },
                      });
                      if (!countdownResult.isConfirmed) {
                        return;
                      }
                      this.allowOverPayment = true;
                      this.placeOrder();
                    }
                  } else {
                    // Code is incorrect, show an error message or take appropriate action
                    this.$swal.fire({
                      icon: "error",
                      title: "Incorrect Passcode",
                      text: "The entered passcode is incorrect. Please try again.",
                      allowOutsideClick: false,
                    });
                  }
                }
              });
          } else {
            this.allowOverPayment = false;
            this.placeOrder();
          }
        });
      } else {
        this.placeOrder();
      }
    },
    async placeOrder() {
      if (parseFloat(this.cashAmount) > 0) {
        let bookid = null;
        let groupid = null;
        let transactid = null;
        const item = this.bookings[this.itemIndex];
        let reserveStatus = null;
        try {
          bookid = this.bookings[this.itemIndex].itemID;
          groupid = this.bookings[this.itemIndex].groupkey;
          reserveStatus = this.bookings[this.itemIndex].status;
        } catch (error) {
          bookid = "f";
        }
        let gkey = "";
        let groupbookings = [];
        try {
          gkey = this.bookings[this.itemIndex].groupkey || "x";
          try {
            const o = await axios.post(`${this.API_URL}bookings/filter/`, [
              { columnName: "groupkey", columnKey: gkey },
            ]);
            groupbookings = o.data;
          } catch (error) { }
        } catch (error) { }
        if (
          this.walkinStatus &&
          parseFloat(this.cashAmount) < parseFloat(this.total)
        ) {
          await this.$swal.fire({
            title: "Error",
            text: "There is no partial payment for walkin guests.",
            icon: "error",
          });
          return false;
        }
        const numGuests = this.cart.filter(
          (o) => o.type.toLowerCase() === "entrance"
        ).length;
        if (bookid === "f") {
          if (numGuests === 0) {
            // await this.$swal.fire({
            //   title: "Error",
            //   text: "Kindly specify the number of guests by providing the quantity within the general/pool entrance fee.",
            //   icon: "error",
            // });
            // return false;
          }
        } else {
          if (
            numGuests === 0 &&
            this.bookings[this.itemIndex].status === "checkedin"
          ) {
            await this.$swal.fire({
              title: "Error",
              text: "Kindly specify the number of guests by providing the quantity within the general/pool entrance fee.",
              icon: "error",
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
        const confirmMessage =
          "Are you sure you want to save this transaction?";
        const result = await this.$swal.fire({
          title: "Confirmation",
          text: confirmMessage,
          icon: "warning",
          showCancelButton: true,
          confirmButtonColor: "#3085d6",
          cancelButtonColor: "#d33",
          confirmButtonText: "Yes, save it!",
          cancelButtonText: "Cancel",
        });
        if (result.isConfirmed) {
          const countdownMessage =
            'Transaction will be saved in <span id="countdown">5</span> seconds. Do you want to cancel?';
          let countdownResult;
          countdownResult = await this.$swal.fire({
            title: "Please wait",
            html: countdownMessage,
            icon: "info",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Confirm now",
            cancelButtonText: "Cancel",
            didOpen: () => {
              const countdownEl = document.querySelector("#countdown");
              let count = 5;
              const timerId = setInterval(() => {
                countdownEl.textContent = count;
                count--;
                if (count < 0) {
                  clearInterval(timerId);
                  this.$swal.close();
                }
              }, 1000);
            },
          });
          if (!countdownResult.isConfirmed) {
            return;
          }
          try {
            let existingTransaction = {
              data: [],
            };
            if (bookid.charAt(0) !== "f") {
              existingTransaction = await axios.post(
                `${this.API_URL}transaction/filter/`,
                {
                  columnName: "groupkey",
                  columnKey: gkey,
                }
              );
              if (existingTransaction.data.length === 0) {
                existingTransaction = {
                  data: [],
                };
                existingTransaction = await axios.post(
                  `${this.API_URL}transaction/filter/`,
                  {
                    columnName: "bookingID",
                    columnKey: bookid,
                  }
                );
              }
            }
            let payStatus = null;
            if (existingTransaction.data.length === 0) {
              // Create a new transaction if it doesn't exist yet
              if (bookid.charAt(0) === "f") {
                bookid = this.walkinID;
              }
              payStatus =
                parseFloat(this.total) -
                  parseFloat(this.cashAmount) -
                  (this.allowOverPayment ? this.change : 0) <=
                  0
                  ? "full"
                  : "partial";
              const updatedcashamount =
                parseFloat(this.cashAmount) > parseFloat(this.total)
                  ? parseFloat(this.total) +
                  (this.allowOverPayment ? this.change : 0)
                  : parseFloat(this.cashAmount);
              const transactionData = {
                clientname: this.billing.clientName,
                clientemail: this.billing.clientEmail,
                clientcontact: this.billing.clientPhone,
                clientaddress: this.billing.clientAddress,
                clientnationality: this.billing.clientNationality,
                clientType: this.billing.clientType,
                nonCashReference:
                  this.paymentMethod === "cash"
                    ? (this.cashOR !== "" ? `OR#${this.cashOR}` : "") +
                    (this.cashOR !== "" && this.cashOS !== "" ? "/" : "") +
                    (this.cashOS !== "" ? `OS#${this.cashOS}` : "")
                    : this.paymentMethod === "non-cash"
                      ? this.nonCashPayPlatform + "-" + this.nonCashReference
                      : this.agentPayPlatform + "-" + this.nonCashReference,
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
              let doneTransaction = await axios.post(
                `${this.API_URL}transaction/`,
                transactionData
              );
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
                payStatus: doneTransaction.data.payStatus,
                agentPayment: this.agentPayment,
              };
              let doneTransactionRecord = await axios.post(
                `${this.API_URL}transaction/record/`,
                transactionRecordData
              );
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
                    category: "main",
                    itemOption: "addons",
                    bookingID: bookid,
                  };
                  try {
                    await axios.post(api, data);
                  } catch (error) { }
                });
              }
              if (bookid.charAt(0) !== "f") {
                if (groupbookings.length > 0) {
                  groupbookings.forEach(async (item) => {
                    let itemIndex = this.bookings.findIndex(
                      (o) => o.itemID === item.itemID
                    );
                    this.bookings[itemIndex].totalPrice =
                      transactionData.totalAmountToPay;
                    this.bookings[itemIndex].partialPayment =
                      transactionData.cashAmountPay;
                    if (payStatus === "partial") {
                      this.bookings[itemIndex].isPaid = "partial";
                    } else {
                      this.bookings[itemIndex].isPaid = "yes";
                    }
                    try {
                      const response = await axios.put(
                        this.API_URL +
                        `bookings/${this.bookings[itemIndex].id}/`,
                        {
                          itemID: this.bookings[itemIndex].itemID,
                          status: this.bookings[itemIndex].status,
                          name: this.bookings[itemIndex].name,
                          clientemail: this.bookings[itemIndex].clientemail,
                          clientaddress: this.bookings[itemIndex].clientaddress,
                          clientnationality:
                            this.bookings[itemIndex].clientnationality,
                          clientType: this.bookings[itemIndex].clientType,
                          checkinDate: this.bookings[itemIndex].checkinDate,
                          checkoutDate: this.bookings[itemIndex].checkoutDate,
                          room_name: this.bookings[itemIndex].room_name,
                          room_price: this.bookings[itemIndex].room_price,
                          room_type: this.bookings[itemIndex].room_type,
                          remarks: this.bookings[itemIndex].remarks,
                          contactNumber: this.bookings[itemIndex].contactNumber,
                          actualCheckoutDate:
                            this.bookings[itemIndex].actualCheckoutDate,
                          cancellationDate:
                            this.bookings[itemIndex].cancellationDate,
                          isPaid: this.bookings[itemIndex].isPaid,
                          totalPrice: this.bookings[itemIndex].totalPrice,
                          partialPayment:
                            this.bookings[itemIndex].partialPayment,
                          processedBy:
                            this.userdata.fName + " " + this.userdata.lName,
                          groupkey: this.bookings[itemIndex].groupkey,
                        }
                      );
                    } catch (error) {
                      console.log(error);
                    }
                  });
                } else {
                  this.bookings[this.itemIndex].totalPrice =
                    transactionData.totalAmountToPay;
                  this.bookings[this.itemIndex].partialPayment =
                    transactionData.cashAmountPay;
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
                const response = await axios.post(
                  `${this.API_URL}transaction/record/filter/`,
                  [
                    {
                      columnName: "transaction",
                      columnKey: doneTransaction.data.id,
                    },
                  ]
                );
                this.cashHistory = response.data;
                this.gbookingscount =
                  groupbookings.length === 0 ? 1 : groupbookings.length;
              } catch (error) { }
              this.billing.bookingID = doneTransaction.data.id;
              transactid =
                doneTransaction.data.id + "-" + doneTransactionRecord.data.id;
            } else {
              // Update the transaction if it already exists
              payStatus =
                parseFloat(this.total) -
                  parseFloat(this.cashAmount) -
                  (this.allowOverPayment ? this.change : 0) <=
                  0
                  ? "full"
                  : "partial";
              const transaction = existingTransaction.data[0];
              const existingCashAmountPay = parseFloat(
                transaction.cashAmountPay
              );
              const newcashAmountPay =
                existingCashAmountPay + parseFloat(this.cashAmount) <
                  parseFloat(this.subtotal)
                  ? existingCashAmountPay + parseFloat(this.cashAmount)
                  : parseFloat(this.subtotal) +
                  (this.allowOverPayment ? this.change : 0);
              const existingbalance = transaction.balance;
              let origCash =
                parseFloat(this.cashAmount) > parseFloat(this.total)
                  ? parseFloat(this.total)
                  : parseFloat(this.cashAmount);
              const newbalance =
                existingCashAmountPay + parseFloat(this.cashAmount) <
                  parseFloat(this.subtotal)
                  ? parseFloat(transaction.totalAmountToPay) -
                  parseFloat(newcashAmountPay)
                  : 0;
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
                nonCashReference:
                  this.paymentMethod === "cash"
                    ? (this.cashOR !== "" ? `OR#${this.cashOR}` : "") +
                    (this.cashOR !== "" && this.cashOS !== "" ? "/" : "") +
                    (this.cashOS !== "" ? `OS#${this.cashOS}` : "")
                    : this.paymentMethod === "non-cash"
                      ? this.nonCashPayPlatform + "-" + this.nonCashReference
                      : this.agentPayPlatform + "-" + this.nonCashReference,
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
              let doneTransaction = await axios.put(
                `${this.API_URL}transaction/${existingTransaction.data[0].id}/`,
                transactionData
              );
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
                payStatus: doneTransaction.data.payStatus,
                agentPayment: this.agentPayment,
              };
              let doneTransactionRecord = await axios.post(
                `${this.API_URL}transaction/record/`,
                transactionRecordData
              );
              if (groupbookings.length > 0) {
                groupbookings.forEach(async (item) => {
                  let itemIndex = this.bookings.findIndex(
                    (o) => o.itemID === item.itemID
                  );
                  this.bookings[itemIndex].totalPrice =
                    transactionRecordData.totalAmountToPay;
                  this.bookings[itemIndex].partialPayment = newcashAmountPay;
                  if (payStatus === "partial") {
                    this.bookings[itemIndex].isPaid = "partial";
                  } else {
                    this.bookings[itemIndex].isPaid = "yes";
                  }
                  try {
                    const response = await axios.put(
                      this.API_URL + `bookings/${this.bookings[itemIndex].id}/`,
                      {
                        itemID: this.bookings[itemIndex].itemID,
                        status: this.bookings[itemIndex].status,
                        name: this.bookings[itemIndex].name,
                        clientemail: this.bookings[itemIndex].clientemail,
                        clientaddress: this.bookings[itemIndex].clientaddress,
                        clientnationality:
                          this.bookings[itemIndex].clientnationality,
                        clientType: this.bookings[itemIndex].clientType,
                        checkinDate: this.bookings[itemIndex].checkinDate,
                        checkoutDate: this.bookings[itemIndex].checkoutDate,
                        room_name: this.bookings[itemIndex].room_name,
                        room_price: this.bookings[itemIndex].room_price,
                        room_type: this.bookings[itemIndex].room_type,
                        remarks: this.bookings[itemIndex].remarks,
                        contactNumber: this.bookings[itemIndex].contactNumber,
                        actualCheckoutDate:
                          this.bookings[itemIndex].actualCheckoutDate,
                        cancellationDate:
                          this.bookings[itemIndex].cancellationDate,
                        isPaid: this.bookings[itemIndex].isPaid,
                        totalPrice: this.bookings[itemIndex].totalPrice,
                        partialPayment: this.bookings[itemIndex].partialPayment,
                        processedBy:
                          this.userdata.fName + " " + this.userdata.lName,
                        groupkey: this.bookings[itemIndex].groupkey,
                      }
                    );
                  } catch (error) {
                    console.log(error);
                  }
                });
              } else {
                this.bookings[this.itemIndex].totalPrice =
                  transactionRecordData.totalAmountToPay;
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
                const response = await axios.post(
                  `${this.API_URL}transaction/record/filter/`,
                  [
                    {
                      columnName: "transaction",
                      columnKey: transactionRecordData.transaction,
                    },
                  ]
                );
                this.cashHistory = response.data;
                this.gbookingscount =
                  groupbookings.length === 0 ? 1 : groupbookings.length;
              } catch (error) { }
              transactid =
                doneTransaction.data.id + "-" + doneTransactionRecord.data.id;
            }
            if (bookid.charAt(0) !== "f") {
              this.actionRecorder(
                `record?type=transact&bookingID=${this.bookings[this.itemIndex].itemID
                }&groupkey=${this.bookings[this.itemIndex].groupkey
                }&remarks=id:${transactid}`
              );
            }
            this.taskRecord(
              `action:/transaction added/client:/${this.billing.clientName}`
            );
            this.walkinStatus = false;
            await this.$swal
              .fire({
                title: "Success",
                text: "Transaction saved successfully!",
                icon: "success",
              })
              .then((response) => {
                setTimeout(() => {
                  this.generateBillingStatement();
                }, 500);
                //document.location.reload();
              });
          } catch (error) {
            // Show an error message using SweetAlert
            await this.$swal.fire({
              title: "Error",
              text: "An error occurred while saving the transaction.",
              icon: "error",
            });
            console.log(error);
          }
        }
      } else {
        await this.$swal.fire({
          title: "Error",
          text: "Invalid entry for cash tendered.",
          icon: "error",
        });
      }
    },
    async printSection(idstring, pLength, pWidth, ft, orientation = 0) {
      const section = document.getElementById(idstring);
      const sectionHTML = section.outerHTML;
      const printBtn =
        '<div class="row no-print"><div class="col-md-12 text-right"><button class="btn btn-danger" onclick="window.print()">Print Now</button></div></div>';
      const footerContent = `<p class="text-right">Total = ${this.filteredTransactionsTotal}</p><p class="text-right">Collectibles = ${this.filteredTransactionsBalance}</p>`;
      const footerSummary = ft ? footerContent : "";
      const pagePortrait = `<style>.highlight {background-color: yellow;}body {font-family: Arial, sans-serif;line-height: 1.25;padding: 0.5in;font-size:16px} hr {margin-top: 0.5px;;margin-bottom: 0.5px;} p {margin-top: 0.5px;;margin-bottom: 0.5px;} table {table-layout: auto;width:100%;margin:0 auto;border-collapse:collapse;margin-top: 1px;margin-bottom: 1px;} tr td:last-child{width:1%;white-space:nowrap;} .container {width: ${pWidth}px;height: ${pLength}px;padding-top: 0.25in;padding-bottom: 0.25in;background-color: #fff;box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);margin: auto;}.text-center {text-align: center;}.text-right {text-align: right;}@media print {.no-print {display: none;}}html, body {width: ${pWidth}px;height: ${pLength}px;margin: 0;padding: 0;}}</style>`;
      const pageLandscape = `<style>html,body{display:none;}.no-print{display: none;} @media print{@page {size: legal landscape; margin:auto} html,body{display: block;zoom: 95%;} tr{page-break-inside: auto;} .no-print{display: none;}}</style>`;
      const bootstrapCSS = `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.0/css/bootstrap.min.css">${!orientation ? pagePortrait : pageLandscape
        }`;
      const bootstrapJS =
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.4/jquery.min.js"><script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.0/js/bootstrap.bundle.min.js">';
      const html = `<!doctype html><html><head>${bootstrapCSS}</head><body>${printBtn}${sectionHTML}${footerSummary}${bootstrapJS}<script>setTimeout('alert()',1000)<\/script></body></html>`;
      // Create a new jsPDF instance
      function printAndDetect() {
        const options =
          "height=500,width=800,scrollbars=no,status=no,toolbar=no,location=no";
        const printWindow = window.open("", options);
        printWindow.document.write(html);
        printWindow.document.close();
        printWindow.addEventListener("load", function () {
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
      document.getElementById(`reportGenerator`).innerHTML =
        document.getElementById(
          `billing-details-preview-view${this.reportview}`
        ).innerHTML;
      this.printSection("billing-details", 1300, 850, false);
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
        this.items = response.data.filter((item) => item.isAvailable === true);
      } catch (error) {
        console.log(error);
      }
    },
    async reloadData() {
      try {
        const roomsResponse = await axios.get(this.API_URL + "rooms/");
        this.rooms = roomsResponse.data.filter(
          (item) => item.isAvailable === true
        );

        const roomscatResponse = await axios.get(
          this.API_URL + "rooms/category/"
        );
        this.roomcategories = roomscatResponse.data.filter(
          (item) => item.isAvailable === true
        );

        const agentsResponse = await axios.get(this.API_URL + "agents/");
        this.agents = agentsResponse.data.filter(
          (item) => item.isAvailable === true
        );

        const packResponse = await axios.get(this.API_URL + "package/");
        this.packages = packResponse.data.filter(
          (item) => item.isAvailable === true
        );

        const histlogsResponse = await axios.get(this.API_URL + "task/record/");
        this.histlogs = histlogsResponse.data.filter((item) =>
          item.task.includes("record?type=")
        );

        /*
                          this.bookings.filter(booking => booking.room_name === this.bookings[this.itemIndex].room_name );
                                  */
        const reservationsResponse = await axios.get(
          this.API_URL + "bookings/"
        );
        this.origbookings = reservationsResponse.data;
        this.populateCalendarItems();
      } catch (error) {
        console.log(error);
      }
    },
    vacantRoom(roomNumber) {
      const bookingIndex = this.reservations.findIndex(
        (reservation) =>
          reservation.room_name === roomNumber &&
          new Date(reservation.checkinDate) < new Date() &&
          new Date(reservation.checkoutDate) > new Date()
      );
      return bookingIndex === -1;
    },
    isItemAvailableInCart(item) {
      const itemIndex = this.cart.findIndex((o) => o.name === item);
      return itemIndex === -1;
    },
    isRoomAvailable(room, checkinDate, checkoutDate) {
      // Get all reservations for the given room
      const roomReservations = this.bookings.filter(
        (reservation) => reservation.room_name === room
      );
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
          reserveStatus = this.bookings[this.itemIndex].status;
        } catch (error) {
          reserveStatus = "n/a";
        }
        // if (reserveStatus === "reserved") {
        //   await this.$swal.fire({
        //     title: "Error",
        //     text: "No purchase of add-ons until guest is checked in.",
        //     icon: "error",
        //   });
        //   return false;
        // }
        if (this.howMany[index] > 0) {
          this.itemCart.name = item.item;
          this.itemCart.type = item.type;
          this.itemCart.rate = item.rate;
          this.itemCart.counter = item.counter;
          this.itemCart.priceRate = item.priceRate + "/" + item.counter;
          this.itemCart.purqty = this.howMany[index];
          this.itemCart.category = "inclusion";
          this.itemCart.itemOption = "addons";
          this.itemCart.totalCartPrice =
            parseFloat(item.priceRate) * parseFloat(this.howMany[index]);
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

          let numdays = 0,
            roompax = 0,
            totalGuests = 0,
            currentroom = "";

          if (!this.walkinStatus) {
            const checkInDate = parseDate(
              this.bookings[this.itemIndex].checkinDate
            );
            const checkOutDate = parseDate(
              this.bookings[this.itemIndex].checkoutDate
            );
            numdays = (checkOutDate - checkInDate) / (1000 * 60 * 60 * 24);

            const roomsBooked = this.bookings[this.itemIndex].room_name;
            roompax = parseFloat(
              this.rooms.filter((o) => o.name === roomsBooked)[0].pax
            );

            const response = await axios.post(
              this.API_URL + "transaction/item/filter/",
              {
                columnName: "bookingID",
                columnKey: this.bookings[this.itemIndex].itemID,
              }
            );

            totalGuests =
              response.data
                .filter((o) => o.itemName.toLowerCase() === "room guest")
                .reduce((acc, item) => acc + parseFloat(item.purchaseQty), 0) +
              data.purchaseQty;

            currentroom = response.data.filter(
              (o) => o.category === "main" && o.itemOption === "room"
            );
          }

          if (
            data.itemName.toLowerCase() === "room guest" &&
            data.itemType.toLowerCase() === "entrance" &&
            !this.walkinStatus
          ) {
            data.numdays = numdays + 1;
            data.totalpax = roompax;
            data.totalguest = totalGuests;
            this.itemCart.numdays = data.numdays;
            this.itemCart.totalpax = data.totalpax;
            this.itemCart.totalguest = data.totalguest;
          } else {
            data.numdays = 0;
            data.totalpax = 0;
            data.totalguest = 0;
            this.itemCart.numdays = data.numdays;
            this.itemCart.totalpax = data.totalpax;
            this.itemCart.totalguest = data.totalguest;
          }

          data.currentroom = !this.walkinStatus
            ? currentroom[0].itemName
            : "n/a";
          this.itemCart.currentroom = data.currentroom;

          try {
            // Access property here
            data.bookingID = this.bookings[this.itemIndex].itemID;
            // Make a POST request to the API to save the data
            await axios
              .post(this.API_URL + "transaction/item/", data)
              .then((response) => {
                // Log a success message to the console
                this.itemCart.id = response.data.id;
              })
              .catch((error) => {
                // Log an error message to the console
                console.error("Error saving data:", error);
              });
          } catch (e) {
            // Handle the error here
            data.bookingID = "walkin";
          }
          this.cart.push(this.itemCart);
          console.log(this.cart);

          $("#shopModal").modal("toggle");
          this.howMany[index] = "";
          this.itemCart = {
            id: 0,
            name: "",
            priceRate: "",
            rate: "",
            counter: "",
            purqty: "",
            totalCartPrice: "",
            category: "",
          };
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
        this.$swal
          .fire({
            title: "Error!",
            text: "Supply first client's info.",
            icon: "error",
          })
          .then((result) => {
            this.howMany[index] = "";
            this.toggleAddAccountModal();
          });
      }
    },
    cancelItem(item) {
      if (item.category === "main" && item.itemOption === "addons") {
        this.$swal
          .fire({
            title: "Authorization Required",
            input: "text",
            showCancelButton: true,
            allowOutsideClick: false,
            inputAttributes: {
              minlength: 6, // Minimum length of 3 characters
              maxlength: 24, // Maximum length of 24 characters
              autocomplete: "off",
              style: "text-security:disc; -webkit-text-security:disc;",
            },
            confirmButtonText: "Submit",
            cancelButtonText: "Cancel",
            inputPlaceholder: "Enter authorization code",
          })
          .then(async (result) => {
            if (result.isConfirmed) {
              const authorizationCode = result.value;
              // Validate the authorization code and perform necessary actions
              if (
                authorizationCode.toLowerCase() ===
                this.AUTHORIZATION_KEY.toLowerCase()
              ) {
                // Code is correct, proceed with the desired action
                const confirmMessage =
                  " If you proceed with voiding, this items will be permanently deleted, and this action cannot be reversed.";
                const result = await this.$swal.fire({
                  title: "Are you sure you want to void this?",
                  text: confirmMessage,
                  icon: "warning",
                  showCancelButton: true,
                  confirmButtonColor: "#3085d6",
                  cancelButtonColor: "#d33",
                  confirmButtonText: "Yes, void it!",
                  cancelButtonText: "Cancel",
                });
                if (result.isConfirmed) {
                  const countdownMessage =
                    'Item will be voided in <span id="countdown">5</span> seconds. Do you want to cancel?';
                  let countdownResult;
                  countdownResult = await this.$swal.fire({
                    title: "Please wait",
                    html: countdownMessage,
                    icon: "info",
                    showCancelButton: true,
                    confirmButtonColor: "#3085d6",
                    cancelButtonColor: "#d33",
                    confirmButtonText: "Confirm now",
                    cancelButtonText: "Cancel",
                    didOpen: () => {
                      const countdownEl = document.querySelector("#countdown");
                      let count = 5;
                      const timerId = setInterval(() => {
                        countdownEl.textContent = count;
                        count--;
                        if (count < 0) {
                          clearInterval(timerId);
                          this.$swal.close();
                        }
                      }, 1000);
                    },
                  });
                  if (!countdownResult.isConfirmed) {
                    return;
                  }
                  this.handleCancelItem(item);
                }
              } else {
                // Code is incorrect, show an error message or take appropriate action
                this.$swal.fire({
                  icon: "error",
                  title: "Incorrect Passcode",
                  text: "The entered passcode is incorrect. Please try again.",
                  allowOutsideClick: false,
                });
              }
            }
          });
      } else {
        this.handleCancelItem(item);
      }
    },
    handleCancelItem(item) {
      this.$swal
        .fire({
          title: "Are you sure?",
          text: "You won't be able to revert this!",
          icon: "warning",
          showCancelButton: true,
          confirmButtonColor: "#d33",
          cancelButtonColor: "#3085d6",
          confirmButtonText: "Yes, delete it!",
        })
        .then((result) => {
          if (result.isConfirmed) {
            this.cart = this.cart.filter((o) => o.id !== item.id);
            if (this.itemIndex !== -1) {
              this.actionRecorder(
                `record?type=deleteitem&bookingID=${this.bookings[this.itemIndex].itemID
                }&groupkey=${this.bookings[this.itemIndex].groupkey
                }&remarks=deleted ${item.name}`
              );
              axios
                .get(this.API_URL + `transaction/item/delete/${item.id}/`)
                .then((response) => {
                  this.$swal.fire(
                    "Deleted!",
                    "Your item has been deleted.",
                    "success"
                  );
                  // perform any additional operations after successful delete
                  this.taskRecord(
                    `action:/voided booking item/client:/${this.bookings[this.itemIndex].name
                    }/item/${item.name}`
                  );
                })
                .catch((error) => {
                  console.log(error);
                  this.$swal.fire("Error!", "Failed to delete item.", "error");
                });
            }
            {
            }
          }
        });
    },
    async bookRoom(room) {
      const checkinDate = new Date(this.reservation.checkinDate);
      const checkoutDate = new Date(this.reservation.checkoutDate);
      const numDays = Math.ceil(
        (checkoutDate - checkinDate) / (1000 * 60 * 60 * 24)
      );
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
            totalPrice: this.reservation.totalPrice,
          });
          this.reservations.push(this.reservation);
          this.reloadData();
          this.reservation = {
            name: "",
            room_name: "",
            room_type: "",
            room_price: "",
            contactNumber: "",
            totalPrice: 0,
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
      if (event.target.classList.contains("cv-item")) {
        //this.$refs.vueSimpleContextMenu1.showMenu(event, event.target.innerHTML);
      } else if (event.target.classList.contains("cv-day")) {
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
    // this.$refs.searchQuery.focus();
    // this.$refs.searchQuery.blur();
    $(".currentPeriod").click();
    $("#suglist").hide();
    this.newItemStartDate = CalendarMath.isoYearMonthDay(CalendarMath.today());
    this.newItemEndDate = CalendarMath.isoYearMonthDay(CalendarMath.today());
    this.$nextTick(() => {
      //document.body.addEventListener("contextmenu", this.handleContextMenu);
    });
    document.addEventListener("keydown", this.handleKeyPress);
    const modal = this.$refs.modal;
    // Attach event listener for modal hidden event
    modal.addEventListener("hidden.bs.modal", this.handleModalClosed);
    this.socket = new WebSocket(
      `ws://${this.API_URL.replace(/^https?:\/\//, "")}ws/realtime/`
    );
    //this.socket = new WebSocket('ws://192.168.1.222:8081/ws/realtime/');
    const vm = this;
    this.socket.onmessage = function (e) {
      const data = JSON.parse(e.data);
      console.log(data.message);
      // $("#BookDayModal").modal("hide");
      vm.loadAlldata();
      vm.componentKey += 1;
    };
    if (typeof google !== "undefined") {
      this.initAutocomplete();
    }
    this.extendView();
  },
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

.cv-item.task-rented {
  background-color: rgb(0, 170, 255);
  color: white;
  font-family:
    Avenir,
    Avenir Next,
    Segoe UI,
    Helvetica,
    Arial,
    sans-serif;
  /* adjust the color as needed */
}

.cv-item.task-returned {
  background-color: rgb(46, 215, 216);
  color: white;
  font-family:
    Avenir,
    Avenir Next,
    Segoe UI,
    Helvetica,
    Arial,
    sans-serif;
  /* adjust the color as needed */
}

.cv-item.task-booked {
  background-color: rgb(208, 31, 46);
  color: white;
  font-family:
    Avenir,
    Avenir Next,
    Segoe UI,
    Helvetica,
    Arial,
    sans-serif;
  /* adjust the color as needed */
}

.cv-item.task-progress {
  background-color: rgb(0, 170, 255);
  color: white;
  font-family:
    Avenir,
    Avenir Next,
    Segoe UI,
    Helvetica,
    Arial,
    sans-serif;
  /* adjust the color as needed */
}

.cv-item.task-inspected {
  background-color: rgb(46, 215, 216);
  color: white;
  font-family:
    Avenir,
    Avenir Next,
    Segoe UI,
    Helvetica,
    Arial,
    sans-serif;
  /* adjust the color as needed */
}

.cv-item.task-open {
  background-color: rgb(208, 31, 46);
  color: white;
  font-family:
    Avenir,
    Avenir Next,
    Segoe UI,
    Helvetica,
    Arial,
    sans-serif;
  /* adjust the color as needed */
}

.cv-item.task-completed {
  background-color: rgb(255, 170, 0);
  color: white;
  font-family:
    Avenir,
    Avenir Next,
    Segoe UI,
    Helvetica,
    Arial,
    sans-serif;
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
  /* z-index: 55000; */
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

.printform {
  -webkit-transition: all 0.5s ease;
  -moz-transition: all 0.5s ease;
  -o-transition: all 0.5s ease;
  transition: all 0.5s ease;
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
  -webkit-transition:
    opacity 0.3s linear,
    right 0.3s ease-out;
  -moz-transition:
    opacity 0.3s linear,
    right 0.3s ease-out;
  -o-transition:
    opacity 0.3s linear,
    right 0.3s ease-out;
  transition:
    opacity 0.3s linear,
    right 0.3s ease-out;
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

.badge-danger {
  background-color: #dc3545;
  color: #fff;
}

.badge-pill {
  display: inline-block;
  padding: 0.25em 0.6em;
  font-size: 75%;
  font-weight: 700;
  vertical-align: top;
  line-height: 1;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: 10rem;
  position: relative;
  top: -0.75em;
  left: -0.25em;
}

.address {
  width: 100%;
  height: 2.5rem;
  margin-top: 0;
  padding: 0.5em;
  border: 0;
  border-bottom: 2px solid gray;
  font-family: "Roboto", sans-serif;
  font-size: 12px;
}

.book-form {
  width: 100%;
  margin-top: 0;
  padding: 0.5em;
  border: 0;
  border-bottom: 2px solid gray;
  font-family: "Roboto", sans-serif;
  font-size: 12px;
}

.address:focus {
  border-bottom: 4px solid black;
}

.pac-container {
  z-index: 999999;
}
</style>
