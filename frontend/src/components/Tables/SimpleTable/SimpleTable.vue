<template>
    <div class="simple-table">
        <table :id="tableID">
            <thead>
                <tr id="legend">
                    <th 
                        v-for="(legend, index) in legends"
                        :id="'legend-' + legend.id"
                    >
                        <input 
                            type="checkbox" 
                            name="" id=""
                            v-if="index === 0"
                            >
                        <span class="legend-text">
                            {{ legend.text }}
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
                        Loading items from the server...
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
                        {{ tableStateText }} seems to be empty...
                    </p>
                    <PrimaryButton 
                        text="Add some!"
                        :has-icon="false"
                        @on-click="handleEmptyAddRequest"
                        >
                    </PrimaryButton>
                </div>
                <SimpleRow 
                    v-for="(row, index) in rows"
                    :key="index"
                    :data="row"
                    :index="index"
                    :is-currently-clicked="activeRowIndex === index"
                    @on-click="handleClickFromSimpleRow"
                    @on-edit="handleEditRequestFromRow"
                    @on-delete="handleDeleteRequestFromRow"
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
import { ref } from 'vue';

// Components
import PrimaryButton from '@/components/Buttons/PrimaryButton.vue';

/**
 * Template for 'props.legends'
 * [ { id: String, text: String } ]
 * i.e. id: 'name', text: 'Product Name'
 * 
 * Template for 'props.rows'
 * [ [ data1, data2 ], [ data1, data2 ] ]
 * +++ The main array contains the rows
 * +++ The second array contains the data
 * 
 * tableState accepts 'loading', 'empty', 'exist'
 */
const props = defineProps({
    tableID: {
        type: String,
        default: ''
    },
    legends: {
        type: Array,
        default: []
    },
    rows: {
        type: Array,
        default: []
    },
    tableState: {
        type: String
    },
    tableStateText: {
        type: String
    }
});

const emits = defineEmits([
    'onRowEdit',
    'onRowDelete',
    'onEmptyAdd'
]);

// Variables for Child
const activeRowIndex = ref(null);

// Function From Child
function handleClickFromSimpleRow(rowIndex) {
    activeRowIndex.value = rowIndex;
};

function handleEditRequestFromRow(rowIndex) {
    emits('onRowEdit', rowIndex);
};

function handleDeleteRequestFromRow(rowItemID, rowIndex) {
    emits('onRowDelete', rowItemID, rowIndex);
};

function handleEmptyAddRequest() {
    emits('onEmptyAdd');
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