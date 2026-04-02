<template>
    <div id="test">
        <!-- Place component here to view alone -->
        <!-- <Nav /> -->
        <!-- <NavButton /> -->
        <!-- <PrimaryButton /> -->
        <!-- <Overlay>
            <template #sSurface> -->
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
                <!-- <MessageModal>
                    <template #sMessageIcon>
                        <PackageCheck 
                        size="75"
                        color="var(--color-valid)"
                        />
                    </template>
                </MessageModal> -->
                <!-- <SimpleAddEditModal 
                    modalType="edit"
                    modalSubmitText="Add Product"
                    :fields="[
                        {
                            id: 1,
                            type: 'text',
                            hintText: 'SKU ID'
                        },
                        {
                            id: 2,
                            type: 'text',
                            hintText: 'Product Name'
                        },
                        {
                            id: 3,
                            type: 'dropdowntext',
                            hintText: 'Category'
                        },
                        {
                            id: 4,
                            type: 'text',
                            hintText: 'Price'
                        },
                    ]"
                    :modelValues="[
                        { id: 1, value: '250001' },
                        { id: 2, value: 'Cat in Box' },
                        { id: 3, value: 'Animal' },
                        { id: 4, value: '150' },
                    ]"
                />
            </template>
        </Overlay> -->
        <!-- <BasicTextInput 
            hint="SKU ID*"
        /> -->
        <!-- <SimpleTextInput 
            :hasHint="true"
            state="default"
            hintText="SKU ID"
            dangerText="I am in danger!"
        />
        <SimpleTextInput 
            :hasHint="true"
            state="valid"
            hintText="SKU ID"
            dangerText="I am in danger!"
        />
        <SimpleDropdownInput 
            :hasHint="true"
            state="missing"
            hintText="SKU ID"
            dangerText="I am in danger!"
        />
        <SimpleDropdownInput 
            :hasHint="true"
            state="invalid"
            hintText="SKU ID"
            dangerText="I am in danger!"
        /> -->
        <SearchInput />
    </div>  
</template>

<script setup>
import Nav from '@/components/Nav/Nav.vue';
import NavButton from '@/components/Buttons/NavButton.vue';
import PrimaryButton from '@/components/Buttons/PrimaryButton.vue';
import Overlay from '@/components/Modals/Overlay.vue';
import BasicTextInput from '@/components/Inputs/BasicTextInput.vue';
import DeleteModal from '@/components/Modals/DeleteModal.vue';
import MessageModal from '@/components/Modals/MessageModal.vue';
import { PackageCheck } from 'lucide-vue-next';
import SimpleTextInput from '@/components/Inputs/SimpleTextInput.vue';
import SimpleDropdownInput from '@/components/Inputs/SimpleDropdownInput.vue';
import SimpleAddEditModal from '@/components/Modals/SimpleAddEditModal.vue';
import SearchInput from '@/components/Inputs/SearchInput.vue';
</script>

<style scoped>
#test {
    background-color: var(--color-primary);
    width: 100%;
    margin-top: 50px;
    margin-left: 50px;
    
    display: flex;
    position: relative;
}
</style>