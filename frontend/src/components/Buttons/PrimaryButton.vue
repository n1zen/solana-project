<template>
    <div class="primary-button">
        <button 
            :style="{ 
                backgroundColor: isHovered ? 'var(--color-primary)' : bgColor, 
                border: isHovered ? '2px solid var(--color-secondary)' : '2px solid transparent'
            }" 
            :class="{ 'with-icon': hasIcon }"
            @click="handleClick"
            @mouseenter="isHovered = true; handleOnHover()"
            @mouseleave="isHovered = false; handleOnLeave()"
            >
            <div id="icon" v-if="hasIcon">
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
    },
    fontSize: {
        type: Number,
        default: 16
    },
    hasIcon: {
        type: Boolean,
        default: false
    }
});

const emits = defineEmits([
    'onClick',
    'onHover',
    'onLeave'
]);

const isHovered = ref(false);

function handleClick() {
    emits('onClick');
}

function handleOnHover() {
    emits('onHover')
}

function handleOnLeave() {
    emits('onLeave')
}
</script>

<style scoped>
button {
    border-radius: 5px;
    cursor: pointer;
    padding: 7px 16px;
    transition: 0.3s;
    display: flex;
    gap: 7px;
    align-items: center;
    justify-content: center;
}

button.with-icon {
    display: flex;
    align-items: center;
}

#text {
    transition: 0.3s;
}

#icon {
    padding-bottom: 2px;
}
</style>