<template>
    <div class="row row-cols-1 row-cols-md-5">
        <div class="col md-5" v-for="item in itemData" :key="item.id">
            <div class="card" style="height: 175px; width: 175px;transition: transform 0.2s ease-in-out;">
                <img :src="item.imageUrl" class="card-img-top" alt="Item Image"
                    style="height:100px ;" />
                    <div class="card-body m-0 p-1">
                        <h6 class="card-title text-truncate" style="max-height: 1.5em; line-height: 1.5em; overflow: hidden;">
                            {{ item.name }}
                        </h6>
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