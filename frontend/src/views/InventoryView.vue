<template>
    <div class="container">
        <h1>Inventory</h1>
        <!--Forms-->
        <div class="form-container">
            <form @submit.prevent="onSubmit">
                <div class="form-fields">
                    <div class="input-group">
                        <label class="label">Product ID: </label>
                        <input class="input" type="number" v-model="product_id" required/>
                    </div>
                    <div class="input-group">
                        <label class="label">Quantity: </label>
                        <input class="input" type="number" v-model="quantity" required/>
                    </div>
                    <div class="input-group">
                        <label class="label">Details: </label>
                        <input class="input" type="text" v-model="details" required/>
                    </div>
                </div>
                <button type="submit">Add Inventory</button>
            </form>
        </div>
        <!--Table-->
        <div class="table-container">
            <InventoryTable :inventory="inventory"/>
        </div>
    </div>
</template>

<script>
import InventoryTable from '@/components/inventory/InventoryTable.vue';
import getInventory from '@/composables/Inventory/getInventory';
import addInventoryItem from '@/composables/Inventory/addInventoryItem';

export default {
    components: { InventoryTable },
    setup() {

        const { inventory, error, load } = getInventory();

        load();

        const { product_id, quantity, details, error: addError, onSubmit } = addInventoryItem(load);

        return { inventory, error, addError, onSubmit, product_id, quantity, details };
    }
}
</script>

<style scoped>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        width: 100%;
        margin: var(--space-8) 0;
    }
    .products-container {
        display: flex;
        flex-wrap: wrap;
        gap: var(--space-4);
    }
    h1 {
        text-align: center;
    }
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
    button:hover {
        background-color: var(--bg);
    }
    button:active {
        box-shadow: none;
        background-color: var(--bg);
    }
</style>