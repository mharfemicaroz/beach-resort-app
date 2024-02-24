<template>
  <div class="tabs">
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <a
          class="nav-link active"
          id="cash-tab"
          data-bs-toggle="tab"
          href="#cash"
          role="tab"
          aria-controls="cash"
          aria-selected="true"
        >
          Direct Cash
        </a>
      </li>
      <li class="nav-item" role="presentation">
        <a
          class="nav-link"
          id="bank-tab"
          data-bs-toggle="tab"
          href="#bank"
          role="tab"
          aria-controls="bank"
          aria-selected="false"
        >
          Bank Payment
        </a>
      </li>
      <li class="nav-item" role="presentation">
        <a
          class="nav-link"
          id="paypal-tab"
          data-bs-toggle="tab"
          href="#paypal"
          role="tab"
          aria-controls="paypal"
          aria-selected="false"
        >
          <img
            src="https://www.bworldonline.com/wp-content/uploads/2021/09/GCash_Horizontal-Full-Blue-Transparent.png"
            width="80"
          />
        </a>
      </li>
    </ul>
    <div class="tab-content" id="myTabContent">
      <div
        class="tab-pane fade show active"
        id="cash"
        role="tabpanel"
        aria-labelledby="cash-tab"
      >
        <div class="mt-4 mx-4">
          <div class="form mt-3">
            <div class="inputbox">
              <input
                type="number"
                name="name"
                class="form-control"
                required="required"
                autocomplete="off"
              />
              <span>Official Receipt NO.</span>
            </div>

            <div class="px-5 pay">
              <button
                class="btn btn-primary btn-block"
                @click="$emit('checkout-action', remarks)"
              >
                Pay ₱{{ totalCost }} Now
              </button>
            </div>
          </div>
        </div>
      </div>
      <div
        class="tab-pane fade"
        id="bank"
        role="tabpanel"
        aria-labelledby="bank-tab"
      >
        <div class="px-5 mt-5">
          <div class="inputbox">
            <input
              type="text"
              name="name"
              class="form-control"
              required="required"
              autocomplete="off"
            />
            <span>Name of the Bank</span>
          </div>
          <div class="inputbox">
            <input
              type="text"
              name="name"
              class="form-control"
              required="required"
              autocomplete="off"
            />
            <span>Account Name</span>
          </div>
          <div class="inputbox">
            <input
              type="text"
              name="name"
              class="form-control"
              required="required"
              autocomplete="off"
            />
            <span>Reference Code</span>
          </div>
          <div class="pay px-5">
            <button
              class="btn btn-primary btn-block"
              @click="$emit('checkout-action', remarks)"
            >
              Pay ₱{{ totalCost }} Now
            </button>
          </div>
        </div>
      </div>
      <div
        class="tab-pane fade"
        id="paypal"
        role="tabpanel"
        aria-labelledby="paypal-tab"
      >
        <div class="px-5 mt-5">
          <div class="inputbox">
            <input
              type="text"
              name="name"
              class="form-control"
              required="required"
              autocomplete="off"
            />
            <span>Reference Code</span>
          </div>
          <div class="pay px-5">
            <button
              class="btn btn-primary btn-block"
              @click="$emit('checkout-action', remarks)"
            >
              Pay ₱{{ totalCost }} Now
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    totalCost: {
      type: Number,
      default: 0,
      required: true,
    },
  },
  data() {
    return {
      //generic config for vue-simple-calendar
      remarks: "",
    };
  },
};
</script>
<style scoped>
.nav-tabs {
  border: none !important;
}
.nav-tabs .nav-link.active {
  color: #495057;
  background-color: #fff;
  border-color: #ffffff #ffffff #fff;
  border-top: 3px solid blue !important;
}
.nav-tabs .nav-link {
  margin-bottom: -1px;
  border: 1px solid transparent;
  border-top-left-radius: 0rem;
  border-top-right-radius: 0rem;
  border-top: 3px solid #eee;
  font-size: 20px;
}
.nav-tabs .nav-link:hover {
  border-color: #e9ecef #ffffff #ffffff;
}
.nav-tabs {
  display: table !important;
  width: 100%;
}
.nav-item {
  display: table-cell;
}
.form-control {
  border-bottom: 1px solid #eee !important;
  border: none;
  font-weight: 600;
}
.form-control:focus {
  color: #495057;
  background-color: #fff;
  border-color: #8bbafe;
  outline: 0;
  box-shadow: none;
}
.inputbox {
  position: relative;
  margin-bottom: 20px;
  width: 100%;
}
.inputbox span {
  position: absolute;
  top: 7px;
  left: 11px;
  transition: 0.5s;
}
.inputbox i {
  position: absolute;
  top: 13px;
  right: 8px;
  transition: 0.5s;
  color: #3f51b5;
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.inputbox input:focus ~ span {
  transform: translateX(-0px) translateY(-15px);
  font-size: 12px;
}
.inputbox input:valid ~ span {
  transform: translateX(-0px) translateY(-15px);
  font-size: 12px;
}
.pay button {
  height: 47px;
  border-radius: 37px;
}

.btn-block {
  display: block;
  width: 100%;
}
</style>
