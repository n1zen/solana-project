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
            <tbody
                :class="[ productList.length === 0 ? 'empty' : '' ]"    
            >
                <ProductInfoRow 
                    v-if="productList.length !== 0"
                    v-for="id in productList.length" 
                    :productInfo="productList[id - 1]" 
                    :index="id"
                    :clickStatusFromParent="activeProductIndex === id" 
                    @isClicked="changeClickedProductInfo" 
                    @onEditClick="handleEditRequestFromChild"
                    @onDeleteClick="handleDeleteRequestFromChild"
                />
                <div v-else id="empty-list">
                    <div id="empty-icon">
                        <PackageSearch 
                            size="80"
                        />
                    </div>
                    <p id="empty-text">
                        There are no products available...
                        <br>
                    </p>
                </div>
            </tbody>
        </table>
    </div>
</template>

<script setup>
import { ref } from 'vue';

import ProductInfoRow from './ProductInfoRow.vue';
import { PackageSearch } from 'lucide-vue-next';

const props = defineProps({
    productList: {
        type: Array,
        default: []
    }
});

const emits = defineEmits([
    'editItemRequest',
    'deleteItemRequest'
]);

const activeProductIndex = ref(null);

function changeClickedProductInfo(indexFromChild) {
    activeProductIndex.value = indexFromChild;
}

function handleEditRequestFromChild(itemID) {
    // emits('editItemRequest', true, itemID);
    emits('editItemRequest', {
        type: 'update',
        itemID
    });
};

function handleDeleteRequestFromChild(itemID) {
    emits('deleteItemRequest', {
        type: 'delete',
        itemID
    });
};
</script>

<style scoped>
table {
    border-collapse: collapse;
    table-layout: fixed;
}

/* tbody.empty {
    position: relative;
} */

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

/* 
*   Position relative @ ProductsView.vue 
*   #products
*/
#empty-list {
    color: var(--color-secondary);
    font-size: 18px;
    text-align: center;
    display: flex;
    flex-direction: column;
    gap: 20px;
    align-items: center;
    justify-content: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

#empty-icon {
    border: 3px solid var(--color-secondary);
    border-radius: 50%;
    padding: 25px;
}
</style>