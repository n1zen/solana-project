<template>
    <div id="test">
        <!-- Place component here to view alone -->
        <!-- <Nav /> -->
        <!-- <NavButton /> -->
        <!-- <PrimaryButton /> -->
        <!-- <ProductTable /> -->
        <Overlay>
            <template #sSurface>
                <!-- <ProductCRUDModal /> -->
                <!-- <DeleteModal 
                    textTitle="product"
                    desc="This action will permanently delete this product."
                    :items="[
                        { type: 'SKU ID', data: '250001' },
                        { type: 'Product Name', data: 'Cat in Box' },
                        { type: 'Categori', data: 'Animal' },
                        { type: 'Price', data: '$15' }
                    ]"
                /> -->
                <MessageModal>
                    <template #sMessageIcon>
                        <PackageCheck 
                        size="75"
                        color="var(--color-valid)"
                        />
                    </template>
                </MessageModal>
            </template>
        </Overlay>
        <!-- <BasicTextInput 
            hint="SKU ID*"
        /> -->
    </div>  
</template>

<script setup>
import Nav from '@/components/Nav/Nav.vue';
import NavButton from '@/components/Buttons/NavButton.vue';
import PrimaryButton from '@/components/Buttons/PrimaryButton.vue';
import ProductTable from '@/components/Tables/ProductTable/ProductTable.vue';
import Overlay from '@/components/Modals/Overlay.vue';
import ProductCRUDModal from '@/components/Modals/ProductCRUDModal.vue';
import BasicTextInput from '@/components/Inputs/BasicTextInput.vue';
import DeleteModal from '@/components/Modals/DeleteModal.vue';
import MessageModal from '@/components/Modals/MessageModal.vue';
import { PackageCheck } from 'lucide-vue-next';
</script>

<style scoped>
#test {
    background-color: var(--color-primary);
    width: 100%;
    
    display: flex;
    position: relative;
}
</style>