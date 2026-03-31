<template>
    <div id="simple-modal" @click.stop="">
        <div class="simple-modal__container">
            <section id="return">
                <button
                    type="button"
                    @click="handleOnCancel"
                    >
                    <ArrowLeft 
                        size="10"
                    />
                    <p class="return-text">{{ returnText }}</p>
                </button>
            </section>
            <header>
                <p id="modal-title">{{ modalTitle }}</p>
            </header>
            <section id="progress">
                Progress
            </section>
            <form class="simple-modal__form" action="" method="post" @submit.prevent="">
                <div 
                    class="input-type"
                    v-for="(field, index) in fields"
                    >
                    <SimpleTextInput 
                        v-if="field.type === 'text'"
                        :has-hint="true"
                        :hint-text="field.hintText"
                        :data="inputData[index]"
                        @on-input="handleOnInputFromSimpleInputs"
                        />
                    <SimpleDropdownInput 
                        v-else-if="field.type === 'dropdowntext'"
                        :has-hint="true"
                        :hint-text="field.hintText"
                        :data="inputData[index]"
                        @on-input="handleOnInputFromSimpleInputs"
                    />
                </div>
            </form>
            <section id="bottom">
                <div 
                    id="missing-container"
                    v-if="hasMissingInput"
                    >
                    {{ missingText }}
                </div>
                <div id="actions">
                    <NudeButton 
                        text="Reset"
                        :txt-color="resetButtonColor"
                        @on-click=""
                        @on-mouse-enter="handleOnEnterFromResetButton"
                        @on-mouse-leave="handleOnLeaveFromResetButton"
                    />
                    <PrimaryButton
                        :text="modalSubmitText"
                        :has-icon="true"
                        @on-click="handleOnSubmit"
                    >
                        <template #sIcon>
                            <Plus 
                                v-if="modalType === 'add'"
                                size="16"
                                color=""
                            />
                            <SquarePen 
                                v-else
                                size="16"
                                color=""
                            />
                        </template>
                    </PrimaryButton>
                </div>
            </section>
        </div>
    </div>
</template>

<script setup>
// Import outside
import { ArrowLeft, Plus, SquarePen } from 'lucide-vue-next';

// Vue
import { ref } from 'vue';

// Modules
import addProduct from '@/modules/product/addProduct';
import updateProduct from '@/modules/product/updateProduct';
import addInventoryItem from '@/modules/inventory/addInventory';

// Components
import SimpleTextInput from '../Inputs/SimpleTextInput.vue';
import SimpleDropdownInput from '../Inputs/SimpleDropdownInput.vue';
import NudeButton from '../Buttons/NudeButton.vue';
import PrimaryButton from '../Buttons/PrimaryButton.vue';

// Modules


// Variables for inits
/**
 * fields object has the following:
 * { id: Number, type: String, hintText: String }
 * The type key accepts: 'text', 'dropdowntext'
 * 
 * modelValues must depend on fields and contains:
 * { id: Number, value: String }
 * 
 * modalType accepts: 'add', 'edit'
 * 
 * itemType accepts: 'product = 0', 'inventory = 1'
 */
const props = defineProps({
    fields: {
        type: Array,
        required: true,
    },
    modelValues: {
        type: Array,
        required: true
    },
    rowIDForEdit: {
        type: Number,
    },
    modalTitle: {
        type: String,
        default: 'Modal Title'
    },
    itemType: {
        type: Number,
        required: true
    },
    modalType: {
        type: String,
        default: 'add'
    },
    modalSubmitText: {
        type: String,
        default: 'Submit'
    },
    missingText: {
        type: String,
        default: 'This is a missing text!'
    },
    returnText: {
        type: String,
        default: 'Return'
    },
});

const emits = defineEmits([
    'onCancel',
    'onSubmit'
]);

const inputData = ref([]);
const hasMissingInput = ref(false);

// Initialise inputData
props.modelValues?.forEach(item => {
    //use for debug
    // console.log('==============')
    // console.log('item: ');
    console.log(item);
    let newInputData = {
        id: item.id,
        value: item.value,
        state: item.value === '' ? 'default' : 'valid'
    };

    inputData.value.push(newInputData);
    //use for debug
    // console.log('==============')
    // console.log('inputData: ');
    // console.log(inputData.value); 
});


// Variables for appearance
const resetButtonColor = ref('var(--color-accent)');

// Function for child
function handleOnEnterFromResetButton() {
    resetButtonColor.value = 'var(--color-secondary)';
};

function handleOnLeaveFromResetButton() {
    resetButtonColor.value = 'var(--color-accent)';
};

// Function handlers
function handleOnInputFromSimpleInputs(childObj) {
    const index = childObj?.refID - 1;
    const newValue = childObj?.newValue;

    inputData.value[index].value = newValue;
    inputData.value[index].state = newValue === '' ? 'default' : 'valid';
};

function handleOnCancel() {
    emits('onCancel', false); // false means turn of modal
};

async function handleOnSubmit() {
    const itemTemplates = [
        { // Products
            sku: 0,
            name: 'Product Name',
            category: 'Category',
            price: 0,
        },
        { // Inventory
            product_id: 0,
            details: '',
            quantity: 0
        },
        { // Orders

        }
    ];

    const addEditTypes = [
        { // Product
            add: addProduct,
            edit: updateProduct
        },
        { // Inventory
            add: addInventoryItem,
            edit: ''
        },
        { // Orders

        }
    ];

    const itemTemplate = itemTemplates[props.itemType];
    
    Object.keys(itemTemplate).forEach((key, index) => {
        itemTemplate[key] = inputData.value[index].value;
    });
    
    if (props.rowIDForEdit) {
        const id = props.rowIDForEdit + 1 // The plus one here is for the server
    
        Object.assign(itemTemplate, { id });
    };

    const modules = addEditTypes[props.itemType];
    const action = props.modalType === 'add' ? modules.add : modules.edit
    const { error, onSubmit } = action(itemTemplate);

    await onSubmit();

    if (error.value === null) {
        emits('onSubmit', itemTemplate);
        // use for debug
        // console.log('==============')
        // console.log('itemTemplate: ');
        // console.log(itemTemplate);
    } else {
        handleExistingInput(error.value);
    };
};

function handleMissingInput() {

};

function handleExistingInput(error) {
    console.log(error);
};
</script>

<style scoped>
@import './baseModal.css';

.input-type {
    margin-bottom: 15px;
}
</style>