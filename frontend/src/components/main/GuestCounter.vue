<template>
    <TopNavBarComponent />
    <div class="container-fluid login-background">
        <div class="row justify-content-center align-items-center vh-100">
            <div class="col-md-3">
                <form @submit.prevent="login" class="animated-form login-form">
                    <div class="widget-container">
                        <div class="status-icons">
                            <div v-for="icon in icons" :key="icon.name"
                                :class="['status-icon', { active: selectedIcon === icon.name }]"
                                @click="selectIcon(icon.name)">
                                <i :class="icon.class"></i>
                                <span>{{ icon.label }}</span>
                            </div>
                        </div>
                        <div class="counter text-dark">
                            {{ counter }}
                        </div>
                        <div class="m-btn-group m-btn-group--pill btn-group d-flex justify-content-center" role="group">
                            <button type="button" class="m-btn btn-light btn btn-default" @click="decrementCounter">
                                <i class="fa fa-minus"></i>
                            </button>
                            <button type="button" class="m-btn btn-light btn btn-default" @click="undo"
                                :disabled="iconHistory.length === 1">
                                <i class="fa fa-undo"></i>
                            </button>
                            <button type="button" class="m-btn btn-light btn btn-default" @click="incrementCounter"
                                :disabled="selectedIcon === ''">
                                <i class="fa fa-plus"></i>
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { useAuthStore } from "@/stores/authStore";
import TopNavBarComponent from "@/components/common/TopNavBar.vue";
export default {
    components: {
        TopNavBarComponent,
    },
    data() {
        return {
            selectedIcon: '', // Tracks the currently selected icon
            counter: 0, // Tracks the counter value
            iconHistory: [
                {
                    counter: 0,
                    icon: '',
                }
            ], // Stores the history of selected icons
            previousCounter: 0 // Stores the previous counter value for undo functionality
        };
    },
    created(){
        this.loadData();
    },
    computed: {
        userdata() {
            const authStore = useAuthStore();
            const user = authStore.user;
            return user;
        },
        icons() {
            return [
                { name: 'walk-in', class: 'fa fa-walking', label: 'Walk-in' },
                { name: 'reserved', class: 'fa fa-calendar-check', label: 'Reserved' },
                { name: 'guest', class: 'fa fa-user', label: 'Guest' }
            ];
        },
    },
    methods: {
        loadData(){
            axios
            .get(`${this.API_URL}guestcounter/`)
            .then(response => {
                this.iconHistory = response.data;
            })
            .catch(error => {
            console.log(error);
            });
        },
        selectIcon(icon) {
            this.selectedIcon = this.selectedIcon === icon ? '' : icon; // Toggle the selectedIcon value
        },
        incrementCounter() {
            this.previousCounter = this.counter; // Store the previous counter value
            this.counter++;
            this.addToHistory();
        },
        decrementCounter() {
            if (this.counter > 0) {
                this.previousCounter = this.counter; // Store the previous counter value
                this.counter--;
                this.addToHistory();
            }
        },
        undo() {
            if (this.iconHistory.length > 0) {
                const previousState = this.iconHistory.pop();
                this.counter = previousState.counter - 1;
                this.selectedIcon = this.iconHistory[this.iconHistory.length - 1].icon;
            } else {
                this.counter = 0;
                this.selectedIcon = '';
            }
        },
        addToHistory() {
            const state = {
                counter: this.counter,
                icon: this.selectedIcon
            };
            this.iconHistory.push(state);
        },
        async logout() {
            const authStore = useAuthStore();
            const user = {
                username: authStore.user.username,
                FirstName: authStore.user.fName,
                LastName: authStore.user.lName,
                role: authStore.user.role
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
    },
    mounted() {

    },
}

</script>

<style>
/* Add custom styles here */
.login-background {
    background: url("@/assets/beach-resort-background.jpg") no-repeat center center fixed;
    background-size: cover;
    background-position: center;
}

.animated-form {
    animation: fly-in 0.5s ease-out;
    opacity: 1;
    transform: translateY(0);
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

.login-background {
    background-color: #f2f2f2;
}

.login-form {
    margin: 0 auto;
}

.widget-container {
    width: 250px;
    margin: 50px;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    padding: 20px;
    text-align: center;
}

.counter {
    font-size: 64px;
    font-weight: bold;
    margin-bottom: 20px;
}

.m-btn-group {
    margin-top: 20px;
}

.btn-default {
    border: none;
    background-color: transparent;
    font-size: 24px;
    padding: 0;
}

.btn-default i {
    color: #333333;
    cursor: pointer;
}

.btn-default:focus {
    outline: none;
}

.btn-default:hover i {
    color: #888888;
}

.status-icons {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.status-icon {
    display: flex;
    flex-direction: column;
    align-items: center;
    cursor: pointer;
}

.status-icon.active {
    font-size: 24px;
    /* Increase the font size when active */
    color: blue;
    /* Change the color when active */
}

.status-icon i {
    font-size: 24px;
    margin-bottom: 5px;
}

.status-icon span {
    font-size: 12px;
    color: #333333;
}
</style>