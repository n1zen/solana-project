<template>
    <div class="simple-table">
        <table :id="tableIsUsedAs">
            <thead>
                <tr id="legend">
                    <th 
                        v-for="(legend, index) in legends"
                    >
                        <input 
                            type="checkbox" 
                            name="" id=""
                            v-if="index === 0"
                            >
                        <span class="legend-text">
                            {{ legend }}
                        </span>
                    </th>
                </tr>
            </thead>
            <tbody>
                <div 
                    class="table-state"
                    id="loading-set"
                    v-if="tableState === 'loading'"
                    >
                    <div class="state-icon">
                        <DatabaseZap 
                            size="80"
                            color="var(--color-secondary)"
                        />
                    </div>
                    <p class="state-text">
                        {{ tableStateTexts.loading }}
                    </p>
                </div>
                <div 
                    class="table-state"
                    id="empty-set"
                    v-else-if="tableState === 'empty'"
                    >
                    <div class="state-icon">
                        <PackageOpen 
                            size="80"
                            color="var(--color-secondary)"
                        />
                    </div>
                    <p class="state-text">
                        {{ tableStateTexts.empty }}
                    </p>
                    <PrimaryButton 
                        text="Add some!"
                        :has-icon="false"
                        @on-click=""
                        >
                    </PrimaryButton>
                </div>
                <SimpleRow 
                    v-for="(row, index) in rows"
                    :key="index"
                    :row-data="row"
                    :table-is-used-as="tableIsUsedAs"
                    :is-currently-clicked="clickedRowIndex === index"
                    @on-click="handleRowOnClick"
                    @on-edit=""
                    @on-delete=""
                />
            </tbody>
        </table>
    </div>
</template>

<script setup>
// Import outside
import { DatabaseZap, PackageOpen } from 'lucide-vue-next';
import SimpleRow from './SimpleRow.vue';

// Vue
import { ref, watch } from 'vue';

// Components
import PrimaryButton from '@/components/Buttons/PrimaryButton.vue';


// Personal Variables
/**
 * tableIsUsedAs is a variable to show that the table
 * is either used as a product, inventory, order, etc. 
 * 
 * tableState is a text to show the current state of the table
 * It accepts 'default', 'loading', 'empty', 'offline'
 * 
 * legends are texts used to display on top of the table
 * to visually show what the rows are about.
 * legends template:
 * legends: [
 *     legendText (String),
 *     legendText (String),
 *     ...
 * ]
 * 
 * rows are the object data to be displayed including data
 * for searching and appearance purposes
 */
const props = defineProps({
    tableIsUsedAs: {
        type: String,
    },
    tableState: {
        type: String,
        required: true
    },
    tableStateTexts: {
        type: Object
    },
    legends: {
        type: Array,
        // required: true
    },
    rows: {
        type: Array
    },
});

const emits = defineEmits([
    'rowOnClick'
]);

// Variables for Rows
const clickedRowIndex = ref(null);

// Function for child
function handleRowOnClick(rowIndex) {
    clickedRowIndex.value = rowIndex;
    
    emits('rowOnClick', rowIndex);
};
</script>

<style scoped>
.simple-table {
    width: 100%;
}

table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 100%;
}

th {
    border-bottom: 1px solid var(--color-accent);
    color: var(--color-accent);
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    padding: 20px 10px;
    text-align: left;
    transition: 0.3s
}

th:nth-child(1) {
    gap: 10px;
}

input[type=checkbox] {
    margin-right: 10px;
}

#legend {
    background-color: transparent;
    transition: 0.3s;

    &:hover {
        background-color: #ffb7b482;
    }
}

.table-state {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: center;
    justify-content: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.state-icon {
    border: 2px solid var(--color-secondary);
    border-radius: 50%;
    padding: 30px;
}

.state-text {
    color: var(--color-secondary);
    font-size: 20px;
}
</style>