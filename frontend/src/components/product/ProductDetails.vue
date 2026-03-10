<template>
    <div class="container" v-if="product">
        <ProductCard :product="product"/>
    </div>
    <div v-else>
        Loading...
    </div>
</template>
<script>
import ProductCard from './ProductCard.vue';
import getProduct from '@/composables/Products/getProduct.js';
import { useRoute } from 'vue-router'
export default {
    components: {
        ProductCard
    },
    setup() {
        const route = useRoute()
        const productId = route.params.id

        const { product, error, load } = getProduct(productId)

        load()

        return { product, error }
    }
}
</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
}
</style>