<template>
    <div class="simple-text-input simple-input" >
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
                name="" 
                id=""
                placeholder=" "
                v-model="modelValue"
                @input="handleOnInput"
                >
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

const modelValue = ref(props.data?.value);

watch(() => props.data?.value, (newValue) => {
    modelValue.value = newValue;
});

// Function handler
function handleOnInput() {
    emits('onInput', {
        refID: props.data?.id,
        newValue: modelValue.value
    });
};
</script>

<style scoped>
@import './baseInput.css';


</style>