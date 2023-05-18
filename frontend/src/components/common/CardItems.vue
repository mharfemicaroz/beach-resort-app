<template>
    <div class="row row-cols-1 row-cols-md-4">
        <div class="col mb-4" v-for="item in itemData" :key="item.id">
            <div class="card" style="transition: transform 0.2s ease-in-out;">
                <img :src="item.imageUrl" class="card-img-top img-xl" alt="Item Image"
                    style="width:200px ;height:150px ;" />
                <div class="card-body m-0 p-1">
                    <h5 class="card-title">{{ item.name }}</h5>
                </div>
                <div class="card-footer m-0 p-1">
                    <div class="d-flex justify-content-between align-items-center">
                        <span class="price">₱{{ parseFloat(item.price).toFixed(2) }}</span>
                        <button class="btn btn-primary btn-sm" @click="$emit('click-action', item)">
                            <i class="fa fa-cart-plus me-2"></i>
                            Add
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        itemData: {
            type: Object,
            required: true,
        }
    },
}
</script>
<style></style>