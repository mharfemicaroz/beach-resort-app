<template :key="componentKey">
    <TopNavBarComponent />
    <div class="container-fluid login-background">
        <div class="row justify-content-center align-items-center vh-100">
            <div class="col-md-3">
                <form @submit.prevent="login" class="animated-form login-form">
                    <div class="widget-container">
                        <div class="counter text-dark">
                            {{ counter }}
                        </div>
                        <div class="m-btn-group m-btn-group--pill btn-group d-flex justify-content-center" role="group">
                            <button type="button" class="m-btn btn-light btn btn-default" @click="decrementCounter">
                                <i class="fa fa-minus"></i>
                            </button>
                            <button type="button" class="m-btn btn-light btn btn-default" @click="undo">
                                <i class="fa fa-undo"></i>
                            </button>
                            <button type="button" class="m-btn btn-light btn btn-default" @click="incrementCounter">
                                <i class="fa fa-plus"></i>
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <FooterComponent />
</template>

<script>
import axios from 'axios';
import { useAuthStore } from "@/stores/authStore";
import TopNavBarComponent from "@/components/common/TopNavBar.vue";
import FooterComponent from "../common/FooterComponent.vue";

function padTo2Digits(num) {
    return num.toString().padStart(2, '0');
}

function parseDate(date = new Date()) {
    return [
        date.getFullYear(),
        padTo2Digits(date.getMonth() + 1),
        padTo2Digits(date.getDate()),
    ].join('-');
}

function formatDate(dateString) {
    const index = dateString.indexOf('T');
    const result = dateString.substring(0, index);
    const [year, month, day] = result.split('-');
    return `${year}-${month}-${day}`;
}

export default {
    components: {
        TopNavBarComponent,
        FooterComponent,
    },
    data() {
        return {
            socket : null,
            componentKey : 0,
            counter: 0, // Tracks the counter value
            track: [],
        };
    },
    created() {
        this.loadData();
    },
    computed: {
        userdata() {
            const authStore = useAuthStore();
            const user = authStore.user;
            return user;
        },
    },
    methods: {
        loadData() {
            axios
                .get(`${this.API_URL}guestcounter/`)
                .then(response => {
                    this.track = response.data;
                    this.viewCounter();
                })
                .catch(error => {
                    console.log(error);
                });
        },
        incrementCounter() {
            this.counter++;
            this.setCounter();
        },
        decrementCounter() {
            if (this.counter > 0) {
                this.counter--;
                this.setCounter();
            }
        },
        async viewCounter() {
            const foundItem = this.track.find((item) => formatDate(item.date_created) === parseDate(new Date()));
            if (foundItem) {
                this.counter = parseFloat(foundItem.counter);
            } else {
                this.counter = 0;
            }
        },
        async setCounter() {
            const foundItem = this.track.find((item) => formatDate(item.date_created) === parseDate(new Date()));
            if (foundItem) {
                await axios.put(`${this.API_URL}guestcounter/${foundItem.id}/`, {
                    counter: this.counter,
                })
            } else {
                await axios.post(`${this.API_URL}guestcounter/`, {
                    counter: this.counter,
                })
            }
            this.socket.send('{"message":"add+1 guest"}');
        },
        async undo() {
            const confirmMessage = 'This action cannot be undone.';
            const result = await this.$swal.fire({
                title: 'Are you sure you want to reset the counter? ',
                text: confirmMessage,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes, reset it!',
                cancelButtonText: 'Cancel'
            });
            if (result.isConfirmed) {
                const countdownMessage = 'This counter will be resetted to zero in <span id="countdown">5</span> seconds. Do you want to cancel?';
                let countdownResult;
                countdownResult = await this.$swal.fire({
                    title: 'Please wait',
                    html: countdownMessage,
                    icon: 'info',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Confirm now',
                    cancelButtonText: 'Cancel',
                    didOpen: () => {
                        const countdownEl = document.querySelector('#countdown');
                        let count = 4;
                        const timerId = setInterval(() => {
                            countdownEl.textContent = count;
                            count--;
                            if (count < 0) {
                                clearInterval(timerId);
                                this.$swal.close();
                            }
                        }, 1000);
                    }
                });

                if (!countdownResult.isConfirmed) {
                    return;
                }

                this.counter = 0;
                this.setCounter();
            }

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
        this.socket = new WebSocket(`ws://${this.API_URL.replace(/^https?:\/\//, '')}ws/realtime/`);
        const vm = this;
        this.socket.onmessage = function (e) {
            const data = JSON.parse(e.data);
            console.log(data.message)
            vm.loadData();
            vm.componentKey += 1;
        };
    },
}

</script>

<style scoped>
/* Add custom styles here */
.login-background {
    background: url("@/assets/beach-resort-background2.jpg") no-repeat center center fixed;
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
    font-size: 128px;
    font-weight: bold;
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
</style>