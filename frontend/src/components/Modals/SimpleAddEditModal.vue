<template>
    <div id="simple-modal" @click.stop="">
        <div class="simple-modal__container">
            <section id="return">
                <ArrowLeft 
                    size="10"
                />
                <p class="return-text">{{ returnText }}</p>
            </section>
            <header>
                <p id="modal-title">{{ modalTitle }}</p>
            </header>
            <section id="progress">
                Progress
            </section>
            <form class="simple-modal__form" action="" method="post" @submit.prevent="">
                <div 
                    class="input-type"
                    v-for="(field, index) in fields"
                    >
                    <SimpleTextInput 
                        v-if="field.type === 'text'"
                        :has-hint="true"
                        :hint-text="field.hintText"
                        :data="inputData[index]"
                        @on-input="handleOnInputFromSimpleInputs"
                        />
                    <SimpleDropdownInput 
                        v-else-if="field.type === 'dropdowntext'"
                        :has-hint="true"
                        :hint-text="field.hintText"
                        :data="inputData[index]"
                        @on-input="handleOnInputFromSimpleInputs"
                    />
                </div>
            </form>
            <section id="bottom">
                <div 
                    id="missing-container"
                    v-if="hasMissingInput"
                    >
                    {{ missingText }}
                </div>
                <div id="actions">
                    <NudeButton 
                        text="Reset"
                        :txt-color="resetButtonColor"
                        @on-click=""
                        @on-mouse-enter="handleOnEnterFromResetButton"
                        @on-mouse-leave="handleOnLeaveFromResetButton"
                    />
                    <PrimaryButton
                        :text="modalSubmitText"
                        :has-icon="true"
                        @on-click="handleOnSubmit"
                    >
                        <template #sIcon>
                            <Plus 
                                v-if="modalType === 'add'"
                                size="16"
                                color=""
                            />
                            <SquarePen 
                                v-else
                                size="16"
                                color=""
                            />
                        </template>
                    </PrimaryButton>
                </div>
            </section>
        </div>
    </div>
</template>

<script setup>
// Import outside
import { ArrowLeft, Plus, SquarePen } from 'lucide-vue-next';

// Vue
import { ref } from 'vue';

// Components
import SimpleTextInput from '../Inputs/SimpleTextInput.vue';
import SimpleDropdownInput from '../Inputs/SimpleDropdownInput.vue';
import NudeButton from '../Buttons/NudeButton.vue';
import PrimaryButton from '../Buttons/PrimaryButton.vue';

// Modules


// Variables for inits
/**
 * fields object has the following:
 * { id: Number, type: String, hintText: String }
 * The type key accepts: 'text', 'dropdowntext'
 * 
 * modelValues must depend on fields and contains:
 * { id: Number, value: String }
 * 
 * modalType accepts: 'add', 'edit'
 */
const props = defineProps({
    fields: {
        type: Array,
        required: true,
    },
    modelValues: {
        type: Array,
    },
    returnText: {
        type: String,
        default: 'Return'
    },
    modalTitle: {
        type: String,
        default: 'Modal Title'
    },
    modalType: {
        type: String,
        default: 'add'
    },
    modalSubmitText: {
        type: String,
        default: 'Submit'
    },
    missingText: {
        type: String,
        default: 'This is a missing text!'
    }
});

const emits = defineEmits([
    'onSubmit'
]);

const inputData = ref([]);
const hasMissingInput = ref(false);

// Initialise inputData
props.modelValues?.forEach(value => {
    console.log(value);
    let newInputData = {
        id: value.id,
        value: value.value,
        state: value === '' ? 'default' : 'valid'
    };

    inputData.value.push(newInputData);
});


// Variables for appearance
const resetButtonColor = ref('var(--color-accent)');

// Function for child
function handleOnEnterFromResetButton() {
    resetButtonColor.value = 'var(--color-secondary)';
};

function handleOnLeaveFromResetButton() {
    resetButtonColor.value = 'var(--color-accent)';
};

// Function handlers
function handleOnInputFromSimpleInputs(childObj) {
    const index = childObj?.refID - 1;
    const newValue = childObj?.newValue;

    inputData.value[index].value = newValue;
    inputData.value[index].state = newValue === '' ? 'default' : 'valid';
};

function handleOnSubmit() {
    console.log(inputData.value);
};
</script>

<style scoped>
@import './baseModal.css';

.input-type {
    margin-bottom: 15px;
}
</style>