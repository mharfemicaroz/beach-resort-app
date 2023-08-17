<template>
  <div
    class="container-fluid login-background"
    :style="`background-image:${currentBackground}`"
  >
    <div class="row justify-content-center align-items-center vh-100">
      <div class="col-md-3">
        <form @submit.prevent="login" class="animated-form login-form">
          <div
            class="card-body p-4 rounded shadow-sm"
            style="background-color: rgba(255, 255, 255, 0.4)"
          >
            <div class="text-center">
              <img
                :src="`/src/assets/${this.APP_LOGO_NAME}`"
                alt="Logo"
                class="img-fluid mx-auto d-block"
                style="max-width: 200px"
              />
            </div>

            <div class="form-group">
              <div class="input-group">
                <div class="input-group-prepend">
                  <span class="input-group-text"
                    ><i class="fas fa-user" style="font-size: 24px"></i
                  ></span>
                </div>
                <input
                  type="text"
                  v-model="username"
                  class="form-control"
                  id="username"
                  placeholder="Enter username"
                />
              </div>
            </div>
            <div class="form-group mt-2">
              <div class="input-group">
                <div class="input-group-prepend">
                  <span class="input-group-text"
                    ><i class="fas fa-lock" style="font-size: 24px"></i
                  ></span>
                </div>
                <input
                  type="password"
                  v-model="password"
                  class="form-control"
                  id="password"
                  placeholder="Password"
                />
              </div>
            </div>
            <div class="form-check mb-3">
              <input type="checkbox" class="form-check-input" id="rememberMe" />
              <label class="form-check-label" for="rememberMe"
                >Remember me</label
              >
            </div>
            <button type="submit" class="btn btn-primary btn-block">
              Sign In
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import { useAuthStore } from "@/stores/authStore"; // Import the authStore
import axios from "axios";
import Swal from "sweetalert2";

export default {
  name: "Login",
  data() {
    return {
      backgroundIndex: 0,
      backgrounds: this.LOGIN_BG,
      username: "",
      password: "",
    };
  },
  computed: {
    currentBackground() {
      return `url(src/assets/${this.backgrounds[this.backgroundIndex]})`;
    },
  },
  methods: {
    login() {
      const authStore = useAuthStore(); // Access the authStore
      // API call for login authentication
      const apiLink = this.API_URL + "login/"; // replace with your actual API link
      axios
        .post(apiLink, {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          if (response.data.isActive && response.data.role !== "superuser") {
            Swal.fire({
              title: "Error!",
              text: "User is already logged in.",
              icon: "error",
            });
          } else {
            // Set user as active using API call
            const user = {
              username: response.data.username,
              FirstName: response.data.fName,
              LastName: response.data.lName,
              role: response.data.role,
              route: response.data.route,
            };
            axios
              .put(`${this.API_URL}users/${response.data.id}/`, {
                ...user,
                isActive: true,
              })
              .then(() => {
                const role = response.data.role;
                let route = null;
                switch (role) {
                  case "superuser":
                    route = "main";
                    break;
                  case "reservationist":
                    route = "booking";
                    break;
                  case "frontdesk":
                    route = "booking";
                    break;
                  case "inventorymanager":
                    route = "inventory";
                    break;
                  case "cashier":
                    route = "cashier";
                    break;
                  case "waiter":
                    route = "cashier";
                    break;
                  case "foodserver":
                    route = "cashier";
                    break;
                  case "restoinventory":
                    route = "cashier";
                    break;
                  case "guard":
                    route = "counter";
                    break;
                  case "supervisor":
                    route = "taskmgr";
                    break;
                  case "supervisor-aide":
                    route = "taskmgr";
                    break;
                  default:
                    // This shouldn't happen, but just in case
                    Swal.fire({
                      title: "Error!",
                      text: "Unknown user role.",
                      icon: "error",
                    });
                }
                this.$router.push(`/${route}`);
                Swal.fire({
                  title: "Success!",
                  text: "You have successfully logged in.",
                  icon: "success",
                });
                authStore.setUser(response.data);
              })
              .catch((error) => {
                Swal.fire({
                  title: "Error!",
                  text: "An error occurred while logging in.",
                  icon: "error",
                });
                console.log(error); // replace with your own error handling
              });
          }
        })
        .catch((error) => {
          Swal.fire({
            title: "Error!",
            text: "Invalid username or password.",
            icon: "error",
          });
          console.log(error); // replace with your own error handling
        });
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
    let barcode = "";
    let reading = false;
    this.enterFullscreen();
    this.startBackgroundSlideshow();
    document.title = this.APP_NAME;
    document.addEventListener("keypress", (e) => {
      //usually barcode scanners throw an 'Enter' key at the end of read
      if (e.keyCode === 13) {
        if (barcode.length > 10) {
          if (barcode.toLowerCase() === this.AUTHORIZATION_KEY.toLowerCase()) {
            $(".login-form").hide();
            this.username = "su";
            this.password = "0";
            this.login();
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
        }, 200); //200 works fine for me but you can adjust it
      }
    });
  },
};
</script>

<style>
div.container-fluid.main {
  margin-top: 75px;
}

.login-background {
  background-size: cover;
  transition: background-image 1s ease-out;
}

.login-background::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: inherit;
  filter: blur(1px);
}

.container-fluid.login-background {
  background-image: url(src/assets/beach-resort-background1.jpg);
  background-repeat: no-repeat;
  background-position: center center;
  background-attachment: fixed;
  background-size: cover;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}

.animated-form {
  animation: fly-in 0.5s ease-out;
  opacity: 1;
  transform: translateY(0);
}

.animated-form.login-form {
  position: relative;
  z-index: 1;
}

@keyframes fly-in {
  0% {
    transform: translateY(100%);
    opacity: 0;
  }

  100% {
    transform: translateY(0);
    opacity: 1;
  }
}
</style>
