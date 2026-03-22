<template>
    <tr class="product-info" :class="[clickStatusFromParent ? 'isClicked' : '']" @click="handleClick">
        <td class="product-id">
            <input type="checkbox" name="" id="">
            <span class="">250001</span>
        </td>
        <td class="product-name">
            Cat in Box
        </td>
        <td class="product-category">
            Animal
        </td>
        <td class="product-price">
            ₱ 100
        </td>
        <td class="actions">
            <button class="edit">
                <SquarePen
                    v-if="!clickStatusFromParent"
                    size="20"
                    :color="editOnHover ? 'var(--color-primary)' : 'var(--color-accent)'"
                    @mouseenter="handleMouseEnterOnEdit"    
                    @mouseleave="handleMouseLeaveOnEdit"    
                />
                <SquarePen
                    v-else
                    size="20"
                    :color="editOnHover ? 'var(--color-accent)' : 'var(--color-primary)'"
                    :style="{ color: clickStatusFromParent ? 'var(--color-primary)' : '' }"
                    @mouseenter.stop="handleMouseEnterOnEdit"    
                    @mouseleave="handleMouseLeaveOnEdit"    
                />
            </button>
            <button class="delete">
                <SquareX 
                    v-if="!clickStatusFromParent"
                    size="20" 
                    :color="deleteOnHover ? 'var(--color-primary)' : 'var(--color-secondary)'"
                    @mouseenter="handleMouseEnterOnDelete"
                    @mouseleave="handleMouseLeaveOnDelete" />
                <SquareX 
                    v-else
                    size="20"
                    :color="deleteOnHover ? 'var(--color-accent)' : 'var(--color-primary)'"
                    :style="{ color: clickStatusFromParent ? 'var(--color-primary)' : 'var(--color-secondary)' }"
                    @mouseenter="handleMouseEnterOnDelete"
                    @mouseleave="handleMouseLeaveOnDelete" />
            </button>
        </td>
    </tr>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue';

import { SquarePen, SquareX } from 'lucide-vue-next';

const props = defineProps({
    index: {
        type: Number
    },
    clickStatusFromParent: {
        type: Boolean,
        default: false
    }
});

const editOnHover = ref(false);
const deleteOnHover = ref(false);

const emit = defineEmits(['isClicked'])

function handleClick() {
    console.log('Clicked !');

    emit('isClicked', props.index);
};

function handleMouseEnterOnEdit() {
    editOnHover.value = true;
}

function handleMouseLeaveOnEdit() {
    editOnHover.value = false;
}

function handleMouseEnterOnDelete() {
    deleteOnHover.value = true;
}

function handleMouseLeaveOnDelete() {
    deleteOnHover.value = false;
}
</script>

<style scoped>
td {
    border-bottom: 1px solid var(--color-accent);
    color: var(--color-accent);
    cursor: pointer;
    font-weight: bold;
    padding: 20px 10px;
    transition: 0.3s;
}

.product-info.isClicked td {
    color: var(--color-primary);
}

.product-id span {
    margin-left: 10px;
}

.actions button {
    background-color: transparent;
    border-radius: 3px;
    border: none;
    cursor: pointer;
    padding: 0;

    &>* {
        transition: 0.3s;
    }
}

.actions .delete {
    margin-left: 12px;
}
</style>