<template>
  <div class="container">
    <div class="row justify-content-center mt-5">
      <div class="col-md-6">
        <div class="card">
          <div class="card-header text-center">
            <img src="@/assets/pantukan-waterworld-logo.jpg" alt="Pantukan Waterworld Logo" class="img-fluid" style="max-width: 200px;">
            <h4 class="text-center mt-3">Login</h4>
          </div>
          <div class="card-body">
            <form @submit.prevent="login">
              <div class="form-group">
                <label for="username">Username</label>
                <input type="text" v-model="username" class="form-control" id="username" aria-describedby="usernameHelp" placeholder="Enter username">
              </div>
              <div class="form-group mb-2">
                <label for="password">Password</label>
                <input type="password" v-model="password" class="form-control" id="password" placeholder="Password">
              </div>
              <button type="submit" class="btn btn-primary btn-block">Submit</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2';

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login() {
      // API call for login authentication
      const apiLink = this.API_URL + "login/"; // replace with your actual API link
      axios.post(apiLink, {
        username: this.username,
        password: this.password
      })
        .then((response) => {
          if (response.data.status) {
            const role = response.data.role;
            switch (role) {
              case "superuser":
                this.$router.push("/main");
                break;
              case "staff1":
                this.$router.push("/booking");
                break;
              case "staff2":
                this.$router.push("/cashier");
                break;
              case "staff3":
                this.$router.push("/inventory");
                break;
              default:
                // This shouldn't happen, but just in case
                Swal.fire({
                  title: "Error!",
                  text: "Unknown user role.",
                  icon: "error",
                });
            }
            Swal.fire({
              title: "Success!",
              text: "You have successfully logged in.",
              icon: "success",
            });
          } else {
            Swal.fire({
              title: "Error!",
              text: "Invalid username or password.",
              icon: "error",
            });
          }
          console.log(response.data); // replace with your own success handling
        })
        .catch((error) => {
          Swal.fire({
            title: "Error!",
            text: "An error occurred while logging in.",
            icon: "error",
          });
          console.log(error); // replace with your own error handling
        });
    },
  },
};
</script>

<style>
/* Add custom styles here */
</style>
