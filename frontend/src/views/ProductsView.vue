<template>
    <div class="container">
        <h2>Add new product</h2>
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
    </div>
    <div class="container">
        <h2>Products</h2>
        <div class="products-container" v-for="product in products" :key="product.id">
            <ProductCard :product="product" />
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import getProducts from '@/composables/Products/getProducts.js';
import addProduct from '@/composables/Products/addProduct.js';
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
