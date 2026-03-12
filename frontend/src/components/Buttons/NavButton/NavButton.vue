<template>
    <div class="cont-nav-item">
        <button class="nav-item" :class="[isSelected ? 'isSelected' : '', isHovered ? 'isSelected' : '', isBlurred ? 'isBlurred' : '', isLogout ? 'isLogout' : '']" @mouseenter="onHover" @mouseleave="onLeave">
            <div class="item-svg" ref="cont_itemSVG"></div>
            <span class="item-text">{{ text }}</span>
        </button>
    </div>
</template>

<script setup>
import { ref, defineProps, defineEmits, onMounted } from 'vue';
import SVGToHTML from '@/modules/useSVGToHTML';

const props = defineProps({
    icon: {
        type: String,
        default: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M9 3H4C3.44772 3 3 3.44772 3 4V11C3 11.5523 3.44772 12 4 12H9C9.55228 12 10 11.5523 10 11V4C10 3.44772 9.55228 3 9 3Z"
                        stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                    <path
                        d="M20 3H15C14.4477 3 14 3.44772 14 4V7C14 7.55228 14.4477 8 15 8H20C20.5523 8 21 7.55228 21 7V4C21 3.44772 20.5523 3 20 3Z"
                        stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                    <path
                        d="M20 12H15C14.4477 12 14 12.4477 14 13V20C14 20.5523 14.4477 21 15 21H20C20.5523 21 21 20.5523 21 20V13C21 12.4477 20.5523 12 20 12Z"
                        stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                    <path
                        d="M9 16H4C3.44772 16 3 16.4477 3 17V20C3 20.5523 3.44772 21 4 21H9C9.55228 21 10 20.5523 10 20V17C10 16.4477 9.55228 16 9 16Z"
                        stroke="#FFFAFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                </svg>`
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

const cont_itemSVG = ref(null);

onMounted(() => {
    const svgIcon = SVGToHTML(props.icon);
    cont_itemSVG.value.appendChild(svgIcon);
})

const emit = defineEmits(['onHover', 'onLeave']);

function onHover() {
    emit('onHover', props.text);
};

function onLeave() {
    emit('onLeave');
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