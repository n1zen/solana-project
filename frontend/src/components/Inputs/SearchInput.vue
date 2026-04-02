<template>
    <div class="search-input">
        <div class="base-input__container">
            <input 
                type="text" 
                name="" id="" 
                placeholder="Search..."
                v-model="inputModel"
                @input="handleInputSearch"
            >
            <Search 
                color="var(--color-accent)"
                size="20"
            />
        </div>
    </div>
</template>

<script setup>
// Outside import
import { Search } from 'lucide-vue-next';

// Vue
import { ref } from 'vue';

// Use Modals
import SearchItem from '@/modules/utils/useSearch';
import DataTypeChecker from '@/modules/utils/useDataTypeChecker';

const props = defineProps({
    itemType: {
        type: String
    }
});

const emits = defineEmits([
    'onInput'
]);

const inputModel = ref('');
const { searchMany } = SearchItem(props.itemType);
const { isNumeric } = DataTypeChecker();

// Function handlers
function handleInputSearch () {

    // deal with this later when filters are added
    let searchBy, value, results = null;

    if (isNumeric(inputModel.value)) {
        searchBy = 'id';
        value = Number(inputModel.value);
    } else {
        searchBy = 'name';
        value = inputModel.value;
    };

    results = searchMany({
        searchBy,
        value,
        returnField: 'all',
        matchType: 'startsWith'
    });

    if (results.length === 0) { // change later
        results = searchMany({
            searchBy: 'category',
            value,
            returnField: 'all',
            matchType: 'startsWith'
        });
    };

    // console.log(results);
    emits('onInput', results);
};
</script>

<style scoped>
@import './baseInput.css';

.base-input__container {
    display: flex;
    gap: 5px;
    align-items: center;
    justify-content: center;
}

.search-input .base-input__container {
    border: 2px solid var(--color-accent);
    padding: 1px 7px;
    transition: 0.3s;
}

.search-input .base-input__container input {
    padding: 4px 8px;
}

.search-input .base-input__container svg {
    margin-right: 7px;
    margin-bottom: 2px;
}
</style>