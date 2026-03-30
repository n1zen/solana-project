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
                    id="empty-set"
                    v-if="rows.length === 0"
                    >
                    <div id="empty-icon">
                        <PackageOpen 
                            size="80"
                            color="var(--color-secondary)"
                        />
                    </div>
                    <p id="empty-text">
                        Inventory seems to be empty...
                    </p>
                    <PrimaryButton 
                        text="Add some!"
                        :has-icon="false"
                        @on-hover=""
                        @on-leave=""
                        @on-click=""
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
                />
            </tbody>
        </table>
    </div>
</template>

<script setup>
// Import outside
import { PackageOpen, Plus } from 'lucide-vue-next';
import SimpleRow from './SimpleRow.vue';

//
import { onMounted, ref } from 'vue';
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
});

// Variables for Child
const activeRowIndex = ref(null);

// Function From Child
function handleClickFromSimpleRow(childIndex) {
    activeRowIndex.value = childIndex;
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

#empty-set {
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

#empty-icon {
    border: 2px solid var(--color-secondary);
    border-radius: 50%;
    padding: 30px;
}

#empty-text {
    color: var(--color-secondary);
    font-size: 20px;
}
</style>