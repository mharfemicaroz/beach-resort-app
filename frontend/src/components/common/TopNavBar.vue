<template>
<nav class="navbar navbar-expand-lg navbar-light bg-primary shadow-sm no-print"
    :style="{
        'background-image': currentBackground,
        'background-repeat': 'no-repeat',
        'background-position': 'center',
        'background-size': 'cover',
        'background-attachment': 'fixed'
    }">
        <div class="container-fluid">
            <!-- Logo and Search Bar -->
            <a class="navbar-brand text-white align-middlev vv  vv  v  vv v " href="#">
                <div style="display: flex; align-items: center;">
                    <img src="@/assets/pantukan-waterworld-logo.png" width="45" height="45" class="d-inline-block align-top"
                        alt="Pantukan Waterworld Logo" style="margin-right: 10px;">
                    <span style="flex: 1;">Pantukan Waterworld Beach Resort</span>
                </div>
            </a>


            <!-- Navigation Links -->
            <div class="collapse navbar-collapse" id="navbarNav">
                <span class="navbar-text ms-auto me-3 text-white" id="clock">
                    <small>Current Date and Time:</small>
                </span>
                <ul class="navbar-nav">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle text-white" href="#" id="navbarDropdown" role="button"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            <i class="fas fa-user-circle me-1"></i> {{ userdata.fName }} {{ userdata.lName }}
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                            <div v-if="userdata.role === 'superuser'">
                                <li><router-link to="/main" tag="a" class="dropdown-item">Main</router-link></li>
                                <li><router-link to="/booking" tag="a" class="dropdown-item">Booking</router-link></li>
                                <li><router-link to="/inventory" tag="a" class="dropdown-item">Inventory</router-link></li>
                                <li><router-link to="/cashier" tag="a" class="dropdown-item">Cashier</router-link></li>
                                <hr class="dropdown-divider">
                            </div>
                            <li><a class="dropdown-item" href="#" @click=logout()><i class="fas fa-sign-out-alt me-1"></i>
                                    Logout</a></li>
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
            backgroundIndex: 0,
            backgrounds: [
                "src/assets/headerbg1.png",
                "src/assets/headerbg2.png",
                "src/assets/headerbg3.png",
            ],
            user: {
                username: "",
                password: "",
                FirstName: "",
                LastName: "",
                role: ""
            },
        }
    },
    created() { 
        this.startBackgroundSlideshow();
    },
    computed: {
        userdata() {
            const authStore = useAuthStore();
            const user = authStore.user;
            return user;
        },
        currentBackground() {
            return `url(${this.backgrounds[this.backgroundIndex]})`;
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
        startBackgroundSlideshow() {
            setInterval(() => {
                this.backgroundIndex = (this.backgroundIndex + 1) % this.backgrounds.length;
                
            }, 5000);
        },

    }
}
</script>

<style scoped>
.navbar {
    position: relative;
    background-image: url("@/assets/headerbg1.png");
    /* Replace with your background image */
    background-size: cover;
    z-index: 1;
    transition: background-image 1s ease-out;
}

.navbar::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    /* Adjust the opacity and color as desired */
    z-index: -1;
}

/* Custom font style for the top navbar */
.navbar {
    font-family: 'Arial', sans-serif;
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