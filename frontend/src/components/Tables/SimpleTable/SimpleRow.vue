<template>
    <tr 
        class="simple-row"
        :class="[ isCurrentlyClicked ? 'clicked' : '' ]"
        @click="handleOnClick">
        <td 
            class="column-data"
            v-for="(datum, index) in data"
            :key="index"
            >
            <span v-if="index !== data.length - 1">{{ datum }}</span>
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

// Variables for inits
/**
 * See SimpleTable.vue to understand what is data
 * but basically, it is datum of the row
 */
const props= defineProps({
    index: {
        type: Number,
    },
    data: {
        type: Array,
        default: []
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

// Function Handlers
function handleOnClick() {
    console.log(props.data);
    emits('onClick', props.index);
};

function handleOnEdit() {
    emits('onEdit', props.index);
};

function handleOnDelete() {
    const length = props.data.length - 1;
    const itemID = props.data[length];

    emits('onDelete', itemID, props.index);
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