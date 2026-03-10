<template>
    <div class="container">
        <h1>Products</h1>
        <!-- Add new product form -->
        <div class="form-container">
            <form @submit.prevent="onSubmit">
                <div class="form-fields">
                    <div class="input-group">
                        <label class="label">SKU: </label>
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
                <button type="submit">Add Product</button>
            </form>
        </div>
        <!-- view of all products -->
        <h3>Products</h3>
        <div v-for="product in products" :key="product.id">
            <ProductCard :product="product" />
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import getProducts from '@/composables/getProducts.js';
import addProduct from '@/composables/addProduct.js';
import ProductCard from '@/components/ProductCard.vue';

export default {
    name: 'ProductsView',
    components: {
        ProductCard,
    },
    setup() {
        // on mount, show all products on a card
        const { products, error, load } = getProducts()

        load();

        // add product form
        const { sku, name, category, price, error: addError, onSubmit } = addProduct(load);

        return { products, error, addError, onSubmit, sku, name, category, price };
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
    }
    h1 {
        text-align: center;
    }
    .form-container {
        background: var(--bg);
        padding: var(--space-5);
        border-radius: var(--radius-lg);
        border: var(--border-card);
        box-shadow: var(--shadow);
        border-top: var(--highlight);
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
        background-color: hsla(234, 50%, 4%, 0.039);
        border-radius: .5rem;
        padding: 0 1rem;
        border: 2px solid transparent;
        font-size: 1rem;
        transition: border-color .3s cubic-bezier(.25,.01,.25,1) 0s, color .3s cubic-bezier(.25,.01,.25,1) 0s,background .2s cubic-bezier(.25,.01,.25,1) 0s;
    }

    .label {
        display: block;
        margin-bottom: .3rem;
        font-size: .9rem;
        font-weight: bold;
        color: hsla(234, 50%, 4%, 0.6);
        transition: color .3s cubic-bezier(.25,.01,.25,1) 0s;
    }

    .input:hover, .input:focus, .input-group:hover .input {
        outline: none;
        border-color: hsl(234, 50%, 4%);
    }

    .input-group:hover .label, .input:focus {
        color: hsla(234, 50%, 4%, 0.761);
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
    }
</style>
