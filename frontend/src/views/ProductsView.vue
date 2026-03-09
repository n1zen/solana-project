<template>
  <h1>Products</h1>
  <!-- Add new product form -->
  <div class="form-container">
    <form @submit.prevent="onSubmit">
      <div class="form-fields">
        <div class="form-group">
          <label>SKU: </label>
          <input type="number" v-model="sku" required/>
        </div>
        <div class="form-group">
          <label>Product Name: </label>
          <input type="text" v-model="name" required/>
        </div>
        <div class="form-group">
          <label>Category: </label>
          <input type="text" v-model="category" required/>
        </div>
        <div class="form-group">
          <label>Price: </label>
          <input type="number" v-model="price" required/>
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
  .form-container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
  }

  .form-fields {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    gap: 15px;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    flex: 1;
    min-width: 150px;
  }

  .form-group label {
    margin-bottom: 4px;
    font-weight: bold;
  }

  .form-group input {
    padding: 6px 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  button[type="submit"] {
    display: block;
    margin-top: 15px;
    padding: 8px 20px;
    cursor: pointer;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #f9f9f9;
  }

  button[type="submit"]:hover {
    background-color: #e9e9e9;
  }
</style>
