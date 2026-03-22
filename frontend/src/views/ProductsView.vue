<template>
    <div class="page" id="page-products">
        <div id="products">
            <h1>Products</h1>
            <ProductTable />
        </div>
    </div>
</template>

<script setup>
import ProductTable from '@/components/Tables/ProductTable/ProductTable.vue';
</script>

<style scoped>
    #products {
        width: 100%;
    }
</style>