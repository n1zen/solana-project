<template>
    <tr 
        class="simple-row"
        :class="[ isCurrentlyClicked ? 'clicked' : '' ]"
        @click="handleOnClick">
        <td 
            class="column-data"
            v-for="(value, key, index) in rowTemplate"
            :key="index"
            >
            <span 
                v-if="index !== Object.keys(rowTemplate).length - 1"
                >
                {{ value }}
            </span>
            <div
                class="actions" 
                v-else
                >
                <button 
                    class="edit"
                    @click="handleOnEdit"
                    >
                    <SquarePen 
                        size="20"
                        :class="''"
                    />
                </button>
                <button 
                    class="delete"
                    @click="handleOnDelete"
                    >
                    <SquareX 
                        size="20"
                    />
                </button>
            </div>
        </td>
    </tr>
</template>

<script setup>
// Imports outside
import { SquarePen, SquareX } from 'lucide-vue-next';
import { reactive, ref } from 'vue';

// Vue

// Variables for inits
/**
 * See SimpleTable.vue for more information
 */
const props= defineProps({
    tableIsUsedAs: {
        type: String
    },
    rowData: {
        type: Object,
        default: {}
    },
    isCurrentlyClicked: {
        type: Boolean,
        default: false
    }  
});

const emits = defineEmits([
    'onClick',
    'onEdit',
    'onDelete'
])

const rowTemplate = ref(null);

const productDataRowTemplate = reactive({
    sku: '',
    name: '',
    category: '',
    price: '',
    id: ''
});

const inventoryDataRowTemplate = reactive({
    productid: '',
    productname: '',
    quantity: '',
    id: ''
});

if (props.tableIsUsedAs === 'products') {
    const datum = props.rowData;
    
    Object.keys(productDataRowTemplate).forEach(key => {
        productDataRowTemplate[key] = datum[key];
    });

    rowTemplate.value = productDataRowTemplate;
} else if (props.itemType === 'inventory') {
    const datum = props.rowData;
    const productData = datum?.product;
    
    inventoryDataRowTemplate.productid = productData?.sku;
    inventoryDataRowTemplate.productname = productData?.name;
    inventoryDataRowTemplate.quantity = datum.quantity;
    inventoryDataRowTemplate.id = datum.id;

    rowTemplate.value = inventoryDataRowTemplate;
};

// Function Handlers
function handleOnClick() {
    emits('onClick', props.rowData.rowIndex);
};

function handleOnEdit() {
    emits('onEdit', props.rowData.rowIndex);
};

function handleOnDelete() {
    emits('onDelete', props.rowData.rowIndex);
};
</script>

<style scoped>
td {
    border-bottom: 1px solid var(--color-accent);
    color: var(--color-accent);
    cursor: pointer;
    font-weight: bold;
    padding: 20px 10px;
    transition: 0.3s;
}

tr {
    background-color: transparent;
    transition: 0.3s;

    &:hover {
        background-color: #ffb7b482;
    }

    &.clicked,
    &.clicked:hover {
        background-color: var(--color-secondary);
    }
}

.column-data span {
    transition: 0.3s;
}

tr.clicked .column-data span {
    color: var(--color-primary);
}

td button svg {
    transition: 0.3s;
}

td button.edit svg {
    color: var(--color-accent);
}

td button.delete svg {
    color: var(--color-secondary);
}

td button svg:hover {
    color: var(--color-primary);
}

tr.clicked button svg {
    color: var(--color-primary);
}

tr.clicked button svg:hover {
    color: var(--color-accent);
}

.actions button {
    background-color: transparent;
    border-radius: 3px;
    border: none;
    cursor: pointer;
    padding: 0;

    &>* {
        transition: 0.3s;
    }
}

.actions .delete {
    margin-left: 12px;
}
</style>