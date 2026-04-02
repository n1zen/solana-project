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

// Vue

// Variables for inits
/**
 * See SimpleTable.vue for more information
 */
import { computed } from 'vue';

const props = defineProps({
    tableIsUsedAs: {
        type: String
    },
    rowData: {
        type: Object,
        default: () => ({})
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
]);

const rowTemplate = computed(() => {
    if (props.tableIsUsedAs === 'products') {
        return {
            sku: props.rowData.sku,
            name: props.rowData.name,
            category: props.rowData.category,
            price: props.rowData.price,
            id: props.rowData.id
        };
    }

    if (props.tableIsUsedAs === 'inventory') {
        return {
            product_sku: props.rowData.product_sku,
            product_name: props.rowData.product_name,
            quantity: props.rowData.quantity,
            id: props.rowData.id
        };
    }

    return {};
});

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
    padding: 13px 10px;
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