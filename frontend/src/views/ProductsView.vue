<template>
    <div class="page" id="page-products">
        <div id="products">
            <section id="header">
                <h1>Product List</h1>
                <div id="actions">
                    <PrimaryButton 
                        :text="'New Product'" 
                        @on-hover="changeButtonAddIconColor"
                        @on-leave="changeButtonAddIconColor"
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
import PrimaryButton from '@/components/Buttons/NavButton/PrimaryButton.vue';

const btnAddIconColor = ref("#FFFAFA");

function changeButtonAddIconColor() {
    btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
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
</style>