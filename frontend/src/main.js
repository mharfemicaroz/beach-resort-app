import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
import vSelect from "vue-select";
import VueSweetalert2 from "vue-sweetalert2";
import VueSimpleContextMenu from "vue-simple-context-menu";
import "vue-simple-context-menu/dist/vue-simple-context-menu.css";
import "sweetalert2/dist/sweetalert2.min.css";
import moment from "moment-timezone";
moment.tz.setDefault("Asia/Hongkong");

const app = createApp(App);
//note fix bug in summary collection report
app.config.globalProperties = {
  AUTHORIZATION_KEY: import.meta.env.VITE_AUTHORIZATION_KEY,
  AUTHORIZATION_KEY2: import.meta.env.VITE_AUTHORIZATION_KEY2,
  APP_NAME: import.meta.env.VITE_APP_NAME,
  APP_RULE1: import.meta.env.VITE_RULE1,
  APP_LOGO_NAME: import.meta.env.VITE_APP_LOGO_NAME,
  SITE_ADDRESS: import.meta.env.VITE_SITE_ADDRESS,
  LOGIN_BG: import.meta.env.VITE_LOGIN_BG.split(" "),
  EVALUATION_STAGE: false,
  EVALUATION_TIME: 15,
  API_URL: `http://${window.location.hostname}:8081/`,
  //API_URL : "http://192.168.1.222:8081/"
};
//6bv7mi88
app.use(router);
app.use(createPinia());
app.use(VueSweetalert2);

app
  .component("v-select", vSelect)
  .component("vue-simple-context-menu", VueSimpleContextMenu)
  .mount("#app");
