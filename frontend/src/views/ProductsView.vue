<template>
    <div class="page" id="page-products">
        <transition name="fade">
            <Overlay 
                v-if="isModalOpen"
                @on-click="renderModal"
            >
                <template #sSurface>
                    <ProductCRUDModal 
                        @on-cancel="renderModal"
                        @on-submit="handleSubmit"
                        :is-edit="editItemState"
                        :product-item="productItemInfo"
                    />
                </template>
            </Overlay>
        </transition>
        <div id="products">
            <section id="header">
                <h1>Product List</h1>
                <div id="actions">
                    <PrimaryButton 
                        :text="'New Product'" 
                        @on-hover="changeButtonAddIconColor"
                        @on-leave="changeButtonAddIconColor"
                        @on-click="renderModal"
                    >
                        <template #sIcon>
                             <Plus 
                                size="18"
                                :color="btnAddIconColor"
                             />
                        </template>
                    </PrimaryButton>
                </div>
            </section>
            <ProductTable 
                :product-list="productList"
                @edit-item-request="renderModal"    
            />
        </div>
    </div>
</template>

<script setup>
import { Plus } from 'lucide-vue-next';

import { onMounted, ref } from 'vue';

import getAllProducts from '@/modules/product/getAllProducts';

import ProductTable from '@/components/Tables/ProductTable/ProductTable.vue';
import PrimaryButton from '@/components/Buttons/PrimaryButton.vue';
import ProductCRUDModal from '@/components/Modals/ProductCRUDModal.vue';
import Overlay from '@/components/Modals/Overlay.vue';

const btnAddIconColor = ref("#FFFAFA");
const isModalOpen = ref(false);
const productList = ref([]);
const productItemInfo = ref({});
const editItemState = ref(false);

const { products, error, load } = getAllProducts();

// Get products from the server
onMounted(async () => {
    await load();

    if (error.value === null) {
        productList.value = products.value;
    };
});

function changeButtonAddIconColor() {
    btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
};

// Renders the modal
function renderModal(isEdit, itemID) {
    editItemState.value = false;
    isModalOpen.value = !isModalOpen.value;

    if (isEdit) {
        editItemState.value = true;
        productItemInfo.value = productList.value[itemID - 1]
        console.log(productItemInfo.value);
    };
};

function handleSubmit(isEdit, newItem) {
    if (!isEdit) {
        newItem.id = productList.value.length + 1
        productList.value.push(newItem);
    } else {
        productList.value[newItem.id - 1].sku = newItem.sku;
        productList.value[newItem.id - 1].name = newItem.name;
        productList.value[newItem.id - 1].category = newItem.category;
        productList.value[newItem.id - 1].price = newItem.price;
    };

    renderModal(); // change this later
};
</script>

<style scoped>
#products {
    width: 100%;
}

#header {
    margin-bottom: 50px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

#header h1 {
    color: var(--color-secondary);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>