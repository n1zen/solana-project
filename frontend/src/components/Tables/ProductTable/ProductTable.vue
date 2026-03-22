<template>
    <div class="product-table">
        <table id="products">
            <thead>
                <tr id="legend">
                    <th id="legend-id">
                        <input type="checkbox" name="" id="">
                        <span class="legend-text">SKU ID</span>
                    </th>
                    <th id="legend-name">
                        <span class="legend-text">Product Name</span>
                    </th>
                    <th id="legend-category">
                        <span class="legend-text">Category</span>
                    </th>
                    <th id="legend-price">
                        <span class="legend-text">Price</span>
                    </th>
                    <th id="legend-actions">
                        <span class="legend-text">Actions</span>
                    </th>
                </tr>
            </thead>
            <tbody>
                <ProductInfoRow
                    :index="1"
                    :clickStatusFromParent="activeProductIndex === 1"
                    @isClicked="changeClickedProductInfo" 
                    />
                <ProductInfoRow 
                    :index="2"
                    :clickStatusFromParent="activeProductIndex === 2"
                    @isClicked="changeClickedProductInfo" 
                />
                <ProductInfoRow
                    :index="3"
                    :clickStatusFromParent="activeProductIndex === 3"
                    @isClicked="changeClickedProductInfo" 
                />
            </tbody>
        </table>
    </div>
</template>

<script setup>
import { ref } from 'vue';

import ProductInfoRow from './ProductInfoRow.vue';

const activeProductIndex = ref(null);

function changeClickedProductInfo(indexFromChild) {
    activeProductIndex.value = indexFromChild;
}
</script>

<style scoped>
table {
    border-collapse: collapse;
    table-layout: fixed;
}

th {
    border-bottom: 1px solid var(--color-accent);
    color: var(--color-accent);
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    padding: 20px 10px;
    transition: 0.3s
}

th:nth-child(5) {
    width: 75px;
}

tr {
    background-color: transparent;
    transition: 0.3s;

    &.isClicked {
        background-color: var(--color-secondary);
    }

    &:hover:not(.isClicked) {
        background-color: #ffb7b482
    }
}

.product-table {
    width: 100%;
}

#products {
    width: 100%;
}

#legend th {
    text-align: left;
}

#legend-id span {
    margin-left: 10px;
}
</style>