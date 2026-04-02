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
                    <p class="return-text">{{ modalReturnText }}</p>
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
                    v-for="(value, key, index) in inputFields"
                    >
                    <SimpleTextInput 
                        v-if="value.type === 'text'"
                        :has-hint="true"
                        :hint-text="value.hint"
                        :data="inputData[key]"
                        :data-key="key"
                        :linked-field="value?.linkedField"
                        @on-input="handleOnInputFromSimpleInputs"
                        />
                    <SimpleDropdownInput 
                        v-else-if="value.type === 'dropdowntext'"
                        :has-hint="true"
                        :hint-text="value.hint"
                        :data="inputData[key]"
                        :data-key="key"
                        :linked-field="value?.linkedField"
                        @on-input="handleOnInputFromSimpleInputs"
                    />
                </div>
            </form>
            <section id="bottom">
                <div 
                    id="missing-container"
                    v-if="hasMissingInput"
                    >
                    {{ modalMissingInputText }}
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
                        id="submit-button"
                        :text="modalSubmitText"
                        :has-icon="true"
                        @on-hover="changeButtonSubmitIconColor"
                        @on-leave="changeButtonSubmitIconColor"
                        @on-click="handleOnSubmit"
                    >
                        <template #sIcon>
                            <Plus 
                                v-if="modalType === 'add'"
                                size="16"
                                :color="btnSubmitIconColor"
                                />
                            <SquarePen 
                                v-else
                                size="16"
                                :color="btnSubmitIconColor"
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
import addInventoryItem from '@/modules/inventory/addInventoryItem';
import updateInventoryItem from '@/modules/inventory/updateInventoryItem';

// Components
import SimpleTextInput from '../Inputs/SimpleTextInput.vue';
import SimpleDropdownInput from '../Inputs/SimpleDropdownInput.vue';
import NudeButton from '../Buttons/NudeButton.vue';
import PrimaryButton from '../Buttons/PrimaryButton.vue';

// Modules

// Use Modules
import Search from '@/modules/utils/useSearch';

// Variables for inits
/**
 * inputFields object has the following:
 * { id: Number, type: String, hintText: String }
 * The type key accepts: 'text', 'dropdowntext'
 * 
 * inputValues must depend on inputFields
 * 
 * modalType accepts: 'add', 'edit'
 * 
 * itemType accepts: 'product = 0', 'inventory = 1'
 */
const props = defineProps({
    modalType: {
        type: String,
        default: 'add'
    },
    inputFields: {
        type: Object,
        required: true,
    },
    inputValues: {
        type: Object,
        required: true
    },
    itemID: {
        type: [ Number, String ],
    },
    itemType: {
        type: Number,
    },
    modalTitle: {
        type: String,
        default: 'Modal Title'
    },
    modalSubmitText: {
        type: String,
        default: 'Submit'
    },
    modalMissingInputText: {
        type: String,
        default: 'This is a missing text!'
    },
    modalReturnText: {
        type: String,
        default: 'Return'
    },
});

const emits = defineEmits([
    'onCancel',
    'onSubmit'
]);

const itemTypeTranslator = [
    'product',
    'inventory'
]

const itemTypeTranslated = ref(itemTypeTranslator[props.itemType]);
const { searchById } = Search(itemTypeTranslated.value);
const hasMissingInput = ref(false);
const inputData = ref({});

// Variables for child
const btnSubmitIconColor = ref('var(--color-primary)');

// Initialise inputData
Object.keys(props.inputValues).forEach((key, index) => {
    let item = props.inputValues[key];

    Object.assign(inputData.value, {
        [key]: {
            // itemID: props.itemID,
            value: item,
            state: item === '' ? 'default' : 'valid'
        }
    });
});

// Variables for appearance
const resetButtonColor = ref('var(--color-accent)');

// Function for child
function changeButtonSubmitIconColor(isHovered) {
    btnSubmitIconColor.value = isHovered ? 
        'var(--color-secondary)' :
        'var(--color-primary)';
};

function handleOnEnterFromResetButton() {
    resetButtonColor.value = 'var(--color-secondary)';
};

function handleOnLeaveFromResetButton() {
    resetButtonColor.value = 'var(--color-accent)';
};

// Function handlers
function handleOnInputFromSimpleInputs(childObj) {
    const key = childObj?.dataKey;
    const newValue = childObj?.newValue;

    inputData.value[key].value = newValue;
    inputData.value[key].state = newValue === '' ? 'default' : 'valid';

    if (childObj.linkedField !== undefined) {
        const searchedItem = searchById(newValue);

        inputData.value[childObj.linkedField].value = searchedItem;
        inputData.value[childObj.linkedField].state = searchedItem === undefined ? 'default' : 'valid';
    };
};

function handleOnCancel() {
    emits('onCancel', false); // false means turn of modal
};

async function handleOnSubmit() {
    const submitTemplates = {
        product: { // Products = 0
            sku: 0,
            name: 'Product Name',
            category: 'Category',
            price: 0,
        },
        inventory: { // Inventory = 1
            product_sku: 0,
            details: '',
            quantity: 0
        },
        order: { // Orders = 2

        }
    };

    const addEditTypes = {
        product: { // Product = 0
            add: addProduct,
            edit: updateProduct
        },
        inventory: { // Inventory = 1
            add: addInventoryItem,
            edit: updateInventoryItem
        },
        order: { // Orders = 2

        }
    };

    const submitTemplate = submitTemplates[itemTypeTranslated];
    
    Object.keys(submitTemplate).forEach((key) => {
        submitTemplate[key] = inputData.value[key].value;
    });
    
    if (props.modalType === 'edit') {
        const id = props.itemID // The plus one here is for the server
        
        Object.assign(submitTemplate, { id });
    };

    // console.log('==============')
    // console.log('submitTemplate:');
    // console.log(submitTemplate);
    
    const modules = addEditTypes[itemTypeTranslated];
    const action = props.modalType === 'add' ? modules.add : modules.edit
    const { error, onSubmit } = action(submitTemplate);

    await onSubmit();

    if (error.value === null) {
        emits('onSubmit', submitTemplate);
        inputData.value = {};
        // use for debug
        // console.log('==============')
        // console.log('submitTemplate: ');
        // console.log(submitTemplate);
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