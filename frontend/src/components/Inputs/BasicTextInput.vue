<template>
    <div class="basic-text-input">
        <div class="container" :class="inputState">
            <p class="hint" v-if="hasHint">{{ hint }}</p>
            <input type="text" name="" placeholder=" " v-model="inputValue" @blur="passInputValue">
        </div>
        <p class="danger" v-if="inputState === 'invalid'">{{ dangerTxt }}</p>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
    inputID: {
        type: Number,
        required: true
    },
    hint: {
        type: String,
        default: ''
    },
    dangerTxt: {
        type: String,
        default: 'Danger'
    },
    inputState: {
        type: String,
        default: 'default'
    }
});

const emits = defineEmits([
    'passValue'
]);

const hasHint = ref(props.hint !== '');
const inputValue = ref('')

function passInputValue(){
    emits('passValue', {
        inputID: props.inputID,
        value: inputValue.value
    });
};
</script>

<style scoped>
/* .basic-text-input {
    margin-top: 30px;
} */

.container {
    border: 2px solid var(--color-accent);
    border-radius: 5px;
    font-weight: bold;
    padding: 7px;
    position: relative;

    &.valid {
        border: 2px solid var(--color-valid);
    }
    
    &.invalid,
    &.missing {
        border: 2px solid var(--color-secondary);
    }
}

.hint {
    background-color: transparent;
    color: #505050bc;
    padding: 0px;
    position: absolute;
    top: 50%;
    left: 8px;
    transform: translate(0, -50%);
    transition: 0.3s;
}

input {
    background-color: transparent;
    border: none;
    color: var(--color-accent);
    width: 100%;
    outline: none;
}

.danger {
    color: var(--color-secondary);
    font-size: 12px;
    padding-left: 7px;
}

input::placeholder {
    color: transparent;
}

.container:has(input:focus)>.hint,
.container:has(input:not(:placeholder-shown))>.hint {
    background-color: var(--color-primary);
    font-size: 12px;
    padding: 0 3px;
    top: -5%
}

.container.valid .hint {
    color: var(--color-valid)
}

.container.invalid .hint {
    color: var(--color-secondary)
}
</style>