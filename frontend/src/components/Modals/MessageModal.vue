<template>
    <div id="message-modal" @click.stop="">
        <div class="simple-modal__container">
            <header>
                <div 
                    id="message-icon"
                    :style="{ border: `3px solid ${ iconBorderColor }` }"
                >
                    <slot name="sMessageIcon"></slot>
                </div>
                <p 
                    class="message" 
                    id="message"
                    :style="{ color: messageTextColor }"
                >
                    {{ message }}
                </p>
            </header>
            <div id="actions">
                <PrimaryButton
                    text="Confirm"
                    :has-icon=true
                    @on-hover="changeButtonAddIconColor"
                    @on-leave="changeButtonAddIconColor"
                    @on-click="handleOnConfirm"
                >
                    <template #sIcon>
                        <Check 
                            size="16"
                            :color="btnAddIconColor"
                        />
                    </template>
                </PrimaryButton>
            </div>
        </div>
    </div>
</template>

<script setup>
import { Check } from 'lucide-vue-next';

import PrimaryButton from '../Buttons/PrimaryButton.vue';

import { ref } from 'vue';

const props = defineProps({
    message: {
        type: String,
        default: 'Message text here.'
    },
    messageTextColor: {
        type: String,
        default: 'var(--color-valid)'
    },
    iconBorderColor: {
        type: String,
        default: 'var(--color-valid)'
    }
})

const emits = defineEmits([
    'onConfirm'
]);

const btnAddIconColor = ref('#FFFAFA');

function changeButtonAddIconColor() {
    btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
};

function handleOnConfirm() {
    emits('onConfirm');
};
</script>

<style scoped>
@import './baseModal.css';

#message-modal .simple-modal__container {
    width: 238px;
}


header {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: center;
    justify-content: center;
    margin-bottom: 15px;
}

#message-icon {
    aspect-ratio: 1;
    border-radius: 50%;
    width: 120px;
    padding: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.message {
    color: var(--color-accent);
    text-align: center;
}

#actions {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>