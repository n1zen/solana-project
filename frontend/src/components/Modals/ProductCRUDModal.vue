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
                    default-color="var(--color-secondary)"
                    done-color="var(--color-valid)"
                    :inputs-value="[
                        inputSKUID,
                        inputProductName,
                        inputCategory,
                        inputPrice
                    ]"
                />
            </section>
            <form action="" method="post" @submit.prevent="">
                <BasicTextInput
                    class="form-input"
                    hint="SKU ID*"
                    danger-txt="This SKU ID already exists!"
                    :input-state="stateInputSKUID"
                    :input-i-d="1"
                    :input-v="inputSKUID"
                    @pass-value="getInputFromChild"
                    />
                    <BasicTextInput 
                    class="form-input"
                    hint="Product Name*"
                    danger-txt="This product name already exists!"
                    :input-state="stateInputProductName"
                    :input-i-d="2"
                    :input-v="inputProductName"
                    @pass-value="getInputFromChild"
                    />
                    <BasicTextInput 
                    class="form-input"
                    hint="Category*"
                    :input-state="stateInputCategory"
                    :input-i-d="3"
                    :input-v="inputCategory"
                    @pass-value="getInputFromChild"
                    />
                    <BasicTextInput 
                    class="form-input"
                    hint="Price*"
                    :input-state="stateInputPrice"
                    :input-i-d="4"
                    :input-v="inputPrice"
                    @pass-value="getInputFromChild"
                />
                <div id="bottom">
                    <p 
                        v-if="hasMissingInput"
                        id="danger-message">
                        Please complete the form!
                    </p>
                    <div id="actions">
                        <NudeButton 
                            text="Reset"
                            txt-color="var(--color-secondary)"
                            @on-click="handleOnReset"
                        />
                        <PrimaryButton
                            :text="isEdit ? 'Edit Item' : 'Add Item'"
                            :has-icon=true
                            @on-hover="changeButtonAddIconColor"
                            @on-leave="changeButtonAddIconColor"
                            @on-click="handleOnSubmit"
                        >
                            <template #sIcon>
                                <Plus 
                                    v-if="!isEdit"
                                    size="16"
                                    :color="btnAddIconColor"
                                />
                                <SquarePen 
                                    v-else
                                    size="16"
                                    :color="btnAddIconColor"
                                 />
                            </template>
                        </PrimaryButton>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { ArrowLeft, Plus, SquarePen } from 'lucide-vue-next';

import PrimaryButton from '../Buttons/PrimaryButton.vue';
import NudeButton from '../Buttons/NudeButton.vue';
import BasicTextInput from '../Inputs/BasicTextInput.vue';
import SimpleProgressBar from '../ProgressBars/SimpleProgressBar.vue';

import addProduct from '@/modules/product/addProduct';
import updateProduct from '@/modules/product/updateProduct';

const emits = defineEmits([
    'onCancel',
    'onSubmit'
]);

const props = defineProps({
    productItem: {
        type: Object,
        default: {}
    },
    isEdit: {
        type: Boolean,
        default: false
    }
});

const btnCancelColor = ref('#505050b0')
const btnAddIconColor = ref("#FFFAFA");

const inputSKUID = ref(props.productItem.sku);
const inputProductName = ref(props.productItem.name);
const inputCategory = ref(props.productItem.category);
const inputPrice = ref(props.productItem.price);

// For resetting edit
const originalInputSKUID = ref(inputSKUID.value); 
const originalProductName = ref(inputProductName.value); 
const originalCategory = ref(inputCategory.value); 
const originalPrice = ref(inputPrice.value); 

const stateInputSKUID = ref(
    props.productItem.sku === '' ||
    props.productItem.sku === undefined ?
    'default' : 'valid'
);
const stateInputProductName = ref(
    props.productItem.name === '' ||
    props.productItem.name === undefined ?
    'default' : 'valid'
);
const stateInputCategory = ref(
    props.productItem.category === '' ||
    props.productItem.category === undefined ?
    'default' : 'valid'
);
const stateInputPrice = ref(
    props.productItem.price === '' ||
    props.productItem.price === undefined ?
    'default' : 'valid'
);

