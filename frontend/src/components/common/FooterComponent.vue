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
                <div>
                    <a href="#" @click="captureScreenshot">
                        <i class="fas fa-bug"></i> Report Bug
                    </a>
                </div>
            </div>
        </div>
    </footer>

    <div class="modal fade" id="bugModal" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Report Bug</h5>
                    <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form>
                        <div class="form-group">
                            <label for="bugDescription">Bug Description:</label>
                            <textarea v-model="bugDescription" class="form-control" id="bugDescription" rows="3"></textarea>
                        </div>
                        <div class="form-group">
                            <label for="screenshot">Attached screenshot:</label>&nbsp;
                            <a :href="this.API_URL+'Photos/'+PhotoFileName" target="_blank" class="text-info">{{ PhotoFileName }}</a>
                        </div>

                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" @click="submitBugReport">Submit</button>
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>

import axios from 'axios';
import html2canvas from 'html2canvas';


export default {
    data() {
        return {
            version: "1.9.8",
            provider: "Web App Solutions",
            pageVisits: 0,
            bugDescription: "",
            PhotoFileName: "",
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
        showModal(){
            $("#bugModal").modal("toggle");
        },
        async submitBugReport() {
            // Perform form validation here, if needed

            const bugReportData = {
                description: this.bugDescription,
                screenshot_file_name: this.PhotoFileName, // Assuming you want to include the uploaded screenshot file name
            };

            try {
                const response = await axios.post(this.API_URL + "bugreports/", bugReportData);
                // Handle the response or perform any necessary actions upon successful submission
                console.log(response);

                // Show success alert
                this.$swal({
                    title: 'Bug Report Submitted',
                    text: 'Thank you for reporting the bug!',
                    icon: 'success',
                    button: 'OK',
                });
                $("#bugModal").modal("toggle");

            } catch (error) {
                // Handle the error or display an error message
                console.error(error);

                // Show error alert
                this.$swal({
                    title: 'Error',
                    text: 'An error occurred while submitting the bug report.',
                    icon: 'error',
                    button: 'OK',
                });
            }
        },

        async captureScreenshot() {
            try {
                const canvas = await html2canvas(document.body);
                const dataUrl = canvas.toDataURL('image/png');

                // Convert data URL to a File object
                const blobBin = atob(dataUrl.split(',')[1]);
                const array = [];
                for (let i = 0; i < blobBin.length; i++) {
                    array.push(blobBin.charCodeAt(i));
                }
                const screenshotFile = new Blob([new Uint8Array(array)], { type: 'image/png' });

                // Generate a unique filename for the screenshot
                const currentDate = new Date().toISOString().slice(0, 10).replace(/-/g, '_');
                const uniqueID = Math.floor(10000 + Math.random() * 90000);
                const fileName = `screenshot_${currentDate}_${uniqueID}.png`;

                // Upload the screenshot file
                let formData = new FormData();
                formData.append('file', screenshotFile, fileName);

                const response = await axios.post(this.API_URL + "bugreports/savefile", formData);
                this.PhotoFileName = response.data;
                this.showModal();
            } catch (error) {
                // Handle the error or display an error message
                console.error(error);

                // Show error alert
                this.$swal({
                    title: 'Error',
                    text: 'An error occurred while capturing the screenshot.',
                    icon: 'error',
                    button: 'OK',
                });
            }
        },
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
        },

        handleFileSelection(event) {
            const file = event.target.files[0];
            const maxFileSize = 10 * 1024 * 1024; // 10MB

            // Check if a file was selected
            if (file) {
                // Check if the file is an image
                if (file.type.startsWith('image/')) {
                    // Check the file size
                    if (file.size <= maxFileSize) {
                        // Handle the valid image file
                        //this.uploadFile(file);
                    } else {
                        this.$swal({
                            title: 'Error',
                            text: `File size exceeds the limit of 10MB: ${file.name}`,
                            icon: 'error',
                            button: 'OK',
                        });

                    }
                } else {
                    this.$swal({
                        title: 'Error',
                        text: `Invalid file type. Only image files are allowed: ${file.name}`,
                        icon: 'error',
                        button: 'OK',
                    });

                }
            }
        },

        uploadFile(file) {
            // Implement your file upload logic here
            // This method will be called with each valid image file
            // You can perform any necessary file upload operations
            // e.g., using AJAX or a file upload library

        }
    },
    mounted() {
        
    }
};
</script>
<style scoped>
body {
    font-family: 'Arial', sans-serif;
}
</style>