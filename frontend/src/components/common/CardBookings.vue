<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <div class="row row-cols-1 row-cols-md-4">
                    <div class="col mb-4" v-for="(item, index) in roomData" :key="item.id">
                        <div class="card" style="transition: transform 0.2s ease-in-out;"
                            @click="$emit('click-action', item.itemID, item.name, item.type, item.price)">
                            <div class="card-header d-flex justify-content-between align-items-center"
                                :style="{ 'background-color': item.status === 'reserved' && item.isPaid === 'no' ? '#ef5350' : (item.status === 'reserved' && item.isPaid === 'partial' ? '#5c6bc0' : (item.status === 'checkedin' && item.isPaid === 'no' ? '#66bb6a' : (item.status === 'checkedin' && item.isPaid === 'partial' ? '#42a5f5' : (item.status === 'checkedin' && item.isPaid === 'yes' ? '#ffee58' : (item.status === 'reserved' && item.isPaid === 'yes' ? '#5c6bc0' : ''))))) }">
                                <h5 class="card-title"><i class="fas fa-home"></i> {{ item.name }}</h5>
                            </div>

                            <div class="card-body" v-if="'itemID' in item">
                                <h6>Client Information:</h6>
                                <ul class="list-unstyled">
                                    <li v-if="'groupkey' in item && item.groupkey !==null"><strong><i class="fas fa-user"></i> Client Name:</strong><span class="text-white bg-danger">GROUP</span> - {{ item.clientName }}</li>
                                    <li v-else><strong><i class="fas fa-user"></i> Client Name:</strong>{{ item.clientName }}</li>
                                    <li><strong><i class="fas fa-map-marker-alt"></i> Client Address:</strong> {{
                                        item.clientAddress }}</li>
                                    <li><strong><i class="fas fa-phone"></i> Contact Number:</strong> {{ item.contactNumber }}</li>
                                </ul>
                                <h6>Booking Information:</h6>
                                <ul class="list-unstyled">
                                    <li><strong><i class="fas fa-calendar-alt"></i> Check-in Date:</strong> {{
                                        item.checkinDate }}</li>
                                    <li><strong><i class="fas fa-calendar-check"></i> Check-out Date:</strong> {{
                                        item.checkoutDate }}</li>
                                    <li><strong><i class="fas fa-dollar-sign"></i> Total Charges:</strong> <span
                                            class="text-success">{{ item.totalPrice }}</span></li>
                                    <li><strong><i class="fas fa-money-bill-wave"></i> Partial Payment:</strong> <span
                                            class="text-warning">{{ item.partialPayment }}</span></li>
                                </ul>
                            </div>

                            <div class="card-body" v-else>
                                <div class="alert alert-warning text-center" role="alert">
                                    <h4 class="alert-heading">This room is available for booking</h4>
                                    <p>Please click to continue.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>

export default {
    props: {
        roomData: {
            type: Boolean,
            required: true,
        }
    },
}
</script>
<style></style>