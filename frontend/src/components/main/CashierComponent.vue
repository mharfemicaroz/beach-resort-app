<template>
  <div class="container-fluid">
    <TopNavBarComponent />
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="tables-tab" data-bs-toggle="tab" data-bs-target="#tables" type="button"
          role="tab" aria-controls="tables" aria-selected="true" @click="resetCounter">Customers</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="pos-tab" data-bs-toggle="tab" data-bs-target="#pos" type="button" role="tab"
          aria-controls="pos" aria-selected="true" @click="activatePOS">{{ (userdata.role !== 'waiter') ? 'POS' : 'Menu'
          }}</button>
      </li>
      <li class="nav-item" role="presentation" v-if="userdata.role !== 'cashier'">
        <button class="nav-link" id="orders-tab" data-bs-toggle="tab" data-bs-target="#orders" type="button" role="tab"
          aria-controls="orders" aria-selected="true">Orders</button>
      </li>
      <li class="nav-item" role="presentation" v-if="userdata.role === 'superuser'">
        <button class="nav-link" id="inventory-tab" data-bs-toggle="tab" data-bs-target="#inventory" type="button"
          role="tab" aria-controls="inventory" aria-selected="true" @click="resetCounter">Inventory</button>
      </li>
      <li class="nav-item" role="presentation" v-if="userdata.role === 'superuser'">
        <button class="nav-link" id="reports-tab" data-bs-toggle="tab" data-bs-target="#reports" type="button" role="tab"
          aria-controls="reports" aria-selected="false" @click="resetCounter">Reports</button>
      </li>
    </ul>

    <div class="tab-content mt-3" id="myTabContent">
      <div class="tab-pane fade show active" id="tables" role="tabpanel" aria-labelledby="tables-tab">
        <div class="row mt-2">
          <div class="col-md-3">
            <ul class="nav bg radius nav-pills nav-fill mb-3 bg mt-3" role="tablist">
              <li class="nav-item">
                <a class="nav-link active show" data-bs-toggle="tab" role="tab" href="#dineintab">
                  <i class="fa fa-tags"></i>Dine-in</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#takeouttab">
                  <i class="fa fa-tags"></i>Take Out</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#onholdtab">
                  <i class="fa fa-tags"></i>On hold</a>
              </li>
            </ul>
          </div>

          <div class="tab-content" id="myTabContent" style="height: 550px; overflow-y: auto;">
            <div class="tab-pane fade show active" id="dineintab" role="tabpanel" aria-labelledby="dinein-tab">
              <div class="container-fluid">
                <div class="row">
                  <div class="col-md-12">
                    <div class="row row-cols-1 row-cols-md-6">
                      <div class="col mb-6" v-for="(item, index) in filteredresto_tables" :key="item.id">
                        <div class="card" style="transition: transform 0.2s ease-in-out;" @click="dineInAction(item)">
                          <div class="card-header d-flex justify-content-between align-items-center"
                            :style="{ 'background-color': ('order_id' in item) ? '#66bb6a' : '' }">
                            <h5 class="card-title"><i class="fas fa-table"></i> {{ item.name }}</h5>
                          </div>
                          <div class="card-body">
                            <h6 class="text-dark">
                              <i class="fas fa-info-circle"></i> {{ ('order_id' in item) ? 'occupied' : 'vacant' }}
                            </h6>
                          </div>

                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="tab-pane fade" id="takeouttab" role="tabpanel" aria-labelledby="takeout-tab">
              <div class="container-fluid">
                <div class="row">
                  <div class="col-md-12">
                    <div class="row row-cols-1 row-cols-md-6">
                      <div class="col mb-6">
                        <div class="card"
                          style="transition: transform 0.2s ease-in-out;border-color: #ffecb5;background-color: #fff3cd; color: #664d03;"
                          @click="addnewTakeout">
                          <div class="card-header d-flex justify-content-between align-items-center">
                            <h5 class="card-title"><i class="fas fa-plus"></i> Add</h5>
                          </div>
                          <div class="card-body">
                            <h6>
                              <i class="fas fa-info-circle"></i> Add new takeout
                            </h6>
                          </div>
                        </div>
                      </div>
                      <div class="col mb-6" v-for="(item, index) in filteredresto_takeouts" :key="item.id">
                        <div class="card" style="transition: transform 0.2s ease-in-out;">
                          <div class="card-header d-flex justify-content-between align-items-center"
                            :style="{ 'background-color': ('order_id' in item) ? '#66bb6a' : '' }">
                            <h5 class="card-title"><i class="fa fa-shopping-cart"></i> {{ item.name }}</h5>
                            <button type="button" class="btn btn-sm btn-close" aria-label="Close"
                              @click="cancelTakeOut(item.id)"></button>
                          </div>
                          <div class="card-body" @click="takeoutAction(item)">
                            <h6 class="text-dark">
                              <i class="fas fa-info-circle"></i> {{ ('order_id' in item) ? 'on progress' : 'on hold' }}
                            </h6>
                          </div>

                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="tab-pane fade" id="onholdtab" role="tabpanel" aria-labelledby="onhold-tab">
              <div class="container-fluid">
                <div class="row">
                  <div class="col-md-12">
                    <div class="row row-cols-1 row-cols-md-6">
                      <div class="col mb-6" v-for="(item, index) in filteredresto_onholds" :key="item.id">
                        <div class="card" style="transition: transform 0.2s ease-in-out;">
                          <div class="card-header d-flex justify-content-between align-items-center"
                            :style="{ 'background-color': ('order_id' in item) ? '#66bb6a' : '' }">
                            <h5 class="card-title"><i class="fa fa-dollars"></i> {{ item.name }}</h5>
                          </div>
                          <div class="card-body" @click="onholdAction(item)">
                            <h6 class="text-dark">
                              <i class="fas fa-info-circle"></i> {{ ('order_id' in item) ? 'on progress' : 'on hold' }}
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
      </div>
      <div class="tab-pane fade" id="pos" role="tabpanel" aria-labelledby="pos-tab">
        <div class="row mt-2" id="posTab">
          <div class="col-md-8">
            <div class="row">
              <div class="col-lg-6 col-sm-6">
                <h4>{{ (userdata.role !== 'waiter') ? 'Point of Sales' : 'Menu' }}
                  <span v-if="customer.reference_id !== null">
                    >>>&NonBreakingSpace; <span class="blink_me text-danger" style="font-style: italic;">Now serving: {{
                      customer.identifier }} for {{ customer.type }}</span>
                  </span>
                </h4>
              </div>
              <div class="col-lg-6 col-sm-6">
                <form class="search-wrap" @submit.prevent="">
                  <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search" ref="myInput" v-model="searchText">
                    <div class="input-group-append">
                      <button class="btn btn-primary" type="submit">
                        <i class="fa fa-search"></i>
                      </button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
            <ul class="nav bg radius nav-pills nav-fill mb-3 bg mt-3" role="tablist">
              <li class="nav-item">
                <a class="nav-link active show" data-bs-toggle="tab" data-bs-target="#alltab" role="tab" href="#alltab"
                  @click="setActiveTab('alltab')">
                  <i class="fa fa-tags"></i> All</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category1"
                  @click="setActiveTab('nav-tab-category1')">
                  <i class="fa fa-tags "></i>Appetizers</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category2"
                  @click="setActiveTab('nav-tab-category2')">
                  <i class="fa fa-tags "></i>Asian Classics</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category3"
                  @click="setActiveTab('nav-tab-category3')">
                  <i class="fa fa-tags "></i>Sizzlers</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category4"
                  @click="setActiveTab('nav-tab-category4')">
                  <i class="fa fa-tags "></i>Soup</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category5"
                  @click="setActiveTab('nav-tab-category5')">
                  <i class="fa fa-tags "></i>Drinks</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category6"
                  @click="setActiveTab('nav-tab-category6')">
                  <i class="fa fa-tags "></i>Desserts & Sweets</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category7"
                  @click="setActiveTab('nav-tab-category7')">
                  <i class="fa fa-tags "></i>Pizza, Pasta, Sandwich</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category8"
                  @click="setActiveTab('nav-tab-category8')">
                  <i class="fa fa-tags "></i>Breakfast</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category9"
                  @click="setActiveTab('nav-tab-category9')">
                  <i class="fa fa-tags "></i>Rice</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" data-bs-toggle="tab" role="tab" href="#nav-tab-category10"
                  @click="setActiveTab('nav-tab-category10')">
                  <i class="fa fa-tags "></i>Miscellaneous</a>
              </li>
            </ul>

            <div class="tab-content" id="myTabContent"
              :style="`height: ${(userdata.role === 'waiter') ? 370 : 462}px; overflow-y: auto;`">
              <div class="tab-pane fade show active" id="alltab" role="tabpanel" aria-labelledby="all-tab">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray" @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category1" role="tabpanel" aria-labelledby="nav-tab-category1">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Appetizers')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category2" role="tabpanel" aria-labelledby="nav-tab-category2">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Asian Classics')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category3" role="tabpanel" aria-labelledby="nav-tab-category3">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Sizzlers')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category4" role="tabpanel" aria-labelledby="nav-tab-category4">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Soup')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category5" role="tabpanel" aria-labelledby="nav-tab-category5">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Drinks')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category6" role="tabpanel" aria-labelledby="nav-tab-category6">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Desserts & Sweets')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category7" role="tabpanel" aria-labelledby="nav-tab-category7">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Pizza, Pasta, Sandwich')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category8" role="tabpanel" aria-labelledby="nav-tab-category8">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Breakfast')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category9" role="tabpanel" aria-labelledby="nav-tab-category9">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Rice')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="nav-tab-category10" role="tabpanel" aria-labelledby="nav-tab-category10">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-md-12">
                      <CardItems :itemData="filtereditemarray.filter(i => i.category === 'Miscellaneous')"
                        @click-action="addItemToCart" />
                    </div>
                  </div>
                </div>
              </div>
            </div>



            <div class="row mt-3">

              <button :disabled="(cartItems.length < 1)" class="btn btn-outline-primary btn-block btn-box btn-gap"
                @click="placeOrder">
                <span class="text-medium">[F1]</span><br>
                Save
              </button>

              <button :disabled="(cartItems.length < 1)" v-if="userdata.role !== 'waiter'"
                class="btn btn-outline-primary btn-block btn-box btn-gap" @click="payOrder">
                <span class="text-medium">[F2]</span><br>
                Charge
              </button>

              <button :disabled="(cartItems.length < 1)" v-if="userdata.role !== 'waiter'"
                class="btn btn-outline-primary btn-block btn-box btn-gap" @click="setQty">
                <span class="text-medium">[F3]</span><br>
                Qty
              </button>

              <button class="btn btn-outline-primary btn-block btn-box btn-gap" v-if="userdata.role !== 'waiter'"
                @click="setDiscount">
                <span class="text-medium">[F4]</span><br>
                Discount
              </button>

              <button class="btn btn-outline-primary btn-block btn-box btn-gap" v-if="userdata.role !== 'waiter'"
                @click="setTax">
                <span class="text-medium">[F5]</span><br>
                Tax
              </button>

              <button :disabled="(cartItems.length < 1 || customer.reference_id !== null)"
                v-if="userdata.role !== 'waiter'" class="btn btn-outline-primary btn-block btn-box btn-gap"
                @click="holdCustomer">
                <span class="text-medium">[F6]</span><br>
                Hold
              </button>

              <button disabled v-if="userdata.role !== 'waiter'" class="btn btn-outline-primary btn-block btn-box btn-gap"
                @click="">
                <span class="text-medium">[F7]</span><br>
                Toggle
              </button>

              <button class="btn btn-outline-primary btn-block btn-box btn-gap" @click="findItem">
                <span class="text-medium">[F8]</span><br>
                {{ (inquiretoggle) ? 'Clear' : 'Find' }}
              </button>

              <button class="btn btn-outline-primary btn-block btn-box btn-gap" @click="toggleInquire">
                <span class="text-medium">[F9]</span><br>
                {{ (inquiretoggle) ? 'Punch' : 'Inquire' }}
              </button>

              <button :disabled="(cartItems.length < 1)" v-if="userdata.role !== 'waiter'"
                class="btn btn-outline-primary btn-block btn-box btn-gap" @click="voidAction">
                <span class="text-medium">[F10]</span><br>
                Void
              </button>

              <button :disabled="(cartItems.length < 1 || customer.order_id !== undefined)"
                class="btn btn-outline-primary btn-block btn-box btn-gap" @click="clearAll">
                <span class="text-medium">[F11]</span><br>
                Clear
              </button>

              <button class="btn btn-outline-primary btn-block btn-box btn-gap" @click="logout">
                <span class="text-medium">[F12]</span><br>
                Log Out
              </button>
            </div>


          </div>
          <div class="col-md-4">

            <div class="card" :style="`height: ${(userdata.role !== 'waiter') ? 340 : 595}px; overflow-y: auto;`">

              <div class="row">
                <div class="col-md-12">
                  <table class="table">
                    <thead>
                      <tr>
                        <th scope="col" style="width: 180px;">Item <span v-if="cartItems.length > 0"
                            class="badge-pill badge-danger">{{ cartItems.length }}</span></th>
                        <th scope="col">Qty</th>
                        <th scope="col">Price</th>
                        <th scope="col">
                          <button v-if="cartItems.length > 0 && customer.order_id === undefined" type="button"
                            @click="clearAll" class="btn btn-sm  btn-danger">
                            <i class="fas fa-trash-alt"></i>
                          </button>
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item, index) in cartItems" :key="index">
                        <td>
                          <div class="row d-flex flex-row">
                            <div class="col-sm-6 text-left">
                              <img :src="item.image" class="img-thumbnail img-xs">
                            </div>
                            <div class="col-sm-6 text-left m-0 p-0 ">
                              <h6 class="text-left title text-truncate" style="font-weight: bold;">{{ item.name }}</h6>
                            </div>
                          </div>
                        </td>
                        <td>
                          <div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
                            <button type="button" class="m-btn btn-light btn btn-default" @click="decreaseQty(item)">
                              <i class="fa fa-minus"></i>
                            </button>
                            <button type="button" class="m-btn btn-light btn btn-default" disabled>
                              {{ item.qty }}
                            </button>
                            <button type="button" class="m-btn btn-light btn btn-default" @click="increaseQty(item, 1)">
                              <i class="fa fa-plus"></i>
                            </button>
                          </div>
                        </td>
                        <td class="text-right">
                          <strong>₱{{ item.totalPrice.toFixed(2) }}</strong>
                        </td>
                        <td>
                          <button v-if="customer.order_id === undefined" class="btn btn-outline-danger btn-sm"
                            type="button" @click="removeFromCart(item)">
                            <i class="fas fa-times"></i>
                          </button>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            <div class="box p-2" v-if="userdata.role !== 'waiter'">
              <div class="row p-0 m-0">
                <div class="col-md-6">
                  <dt>Tax: </dt>
                </div>
                <div class="col-md-6 d-flex flex-row-reverse">
                  <dd class="text-right">{{ taxValue }}%</dd>
                </div>
              </div>
              <div class="row p-0 m-0">
                <div class="col-md-6">
                  <dt>Discount:</dt>
                </div>
                <div class="col-md-6 d-flex flex-row-reverse">
                  <dd class="text-right"><a href="#">{{ discountValue }}%</a></dd>
                </div>
              </div>
              <div class="row p-0 m-0">
                <div class="col-md-6">
                  <dt>Sub Total:</dt>
                </div>
                <div class="col-md-6 d-flex flex-row-reverse">
                  <dd class="text-right">₱{{ subTotal }}</dd>
                </div>
              </div>
              <div class="row p-0 m-0">
                <div class="col-md-6">
                  <dt>Total: </dt>
                </div>
                <div class="col-md-6 d-flex flex-row-reverse">
                  <dd class="text-right h4 b"> ₱{{ totalCost }} </dd>
                </div>
              </div>
            </div> <!-- box.// -->
            <div class="box mt-2" v-if="userdata.role !== 'waiter'">
              <div class="row bg-primary text-white d-flex flex-row-reverse align-items-center">
                <div class="col-md-6">
                  <div class="input-group">
                    <span class="input-group-text bg-primary text-white "
                      style="vertical-align: middle;font-weight: bold;border: none; font-size: x-large;">₱</span>
                    <input :disabled="(cartItems.length < 1)" type="number" min="0" ref="tenderedCash"
                      class="form-control bg-primary text-white rounded-lg px-2 outline-none"
                      style="text-align:right; font-weight: bold; font-size: x-large; border: none;" v-model="totalCash">
                  </div>
                </div>
                <div class="col-md-6">
                  <dd class="text-right h3 b" style="margin-right: 10px;"> Cash</dd>
                </div>
              </div>
              <div class="row mt-2" v-if="userdata.role !== 'waiter'">
                <div class="col-md-12">
                  <div class="row row-cols-1 row-cols-md-4">
                    <div class="col mb-1" v-for="item in cashDenominations" :key="item.id">
                      <button :disabled="(cartItems.length < 1)"
                        class="btn bg-white rounded-lg shadow hover:shadow-xs focus:outline-none inline-block px-2 py-0 text-sm"
                        @click="addToCash(item.value)"><span>{{
                          item.label }}</span></button>
                    </div>
                  </div>
                </div>
              </div>
              <div
                :class="(totalChange < 0 ? 'row mt-2 mb-2 bg-danger text-white' : 'row mt-2 mb-2 bg-success text-white')"
                v-if="userdata.role !== 'waiter'">
                <div class="col-md-6">
                  <dt v-if="totalChange >= 0">Change: </dt>
                </div>
                <div class="col-md-6 d-flex flex-row-reverse">
                  <dd class="text-right h4 b"> ₱{{ totalChange }} </dd>
                </div>
              </div>
              <!-- <div class="row">
                <div class="col-md-4">
                  <button :disabled="(cartItems.length < 1)" class="btn btn-light btn-default btn-sm btn-block"
                    @click="printBill" style="width: 125px;">
                    <i class="fa fa-print"></i> Print Bill [F1]
                  </button>
                </div>
                <div class="col-md-4">
                  <button :disabled="(cartItems.length < 1)" class="btn btn-danger btn-default btn-sm btn-block"
                    style="width: 125px;" @click="placeOrder">
                    <i class="fa fa-bookmark"></i> Place Order [F2]
                  </button>
                </div>
                <div class="col-md-4 d-flex flex-row-reverse" v-if="userdata.role !== 'waiter'">
                  <button :disabled="(cartItems.length < 1)" class="btn btn-primary btn-sm btn-block" @click="payOrder"
                    style="width: 125px;">
                    <i class="fa fa-shopping-bag"></i> Charge [F3]
                  </button>
                </div>
              </div> -->
            </div>
          </div>
        </div>
      </div>
      <div class="tab-pane fade" id="orders" role="tabpanel" aria-labelledby="orders-tab">
        <div class="row mt-2">
          <div class="col-md-12">
            <div class="row">
              <div class="col-md-12">
                <div class="row row-cols-1 row-cols-md-4">
                  <div class="col mb-4" v-for="(item, index) in resto_allorders" :key="item.id">
                    <div class="card" style="transition: transform 0.2s ease-in-out;">
                      <div
                        :class="`card-header d-flex justify-content-between align-items-center text-white ${(item.status === 'closed') ? 'bg-danger' : (item.status === 'void' ? 'bg-warning' : (item.status === 'served' ? 'bg-info' : 'bg-success'))}`">
                        <h5 class="card-title">#{{ Number(item.id).toString().padStart(5, "0") }}</h5>
                        <p class="card-subtitle" style="font-size: 12px;">{{ item.datestarted }}</p>
                      </div>
                      <div class="card-body" style="height: 250px; overflow-y: auto;">
                        <ul style="list-style-type: none; padding-left: 20px;">
                          {{ item.order_type.toString().toUpperCase() }}/{{ item.customer_name }} <span
                            style="font-style: italic;">({{ item.status }})</span>
                          <li v-for="orderItem in item.order_items" :key="orderItem.id"
                            style="font-weight:bold; font-size:16px; padding-left:30px;">
                            {{ orderItem.qty }} &times; {{ orderItem.name }}
                          </li>
                        </ul>
                      </div>
                      <div class="card-footer d-flex justify-content-between" v-if="item.status === 'progress'">
                        <span>
                          <button class="btn btn-sm btn-outline-primary" @click="doneServe(item)">Done</button>
                          &NonBreakingSpace;
                          <button class="btn btn-sm btn-outline-danger" @click="toggleTimer(item)">
                            {{ item.isRunning ? 'Hold' : 'Resume' }}
                          </button>
                        </span>

                        <span>{{ item.timePassed }}</span>

                      </div>
                    </div>

                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="tab-pane fade" id="inventory" role="tabpanel" aria-labelledby="inventory-tab">
        <div class="row">
          <div class="col-md-3">
            <form @submit.prevent="saveInventory" class="no-print">
              <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" v-model="stock.name" required>
              </div>
              <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <input type="text" class="form-control" id="description" v-model="stock.description">
              </div>
              <div class="mb-3">
                <label for="sku" class="form-label">SKU</label>
                <input type="text" class="form-control" id="SKU" v-model="stock.sku" required>
              </div>
              <div class="mb-3">
                <label for="imgurl" class="form-label">Image URL</label>
                <input type="text" class="form-control" id="imgurl" v-model="stock.imageUrl" required>
              </div>
              <div class="mb-3">
                <label for="is-available" class="form-label">Category</label>
                <select class="form-select" id="is-available" v-model="stock.category" required>
                  <option value="">-- Select --</option>
                  <option value="Appetizers">Appetizers</option>
                  <option value="Asian Classics">Asian Classics</option>
                  <option value="Sizzlers">Sizzlers</option>
                  <option value="Soup">Soup</option>
                  <option value="Drinks">Drinks</option>
                  <option value="Desserts & Sweets">Desserts & Sweets</option>
                  <option value="Pizza, Pasta, Sandwich">Pizza, Pasta, Sandwich</option>
                  <option value="Breakfast">Breakfast</option>
                  <option value="Rice">Rice</option>
                  <option value="Miscellaneous">Miscellaneous</option>
                </select>
              </div>

              <div class="mb-3">
                <label for="qty" class="form-label">Qty</label>
                <input type="number" min="0" class="form-control" id="qty" v-model="stock.stocks" required>
              </div>


              <div class="mb-3">
                <label for="price" class="form-label">Price</label>
                <input type="number" min="0" class="form-control" id="price" v-model="stock.price" required>
              </div>

              <div class="mb-3">
                <label for="is-available" class="form-label">Availability</label>
                <select class="form-select" id="is-available" v-model="stock.isAvailable" required>
                  <option value="">-- Select --</option>
                  <option value=true>Yes</option>
                  <option value=false>No</option>
                </select>
              </div>
              <button type="submit" class="btn btn-primary">{{ isUpdatingInventory ? 'Update'
                :
                'Save'
              }}</button>
            </form>
          </div>
          <div class="col-md-9">
            <div>
              <table-component :mainHeaders=stocksOptions :mainItems="filtereditemarray" :subHeaders="inventorysubitem"
                @edit-action="editInventory" :editable="true" :toggleable="true" :slotsub="true">
                <template #subcontent="{ data }">
                  <table-component :mainHeaders="inventorysubitem" :mainItems="data" />
                </template>
                <template #content="{ data }">
                  <template v-if="data.h === 'isAvailable'">
                    <span v-if="data.dt.isAvailable">Yes</span>
                    <span v-else>No</span>
                  </template>
                  <template v-else="data.h==='imageUrl'">
                    <img :src="data.dt.imageUrl" class="img-thumbnail" style="height: 80px;width: 80px;" />
                  </template>
                </template>
              </table-component>
            </div>
          </div>
        </div>
      </div>
      <div class="tab-pane fade" id="reports" role="tabpanel" aria-labelledby="reports-tab">
        <div class="row">
          <div class="col-sm-1">
            <ul class="nav nav-tabs flex-column">
              <li class="nav-item">
                <a class="nav-link rotated-text active" data-bs-toggle="tab" href="#bytransaction">Transactions</a>
              </li>
              <li class="nav-item">
                <a class="nav-link rotated-text" data-bs-toggle="tab" href="#byitems">Orders</a>
              </li>
            </ul>
          </div>
          <div class="col-sm-11">
            <div class="tab-content">
              <div id="bytransaction" class="tab-pane active">
                <div class="row">
                  <div class="col-sm-2">
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
                  </div>
                  <div class="col-sm-10">
                    <table-component :mainHeaders=transactionsOptions :mainItems="superfilteredTransactions"
                      :subHeaders="transactionitem" :toggleable="true" />
                  </div>
                </div>
              </div>
              <div id="byitems" class="tab-pane">
                <div class="row">
                  <div class="col-sm-2">
                    <div class="form-group">
                      <label for="date-filter">Date Filter:</label>
                      <select class="form-control" id="date-filter" v-model="resitemdateFilter">
                        <option value="any">Any</option>
                        <option value="range">Date Range</option>
                      </select>
                      <div v-if="resitemdateFilter === 'range'">
                        <div class="form-group">
                          <input type="date" class="form-control" v-model="resitemfromDate">
                        </div>
                        <div class="form-group">
                          <input type="date" class="form-control" v-model="resitemtoDate">
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-sm-10">
                    <table-component :mainHeaders=transactionordersoptions :mainItems="filteredtransactionorders"
                      :subHeaders="transactionitem" :toggleable="true" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>


  </div>

  <div style="display:none;">
    <div class="receipt" id="billing-statement">
      <div style="text-align: center;">
        <span style="font-size: 18px; font-weight: bold;">PANTUKAN WATERWORLD RESORT</span><br>
        <span>8809 MAGNAGA, PANTUKAN</span><br>
        <span>+63917 102 5273</span>
      </div>
      <h2 style="text-align: center;font-size: 14px;">***COPY RECEIPT***</h2>
      <hr style="border: none; border-top: 1px dashed #000; margin-top: 10px; margin-bottom: 10px;">
      <div style="display: flex; justify-content: space-between; font-weight: bold;">
        <div>{{ new Date().toLocaleDateString() }}</div>
        <div>{{ getTime() }}</div>
      </div>
      <hr style="margin-top: 5px; margin-bottom: 5px;">
      <div style="display: flex; justify-content: space-between;">
        <div>TRANS#: {{ transactionno }}</div>
        <div>CUST#: {{ customerno }}</div>
      </div>
      <table style="width: 100%; margin-top: 10px;">
        <thead>
          <tr>
            <th>#</th>
            <th>Item</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in cartItems" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ item.name }}</td>
            <td>{{ parseFloat(item.price).toFixed(2) }}</td>
          </tr>
        </tbody>
      </table>
      <div style="margin-top: 10px;">
        <table style="width: 100%; margin-top: 10px;">
          <tr>
            <td> </td>
            <td>CASHIER:</td>
            <td>{{ userdata.username }}</td>
          </tr>
          <tr>
            <td> </td>
            <td>ORDER ID:</td>
            <td>{{ (this.customer.order_id === undefined) ? 'N/A' : this.customer.order_type + '/' + this.customer.order_id
            }}</td>
          </tr>
          <tr>
            <td colspan="3" style="height: 10px;"></td>
          </tr>
          <tr>
            <td> </td>
            <td>SUBTOTAL:</td>
            <td>₱{{ subTotal }}</td>
          </tr>
          <tr>
            <td> </td>
            <td>TAX:</td>
            <td>₱{{ (parseFloat(taxValue) / 100 * parseFloat(subTotal)).toFixed(2) }}</td>
          </tr>
          <tr>
            <td> </td>
            <td>DISCOUNT:</td>
            <td>₱{{ (parseFloat(discountValue) / 100 * parseFloat(subTotal)).toFixed(2) }}</td>
          </tr>
          <tr>
            <td> </td>
            <td>TOTAL:</td>
            <td>₱{{ parseFloat(totalCost).toFixed(2) }}</td>
          </tr>
          <tr>
            <td> </td>
            <td>Change:</td>
            <td>₱{{ parseFloat(totalChange).toFixed(2) }}</td>
          </tr>
        </table>
        <div style="text-align: center;">
          X:_____________________________________
          <br>
          SIGNATURE
        </div>
      </div>
      <h2 style="text-align: center;font-size: 14px;">***COPY RECEIPT***</h2>
      <p style="text-align: center;">THANK YOU</p>
      <!-- <img src="@/assets/barcode.png"> -->
    </div>
  </div>
