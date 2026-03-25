<template>
    <div class="cont-nav-item">
        <button 
            class="nav-item" 
            :class="[
                isSelected ? 'isSelected' : '', 
                isHovered ? 'isSelected' : '', 
                isBlurred ? 'isBlurred' : '', 
                isLogout ? 'isLogout' : ''
            ]" 
            @mouseenter="onHover" 
            @mouseleave="onLeave" 
            @click="onClick">
            <div class="item-svg">
                <slot name="sIcon"></slot>
            </div>
            <span 
                class="item-text">{{ text }}</span>
        </button>
    </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';


const props = defineProps({
    icon: {
        type: String,
    },
    text: {
        type: String,
        default: 'Button'
    },
    isSelected: {
        type: Boolean,
        default: false
    },
    isHovered: {
        type: Boolean,
        default: false
    },
    isBlurred: {
        type: Boolean,
        default: false
    },
    isLogout: {
        type: Boolean,
        default: false
    }
});

const emit = defineEmits(['onHover', 'onLeave', 'onClick']);

function onHover() {
    emit('onHover', props.text);
};

function onLeave() {
    emit('onLeave');
};

function onClick() {
    emit('onClick', props.text);
};
</script>

<style scoped>
    .cont-nav-item {
        display: inline-block;
        width: 100%;
    }

    button.nav-item {
        background-color: transparent;
        border: 0;
        border-radius: 8px;
        cursor: pointer;
        max-width: 276px;
        width: 100%;
        height: 38px;
        padding: 0;
        display: flex;
        gap: 10px;
        align-items: center;
        transition: 0.3s ease-in-out;
    
        &.isSelected {
            background-color: #FF6868;
        }
        
        &.isBlurred {
            background-color: #ff68686e;
        }

        &.isSelected.isLogout {
            background-color: var(--color-secondary);
        }
    }

    .item-svg {
        padding: 0 7px;
    }
    
    .item-text {
        color: var(--color-primary);
        font-size: 16px;
    }
    
    .isLogout > .item-text {
        color: var(--color-secondary);
        transition: 0.3s;;
    }

    .isSelected.isLogout > .item-text {
        color: var(--color-primary);
    }
</style>