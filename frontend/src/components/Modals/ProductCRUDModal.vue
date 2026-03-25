<template>
    <div id="product-crud" @click.stop="">
        <div class="container">
            <section id="return">
                <NudeButton 
                    text="Cancel" 
                    :txt-color="btnCancelColor" 
                    :fn-size="14"
                    @on-click="handleOnCancel()"
                >
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
                <SimpleProgressBar 
                    :count="4"
                    :progress-bars="progressValues"
                    default-color="var(--color-secondary)"
                    done-color="var(--color-valid)"
                    @pass-init-values="catchInitProgressValues"
                />
            </section>
            <form action="" method="post" @submit.prevent="">
                <BasicTextInput
                    class="form-input"
                    hint="SKU ID*"
                    :input-i-d="1"
                    @pass-value="getInputFromChild"
                    />
                    <BasicTextInput 
                    class="form-input"
                    hint="Product Name*"
                    :input-i-d="2"
                    @pass-value="getInputFromChild"
                    />
                    <BasicTextInput 
                    class="form-input"
                    hint="Category*"
                    :input-i-d="3"
                    @pass-value="getInputFromChild"
                    />
                    <BasicTextInput 
                    class="form-input"
                    hint="Price*"
                    :input-i-d="4"
                    @pass-value="getInputFromChild"
                />
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
                        @on-click="handleOnSumbit"
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
import BasicTextInput from '../Inputs/BasicTextInput.vue';
import SimpleProgressBar from '../ProgressBars/SimpleProgressBar.vue';

import addProduct from '@/modules/product/addProduct';
import getAllProducts from '@/modules/product/getAllProducts';

const emits = defineEmits([
    'onCancel',
    'onSubmit'
]);

// Cancels the modal
function handleOnCancel() {
    emits('onCancel');
};

function handleOnSumbit() {
    const { error, onSubmit } = addProduct({
        sku: inputSKUID.value,
        name: inputProductName.value,
        category: inputCategory.value,
        price: inputPrice.value
    });

    onSubmit();

    if (error !== null) {
        emits('onSubmit');
    };

    const { product, err, load } = getAllProducts();
    load();

    console.log(product)
};

const btnCancelColor = ref('#505050b0')
const btnAddIconColor = ref("#FFFAFA");
const inputSKUID = ref('');
const inputProductName = ref('');
const inputCategory = ref('');
const inputPrice = ref('');
const progressValues = ref([]);

function catchInitProgressValues(obj) {
    progressValues.value = obj;
};

function changeButtonAddIconColor() {
    btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
};

function getInputFromChild(obj) {
    if (obj.inputID === 1) { 
        inputSKUID.value = obj.value;
        progressValues.value[0].status = obj.value !== '' ? true : false;
        
    } else if (obj.inputID === 2) {
        inputProductName.value = obj.value;
        progressValues.value[1].status = obj.value !== '' ? true : false;
    } else if (obj.inputID === 3) {
        inputCategory.value = obj.value;
        progressValues.value[2].status = obj.value !== '' ? true : false;
    } else { 
        inputPrice.value = obj.value;
        progressValues.value[3].status = obj.value !== '' ? true : false;
    };
};
</script>

<style scoped>
.container {
    background-color: var(--color-primary);
    border-radius: 5px;
    box-shadow: -4px 4px 0 0 var(--color-secondary);
    width: 435px;
    min-height: 300px;
    padding: 30px 20px;
}

#title {
    color: var(--color-secondary);
    font-weight: bold;
}

header {
    margin-bottom: 5px;
}

#return {
    margin-bottom: 15px;
}

#progress {
    margin-bottom: 15px;
}

.form-input {
    margin-bottom: 20px;
}

#actions {
    display: flex;
    gap: 30px;
    align-items: center;
    justify-content: right;
}
</style>