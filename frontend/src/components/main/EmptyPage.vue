<template>
    <div class="container-fluid login-background">
        <div class="row justify-content-center align-items-center vh-100">
            <div class="col-md-3">

            </div>
        </div>
    </div>
</template>

<script>
export default {
    components: {

    },
    data() {
        return {

        };
    },
    created(){

    },
    computed: {

    },
    methods: {

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