</template>
<script>
import { useAuthStore } from "@/stores/authStore";
import TopNavBarComponent from "@/components/common/TopNavBar.vue";
import TableComponent from "@/components/common/GenericTable.vue";
import CardItems from "../common/CardItems.vue";
import axios from 'axios';

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

function formatDate(date) {
  const options = {
    month: '2-digit',
    day: '2-digit',
    year: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
    second: 'numeric'
  };
  return new Intl.DateTimeFormat('en-US', options).format(date);
}

export default {
  components: {
    TopNavBarComponent,
    TableComponent,
    CardItems,
  },
  data() {
    return {
      currentItem: null,
      inquiretoggle: false,
      restypeFilter: "0",
      resdateFilter: "any",
      resfromDate: null,
      restoDate: null,
      customer: {
        reference_id: null,
        type: '',
        identifier: '',
        order_type: '',
        items: [],
      },
      orderStaus: false,
      barcodeText: "",
      searchText: "",
      isUpdatingInventory: false,
      stock: {
        name: "",
        imageUrl: "",
        description: "",
        sku: "",
        category: "",
        stocks: 0,
        price: 0,
        inventory: "",
        isAvailable: "",
      },
      transactionitem: [{
        'label': 'Name',
        'field': 'name',
      }, {
        'label': 'Category',
        'field': 'category',
      }, {
        'label': 'Qty',
        'field': 'qty',
      }, {
        'label': 'Price',
        'field': 'price',
      }, {
        'label': 'Total',
        'field': 'totalPrice',
      }],
      transactionsOptions: [{
        'label': '',
        'field': 'toggle',
        'sortable': false,
      }, {
        'label': 'Transaction ID',
        'field': 'id',
        'sortable': true,
      }, {
        'label': 'Sub-Total',
        'field': 'subTotal',
        'sortable': true,
        'reducible': true
      }, {
        'label': 'Tax Value',
        'field': 'taxValue',
        'sortable': true,
      }, {
        'label': 'Discount Value',
        'field': 'discountValue',
        'sortable': true,
      }, {
        'label': 'Total',
        'field': 'totalCharge',
        'sortable': true,
        'reducible': true
      }, {
        'label': 'Date',
        'field': 'date_created',
        'sortable': true,
      }, {
        'label': 'Processed By',
        'field': 'processedBy',
        'sortable': true,
      }],
      transactionordersoptions: [{
        'label': '',
        'field': 'toggle',
        'sortable': false,
      }, {
        'label': 'Order ID',
        'field': 'id',
        'sortable': true,
      }, {
        'label': 'Type',
        'field': 'order_type',
        'sortable': true,
      }, {
        'label': 'Reference #',
        'field': 'table_id',
        'sortable': true,
      }, {
        'label': 'Reference Name',
        'field': 'customer_name',
        'sortable': true,
      }, {
        'label': 'Date',
        'field': 'date_created',
        'sortable': true,
      }, {
        'label': 'Processed By',
        'field': 'processedBy',
        'sortable': true,
      }, {
        'label': 'Status',
        'field': 'status',
        'sortable': true,
      }],
      stocksOptions: [{
        'label': '',
        'field': 'toggle',
        'sortable': false,
      }, {
        'label': 'Image',
        'field': 'imageUrl',
        'slot': true,
      }, {
        'label': 'Name',
        'field': 'name',
        'sortable': true
      }, {
        'label': 'Description',
        'field': 'description',
        'sortable': true
      }, {
        'label': 'SKU',
        'field': 'sku',
        'sortable': true
      }, {
        'label': 'Category',
        'field': 'category',
        'sortable': true
      }, {
        'label': 'Qty',
        'field': 'stocks',
        'sortable': true
      }, {
        'label': 'Price',
        'field': 'price',
        'sortable': true
      }, {
        'label': 'Is Available?',
        'field': 'isAvailable',
        'sortable': true,
        'slot': true,
      }, {
        'label': '',
        'field': 'action',
        'sortable': false
      }],
      inventorysubitem: [{
        'label': 'Type',
        'field': 'type',
      }, {
        'label': 'Qty',
        'field': 'qty',
      }, {
        'label': 'Stocks',
        'field': 'stocks',
      }, {
        'label': 'processedBy',
        'field': 'processedBy',
      }, {
        'label': 'Date',
        'field': 'date_created',
      },],
      activeTab: 'alltab',
      taxValue: 12,
      discountValue: 0,
      totalCash: 0,
      resto_order: [

      ],
      resto_orders: [

      ],
      resto_allorders: [

      ],
      resto_tables: [

      ],
      resto_takeouts: [

      ],
      resto_onholds: [

      ],
      itemarray: [

      ],
      cartItems: [

      ],
      transactions: [

      ],
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
    }
  },
  async created() {

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

    this.loadAlldata();
    this.loadCookiedata();
  },
  computed: {
    userdata() {
      const authStore = useAuthStore();
      const user = authStore.user;
      return user;
    },
    getTimePassed() {
      return function (datestarted) {
        const startedTime = new Date(datestarted).getTime();
        const currentTime = new Date().getTime();
        const timeDiff = currentTime - startedTime;
        const minutes = Math.floor(timeDiff / (1000 * 60));
        const seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);
        return `${minutes}:${seconds.toString().padStart(2, '0')}`;
      };
    },
    subTotal() {
      return this.cartItems.reduce((acc, item) => acc + parseFloat(item.totalPrice), 0).toFixed(2);
    },
    totalCost() {
      return (this.subTotal * (1 + this.taxValue / 100) * (1 - this.discountValue / 100)).toFixed(2);
    },
    totalChange() {
      return (this.totalCash - this.totalCost).toFixed(2);
    },
    filteredresto_takeouts() {
      return this.resto_takeouts.map(item => {
        const order = this.resto_order.filter(o => o.table_id === item.id);
        if (order.length > 0) {
          const order_data = order[0];
          const order_id = order_data.id;
          const order_type = order_data.order_type;
          const order_cname = order_data.customer_name;
          const order_status = order_data.status;
          const order_items = JSON.parse(order_data.items);
          return {
            ...item,
            order_id,
            order_type,
            order_cname,
            order_status,
            order_items,
          };
        } else {
          return {
            ...item,
          };
        }
      }).filter(item => item.status !== 'done')
    },
    filteredresto_tables() {
      return this.resto_tables.map(item => {
        const order = this.resto_order.filter(o => o.table_id === item.id);
        if (order.length > 0) {
          const order_data = order[0];
          const order_id = order_data.id;
          const order_type = order_data.order_type;
          const order_cname = order_data.customer_name;
          const order_status = order_data.status;
          const order_items = JSON.parse(order_data.items);
          return {
            ...item,
            order_id,
            order_type,
            order_cname,
            order_status,
            order_items,
          };
        } else {
          return {
            ...item,
          };
        }
      })
    },
    filteredtransactionorders() {
      return this.resto_allorders.map(item => {
        const timePassed = this.getTimePassed(item.datestarted);;
        const isRunning = (item.status === 'progress') ? true : false;
        return {
          ...item,
          timePassed,
          isRunning,
        }
      });
    },
    filteredresto_onholds() {
      return this.resto_onholds.map(item => {
        const order = this.resto_order.filter(o => o.table_id === item.id);
        if (order.length > 0) {
          const order_data = order[0];
          const order_id = order_data.id;
          const order_type = order_data.order_type;
          const order_cname = order_data.customer_name;
          const order_status = order_data.status;
          const order_items = JSON.parse(order_data.items);
          return {
            ...item,
            order_id,
            order_type,
            order_cname,
            order_status,
            order_items,
          };
        } else {
          return {
            ...item,
          };
        }
      }).filter(item => item.status !== 'done')
    },
    filtereditemarray() {
      return this.itemarray.map(item => {
        const searchCode = item.name + "~" + item.description + "~" + item.sku;
        const items = JSON.parse(item.inventory);
        return {
          ...item,
          items,
          searchCode
        };
      }).filter(item => item.searchCode.toString().toLowerCase().includes(this.searchText.toLowerCase()));
    },
    superfilteredTransactions() {

      let filtered = this.filteredTransactions;
      if (this.resdateFilter === 'range' && this.resfromDate && this.restoDate) {
        filtered = filtered.filter(transaction => {
          return parseDate2(transaction.date_created) >= parseDate(this.resfromDate) && parseDate2(transaction.date_created) <= parseDate(this.restoDate);
        });
      }

      return filtered;
    },
    itemfilteredTransactions() {
      let itemsArray = [];
      let filtered = this.transactions.map(item => {
        const items = JSON.parse(item.items);
        return {
          ...item,
          items
        };
      })
      for (let obj of filtered) {
        for (let key in obj) {
          if (key === "items") {
            itemsArray.push(...obj[key]);
          }
        }
      }
      return itemsArray
    },
    transactionno() {
      return parseFloat(this.transactions[this.transactions.length - 1].id) + 1;
    },
    customerno() {
      const today = new Date().toLocaleDateString();
      return this.transactions.filter(transaction => {
        const transactionDate = new Date(transaction.date_created).toLocaleDateString();
        return transactionDate === today;
      }).length + 1;
    },
    filteredTransactions() {
      return this.transactions.map(item => {
        const items = JSON.parse(item.items);
        return {
          ...item,
          items
        };
      })
    },
  },
  methods: {
    loadAlldata() {
      this.getInventory();
      this.getTransaction();
      this.getRestoTables();
      this.getRestoTakeout();
      this.getRestoOnholds();
      this.getAllOrders();
      this.getCurrentOrders();
    },
    loadCookiedata() {
      const cookies = document.cookie.split(';'); // Split cookies into an array

      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim(); // Remove whitespace from the cookie string
        if (cookie.startsWith('taxValue=')) {
          const taxValue = cookie.substring('taxValue='.length); // Extract the value
          this.taxValue = parseFloat(taxValue).toFixed(2);
          break;
        }
      }
    },
    getTime() {
      const date = new Date();
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');
      return `${hours}:${minutes}`;
    },
    toggleTimer(item) {
      item.isRunning = !item.isRunning;
    },
    async doneServe(item) {
      const customer_id = item.table_id;
      const customer_type = item.order_type;
      const customer_name = item.customer_name;
      const customer_orderId = item.id || -1;
      if (customer_id !== null) {
        const res = await axios.post(`${this.API_URL}restoorders/filter/`, { columnName: 'id', columnKey: customer_orderId });
        const existingOrder = res.data;
        axios
          .put(`${this.API_URL}restoorders/${existingOrder[0].id}/`, {
            order_type: customer_type,
            table_id: customer_id,
            customer_name: customer_name,
            status: 'served',
            items: JSON.stringify(item.items),
            processedBy: this.userdata.fName + " " + this.userdata.lName,
          })
      }
    },
    activatePOS() {
      this.$nextTick(() => {
        this.setFocus();
      });
    },
    setFocus() {
      $("#posTab").focus();
      this.$refs.tenderedCash.focus();
    },
    setActiveTab(tab) {
      this.activeTab = tab
    },
    holdCustomer() {
      if (this.cartItems.length >= 1 && this.customer.reference_id === null) {
        this.$swal.fire({
          title: 'Enter customer\'s name',
          input: 'text',
          inputPlaceholder: 'Enter customer\'s name',
          inputAttributes: {
            minlength: 3, // Minimum length of 3 characters
            maxlength: 24, // Maximum length of 24 characters
          },
          showCancelButton: true,
          confirmButtonText: 'Submit',
          cancelButtonText: 'Cancel',
          allowOutsideClick: false,
        }).then((result) => {
          if (result.isConfirmed) {
            const inputValue = result.value;
            axios.post(`${this.API_URL}restoonholds/`, {
              name: inputValue,
              status: "on hold",
            }).then(response => {
              const item = response.data;
              this.getRestoOnholds();
              this.customer = {
                reference_id: item.id,
                type: "on-hold",
                identifier: item.name,
              }
              this.placeOrder();
            })
          }
        });
      }
    },
    onholdAction(item) {
      this.customer = {
        reference_id: item.id,
        type: "on-hold",
        identifier: item.name,
      }
      if ('order_id' in item) {
        this.cartItems = item.order_items;
        this.customer.order_id = item.order_id;
        this.customer.order_type = item.order_type;
      }
      this.customer.items = (item.order_items || []);
      $("#pos-tab").tab('show');
    },
    setDiscount() {
      this.$swal.fire({
        title: 'Set discount value',
        input: 'number',
        inputPlaceholder: 'Enter discount percentage',
        inputAttributes: {
          min: 0, // Minimum value
          max: 100,
          step: 'any',
        },
        showCancelButton: true,
        confirmButtonText: 'Submit',
        cancelButtonText: 'Cancel',
        allowOutsideClick: false,
      }).then((result) => {
        if (result.isConfirmed) {
          const inputValue = result.value;
          if (inputValue !== "") {
            this.discountValue = parseFloat(inputValue).toFixed(2);
            this.$refs.tenderedCash.focus();
          }
        }
      });
    },
    setTax() {
      this.$swal.fire({
        title: 'Set tax value',
        input: 'number',
        inputPlaceholder: 'Enter added tax percentage',
        inputAttributes: {
          min: 0, // Minimum value
          max: 100,
          step: 'any',
        },
        showCancelButton: true,
        confirmButtonText: 'Submit',
        cancelButtonText: 'Cancel',
        allowOutsideClick: false,
      }).then((result) => {
        if (result.isConfirmed) {
          const inputValue = result.value;
          if (inputValue !== "") {
            this.taxValue = parseFloat(inputValue).toFixed(2);

            const expirationDate = new Date();
            expirationDate.setFullYear(expirationDate.getFullYear() + 30);
            document.cookie = `taxValue=${this.taxValue}; expires=${expirationDate.toUTCString()}; path=/`;
            this.$refs.tenderedCash.focus();
          }
        }
      });
    },
    setQty() {
      if (this.cartItems.length < 1) {
        return;
      }
      this.$swal.fire({
        title: 'Set quantity value',
        input: 'number',
        inputPlaceholder: 'Enter quantity',
        inputAttributes: {
          min: 0, // Minimum value
        },
        showCancelButton: true,
        confirmButtonText: 'Submit',
        cancelButtonText: 'Cancel',
        allowOutsideClick: false,
      }).then((result) => {
        if (result.isConfirmed) {
          const inputValue = result.value;
          if (inputValue !== "") {
            this.increaseQty(this.currentItem, inputValue)
            this.$refs.tenderedCash.focus();
          }
        }
      });
    },
    increaseQty(item, plus) {
      this.plusQty(item, plus);
    },
    plusQty(item, add) {
      if (parseFloat(item.qty) + parseFloat(add) <= item.stocks) {
        item.qty = parseFloat(item.qty) + parseFloat(add);
      } else {
        this.$swal({
          title: "Out of Stock",
          text: `Item unavailable. Maximum quantity added.`,
          icon: "warning",
          buttons: {
            confirm: "OK",
          },
        });
        item.qty = item.stocks;
      }
      this.updatePrice(item)
    },
    decreaseQty(item) {
      if (item.qty > 1) {
        item.qty--
        this.updatePrice(item)
      }
    },
    cancelTakeOut(id) {
      this.$swal.fire({
        title: 'Delete Takeout Order',
        text: 'Are you sure you want to delete this takeout order?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Delete',
        cancelButtonText: 'Cancel',
        allowOutsideClick: false,
      }).then((result) => {
        if (result.isConfirmed) {
          // Perform deletion logic here
          axios.get(this.API_URL + `restotakeouts/delete/${id}/`).then(response => {
            this.getRestoTakeout();
            this.$swal.fire(
              'Deleted!',
              'The takeout order has been successfully deleted.',
              'success'
            );
          })

        }
      });
    },
    addnewTakeout() {
      this.$swal.fire({
        title: 'Enter customer\'s name',
        input: 'text',
        inputPlaceholder: 'Enter customer\'s name',
        showCancelButton: true,
        confirmButtonText: 'Submit',
        cancelButtonText: 'Cancel',
        allowOutsideClick: false,
      }).then((result) => {
        if (result.isConfirmed) {
          const inputValue = result.value;
          axios.post(`${this.API_URL}restotakeouts/`, {
            name: inputValue,
            status: "on process",
          }).then(response => {
            this.getRestoTakeout();
          })
        }
      });
    },
    voidAction() {
      if (this.cartItems.length < 1) {
        return;
      }
      this.$swal.fire({
        title: 'Void',
        text: 'Are you sure you want to void this order?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Void',
        cancelButtonText: 'Cancel',
        allowOutsideClick: false,
      }).then(async (result) => {
        if (result.isConfirmed) {
          const customer = this.customer;
          const customer_id = customer.reference_id;
          const customer_type = customer.type;
          const customer_name = customer.identifier;
          const customer_orderId = customer.order_id || -1;
          if (customer_id !== null) {
            const res = await axios.post(`${this.API_URL}restoorders/filter/`, { columnName: 'id', columnKey: customer_orderId });
            const existingOrder = res.data;
            axios
              .put(`${this.API_URL}restoorders/${existingOrder[0].id}/`, {
                order_type: customer_type,
                table_id: customer_id,
                customer_name: customer_name,
                status: 'void',
                items: JSON.stringify(this.cartItems),
                processedBy: this.userdata.fName + " " + this.userdata.lName,
              })
            for (const item of this.cartItems) {
              const items = item.inventory;
              items.push({ "type": "stockin", "qty": parseFloat(item.qty), "stocks": parseFloat(item.stocks), "date_created": formatDate(new Date()), "processedBy": (this.userdata.fName + " " + this.userdata.lName).toString() });
              const inventory = JSON.stringify(items);
              axios
                .put(`${this.API_URL}restoitem/${item.id}/`, {
                  sku: item.sku,
                  name: item.name,
                  description: item.description,
                  imageUrl: item.image,
                  category: item.category,
                  price: item.price,
                  inventory: inventory,
                  isAvailable: item.isAvailable,
                  stocks: parseFloat(item.stocks),
                });
            }
            this.taskRecord(`action:/voidorder/${customer_orderId}`);
            this.$swal({
              title: 'Success',
              icon: "success",
              title: "Order voided successfully!"
            }).then((result) => {
              document.location.reload();
            });
          }
        }
      });
    },
    takeoutAction(item) {
      this.customer = {
        reference_id: item.id,
        type: "take-out",
        identifier: item.name,
      }
      if ('order_id' in item) {
        this.cartItems = item.order_items;
        this.customer.order_id = item.order_id;
        this.customer.order_type = item.order_type;
      }
      this.customer.items = (item.order_items || []);
      $("#pos-tab").tab('show');
    },
    dineInAction(item) {
      this.customer = {
        reference_id: item.id,
        type: "dine-in",
        identifier: item.name,
      }
      if ('order_id' in item) {
        this.cartItems = item.order_items;
        this.customer.order_id = item.order_id;
        this.customer.order_type = item.order_type;
      }
      this.customer.items = (item.order_items || []);
      $("#pos-tab").tab('show');
    },
    async placeOrder() {

      if (this.cartItems.length < 1) {
        return;
      }

      if (this.customer.reference_id === null) {
        $("#tables-tab").tab('show');
        return;
      }

      const confirmMessage = 'Are you sure you want to place this order?';
      const result = await this.$swal.fire({
        title: 'Confirmation',
        text: confirmMessage,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, place it!',
        cancelButtonText: 'Cancel',
        allowOutsideClick: false,
      });

      if (result.isConfirmed) {
        const countdownMessage = 'Order will be saved in <span id="countdown">5</span> seconds. Do you want to cancel?';
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
          allowOutsideClick: false,
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

        const customer = this.customer;
        const customer_id = customer.reference_id;
        const customer_type = customer.type;
        const customer_name = customer.identifier;
        const customer_orderId = customer.order_id || -1;
        if (customer_id !== null) {
          if (customer_type === "dine-in" || customer_type === "take-out" || customer_type === "on-hold") {

            const res = await axios.post(`${this.API_URL}restoorders/filter/`, { columnName: 'id', columnKey: customer_orderId });
            const existingOrder = res.data;
            if (existingOrder.length > 0) {

              for (const item of (this.cartItems || this.cartItems.filter(item => !this.customer.items.includes(item)))) {
                const items = item.inventory;
                const curstock = parseFloat(item.stocks) - parseFloat(item.qty);
                const prevstock = parseFloat(items[items.length - 1].stocks);
                if (prevstock - curstock > 0) {
                  items.push({ "type": "stockout", "qty": prevstock - curstock, "stocks": curstock, "date_created": formatDate(new Date()), "processedBy": (this.userdata.fName + " " + this.userdata.lName).toString() });
                }
                const inventory = JSON.stringify(items);
                axios
                  .put(`${this.API_URL}restoitem/${item.id}/`, {
                    sku: item.sku,
                    name: item.name,
                    description: item.description,
                    imageUrl: item.image,
                    category: item.category,
                    price: item.price,
                    inventory: inventory,
                    isAvailable: item.isAvailable,
                    stocks: parseFloat(item.stocks) - parseFloat(item.qty),
                  });
              }

              axios
                .put(`${this.API_URL}restoorders/${existingOrder[0].id}/`, {
                  order_type: customer_type,
                  table_id: customer_id,
                  customer_name: customer_name,
                  status: 'progress',
                  items: JSON.stringify(this.cartItems),
                  processedBy: this.userdata.fName + " " + this.userdata.lName,
                })
              this.taskRecord(`action:/placeorder/update/${customer_name}`);
              this.$swal({
                title: 'Success',
                icon: "success",
                title: "Order updated successfully!"
              }).then((result) => {
                document.location.reload();
              });

            } else {

              for (const item of this.cartItems) {
                const items = item.inventory;
                const curstock = parseFloat(item.stocks) - parseFloat(item.qty);
                const prevstock = parseFloat(items[items.length - 1].stocks);
                if (prevstock - curstock > 0) {
                  items.push({ "type": "stockout", "qty": prevstock - curstock, "stocks": curstock, "date_created": formatDate(new Date()), "processedBy": (this.userdata.fName + " " + this.userdata.lName).toString() });
                }
                const inventory = JSON.stringify(items);
                axios
                  .put(`${this.API_URL}restoitem/${item.id}/`, {
                    sku: item.sku,
                    name: item.name,
                    description: item.description,
                    imageUrl: item.image,
                    category: item.category,
                    price: item.price,
                    inventory: inventory,
                    isAvailable: item.isAvailable,
                    stocks: parseFloat(item.stocks) - parseFloat(item.qty),
                  });
              }

              axios
                .post(`${this.API_URL}restoorders/`, {
                  order_type: customer_type,
                  table_id: customer_id,
                  customer_name: customer_name,
                  status: 'progress',
                  items: JSON.stringify(this.cartItems),
                  processedBy: this.userdata.fName + " " + this.userdata.lName,
                })
              this.taskRecord(`action:/placeorder/posted/${customer_name}`);
              this.$swal({
                title: 'Success',
                icon: "success",
                title: "Order placed successfully!"
              }).then((result) => {
                document.location.reload();
              });

            }

          } else {
            //take-out
          }
        }

      }

    },
    addToCash(d) {
      this.totalCash = isNaN(parseFloat(this.totalCash)) ? 0 : parseFloat(this.totalCash) + d;
    },
    clearAll() {
      if (this.cartItems.length > 0 && this.customer.order_id === undefined) {
        this.customer = {
          reference_id: null,
          type: '',
          identifier: '',
          order_type: '',
          items: [],
        },
          this.cartItems = [];
        this.totalCash = 0;
      }
    },
    resetCounter() {
      this.clearAll();
      this.customer = {
        reference_id: null,

      }
    },
    async payOrder() {

      if (this.cartItems.length < 1) {
        return;
      }

      if (this.totalCash < this.totalCost) {
        this.$swal({
          title: 'Warning',
          text: 'The tendered amount is less than the total cost.',
          icon: 'warning',
        });
        return;
      }

      const confirmMessage = 'Are you sure you want to save this transaction?';
      const result = await this.$swal.fire({
        title: 'Confirmation',
        text: confirmMessage,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, save it!',
        cancelButtonText: 'Cancel',
        allowOutsideClick: false,
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
          allowOutsideClick: false,
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

        for (const item of (this.cartItems || this.cartItems.filter(item => !this.customer.items.includes(item)))) {
          const items = item.inventory;
          const curstock = parseFloat(item.stocks) - parseFloat(item.qty);
          const prevstock = parseFloat(items[items.length - 1].stocks);
          if (prevstock - curstock > 0) {
            items.push({ "type": "stockout", "qty": prevstock - curstock, "stocks": curstock, "date_created": formatDate(new Date()), "processedBy": (this.userdata.fName + " " + this.userdata.lName).toString() });
          }
          const inventory = JSON.stringify(items);
          axios
            .put(`${this.API_URL}restoitem/${item.id}/`, {
              sku: item.sku,
              name: item.name,
              description: item.description,
              imageUrl: item.image,
              category: item.category,
              price: item.price,
              inventory: inventory,
              isAvailable: item.isAvailable,
              stocks: parseFloat(item.stocks) - parseFloat(item.qty),
            });

        }

        if (this.customer.reference_id !== null) {
          axios
            .put(`${this.API_URL}restoorders/${this.customer.order_id}/`, {
              order_type: this.customer.order_type,
              table_id: this.customer.reference_id,
              customer_name: this.customer.order_cname,
              items: JSON.stringify(this.customer.order_items),
              processedBy: this.userdata.fName + " " + this.userdata.lName,
              status: 'closed',
            })
          if (this.customer.type === 'take-out') {
            axios
              .put(`${this.API_URL}restotakeouts/${this.customer.reference_id}/`, {
                name: this.customer.identifier,
                status: 'done',
              })
          } else if (this.customer.type === 'on-hold') {
            axios
              .put(`${this.API_URL}restoonholds/${this.customer.reference_id}/`, {
                name: this.customer.identifier,
                status: 'done',
              })
          }
        }

        axios
          .post(`${this.API_URL}restotransaction/`, {
            taxValue: this.taxValue,
            discountValue: this.discountValue,
            subTotal: this.subTotal,
            totalCharge: this.totalCost,
            totalPay: this.totalCost,
            items: JSON.stringify(this.cartItems),
            processedBy: this.userdata.fName + " " + this.userdata.lName,
          })
          .then(response => {
            this.taskRecord(`action:/payorder/posted`);
            this.printBill();
            this.$swal({
              title: 'Success',
              icon: "success",
              title: "Transaction saved successfully!"
            }).then((result) => {
              document.location.reload();
            });

          })
          .catch(error => {
            console.log(error);
          });
      }
    },
    printBill() {
      if (this.cartItems.length >= 1) {
        this.printSection();
      }
    },
    getInventory() {
      axios
        .get(`${this.API_URL}restoitem/`)
        .then(response => {
          this.itemarray = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getRestoTables() {
      axios
        .get(`${this.API_URL}restotables/`)
        .then(response => {
          this.resto_tables = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getRestoTakeout() {
      axios
        .get(`${this.API_URL}restotakeouts/`)
        .then(response => {
          this.resto_takeouts = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getRestoOnholds() {
      axios
        .get(`${this.API_URL}restoonholds/`)
        .then(response => {
          this.resto_onholds = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getTransaction() {
      axios
        .get(`${this.API_URL}restotransaction/`)
        .then(response => {
          this.transactions = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getAllOrders() {
      axios
        .get(`${this.API_URL}restoorders/`)
        .then(response => {
          this.resto_allorders = response.data.map(item => {
            const timePassed = this.getTimePassed(item.datestarted);;
            const isRunning = (item.status === 'progress') ? true : false;
            const order_items = JSON.parse(item.items);
            const items = JSON.parse(item.items);
            const datestarted = formatDate(new Date(item.date_modified));
            return {
              ...item,
              items,
              datestarted,
              order_items,
              timePassed,
              isRunning,
            };
          }).sort((a, b) => {
            const dateA = new Date(a.date_created);
            const dateB = new Date(b.date_created);
            return dateB - dateA;
          }).sort((a, b) => {
            const aStatus = a.status;
            const bStatus = b.status;
            if (aStatus === 'closed' && bStatus === 'progress') {
              return 1;
            } else if (bStatus === 'closed' && aStatus === 'progress') {
              return -1;
            } else {
              return 0;
            }
          });
        })
        .catch(error => {
          console.log(error);
        });

    },
    getCurrentOrders() {
      axios
        .post(`${this.API_URL}restoorders/filter/`, { columnName: 'status', columnKey: 'progress' })
        .then(response => {
          this.resto_order = response.data;
          axios
            .post(`${this.API_URL}restoorders/filter/`, { columnName: 'status', columnKey: 'served' })
            .then(response2 => {
              // Combine response and response2
              this.resto_order = [...this.resto_order, ...response2.data];
            })
            .catch(error2 => {
              console.log(error2);
            });
        })
        .catch(error => {
          console.log(error);
        });
    },
    saveInventory() {
      if (this.isUpdatingInventory) {
        axios.get(`${this.API_URL}restoitem/${this.stock.id}/`)
          .then(response => {
            const items = JSON.parse(response.data.inventory);
            const curstock = this.stock.stocks;
            const prevstock = items[items.length - 1].stocks;
            if (curstock < prevstock) {
              items.push({ "type": "stockout", "qty": prevstock - curstock, "stocks": curstock, "date_created": formatDate(new Date()), "processedBy": (this.userdata.fName + " " + this.userdata.lName).toString() });
            } else {
              items.push({ "type": "stockin", "qty": curstock - prevstock, "stocks": curstock, "date_created": formatDate(new Date()), "processedBy": (this.userdata.fName + " " + this.userdata.lName).toString() });
            }
            this.stock.inventory = JSON.stringify(items);
            axios
              .put(`${this.API_URL}restoitem/${this.stock.id}/`, this.stock)
              .then(response => {
                this.$swal({
                  icon: "success",
                  title: "Item updated successfully"
                }).then((result) => {
                  document.location.reload();
                });
                // this.getInventory();
                // this.stock = {
                //   id: null,
                //   name: "",
                //   imageUrl: "",
                //   description: "",
                //   sku: "",
                //   category: "",
                //   stocks: 0,
                //   price: 0,
                //   isAvailable: "",
                // };
                // this.isUpdatingInventory = false;

              })
              .catch(error => {
                console.log(error);
              });
          })
      } else {
        axios
          .post(`${this.API_URL}restoitem/filter/`, { columnName: 'name', columnKey: this.stock.name })
          .then(response => {
            if (response.data.length > 0) {
              this.$swal({
                icon: "error",
                title: "Item already exists"
              });
            } else {
              this.stock.inventory = `[{"type":"stockin","qty":${this.stock.stocks},"stocks":${this.stock.stocks},"date_created":"${formatDate(new Date())}", "processedBy": "${this.userdata.fName + " " + this.userdata.lName}"}]`;
              axios
                .post(`${this.API_URL}restoitem/`, this.stock)
                .then(response => {
                  this.$swal({
                    icon: "success",
                    title: "Item saved successfully"
                  }).then((result) => {
                    document.location.reload();
                  });
                  // this.getInventory();
                  // this.stock = {
                  //   id: null,
                  //   name: "",
                  //   imageUrl: "",
                  //   description: "",
                  //   sku: "",
                  //   category: "",
                  //   stocks: 0,
                  //   price: 0,
                  //   isAvailable: "",
                  // };

                })
                .catch(error => {
                  console.log(error);
                });
            }
          })
          .catch(error => {
            console.log(error);
          });
      }
    },
    editInventory(id) {
      axios
        .get(`${this.API_URL}restoitem/${id}/`)
        .then(response => {
          this.stock = response.data;
          this.isUpdatingInventory = true;
        })
        .catch(error => {
          console.log(error);
        });
    },
    addItemToCart(item) {
      const isItemExist = (this.cartItems.filter(o => o.id === item.id).length > 0);
      const cart = {
        id: item.id,
        sku: item.sku,
        name: item.name,
        description: item.description,
        category: item.category,
        isAvailable: item.isAvailable,
        image: item.imageUrl,
        qty: 1,
        inventory: JSON.parse(item.inventory),
        price: parseFloat(item.price),
        totalPrice: parseFloat(item.price),
        stocks: parseFloat(item.stocks),
      }

      if (item.stocks > 0) {
        if (!isItemExist) {
          this.cartItems.push(cart);
          this.currentItem = cart;
        } else {
          const obj = this.cartItems.find(item => item.id === cart.id);
          obj.qty += (obj.qty < obj.stocks) ? 1 : 0;
          obj.totalPrice = obj.price * obj.qty;
        }
      } else {
        this.$swal({
          title: "Out of Stock",
          text: "The item you are trying to add is currently out of stock.",
          icon: "warning",
          buttons: {
            confirm: "OK",
          },
        });
      }
    },
    removeFromCart(item) {
      const index = this.cartItems.indexOf(item)
      this.cartItems.splice(index, 1)
    },
    updatePrice(item) {
      item.totalPrice = item.qty * item.price
    },
    printSection() {
      // Add Bootstrap stylesheet to the head
      const bootstrapLink = document.createElement('link');
      bootstrapLink.rel = 'stylesheet';
      bootstrapLink.href = 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css';
      document.head.appendChild(bootstrapLink);

      // Create the overlay element
      const overlay = document.createElement('div');
      overlay.style.position = 'fixed';
      overlay.style.top = 0;
      overlay.style.left = 0;
      overlay.style.width = '100%';
      overlay.style.height = '100%';
      overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
      overlay.style.zIndex = 1056;
      overlay.classList.add('overlay');
      document.body.appendChild(overlay);

      // Get the dataTable section and create the print window
      const dataTable = document.getElementById('billing-statement');
      const printElement = document.createElement('div');
      printElement.appendChild(dataTable.cloneNode(true));

      // Open a new window and write the printElement to it
      const printWindow = window.open('', 'Print Window');
      printWindow.document.write('<html><head>');
      // printWindow.document.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">');
      printWindow.document.write('<style>@media print { body { font-size: 10pt; padding:0; margin: 0cm; padding: 0; width: 58mm; transform: scale(0.97); transform-origin: 0 0; } tr { page-break-inside: auto; } .no-print { display: none; } }</style>');
      printWindow.document.write('</head><body>');
      printWindow.document.write(printElement.innerHTML);
      printWindow.document.write('</body></html>');
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
    },


    handleKeyPress(event) {
      switch (event.key) {
        case 'F1':
          event.preventDefault()
          if (this.cartItems.length >= 1)
            this.placeOrder();
          break;
        case 'F2':
          event.preventDefault()
          if (this.cartItems.length >= 1 && this.userdata.role !== 'waiter')
            this.payOrder();
          break;
        case 'F3':
          event.preventDefault()
          if (this.cartItems.length >= 1 && this.userdata.role !== 'waiter')
            this.setQty();
          this.$refs.tenderedCash.focus();
          break;
        case 'F4':
          event.preventDefault()
          if (this.userdata.role !== 'waiter')
            this.setDiscount();
          this.$refs.tenderedCash.focus();
          break;
        case 'F5':
          event.preventDefault()
          if (this.userdata.role !== 'waiter')
            this.setTax();
          this.$refs.tenderedCash.focus();
          break;
        case 'F6':
          event.preventDefault()
          if (this.cartItems.length >= 1 && this.userdata.role !== 'waiter' && this.customer.reference_id === null)
            this.holdCustomer();
          break;
        case 'F7':
          event.preventDefault()
          if (this.cartItems.length >= 1 && this.userdata.role !== 'waiter')
            //toggle drawer
            break;
        case 'F8':
          event.preventDefault()
          this.findItem();
          break;
        case 'F9':
          event.preventDefault()
          if (this.userdata.role !== 'waiter')
            this.toggleInquire();
          break;
        case 'F10':
          event.preventDefault()
          if (this.cartItems.length >= 1 && this.userdata.role !== 'waiter')
            this.voidAction();
          break;
        case 'F11':
          event.preventDefault()
          if (this.cartItems.length > 0 && this.customer.order_id === undefined)
            this.clearAll();
          this.$refs.tenderedCash.focus();
          break;
        case 'F12':
          event.preventDefault()
          this.logout();
          break;
        default:
          break;
      }
    },
    toggleInquire() {
      this.barcodeText = "";
      this.searchText = "";
      this.inquiretoggle = !this.inquiretoggle;
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
    findItem() {
      this.$refs.myInput.focus();
      this.searchText = "";
      this.inquiretoggle = false;
    },
    async logout() {
      const authStore = useAuthStore();
      const user = {
        username: authStore.user.username,
        FirstName: authStore.user.fName,
        LastName: authStore.user.lName,
        role: authStore.user.role,
        route: authStore.user.route,
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
    }
  },
  mounted() {

    let barcode = "";
    let reading = false;

    document.addEventListener('keypress', e => {
      //usually barcode scanners throw an 'Enter' key at the end of read
      if (e.keyCode === 13) {
        if (barcode.length > 10) {
          if (!this.inquiretoggle) {
            this.barcodeText = barcode;
            const itemlist = this.filtereditemarray.filter(item => item.sku.toString().toLowerCase().includes(this.barcodeText));
            if (itemlist.length === 1) {
              const item = itemlist[0];
              this.addItemToCart(item);
              $("#pos-tab").tab('show');
              this.$refs.tenderedCash.focus();
              this.totalCash = 0;
            }
          } else {
            this.searchText = barcode;
          }
          /// code ready to use                
          barcode = "";
        }
      } else {
        barcode += e.key; //while this is not an 'enter' it stores the every key            
      }

      //run a timeout of 200ms at the first read and clear everything
      if (!reading) {
        reading = true;
        setTimeout(() => {
          barcode = "";
          reading = false;
          this.barcodeText = "";
        }, 200);  //200 works fine for me but you can adjust it
      }
    });

    setInterval(() => {
      this.resto_allorders.forEach(item => {

        if (item.status === 'progress' && item.isRunning) {
          item.timePassed = this.getTimePassed(item.datestarted);
        }
      });
    }, 1000);

    document.addEventListener('keydown', this.handleKeyPress);
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
  },
}
</script>
<style>
.title {
  margin: 0;
  font-size: 1rem;
  line-height: 1.2;
}

.text-truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.media-body {
  margin-left: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

dt,
dd {
  font-size: medium;
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

.blink_me {
  animation: blinker 1s linear infinite;
}

@keyframes blinker {
  50% {
    opacity: 0;
  }
}

.badge-danger {
  background-color: #dc3545;
  color: #fff;
}

.btn-error {
  color: #ef5f5f;
}

.btn-box {
  border-radius: 5%;
  width: 75px;
  height: 75px;
  font-size: small;
}

.btn-gap {
  margin-right: 5px;
  /* Adjust the value to increase or decrease the gap between buttons */
}

.text-medium {
  font-size: 16px;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>