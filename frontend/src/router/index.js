import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "../stores/authStore";
import login from "../components/auth/Login.vue";
import Main from "../components/main/MainComponent.vue";
import Booking from "../components/main/BookingComponent.vue";
import BookingMgr from "../components/main/BookingManager.vue";
import Cashier from "../components/main/CashierComponent.vue";
import Inventory from "../components/main/InventoryComponent.vue";
import GuestCounter from "../components/main/GuestCounter.vue";
import TaskManager from "../components/main/TaskManager.vue";
// import ReceptionHotel from "../components/main/ReceptionHotel.vue";
import Error403 from "../components/main/ErrorPage.vue";
import ExpiredPage from "../components/main/ExpiredPage.vue";
import EmptyPage from "../components/main/EmptyPage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      redirect: "/login",
    },
    {
      path: "/login",
      name: "login",
      component: login,
    },
    {
      path: "/main",
      name: "main",
      component: Main,
      meta: { 
        requiresAuth: true,
        roles: ["superuser"]
      },
    },
    {
      path: "/counter",
      name: "counter",
      component: GuestCounter,
      meta: { 
        requiresAuth: true,
        roles: ["superuser","guard"]
      },
    },
    {
      path: "/taskmgr",
      name: "taskmgr",
      component: TaskManager,
      meta: { 
        requiresAuth: true,
        roles: ["superuser","supervisor","supervisor-aide"]
      },
    },
    {
      path: "/booking",
      name: "booking",
      component: Booking,     
      meta: { 
        requiresAuth: true,
        roles: ["superuser", "reservationist", "frontdesk","supervisor","supervisor-aide"]
      },
    },    
    {
      path: "/booking_mgr",
      name: "booking_mgr",
      component: BookingMgr,     
      meta: { 
        requiresAuth: true,
        roles: ["superuser", "reservationist", "frontdesk","supervisor","supervisor-aide"]
      },
    },   
    // {
    //   path: "/reception",
    //   name: "reception",
    //   component: ReceptionHotel,     
    //   meta: { 
    //     requiresAuth: true,
    //     roles: ["superuser"]
    //   },
    // }, 
    {
      path: "/cashier",
      name: "cashier",
      component: Cashier,
      meta: { 
        requiresAuth: true,
        roles: ["superuser", "cashier", "waiter", "foodserver", "restoinventory"]
      },
    },
    {
      path: "/inventory",
      name: "inventory",
      component: Inventory,
      meta: { 
        requiresAuth: true,
        roles: ["superuser", "inventorymanager"]
      },
    },   
    {
      path: "/403",
      name: "error403",
      component: Error403,
    },
    {
      path: "/:catchAll(.*)",
      redirect: { name: "error403" },
    },     
  ],
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  const userRole = authStore.user?.role;
  const userRoute = authStore.user?.route;

  if (to.path === '/login' && authStore.isAuthenticated) {
    next({ name: userRoute });
  } else if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!authStore.isAuthenticated) {
      next({ name: 'login' });
    } else if (!to.meta.roles.includes(userRole)) {
      next({ name: userRoute, params: { from: from.path }, replace: true });
    } else {
      next();
    }
  } else {
    next();
  }
});

router.addRoute({
  path: '/403/:from*',
  name: '403',
  component: Error403,
  props: route => ({ from: route.params.from || '/' })
});


export default router;
