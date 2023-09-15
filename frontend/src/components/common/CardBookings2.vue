<template>
  <div class="container-fluid">
    <div class="row">
      <div class="accordion" id="accordionExample">
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapseOne"
              aria-expanded="true"
              aria-controls="collapseOne"
            >
              Arriving
              <span
                v-if="arrivingRoomData.length > 0"
                class="badge-pill badge-danger"
                >{{ arrivingRoomData.length }}</span
              >
            </button>
          </h2>
          <div
            id="collapseOne"
            class="accordion-collapse collapse show"
            data-bs-parent="#accordionExample"
          >
            <div class="accordion-body">
              <div class="col-md-12">
                <div class="row row-cols-1 row-cols-md-4">
                  <div
                    class="col mb-4"
                    v-for="(item, index) in arrivingRoomData"
                    :key="item.id"
                  >
                    <div
                      class="card"
                      style="transition: transform 0.2s ease-in-out"
                      @click="
                        $emit(
                          'click-action',
                          item.itemID,
                          item.name,
                          item.type,
                          item.price
                        )
                      "
                    >
                      <div
                        class="card-header d-flex justify-content-between align-items-center"
                        :style="{
                          'background-color':
                            item.status === 'reserved' && item.isPaid === 'no'
                              ? '#ef5350'
                              : item.status === 'reserved' &&
                                item.isPaid === 'partial'
                              ? '#5c6bc0'
                              : item.status === 'checkedin' &&
                                item.isPaid === 'no'
                              ? '#66bb6a'
                              : item.status === 'checkedin' &&
                                item.isPaid === 'partial'
                              ? '#42a5f5'
                              : item.status === 'checkedin' &&
                                item.isPaid === 'yes'
                              ? '#ffee58'
                              : item.status === 'reserved' &&
                                item.isPaid === 'yes'
                              ? '#5c6bc0'
                              : '',
                        }"
                      >
                        <h5 class="card-title">
                          <i class="fas fa-home"></i> {{ item.name }}
                        </h5>
                      </div>

                      <div class="card-body" v-if="'itemID' in item">
                        <h6>Client Information:</h6>
                        <ul class="list-unstyled">
                          <li
                            v-if="'groupkey' in item && item.groupkey !== null"
                          >
                            <strong
                              ><i class="fas fa-user"></i> Client Name:</strong
                            ><span class="text-white bg-danger">GROUP</span> -
                            {{ item.clientName }}
                          </li>
                          <li v-else>
                            <strong
                              ><i class="fas fa-user"></i> Client Name:</strong
                            >{{ item.clientName }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-map-marker-alt"></i> Client
                              Address:</strong
                            >
                            {{ item.clientAddress }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-phone"></i> Contact
                              Number:</strong
                            >
                            {{ item.contactNumber }}
                          </li>
                        </ul>
                        <h6>Booking Information:</h6>
                        <ul class="list-unstyled">
                          <li>
                            <strong
                              ><i class="fas fa-calendar-alt"></i> Check-in
                              Date:</strong
                            >
                            {{ item.checkinDate }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-calendar-check"></i> Check-out
                              Date:</strong
                            >
                            {{ item.checkoutDate }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-dollar-sign"></i> Total
                              Charges:</strong
                            >
                            <span class="text-success">{{
                              item.totalPrice
                            }}</span>
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-money-bill-wave"></i> Partial
                              Payment:</strong
                            >
                            <span class="text-warning">{{
                              item.partialPayment
                            }}</span>
                          </li>
                        </ul>
                      </div>

                      <div class="card-body" v-else>
                        <div
                          class="alert alert-warning text-center"
                          role="alert"
                        >
                          <h4 class="alert-heading">
                            This room is available for booking
                          </h4>
                          <p>Please click to continue.</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapseTwo"
              aria-expanded="false"
              aria-controls="collapseTwo"
            >
              Staying
              <span
                v-if="stayRoomData.length > 0"
                class="badge-pill badge-danger"
                >{{ stayRoomData.length }}</span
              >
            </button>
          </h2>
          <div
            id="collapseTwo"
            class="accordion-collapse collapse"
            data-bs-parent="#accordionExample"
          >
            <div class="accordion-body">
              <div class="col-md-12">
                <div class="row row-cols-1 row-cols-md-4">
                  <div
                    class="col mb-4"
                    v-for="(item, index) in stayRoomData"
                    :key="item.id"
                  >
                    <div
                      class="card"
                      style="transition: transform 0.2s ease-in-out"
                      @click="
                        $emit(
                          'click-action',
                          item.itemID,
                          item.name,
                          item.type,
                          item.price
                        )
                      "
                    >
                      <div
                        class="card-header d-flex justify-content-between align-items-center"
                        :style="{
                          'background-color':
                            item.status === 'reserved' && item.isPaid === 'no'
                              ? '#ef5350'
                              : item.status === 'reserved' &&
                                item.isPaid === 'partial'
                              ? '#5c6bc0'
                              : item.status === 'checkedin' &&
                                item.isPaid === 'no'
                              ? '#66bb6a'
                              : item.status === 'checkedin' &&
                                item.isPaid === 'partial'
                              ? '#42a5f5'
                              : item.status === 'checkedin' &&
                                item.isPaid === 'yes'
                              ? '#ffee58'
                              : item.status === 'reserved' &&
                                item.isPaid === 'yes'
                              ? '#5c6bc0'
                              : '',
                        }"
                      >
                        <h5 class="card-title">
                          <i class="fas fa-home"></i> {{ item.name }}
                        </h5>
                      </div>

                      <div class="card-body" v-if="'itemID' in item">
                        <h6>Client Information:</h6>
                        <ul class="list-unstyled">
                          <li
                            v-if="'groupkey' in item && item.groupkey !== null"
                          >
                            <strong
                              ><i class="fas fa-user"></i> Client Name:</strong
                            ><span class="text-white bg-danger">GROUP</span> -
                            {{ item.clientName }}
                          </li>
                          <li v-else>
                            <strong
                              ><i class="fas fa-user"></i> Client Name:</strong
                            >{{ item.clientName }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-map-marker-alt"></i> Client
                              Address:</strong
                            >
                            {{ item.clientAddress }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-phone"></i> Contact
                              Number:</strong
                            >
                            {{ item.contactNumber }}
                          </li>
                        </ul>
                        <h6>Booking Information:</h6>
                        <ul class="list-unstyled">
                          <li>
                            <strong
                              ><i class="fas fa-calendar-alt"></i> Check-in
                              Date:</strong
                            >
                            {{ item.checkinDate }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-calendar-check"></i> Check-out
                              Date:</strong
                            >
                            {{ item.checkoutDate }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-dollar-sign"></i> Total
                              Charges:</strong
                            >
                            <span class="text-success">{{
                              item.totalPrice
                            }}</span>
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-money-bill-wave"></i> Partial
                              Payment:</strong
                            >
                            <span class="text-warning">{{
                              item.partialPayment
                            }}</span>
                          </li>
                        </ul>
                      </div>

                      <div class="card-body" v-else>
                        <div
                          class="alert alert-warning text-center"
                          role="alert"
                        >
                          <h4 class="alert-heading">
                            This room is available for booking
                          </h4>
                          <p>Please click to continue.</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapseThree"
              aria-expanded="false"
              aria-controls="collapseThree"
            >
              Departing
              <span
                v-if="departRoomData.length > 0"
                class="badge-pill badge-danger"
                >{{ departRoomData.length }}</span
              >
            </button>
          </h2>
          <div
            id="collapseThree"
            class="accordion-collapse collapse"
            data-bs-parent="#accordionExample"
          >
            <div class="accordion-body">
              <div class="col-md-12">
                <div class="row row-cols-1 row-cols-md-4">
                  <div
                    class="col mb-4"
                    v-for="(item, index) in departRoomData"
                    :key="item.id"
                  >
                    <div
                      class="card"
                      style="transition: transform 0.2s ease-in-out"
                      @click="
                        $emit(
                          'click-action',
                          item.itemID,
                          item.name,
                          item.type,
                          item.price
                        )
                      "
                    >
                      <div
                        class="card-header d-flex justify-content-between align-items-center"
                        :style="{
                          'background-color':
                            item.status === 'reserved' && item.isPaid === 'no'
                              ? '#ef5350'
                              : item.status === 'reserved' &&
                                item.isPaid === 'partial'
                              ? '#5c6bc0'
                              : item.status === 'checkedin' &&
                                item.isPaid === 'no'
                              ? '#66bb6a'
                              : item.status === 'checkedin' &&
                                item.isPaid === 'partial'
                              ? '#42a5f5'
                              : item.status === 'checkedin' &&
                                item.isPaid === 'yes'
                              ? '#ffee58'
                              : item.status === 'reserved' &&
                                item.isPaid === 'yes'
                              ? '#5c6bc0'
                              : '',
                        }"
                      >
                        <h5 class="card-title">
                          <i class="fas fa-home"></i> {{ item.name }}
                        </h5>
                      </div>

                      <div class="card-body" v-if="'itemID' in item">
                        <h6>Client Information:</h6>
                        <ul class="list-unstyled">
                          <li
                            v-if="'groupkey' in item && item.groupkey !== null"
                          >
                            <strong
                              ><i class="fas fa-user"></i> Client Name:</strong
                            ><span class="text-white bg-danger">GROUP</span> -
                            {{ item.clientName }}
                          </li>
                          <li v-else>
                            <strong
                              ><i class="fas fa-user"></i> Client Name:</strong
                            >{{ item.clientName }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-map-marker-alt"></i> Client
                              Address:</strong
                            >
                            {{ item.clientAddress }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-phone"></i> Contact
                              Number:</strong
                            >
                            {{ item.contactNumber }}
                          </li>
                        </ul>
                        <h6>Booking Information:</h6>
                        <ul class="list-unstyled">
                          <li>
                            <strong
                              ><i class="fas fa-calendar-alt"></i> Check-in
                              Date:</strong
                            >
                            {{ item.checkinDate }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-calendar-check"></i> Check-out
                              Date:</strong
                            >
                            {{ item.checkoutDate }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-dollar-sign"></i> Total
                              Charges:</strong
                            >
                            <span class="text-success">{{
                              item.totalPrice
                            }}</span>
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-money-bill-wave"></i> Partial
                              Payment:</strong
                            >
                            <span class="text-warning">{{
                              item.partialPayment
                            }}</span>
                          </li>
                        </ul>
                      </div>

                      <div class="card-body" v-else>
                        <div
                          class="alert alert-warning text-center"
                          role="alert"
                        >
                          <h4 class="alert-heading">
                            This room is available for booking
                          </h4>
                          <p>Please click to continue.</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapse4"
              aria-expanded="false"
              aria-controls="collapse4"
            >
              Vacant
              <span
                v-if="vacantRoomData.length > 0"
                class="badge-pill badge-danger"
                >{{ vacantRoomData.length }}</span
              >
            </button>
          </h2>
          <div
            id="collapse4"
            class="accordion-collapse collapse"
            data-bs-parent="#accordionExample"
          >
            <div class="accordion-body">
              <div class="col-md-12">
                <div class="row row-cols-1 row-cols-md-4">
                  <div
                    class="col mb-4"
                    v-for="(item, index) in vacantRoomData"
                    :key="item.id"
                  >
                    <div
                      class="card"
                      style="transition: transform 0.2s ease-in-out"
                      @click="
                        $emit(
                          'click-action',
                          item.itemID,
                          item.name,
                          item.type,
                          item.price
                        )
                      "
                    >
                      <div
                        class="card-header d-flex justify-content-between align-items-center"
                        :style="{
                          'background-color':
                            item.status === 'reserved' && item.isPaid === 'no'
                              ? '#ef5350'
                              : item.status === 'reserved' &&
                                item.isPaid === 'partial'
                              ? '#5c6bc0'
                              : item.status === 'checkedin' &&
                                item.isPaid === 'no'
                              ? '#66bb6a'
                              : item.status === 'checkedin' &&
                                item.isPaid === 'partial'
                              ? '#42a5f5'
                              : item.status === 'checkedin' &&
                                item.isPaid === 'yes'
                              ? '#ffee58'
                              : item.status === 'reserved' &&
                                item.isPaid === 'yes'
                              ? '#5c6bc0'
                              : '',
                        }"
                      >
                        <h5 class="card-title">
                          <i class="fas fa-home"></i> {{ item.name }}
                        </h5>
                      </div>

                      <div class="card-body" v-if="'itemID' in item">
                        <h6>Client Information:</h6>
                        <ul class="list-unstyled">
                          <li
                            v-if="'groupkey' in item && item.groupkey !== null"
                          >
                            <strong
                              ><i class="fas fa-user"></i> Client Name:</strong
                            ><span class="text-white bg-danger">GROUP</span> -
                            {{ item.clientName }}
                          </li>
                          <li v-else>
                            <strong
                              ><i class="fas fa-user"></i> Client Name:</strong
                            >{{ item.clientName }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-map-marker-alt"></i> Client
                              Address:</strong
                            >
                            {{ item.clientAddress }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-phone"></i> Contact
                              Number:</strong
                            >
                            {{ item.contactNumber }}
                          </li>
                        </ul>
                        <h6>Booking Information:</h6>
                        <ul class="list-unstyled">
                          <li>
                            <strong
                              ><i class="fas fa-calendar-alt"></i> Check-in
                              Date:</strong
                            >
                            {{ item.checkinDate }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-calendar-check"></i> Check-out
                              Date:</strong
                            >
                            {{ item.checkoutDate }}
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-dollar-sign"></i> Total
                              Charges:</strong
                            >
                            <span class="text-success">{{
                              item.totalPrice
                            }}</span>
                          </li>
                          <li>
                            <strong
                              ><i class="fas fa-money-bill-wave"></i> Partial
                              Payment:</strong
                            >
                            <span class="text-warning">{{
                              item.partialPayment
                            }}</span>
                          </li>
                        </ul>
                      </div>

                      <div class="card-body" v-else>
                        <div
                          class="alert alert-warning text-center"
                          role="alert"
                        >
                          <h4 class="alert-heading">
                            This room is available for booking
                          </h4>
                          <p>Please click to continue.</p>
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
    <div class="row row justify-content-center">
      <div class="col-md-12">
        <div class="card x" style="height: 50px">----------------</div>
      </div>
    </div>
  </div>
</template>
<script>
function parseDate(dateString) {
  const [day, month, year] = dateString.split("/");
  return new Date(`${year}-${month}-${day}`).setHours(0, 0, 0, 0);
}
export default {
  props: {
    roomData: {
      type: Object,
      required: true,
    },
    departingRoomData: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      guestStatus: ["Arriving", "Staying", "Departing", "Vacant"],
    };
  },
  computed: {
    arrivingRoomData() {
      return this.roomData
        .filter((o) => o.status === "reserved")
        .sort(function (a, b) {
          return a.isPaid.localeCompare(b.isPaid);
        });
    },
    stayRoomData() {
      return this.roomData
        .filter((o) => "itemID" in o)
        .filter((o) => {
          const isCheckedin = o.status === "checkedin";
          const today = new Date().setHours(0, 0, 0, 0);
          let checkoutDate = new Date(parseDate(o.checkoutDate));
          checkoutDate.setDate(checkoutDate.getDate() + 1);
          checkoutDate = checkoutDate.setHours(0, 0, 0, 0);
          const isStaying = checkoutDate > today;
          return isCheckedin && isStaying;
        })
        .sort(function (a, b) {
          return a.isPaid.localeCompare(b.isPaid);
        });
    },
    departRoomData() {
      return this.departingRoomData
        .filter((o) => "itemID" in o)
        .sort(function (a, b) {
          return a.isPaid.localeCompare(b.isPaid);
        });
    },
    vacantRoomData() {
      return this.roomData.filter((o) => !("itemID" in o));
    },
  },
};
</script>
<style>
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
</style>
