<template>
    <div id="product-crud">
        <div class="container">
            <section id="return">
                <NudeButton 
                    text="Cancel" 
                    :txt-color="btnCancelColor" 
                    :fn-size="14">
                    <template #sIcon>
                        <ArrowLeft 
                            size="12" 
                            :color="btnCancelColor" />
                    </template>
                </NudeButton>
            </section>
            <header>
                <p id="title">Add new item</p>
            </header>
            <section id="progress">

            </section>
            <form action="" method="post">
                <div id="actions">
                    <NudeButton 
                        text="Reset"
                        txt-color="var(--color-secondary)"
                    />
                    <PrimaryButton
                        text="Add Item"
                        :has-icon=true
                        @on-hover="changeButtonAddIconColor"
                        @on-leave="changeButtonAddIconColor"
                    >
                        <template #sIcon>
                             <Plus 
                                size="16"
                                :color="btnAddIconColor"
                             />
                        </template>
                    </PrimaryButton>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { ArrowLeft, Plus } from 'lucide-vue-next';

import PrimaryButton from '../Buttons/PrimaryButton.vue';
import NudeButton from '../Buttons/NudeButton.vue';

const btnCancelColor = ref('#505050b0')
const btnAddIconColor = ref("#FFFAFA");

function changeButtonAddIconColor() {
    btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
};
</script>

<style scoped>
.container {
    background-color: var(--color-primary);
    border-radius: 5px;
    box-shadow: 0 4px 0 -1px var(--color-secondary);
    width: 435px;
    min-height: 300px;
    padding: 30px 20px;
}

#title {
    color: var(--color-secondary);
    font-weight: bold;
}

#return {
    margin-bottom: 15px;
}

#actions {
    display: flex;
    gap: 30px;
    align-items: center;
    justify-content: right;
}
</style>