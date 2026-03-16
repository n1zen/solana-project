<template>
    <div class="modal-background" @click.self="$emit('close')">
        <div class="modal-container">
            <!-- Form fields -->
            <div class="form-container">
                <form @submit.prevent="onSubmit">
                    <div class="form-fields">
                        <div class="input-group">
                            <label class="label">Product SKU: </label>
                            <input class="input" type="number" v-model="sku" required/>
                        </div>
                        <div class="input-group">
                            <label class="label">Product Name: </label>
                            <input class="input" type="text" v-model="name" required/>
                        </div>
                        <div class="input-group">
                            <label class="label">Category: </label>
                            <input class="input" type="text" v-model="category" required/>
                        </div>
                        <div class="input-group">
                            <label class="label">Price: </label>
                            <input class="input" type="number" v-model="price" required/>
                        </div>
                    </div>
                    <button type="submit" class="editBtn">Edit Product</button>
                </form>
            </div>
            <button @click="$emit('close')" class="cancelBtn">Cancel</button>
        </div>
    </div>
</template>
<script setup>
import updateProduct from '@/composables/Products/updateProduct.js';

const emit = defineEmits(['close']);
const props = defineProps({ product: {
    type: Object,
    required: true
} });

const { sku, name, category, price, error, onSubmit } = updateProduct(props.product);
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

/* Form styles */

.form-container {
        background: var(--gradient);
        padding: var(--space-5);
        border-radius: var(--radius-lg);
        border: var(--border-card);
        box-shadow: var(--shadow);
        border-top: var(--highlight);
    }
    .form-container:hover {
        background: var(--gradient-hover);
    }
    form {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .input-group {
        margin-bottom: var(--space-2);
    }
    .input {
        max-width: 190px;
        height: 44px;
        /* background-color: hsla(234, 50%, 4%, 0.039); */
        background-color: var(--bg-dark);
        border-radius: .5rem;
        padding: 0 1rem;
        color: var(--text);
        border: 2px solid transparent;
        font-size: 1rem;
        transition: border-color .3s cubic-bezier(.25,.01,.25,1) 0s, color .3s cubic-bezier(.25,.01,.25,1) 0s,background .2s cubic-bezier(.25,.01,.25,1) 0s;
    }

    .label {
        display: block;
        margin-bottom: .3rem;
        font-size: .9rem;
        font-weight: bold;
        /* color: hsla(234, 50%, 4%, 0.6); */
        color: var(--text-more-muted);
        transition: color .3s cubic-bezier(.25,.01,.25,1) 0s;
    }

    .input:hover, .input:focus, .input-group:hover .input {
        outline: none;
        /* border-color: hsl(234, 50%, 4%); */
        border-color: var(--border);
    }

    .input-group:hover .label, .input:focus {
        /* color: hsla(234, 50%, 4%, 0.761);
         */
        color: var(--text);
    }
    button {
        margin-top: var(--space-4);
        padding: var(--space-2) var(--space-4);
        border-radius: var(--radius-md);
        cursor: pointer;
        background: var(--bg-light);
        border: var(--border-card);
        box-shadow: var(--shadow);
        border-top: var(--highlight);
        color: var(--text);
    }
    button.editBtn:hover {
        background-color: var(--primary);
        color: var(--text-inverse);
    }
    button.editBtn:active {
        box-shadow: none;
        background-color: var(--success);
        color: var(--text-inverse);
    }
    button.cancelBtn:hover {
        background-color: var(--warning);
        color: var(--text-inverse);
    }
    button.cancelBtn:active {
        box-shadow: none;
        background-color: var(--danger);
        color: var(--text-inverse);
    }
</style>