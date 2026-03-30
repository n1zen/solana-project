<template>
    <div id="delete-modal"  @click.stop="">
        <div class="container">
            <section id="return">
                <NudeButton 
                    text="Cancel" 
                    :txt-color="btnCancelColor" 
                    :fn-size="14"
                    @on-click="handleOnCancel()"
                >
                    <template #sIcon>
                        <ArrowLeft 
                            size="12" 
                            :color="btnCancelColor" />
                    </template>
                </NudeButton>
            </section>
            <header>
                <p id="title">Delete {{ textTitle }} item</p>
                <p class="description" id="desc">{{ desc }}</p>
                <p class="description" id="desc-2">Are you sure to proceed?</p>
            </header>
            <section id="info">
                <table>
                    <tr v-for="item in items">
                       <td class="type">{{ item.type }} :</td> 
                       <td class="data">{{ item.data }}</td> 
                    </tr>
                </table>
            </section>
            <div id="actions">
                <PrimaryButton
                    text="Delete Item"
                    :has-icon=true
                    @on-hover="changeButtonAddIconColor"
                    @on-leave="changeButtonAddIconColor"
                    @on-click="handleOnConfirm"
                >
                    <template #sIcon>
                         <Trash 
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
import {  ArrowLeft, Trash } from 'lucide-vue-next';

import PrimaryButton from '../Buttons/PrimaryButton.vue';
import NudeButton from '../Buttons/NudeButton.vue';

import { ref } from 'vue';

const props = defineProps({
    textTitle: {
        type: String,
        default: 'text title'
    },
    desc: {
        type: String,
        default: 'A description for the delete modal.'
    },
    items: {
        type: Array,
        default: []
    }
});

const emits = defineEmits([
    'onCancel',
    'onConfirm'
])

const btnCancelColor = ref('#505050b0')
const btnAddIconColor = ref('#FFFAFA');

function changeButtonAddIconColor() {
    btnAddIconColor.value = btnAddIconColor.value === '#FFFAFA' ? '#C84A46' : '#FFFAFA';
};

function handleOnCancel() {
    emits('onCancel');
};

function handleOnConfirm() {
    emits('onConfirm');
};
</script>

<style scoped>
.container {
    background-color: var(--color-primary);
    border-radius: 5px;
    box-shadow: -4px 4px 0 0 var(--color-secondary);
    width: 435px;
    min-height: 300px;
    padding: 30px 20px;
}

p {
    font-weight: bold;
}

#title {
    color: var(--color-secondary);
}

.description {
    color: var(--color-accent);
}

header {
    margin-bottom: 15px;
}

#return {
    margin-bottom: 15px;
}

#info {
    padding: 0 7px;
    margin-bottom: 30px;
}

table {
    border-collapse: collapse;
    border-spacing: 0;
    width: 100%;
}

td {
    color: var(--color-accent);
    font-weight: bold;
}

td.type {
    width: 40%;
}

td.data {
    width: 100%;
}

#actions {
    display: flex;
    align-items: center;
    justify-content: right;
}
</style>