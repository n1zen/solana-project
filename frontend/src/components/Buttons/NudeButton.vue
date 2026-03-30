<template>
    <div class="nude-button">
        <button 
            type="button" 
            @click="handleOnClick()"
            @mouseenter="handleOnMouseEnter"
            @mouseleave="handleOnMouseLeave">
            <div id="icon">
                <slot name="sIcon"></slot>
            </div>
            <p 
                id="text"
                :style="{
                    color: txtColor,
                    fontSize: fnSize
                }"
                >
                {{ text }}
            </p>
        </button>
    </div>
</template>

<script setup>
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
    fnSize: {
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
    'onMouseEnter',
    'onMouseLeave'
]);

function handleOnClick() {
    emits('onClick');
};

function handleOnMouseEnter() {
    emits('onMouseEnter');
}

function handleOnMouseLeave() {
    emits('onMouseLeave');
}
</script>

<style scoped>
button {
    background-color: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
    transition: 0.3s;
    display: flex;
    gap: 5px;
    align-items: center;
    justify-content: center;
}

#icon {
    padding-bottom: 2px;
}

#text {
    transition: 0.3s;
}
</style>