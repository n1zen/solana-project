<template>
    <div class="container" v-if="product">
        <ProductCard :product="product" @edit="showEdit = true" @delete="showDelete = true"/>
    </div>
    <div v-else>
        Loading...
    </div>
    <ProductEdit v-if="showEdit" :product="product" @close="showEdit = false"/>
    <ProductDelete v-if="showDelete" @close="showDelete = false" @onDelete="onDelete"/>
</template>
<script>
import deleteProduct from '@/composables/Products/deleteProduct';
import ProductCard from './ProductCard.vue';
import ProductDelete from './modals/ProductDelete.vue';
import ProductEdit from './modals/ProductEdit.vue';
import getProduct from '@/composables/Products/getProduct.js';
import { useRoute } from 'vue-router';
import { ref } from 'vue';
export default {
    components: {
        ProductCard,
        ProductEdit,
        ProductDelete,
    },
    setup() {
        const route = useRoute()
        const productId = route.params.id
        const showEdit = ref(false);
        const showDelete = ref(false);

        const { product, error, load } = getProduct(productId)
        const { delError, onDelete } = deleteProduct(productId)

        load()

        return { product, error, showEdit, showDelete , onDelete, delError }
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