const hasMissingInput = ref(false);

function changeButtonAddIconColor() {
    btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
};

function getInputFromChild({ inputID, value }) {
    hasMissingInput.value = false;

    const inputsMap = {
        1: inputSKUID,
        2: inputProductName,
        3: inputCategory,
        4: inputPrice
    };

    const statesMap = {
        1: stateInputSKUID,
        2: stateInputProductName,
        3: stateInputCategory,
        4: stateInputPrice
    };

    const targetInput = inputsMap[inputID];
    const targetState = statesMap[inputID];

    if (!targetInput || !targetState) return;

    targetInput.value = value;
    targetState.value = value !== '' ? 'valid' : 'default';
};

function handleOnCancel() {
    emits('onCancel');
};

function handleOnReset() {
    const inputMap = [
        inputSKUID,
        inputProductName,
        inputCategory,
        inputPrice
    ];

    const stateMap = [
        stateInputSKUID,
        stateInputProductName,
        stateInputCategory,
        stateInputPrice
    ];
    
    if (props.isEdit) {
        const originalInputMap = [
            originalInputSKUID,
            originalProductName,
            originalCategory,
            originalPrice
        ];

        inputMap.forEach((el, index) => {
            el.value = originalInputMap[index].value;
        });
    } else {
        inputMap.forEach(el => {
            el.value = '';
        });

        stateMap.forEach(el => {
           el.value = 'default'; 
        });
    };
};

async function handleOnSubmit() {
    if (handleMissingInput()) {
        hasMissingInput.value = true;
        return;
    }

    const isEditMode = props.isEdit;

    const item = {
        sku: inputSKUID.value,
        name: inputProductName.value,
        category: inputCategory.value,
        price: inputPrice.value,
        ...(isEditMode && { id: props.productItem.id })
    };

    if (isEditMode) {
        const noChanges =
            item.sku === props.productItem.sku &&
            item.name === props.productItem.name &&
            item.category === props.productItem.category &&
            item.price === props.productItem.price;

        if (noChanges) {
            emits('onSubmit', {
                responseType: 'noUpdate',
                item
            });
            return;
        };
    };

    const action = isEditMode ? updateProduct : addProduct;
    const { error, onSubmit } = action(item);

    await onSubmit();

    if (error.value === null) {
        emits('onSubmit', {
            responseType: isEditMode ? 'updated' : 'add',
            item
        });
    } else {
        handleExistingInput(error);
    };
};

function handleMissingInput() {
    let hasMissingInput = false;

    const inputs = [
        inputSKUID.value,
        inputProductName.value,
        inputCategory.value,
        inputPrice.value
    ];

    const inputStates = [
        stateInputSKUID,
        stateInputProductName,
        stateInputCategory,
        stateInputPrice
    ];

    for (let iter = 0; iter < inputs.length; iter++) {
        if (inputs[iter] === '' || inputs[iter] === undefined ) {
            inputStates[iter].value = 'missing';
            hasMissingInput = true;
        };
    };

    return hasMissingInput;
};

function handleExistingInput(error) {
    if (error.value === 'Product SKU already exists.') {
        stateInputSKUID.value = 'invalid';
        inputSKUID.value = '';
    };
    
    if (error.value === 'Product NAME already exists.') {
        stateInputProductName.value = 'invalid';
        inputProductName.value = '';
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

    transition: 0.3s;
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

#bottom {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

#danger-message {
    padding-left: 10px;
    color: var(--color-secondary);
    font-size: 14px;
    font-weight: bold;
}

#actions {
    flex-grow: 1;

    display: flex;
    gap: 30px;
    align-items: center;
    justify-content: right;
}
</style>