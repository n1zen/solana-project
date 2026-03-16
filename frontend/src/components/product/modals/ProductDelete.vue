<template>
    <div class="modal-background" @click.self="$emit('close')">
        <div class="modal-container">
            <h1>Are you sure you want to delete?</h1>
            <div class="actions">
                <button @click="$emit('onDelete')" class="agree">
                    <CheckIcon
                        size="var(--text-base)",
                        stroke-width="3"
                    />
                </button>
                <button @click="$emit('close')" class="disagree">
                    <XIcon
                        size="var(--text-base)",
                        stroke-width="3"
                    />
                </button>
            </div>
        </div>
    </div>
</template>
<script setup>
import { CheckIcon, XIcon } from 'lucide-vue-next';
defineEmits(
    ['close', 'onDelete']
);
</script>
<style scoped>
.modal-background {
    /* Cover the whole page */
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1000;

    /* Dim the background */
    background: hsla(0, 0%, 0%, 0.5);

    /* Center the modal box */
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal-container {
    width: var(--max-w-lg);
    background: var(--bg-dark);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: var(--space-4);
    border-radius: var(--radius-xl);
}

.actions {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    width: 35%;
}

button {
    margin: 0 var(--space-1) var(--space-4) var(--space-1);
    border-radius: var(--radius-xl);
    padding: var(--space-2) var(--space-2);
    color: var(--text);
    background: var(--bg-light);
    border: var(--border-card);
    border-top: var(--highlight);
    box-shadow: var(--shadow);
    display: flex;
    justify-content: center;
    align-items: center;
}
button.agree:hover {
    background-color: var(--warning);
    color: var(--text-inverse);
}
button.agree:active {
    box-shadow: none;
    color: var(--text-inverse);
    background-color: var(--danger);
}
button.disagree:hover {
    background-color: var(--primary);
    color: var(--text-inverse);
}
button.disagree:active {
    box-shadow: none;
    color: var(--text-inverse);
    background-color: var(--secondary);
}
</style>