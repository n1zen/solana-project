<template>
    <div id="test">
        <!-- Place component here to view alone -->
        <!-- <Nav /> -->
        <!-- <NavButton /> -->
        <!-- <PrimaryButton /> -->
        <!-- <ProductTable /> -->
        <!-- <div>Tite ko</div> -->
        <Overlay>
            <template #sSurface>
                <ProductCRUDModal />
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
</script>

<style scoped>
#test {
    background-color: var(--color-primary);
    width: 100%;
    
    display: flex;
    position: relative;
}
</style>