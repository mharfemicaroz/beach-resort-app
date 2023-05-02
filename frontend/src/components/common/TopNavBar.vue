<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm no-print">
        <div class="container-fluid">
            <!-- Logo and Search Bar -->
            <a class="navbar-brand" href="#">
                <img src="@/assets/pantukan-waterworld-logo.png" width="45" height="45" class="d-inline-block align-top"
                    alt="Pantukan Waterworld Logo">
                Pantukan Waterworld Beach Resort
            </a>

            <!-- Navigation Links -->
            <div class="collapse navbar-collapse" id="navbarNav">
    <span class="navbar-text ms-auto me-3" id="clock">
        <small>Current Date and Time:</small>
    </span>
    <ul class="navbar-nav">
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                data-bs-toggle="dropdown" aria-expanded="false">
                <img src="@/assets/user-avatar.png" class="rounded-circle" alt="User Avatar" height="32"
                    width="32">
                {{ userdata.fName }} {{ userdata.lName }}
            </a>
            <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                <div v-if="userdata.role === 'superuser'">
                    <li><router-link to="/main" tag="a" class="dropdown-item">Main</router-link></li>
                    <li><router-link to="/booking" tag="a" class="dropdown-item">Booking</router-link></li>
                    <li><router-link to="/inventory" tag="a" class="dropdown-item">Inventory</router-link></li>
                    <li><router-link to="/cashier" tag="a" class="dropdown-item">Cashier</router-link></li>
                    <hr class="dropdown-divider">
                </div>
                <li><a class="dropdown-item" href="#" @click=logout()>Logout</a></li>
            </ul>
        </li>
    </ul>
</div>


        </div>
    </nav>
</template>

<script>

setInterval(() => {
        const clock = document.querySelector('#clock');
        const now = new Date();
        clock.innerHTML = `<small>Current Date and Time: ${now.toLocaleString()}</small>`;
    }, 1000);

import { useAuthStore } from "@/stores/authStore";
import axios from 'axios';
export default {
    data() {
        return {
            user: {
                username: "",
                password: "",
                FirstName: "",
                LastName: "",
                role: ""
            },
        }
    },
    computed: {
        userdata() {
            const authStore = useAuthStore();
            const user = authStore.user;
            return user;
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
        },
    }
}
</script>