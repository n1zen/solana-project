<template>
    <div id="delete-modal"  @click.stop="">
        <div class="simple-modal__container">
            <section id="return">
                <button
                    type="button"
                    @click="handleOnCancel"
                    >
                    <ArrowLeft 
                        size="10"
                    />
                    <p class="return-text">Cancel</p>
                </button>
            </section>
            <header>
                <p id="title">{{ modalTitle }}</p>
                <p class="description" id="desc">This action is irreversible.</p>
                <p class="description" id="desc-2">Are you sure to proceed?</p>
            </header>
            <section id="info">
                <table>
                    <tr v-for="item in tableValues">
                       <td class="type">{{ item.legend }} :</td> 
                       <td class="data">{{ item.value }}</td> 
                    </tr>
                </table>
            </section>
            <div id="actions">
                <PrimaryButton
                    text="Delete Item"
                    :has-icon=true
                    @on-hover="changeButtonAddIconColor"
                    @on-leave="changeButtonAddIconColor"
                    @on-click="handleOnConfirm"
                >
                    <template #sIcon>
                         <Trash 
                            size="16"
                            :color="btnAddIconColor"
                        />
                    </template>
                </PrimaryButton>
            </div>
        </div>
    </div>
</template>

<script setup>
// Import outside
import {  ArrowLeft, Trash } from 'lucide-vue-next';

// Vue
import { ref } from 'vue';

// Components
import PrimaryButton from '../Buttons/PrimaryButton.vue';

// Modules
import deleteProduct from '@/modules/product/deleteProduct';
import deleteInventoryItem from '@/modules/inventory/deleteInventoryItem';

// Variables for initialisations
/**
 * tableValues should look something like this:
 * {
 *    key: { legend: 'Legend Text', value: Any }
 * }
 */
const props = defineProps({
    modalTitle: {
        type: String,
        default: 'text title'
    },
    tableValues: {
        type: Object
    },
    itemID: {
        type: Number,
    },
    itemRowIndex: {
        type: Number
    },
    itemType: {
        type: String
    },
});

const emits = defineEmits([
    'onCancel',
    'onConfirm'
])

// Variables for child
// Primary button
const btnAddIconColor = ref('#FFFAFA');

function changeButtonAddIconColor() {
    btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
};

function handleOnCancel() {
    emits('onCancel');
};

async function handleOnConfirm() {
    const deleteModules = {
        product: deleteProduct,
        inventory: deleteInventoryItem
    };

    const deleteModule = deleteModules[props.itemType];
    const { error, onDelete } = deleteModule(props.itemID);

    await onDelete();

    if (error.value === null) {
        let deletedValues = {};

        Object.keys(props.tableValues).forEach(key => {
            let value = props.tableValues[key].value;

            Object.assign(deletedValues, { [key]: value });
        });

        emits('onConfirm', deletedValues, props.itemRowIndex);
    } else {
        // add a catcher if possible
    };

};
</script>

<style scoped>
@import './baseModal.css';

p {
    font-weight: bold;
}

#title {
    color: var(--color-secondary);
}

.description {
    color: var(--color-accent);
}

#info {
    padding: 0 7px;
    margin: 20px 0 30px;
}

table {
    border-collapse: separate;
    border-spacing: 0 5px;
    width: 100%;
}

td {
    color: var(--color-accent);
    font-weight: bold;
}

td.type {
    width: 40%;
}

td.data {
    width: 100%;
}

#actions {
    display: flex;
    align-items: center;
    justify-content: right;
}
</style>