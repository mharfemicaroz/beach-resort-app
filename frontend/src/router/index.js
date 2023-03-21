import { createRouter, createWebHistory } from "vue-router";
import login from "../components/auth/Login.vue";
import Main from "../components/main/MainComponent.vue";
import Booking from "../components/main/BookingComponent.vue";
import Cashier from "../components/main/CashierComponent.vue";
import Inventory from "../components/main/InventoryComponent.vue";
import Calendar from "../components/main/CalendarComponent.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "login",
      component: login,
    },
    {
      path: "/main",
      name: "main",
      component: Main,
    },
    {
      path: "/booking",
      name: "booking",
      component: Booking,     
    },    
    {
      path: "/cashier",
      name: "cashier",
      component: Cashier,
    },
    {
      path: "/inventory",
      name: "inventory",
      component: Inventory,
    },        
  ],
});

export default router;
