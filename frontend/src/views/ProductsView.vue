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
            <ProductTable />
        </div>
    </div>
</template>

<script setup>
import { Plus } from 'lucide-vue-next';

import { ref } from 'vue';

import ProductTable from '@/components/Tables/ProductTable/ProductTable.vue';
import PrimaryButton from '@/components/Buttons/PrimaryButton.vue';
import ProductCRUDModal from '@/components/Modals/ProductCRUDModal.vue';
import Overlay from '@/components/Modals/Overlay.vue';

const btnAddIconColor = ref("#FFFAFA");
const isModalOpen = ref(false);

function changeButtonAddIconColor() {
    btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
};

// Renders the modal
function renderModal() {
    isModalOpen.value = !isModalOpen.value;
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