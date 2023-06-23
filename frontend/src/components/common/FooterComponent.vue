<template>
    <footer class="text-dark mt-2 fixed-bottom" style="background-color: #ECEFF1;">
        <div class="container py-3">
            <div class="d-flex justify-content-between align-items-center">
                <div>
                    <i class="fas fa-code-branch"></i> Version: {{ version }}
                </div>
                <div>
                    <i class="fas fa-user"></i> Provider: {{ provider }}
                </div>
                <div>
                    <i class="fas fa-eye"></i> Page Visits: {{ pageVisits }}
                </div>
            </div>
        </div>
    </footer>
</template>
  
<script>
export default {
    data() {
        return {
            version: "1.3.0",
            provider: "Web App Solutions",
            pageVisits: 0
        };
    },
    mounted() {
        // Retrieve the page visits count from the cookie
        this.pageVisits = parseInt(this.getCookie("pageVisits")) || 0;

        // Increment the page visits count
        this.pageVisits++;

        // Set the updated page visits count to the cookie
        this.setCookie("pageVisits", this.pageVisits, 30);
    },
    methods: {
        setCookie(name, value, days) {
            const date = new Date();
            date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
            const expires = "expires=" + date.toUTCString();
            document.cookie = name + "=" + value + ";" + expires + ";path=/";
        },
        getCookie(name) {
            const cookieName = name + "=";
            const decodedCookie = decodeURIComponent(document.cookie);
            const cookieArray = decodedCookie.split(";");

            for (let i = 0; i < cookieArray.length; i++) {
                let cookie = cookieArray[i];
                while (cookie.charAt(0) === " ") {
                    cookie = cookie.substring(1);
                }
                if (cookie.indexOf(cookieName) === 0) {
                    return cookie.substring(cookieName.length, cookie.length);
                }
            }

            return "";
        }
    }
};
</script>
<style scoped>
body {
    font-family: 'Arial', sans-serif;
}
</style>