<template>
    <div class="container-fluid">
        <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm">
            <div class="container-fluid">
                <!-- Logo and Search Bar -->
                <a class="navbar-brand" href="#">
                    <img src="@/assets/pantukan-waterworld-logo.jpg" width="45" height="45" class="d-inline-block align-top"
                        alt="Pantukan Waterworld Logo">
                    Pantukan Waterworld Beach Resort
                </a>

                <!-- Navigation Links -->
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav me-auto">

                    </ul>
                    <ul class="navbar-nav">
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                                data-bs-toggle="dropdown" aria-expanded="false">
                                <img src="@/assets/user-avatar.png" class="rounded-circle" alt="User Avatar" height="32"
                                    width="32">
                                    {{ userdata.fName }} {{ userdata.lName }}
                            </a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a class="dropdown-item" href="#" @click=logout()>Logout</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>


        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-12">
                    <ul class="nav nav-tabs justify-content-left">
                        <li class="nav-item">
                            <a class="nav-link active" data-bs-toggle="tab" href="#users">
                                <i class="fas fa-users fa-2x"></i>
                                <br>
                                Users
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="tab" href="#rooms">
                                <i class="fas fa-door-open fa-2x"></i>
                                <br>
                                Rooms
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="tab" href="#leisures">
                                <i class="fas fa-swimming-pool fa-2x"></i>
                                <br>
                                Leisures
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-bs-toggle="tab" href="#settings">
                                <i class="fas fa-cog fa-2x"></i>
                                <br>
                                Settings
                            </a>
                        </li>
                    </ul>
                    <div class="tab-content">
                        <div id="users" class="tab-pane active">
                            <div id="users" class="tab-pane active">
                                <div class="row">
                                    <div class="col-md-3">
                                        <form @submit.prevent="saveUser">
                                            <div class="mb-3">
                                                <label for="username" class="form-label">Username</label>
                                                <input type="text" class="form-control" id="username"
                                                    v-model="user.username" required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="password" class="form-label">Password</label>
                                                <input type="text" class="form-control" id="password"
                                                    v-model="user.password" required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="firstName" class="form-label">First Name</label>
                                                <input type="text" class="form-control" id="firstName"
                                                    v-model="user.FirstName" required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="lastName" class="form-label">Last Name</label>
                                                <input type="text" class="form-control" id="lastName"
                                                    v-model="user.LastName" required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="role" class="form-label">Role</label>
                                                <select class="form-select" id="role" v-model="user.role" required>
                                                    <option value="">-- Select Role --</option>
                                                    <option value="reservationist">Front Desk</option>
                                                    <option value="cashier">Cashier</option>
                                                    <option value="inventorymanager">Inventory Manager</option>
                                                </select>
                                            </div>
                                            <button type="submit" class="btn btn-primary">{{ isUpdating ? 'Update' : 'Save' }}</button>
                                        </form>
                                    </div>
                                    <div class="col-md-9">
                                        <table class="table">
                                            <thead>
                                                <tr>
                                                    <th>Username</th>
                                                    <th>First Name</th>
                                                    <th>Last Name</th>
                                                    <th>Role</th>
                                                    <th>Action</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr v-for="user in users" :key="user.id">
                                                    <td>{{ user.username }}</td>
                                                    <td>{{ user.FirstName }}</td>
                                                    <td>{{ user.LastName }}</td>
                                                    <td>{{ user.role }}</td>
                                                    <td>
                                                        <button type="button" class="btn btn-primary btn-sm"
                                                            @click="editUser(user.id)"><i
                                                                class="fas fa-edit"></i></button>&nbsp;
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>

                        </div>
                        <div id="rooms" class="tab-pane">
                            <!-- Rooms content here -->
                        </div>
                        <div id="leisures" class="tab-pane">
                            <!-- Leisures content here -->
                        </div>
                        <div id="settings" class="tab-pane">
                            <!-- Settings content here -->
                        </div>
                    </div>
                </div>
            </div>
        </div>



    </div>
</template>
  
<script>
import { useAuthStore } from "@/stores/authStore";
import axios from 'axios';

export default {
    data() {
        return {
            users: [],
            user: {
                username: "",
                password: "",
                FirstName: "",
                LastName: "",
                role: ""
            },
            isUpdating: false
        };
    },
    created() {
        this.getUsers();
    },
    computed: {
        userdata() {
        const authStore = useAuthStore();
        const user = authStore.user;
        return user;
        },
    },
    methods: {
        logout() {
      const authStore = useAuthStore();
      authStore.logout();
      this.$router.push('/');
    },
        getUsers() {
            axios
                .get(`${this.API_URL}users/`)
                .then(response => {
                    this.users = response.data.filter(item => item.role !== 'superuser');
                })
                .catch(error => {
                    console.log(error);
                });
        },
        saveUser() {
            if (this.isUpdating) {
                axios
                    .put(`${this.API_URL}users/${this.user.id}/`, this.user)
                    .then(response => {
                        this.$swal({
                            icon: "success",
                            title: "User updated successfully"
                        });
                        this.getUsers();
                        this.user = {
                            id: null,
                            username: "",
                            password: "",
                            firstName: "",
                            lastName: "",
                            role: ""
                        };
                        this.isUpdating = false;
                    })
                    .catch(error => {
                        console.log(error);
                    });
            } else {
                axios
                    .post(`${this.API_URL}users/filter/`, { columnName: 'username', columnKey: this.user.username })
                    .then(response => {
                        if (response.data.length > 0) {
                            this.$swal({
                                icon: "error",
                                title: "Username already exists"
                            });
                        } else {
                            axios
                                .post(`${this.API_URL}users/`, this.user)
                                .then(response => {
                                    this.$swal({
                                        icon: "success",
                                        title: "User saved successfully"
                                    });
                                    this.getUsers();
                                    this.user = {
                                        username: "",
                                        password: "",
                                        FirstName: "",
                                        LastName: "",
                                        role: ""
                                    };
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
        editUser(id) {
            axios
                .get(`${this.API_URL}users/${id}/`)
                .then(response => {
                    this.user = response.data;
                    this.isUpdating = true;
                })
                .catch(error => {
                    console.log(error);
                });
        }
    },
    mounted() {
        document.documentElement.requestFullscreen();
    }
};
</script>
  