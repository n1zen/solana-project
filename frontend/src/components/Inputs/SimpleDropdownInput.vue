<template>
    <div class="simple-text-input simple-input">
        <div 
            class="base-input__container"
            :class="data?.state"
        >
            <p 
                class="hint"
                v-if="hasHint"
                >
                {{ hintText }}
            </p>
            <input 
                type="text" 
                id=""
                name=""
                placeholder=" " 
                v-model="modelValue"
                ref="inputEl"
                @input="handleOnInput"
                >
            <ChevronDown 
                color="var(--color-secondary)"
            />
            <!-- Could be a future component (watch) -->
            <div class="dropdown-list">

            </div>
        </div>
        <p 
            class="danger-text"
            v-if="data?.state === 'invalid'"
            >{{ dangerText }}
        </p>
    </div>
</template>

<script setup>
// Import outside
import { ChevronDown } from 'lucide-vue-next';

// Vue
import { ref, watch } from 'vue';

// Variables for inits
/**
 * data object should be:
 * { id: Number, value: String, state: String }
 * --- state has 4 states:
 * default, missing, invalid, valid
 */
const props = defineProps({
    data: {
        type: Object,
    },
    dataKey: {
        type: String
    },
    linkedField: {
        type: String
    },
    hasHint: {
        type: Boolean,
        default: true
    },
    hintText: {
        type: String,
        default: 'Hint'
    },
    dangerText: {
        type: String,
        default: 'Danger Text'
    }
});

const emits = defineEmits([
    'onInput'
]);

const modelValue = ref(props.data.value);

watch(() => props.data?.value, (newValue) => {
    modelValue.value = newValue;
});

// Function handler
function handleOnInput() {
    emits('onInput', {
        dataKey: props.dataKey,
        newValue: modelValue.value,
        linkedField: props.linkedField
    });
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

/* Change later */
.dropdown-list {
    position: absolute;
}

.base-input__container svg {
    cursor: pointer;
}
</style>