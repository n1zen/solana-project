<template>
    <div class="container" v-if="product">
        <ProductCard :product="product" @edit="showEdit = true"/>
    </div>
    <div v-else>
        Loading...
    </div>
    <ProductEdit v-if="showEdit" :product="product" @close="showEdit = false"/>
</template>
<script>
import ProductCard from './ProductCard.vue';
import ProductEdit from './modals/ProductEdit.vue';
import getProduct from '@/composables/Products/getProduct.js';
import { useRoute } from 'vue-router';
import { ref } from 'vue';
export default {
    components: {
        ProductCard,
        ProductEdit
    },
    setup() {
        const route = useRoute()
        const productId = route.params.id
        const showEdit = ref(false);

        const { product, error, load } = getProduct(productId)

        load()

        return { product, error, showEdit }
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