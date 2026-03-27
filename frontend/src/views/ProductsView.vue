<template>
    <div class="page" id="page-products">
        <transition name="fade">
            <Overlay 
                v-if="isModalOpen"
                @on-click="reinitalize"
            >
                <template #sSurface>
                    <transition name="fade" mode="out-in">
                        <ProductCRUDModal 
                            v-if="requestedModal === 'update' || requestedModal === 'add'"
                            key="crud"
                            @on-cancel="reinitalize"
                            @on-submit="handleSubmit"
                            :is-edit="requestedModal === 'update'"
                            :product-item="productItemInfo"
                        />
                        <DeleteModal 
                            v-else-if="requestedModal === 'delete'"
                            key="delete"
                            textTitle="product"
                            desc="This action will permanently delete this product."
                            :items="itemToDelete"
                            @on-cancel="reinitalize"
                            @on-confirm="handleConfirmedDelete"
                        />
                        <MessageModal
                            v-else
                            key="message"
                            :message="messageModalInfo.message"
                            :message-text-color="messageModalInfo.messageTextColor"
                            :icon-border-color="messageModalInfo.iconBorderColor"
                            @on-confirm="reinitalize"
                        >      
                            <template #sMessageIcon>
                                <PackagePlus 
                                    v-if="messageModalInfo.iconType === 'add'"
                                    size="60"
                                    color="var(--color-valid)"
                                />
                                <PackageCheck 
                                    v-else-if="messageModalInfo.iconType === 'update'"
                                    size="60"
                                    color="var(--color-valid)"
                                />
                                <PackageX 
                                    v-else-if="messageModalInfo.iconType === 'delete'"
                                    size="60"
                                    color="var(--color-valid)"
                                />
                                <FilePen 
                                    v-else
                                    size="60"
                                    color="var(--color-valid)"
                                />
                            </template>
                        </MessageModal>
                    </transition>
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
                        @on-click="handleAddRequest"
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
                @edit-item-request="handleEditRequest"
                @delete-item-request="handleDeleteRequest"   
            />
        </div>
    </div>
</template>

<script setup>
import { FilePen, Plus, PackagePlus, PackageCheck, PackageX } from 'lucide-vue-next';

import { onMounted, reactive, ref } from 'vue';

import getAllProducts from '@/modules/product/getAllProducts';
import deleteProduct from '@/modules/product/deleteProduct';

import ProductTable from '@/components/Tables/ProductTable/ProductTable.vue';
import PrimaryButton from '@/components/Buttons/PrimaryButton.vue';
import ProductCRUDModal from '@/components/Modals/ProductCRUDModal.vue';
import Overlay from '@/components/Modals/Overlay.vue';
import DeleteModal from '@/components/Modals/DeleteModal.vue';
import MessageModal from '@/components/Modals/MessageModal.vue';

const btnAddIconColor = ref("#FFFAFA");
const isModalOpen = ref(false);
const requestedModal = ref('');
const productList = ref([]);
const productItemInfo = ref({});
const itemToDelete = ref([]);
const messageModalInfo = reactive({ 
    message: '', 
    messageTextColor: '', 
    iconBorderColor: '',
    iconType: ''
});

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
function renderOverlay(state) {
    isModalOpen.value = state;
};

function handleAddRequest() {
    requestedModal.value = 'add';

    renderOverlay(true);
};

function handleEditRequest(request) {
    for(let iter = 0; iter < productList.value.length; iter++) {
        if (productList.value[iter].id === request.itemID) {
            productItemInfo.value = productList.value[iter];
            break;
        };
    };
    
    requestedModal.value = request.type;
    renderOverlay(true);
};

function handleDeleteRequest(request) {
    for(let iter = 0; iter < productList.value.length; iter++) {
        if (productList.value[iter].id === request.itemID) {
            productItemInfo.value = productList.value[iter];
            break;
        };
    };

    const itemData = [
        { type: 'SKU ID', data: productItemInfo.value.sku },
        { type: 'Product name', data: productItemInfo.value.name },
        { type: 'Category', data: productItemInfo.value.category },
        { type: 'Price', data: productItemInfo.value.price }
    ]

    requestedModal.value = request.type;
    itemToDelete.value = itemData;
    renderOverlay(true);
};

function reinitalize(overlayState) {
    productItemInfo.value = [];
    itemToDelete.value = [];
    requestedModal.value = ''

    renderOverlay(overlayState);
};

function showMessageModal({ message, iconType, color = 'var(--color-valid)' }) {
    messageModalInfo.message = message;
    messageModalInfo.messageTextColor = color;
    messageModalInfo.iconBorderColor = color;
    messageModalInfo.iconType = iconType;

    requestedModal.value = 'message';
};

function updateProduct(product) {
    const targetProduct = productList.value[product.id - 1];

    if (!targetProduct) return;

    Object.assign(targetProduct, {
        sku: product.sku,
        name: product.name,
        category: product.category,
        price: product.price
    });
};

function handleSubmit({ responseType, item }) {
    if (responseType === 'add') {
        item.id = productList.value.length + 1;
        productList.value.push(item);

        showMessageModal({
            message: 'Product added successfully!',
            iconType: 'add'
        });

        return;
    };

    if (responseType === 'updated') {
        updateProduct(item);

        showMessageModal({
            message: 'Product updated successfully!',
            iconType: 'update'
        });

        return;
    };

    showMessageModal({
        message: 'No changes occurred...',
        iconType: 'nochange'
    });
};

async function handleConfirmedDelete() {
    const itemID = productItemInfo.value.id
    const { error, onDelete } = deleteProduct(itemID);

    await onDelete();

    if (error.value === null) {
        for(let iter = 0; iter < productList.value.length; iter++) {
            if (productList.value[iter].id === itemID) {
                productList.value.splice(iter, 1);
                break;
            };
        };

        messageModalInfo.message = 'Product deleted successfully!';
        messageModalInfo.messageTextColor = 'var(--color-valid)';
        messageModalInfo.iconBorderColor = 'var(--color-valid)';
        messageModalInfo.iconType = 'delete'
        requestedModal.value = 'message'
    };
};
</script>

<style scoped>
#products {
    width: 100%;
    position: relative;
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