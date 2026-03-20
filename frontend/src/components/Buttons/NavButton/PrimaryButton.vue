<template>
    <div class="primary-button">
        <button 
            :style="{ 
                backgroundColor: isHovered ? 'var(--color-primary)' : bgColor, 
                border: isHovered ? '2px solid var(--color-secondary)' : '2px solid transparent'
            }" 
            :class="{ 'with-icon': icon }"
            @click="handleClick"
            @mouseenter="isHovered = true"
            @mouseleave="isHovered = false"
            >
            <div id="icon">
                <slot name="sIcon"></slot>
            </div>
            <div id="text" 
                :style="{ 
                    color: isHovered ? 'var(--color-secondary)' : txtColor 
                }"
                >
                {{ text }}
            </div>
        </button>
    </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue';

const props = defineProps({
    text: {
        type: String,
        default: 'Button'
    },
    bgColor: {
        type: String,
        default: 'var(--color-secondary)'
    },
    txtColor: {
        type: String,
        default: 'var(--color-primary)'
    }
});

const emits = defineEmits([
    'onClick'
]);

const isHovered = ref(false);

function handleClick() {
    console.log(`PrimaryButton clicked: ${props.text}`);
    emits('onClick');
}
</script>

<style scoped>
button {
    border-radius: 5px;
    cursor: pointer;
    padding: 7px 16px;
    transition: 0.3s;
}

button.with-icon {
    display: flex;
    align-items: center;
}

#text {
    transition: 0.3s
}
</style>