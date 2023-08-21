<template>
  <nav
    class="navbar navbar-fixed-top navbar-expand-lg navbar-light bg-primary shadow-sm no-print"
    :style="{
      'background-image': currentBackground,
      'background-repeat': 'no-repeat',
      'background-position': 'center',
      'background-size': 'cover',
      'background-attachment': 'fixed',
      position: 'fixed',
      width: '100vw',
      left: 0,
      top: 0,
      display: 'flex',
      'z-index': 200,
    }"
  >
    <div
      class="container-fluid"
      style="padding-left: 25px; padding-right: 25px"
    >
      <!-- Logo and Search Bar -->
      <a class="navbar-brand text-white align-middlev vv vv v vv v" href="#">
        <div style="display: flex; align-items: center">
          <img
            :src="`/src/assets/${this.APP_LOGO_NAME}`"
            width="45"
            height="45"
            class="d-inline-block align-top"
            alt="Logo"
            style="margin-right: 10px"
          />
          <span style="flex: 1">{{ this.APP_NAME }}</span>
        </div>
      </a>

      <!-- Navigation Links -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <span class="navbar-text ms-auto me-3 text-white">
          <small>Current Date and Time: {{ formattedTime }}</small>
        </span>
        <ul class="navbar-nav">
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle text-white"
              href="#"
              id="navbarDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              <i class="fas fa-user-circle me-1"></i> {{ userdata.fName }}
              {{ userdata.lName }}
            </a>
            <ul
              class="dropdown-menu dropdown-menu-end"
              aria-labelledby="navbarDropdown"
            >
              <div v-if="userdata.role === 'superuser'">
                <li>
                  <router-link to="/main" tag="a" class="dropdown-item"
                    >Main</router-link
                  >
                </li>
                <li>
                  <router-link to="/booking" tag="a" class="dropdown-item"
                    >Booking</router-link
                  >
                </li>
                <li>
                  <router-link to="/inventory" tag="a" class="dropdown-item"
                    >Inventory</router-link
                  >
                </li>
                <li>
                  <router-link to="/restaurant" tag="a" class="dropdown-item"
                    >Restaurant</router-link
                  >
                </li>
                <li>
                  <router-link
                    to="/taskmgr"
                    tag="a"
                    target="_blank"
                    class="dropdown-item"
                    >Task Manager</router-link
                  >
                </li>
                <hr class="dropdown-divider" />
              </div>
              <li>
                <a class="dropdown-item" href="#" @click="logout()"
                  ><i class="fas fa-sign-out-alt me-1"></i> Logout</a
                >
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { useAuthStore } from "@/stores/authStore";
import axios from "axios";
export default {
  data() {
    return {
      currentTime: new Date(),
      backgroundIndex: 0,
      backgrounds: this.LOGIN_BG,
      user: {
        username: "",
        password: "",
        FirstName: "",
        LastName: "",
        role: "",
      },
    };
  },
  created() {
    this.startBackgroundSlideshow();
    //this.enterFullscreen();
    setInterval(() => {
      this.currentTime = new Date();
    }, 1000);
  },
  computed: {
    formattedTime() {
      return `Current Date and Time: ${this.currentTime.toLocaleString()}`;
    },
    userdata() {
      const authStore = useAuthStore();
      const user = authStore.user;
      return user;
    },
    currentBackground() {
      return `url(src/assets/${this.backgrounds[this.backgroundIndex]})`;
    },
  },
  methods: {
    async logout() {
      const authStore = useAuthStore();
      const user = {
        username: authStore.user.username,
        FirstName: authStore.user.fName,
        LastName: authStore.user.lName,
        role: authStore.user.role,
        route: authStore.user.route,
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
    startBackgroundSlideshow() {
      setInterval(() => {
        this.backgroundIndex =
          (this.backgroundIndex + 1) % this.backgrounds.length;
      }, 5000);
    },

    enterFullscreen() {
      const element = document.documentElement; // Select the root element of your component
      if (element.requestFullscreen) {
        element.requestFullscreen();
      } else if (element.mozRequestFullScreen) {
        element.mozRequestFullScreen();
      } else if (element.webkitRequestFullscreen) {
        element.webkitRequestFullscreen();
      } else if (element.msRequestFullscreen) {
        element.msRequestFullscreen();
      }
    },
  },
  mounted() {
    //this.enterFullscreen();
  },
};
</script>

<style scoped>
.navbar {
  position: relative;
  background-image: url("@/assets/headerbg1.png");
  /* Replace with your background image */
  z-index: 1;
  transition: background-image 1s ease-out;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  background-attachment: fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}

.navbar::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  /* Adjust the opacity and color as desired */
  z-index: -1;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  background-attachment: fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}

/* Custom font style for the top navbar */
.navbar {
  font-family: "Arial", sans-serif;
  font-weight: bold;
}

.navbar-brand {
  font-size: 18px;
}

.navbar-text small {
  font-size: 12px;
}

.dropdown-item {
  font-size: 14px;
}
</style>
